# Tensorpack DataFlow

Tensorpack DataFlow is an **efficient** and **flexible** data
loading pipeline for deep learning, written in pure Python.

Its main features are:

1. **Highly-optimized for speed**.
	 Parallelization in Python is hard and most libraries do it wrong.
	 DataFlow implements highly-optimized
	 parallel building blocks which gives you an easy interface to parallelize your workload.

2. **Written in pure Python**.
	 This allows it to be used together with any other Python-based library.

DataFlow is originally part of the [tensorpack library](https://github.com/tensorpack/tensorpack/)
and has been through 3 years of active development.
Given its independence of the rest of the tensorpack library, and
the high demand from users, it is now a separate library whose source code is synced with tensorpack.

Why would you want to use DataFlow instead of a platform-specific data loading solutions?
We recommend you to read
[Why DataFlow?](https://tensorpack.readthedocs.io/tutorial/philosophy/dataflow.html).

## Install:
```
pip install --upgrade git+https://github.com/tensorpack/dataflow.git
# or add `--user` to install to user's local directories
```
You may also need to install opencv, which is used by many builtin DataFlows.

## Examples:
```python
import dataflow as D
d = D.ILSVRC12('/path/to/imagenet')  # produce [img, label]
d = D.MapDataComponent(d, lambda img: some_transform(img), index=0)
d = D.MultiProcessMapData(d, num_proc=10, lambda img, label: other_transform(img, label))
d = D.BatchData(d, 64)
d.reset_state()
for img, label in d:
  # ...
```

## Documentation:
### Tutorials:
1. [Basics](https://tensorpack.readthedocs.io/tutorial/dataflow.html)
1. [Why DataFlow?](https://tensorpack.readthedocs.io/tutorial/philosophy/dataflow.html)
1. [Write a DataFlow](https://tensorpack.readthedocs.io/tutorial/extend/dataflow.html)
1. [Parallel DataFlow](https://tensorpack.readthedocs.io/tutorial/parallel-dataflow.html)
1. [Efficient DataFlow](https://tensorpack.readthedocs.io/tutorial/efficient-dataflow.html)

### APIs:
1. [Built-in DataFlows](https://tensorpack.readthedocs.io/modules/dataflow.html)
1. [Built-in Datasets](https://tensorpack.readthedocs.io/modules/dataflow.dataset.html)

## Support & Contributing

Please send issues and pull requests (for the `dataflow/` directory) to the
[tensorpack project](https://github.com/tensorpack/tensorpack/) where the source code is developed.
