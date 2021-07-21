# Javascript.py

This package lets you use javascript like objects in python.

## Installation

Stable version:

```
pip install javascript.py
```

Working version:

```
pip install git+https://github.com/CodeWithSwastik/javascript-py
```

## Example Usage

```python
from javascript import console, Array

array = Array([1,2,3])
console.log(array.find(lambda x: x > 2))
```
