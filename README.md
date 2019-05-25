# Tensorpack Dataflow

Tensorpack Dataflow is an **efficient** and **flexible** data
loading pipeline for deep learning, written in pure Python.

It's main features are:

1. **Highly-optimized for speed**.
	 Parallization in Python is hard.
	 Dataflow implements highly-optimized
	 parallel building blocks which gives you an easy interface to parallelize your workload.

2. **Written in pure Python**.
	 This allows it to be used together with any other Python-based library.


Dataflow is originally part of the [tensorpack library](https://github.com/tensorpack/tensorpack/)
and has been through 3 years of active development.
Given its independence of the rest of the tensorpack library, and
the high demand from users, it is now a separate library.

## Examples:
```python
import dataflow as D
d = D.ILSVRC12('/path/to/imagenet')  # produce [img, label]
d = D.MapDataComponent(d, lambda img: some_transform(img), 0)
d = D.MultiProcessMapData(d, nr_proc=10, lambda img, label: other_transform(img, label))
d = D.BatchData(d, 64)
d.reset_state()
for img, label in d:
	# ...
```

## Documentation:
### Tutorials:
1. [Basics](https://tensorpack.readthedocs.io/tutorial/dataflow.html)
1. [Write a Dataflow](https://tensorpack.readthedocs.io/tutorial/extend/dataflow.html)
1. [Efficient Dataflow](https://tensorpack.readthedocs.io/tutorial/efficient-dataflow.html)
### APIs:
1. [Built-in Dataflows](https://tensorpack.readthedocs.io/modules/dataflow.html)
1. [Built-in Datasets](https://tensorpack.readthedocs.io/modules/dataflow.dataset.html)

## Benchmarks:
TBA
