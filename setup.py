from os import path
import setuptools
from setuptools import setup, find_packages

version = int(setuptools.__version__.split('.')[0])
assert version > 30, "Dataflow installation requires setuptools > 30"

this_directory = path.abspath(path.dirname(__file__))


# setup metainfo

with open(path.join(this_directory, 'README.md'), 'rb') as f:
    long_description = f.read().decode('utf-8')
__version__ = '0.9.5'


setup(
    name='dataflow',
    author="TensorPack contributors",
    author_email="ppwwyyxxc@gmail.com",
    url="https://github.com/tensorpack/dataflow",
    keywords="deep learning, neural network, data processing",
    license="Apache",

    version=__version__,   # noqa
    description='',
    long_description=long_description,
    long_description_content_type='text/markdown',

    packages=find_packages(exclude=["examples", "tests"]),
    zip_safe=False,  		    # dataset and __init__ use file

    install_requires=[
        "numpy>=1.14",
        "six",
        "termcolor>=1.1",
        "tabulate>=0.7.7",
        "tqdm>4.29.0",
        "msgpack>=0.5.2",
        "msgpack-numpy>=0.4.4.2",
        "pyzmq>=16",
        "psutil>=5",
        "subprocess32; python_version < '3.0'",
        "functools32; python_version < '3.0'",
    ],
    tests_require=['flake8'],
    extras_require={
        'all': ['scipy', 'h5py', 'lmdb>=0.92', 'matplotlib', 'scikit-learn'],
        'all: "linux" in sys_platform': ['python-prctl'],
    },

    # https://packaging.python.org/guides/distributing-packages-using-setuptools/#universal-wheels
    options={'bdist_wheel': {'universal': '1'}},
)
