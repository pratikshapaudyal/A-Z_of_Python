# Generators

## What is a generator?

A generator lazily creates values.
They are very useful when working with large data sets.

A generator will use the 'yield' keyword rather than 'return'

## Code example
Running the [generator_fibonacci.py](https://github.com/pratikshapaudyal/A-Z_of_Python/blob/develop/G/generator_fibonacci.py) example in an interactive python terminal:
``` bash
>>> import generator_fibonacci
>>> g = generator_fibonacci.fib6(3)
>>> next(g)
0
>>> next(g)
1
>>> next(g)
1
>>> next(g)
2
>>> next(g)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
>>>
```