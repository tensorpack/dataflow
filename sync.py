#!/usr/bin/env python
#-*- coding: utf-8 -*-

"""
This script sync commits from tensorpack to dataflow.

Dependencies:
    gitpython
"""

import os
import sys
import shutil
from datetime import datetime
import git
import argparse
from dataflow.utils import logger


DF_ROOT = os.path.dirname(__file__)
UTILS_TO_SYNC = [
    'argtools', 'concurrency', 'compatible_serialize', 'develop',
    'fs', '__init__', 'loadcaffe', 'logger', 'serialize', 'stats',
    'timer', 'utils']


def match_commit(tp_commit, df_commit):
    if (tp_commit.message == df_commit.message) and \
            (tp_commit.authored_date == df_commit.authored_date):
        return True
    return False


def show_commit(commit):
    return commit.repo.git.show('-s', commit.hexsha, '--color=always')


def show_date(timestamp):
    return datetime.fromtimestamp(timestamp).strftime("%Y/%M/%d-%H:%m:%S")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('tensorpack')
    args = parser.parse_args()
    tp_root = args.tensorpack

    tp_repo = git.Repo(tp_root)
    assert tp_repo.active_branch.name == 'master'
    if tp_repo.is_dirty():
        print("Warning: tensorpack repo is not clean!")

    df_repo = git.Repo(DF_ROOT)
    assert not df_repo.is_dirty()
    df_commits = df_repo.iter_commits(paths='dataflow')
    df_latest_commit = next(df_commits)
    logger.info("DataFlow commit to match: \n" + show_commit(df_latest_commit))

    unsynced_commits = []
    for cmt in tp_repo.iter_commits(paths=['tensorpack/dataflow', 'tensorpack/utils']):
        if match_commit(cmt, df_latest_commit):
            logger.info("Matched tensorpack commit: \n" + show_commit(cmt))
            break
        unsynced_commits.append(cmt)
    else:
        logger.error("Cannot find tensorpack commit that matches the above commit.")
        sys.exit(1)
    logger.info("{} more commits to sync".format(len(unsynced_commits)))

    unsynced_commits = unsynced_commits[::-1]

    try:
        for commit_to_sync in unsynced_commits:
            tp_repo.git.checkout(commit_to_sync.hexsha)
            logger.info("-" * 60)
            logger.info("Syncing commit '{}' at {}".format(
                commit_to_sync.message.strip(), show_date(commit_to_sync.authored_date)))

            # sync files
            dst = os.path.join(DF_ROOT, 'dataflow', 'dataflow')
            logger.info("Syncing {} ...".format(dst))
            shutil.rmtree(dst)
            shutil.copytree(os.path.join(tp_root, 'tensorpack', 'dataflow'), dst)

            logger.info("Syncing utils ...")
            for util in UTILS_TO_SYNC:
                dst = os.path.join(DF_ROOT, 'dataflow', 'utils', util + '.py')
                src = os.path.join(tp_root, 'tensorpack', 'utils', util + '.py')
                os.unlink(dst)
                shutil.copy2(src, dst)

            log = df_repo.git.commit(
                '--all',
                message=commit_to_sync.message,
                date=commit_to_sync.authored_date,
                author=commit_to_sync.author)
            logger.info("Successfully sync commit:\n" + log)
    finally:
        tp_repo.git.checkout('master')
