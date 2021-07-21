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

## Console 
```py
from javascript import console, Array

console.clear()
console.error("Syntax Error!")
console.warn("Forgot an import!")
array = Array(['earth', 'venus'])
console.table(array)
```

![image](https://user-images.githubusercontent.com/61446939/126521684-669e4dd5-4263-4c5e-9cce-9c0e097759e3.png)
