# Javascript.py

This package lets you use javascript like objects in python.

## Installation

Stable version:

```
pip install javascriptpy
```

Working version:

```
pip install git+https://github.com/CodeWithSwastik/javascript-py
```

## Example Usage

```python
from javascript import *

array = Array('apple', 'orange', 'cherry')
index = Math.floor(Math.random()*array.length)

console.info('Random element:',array[index])
console.table(array)
```

## Console

```py
from javascript import console, Array

console.clear()
console.error("Syntax Error!")
console.warn("Forgot an import!")
console.table(Array(['earth', 'venus']))
```

![image](https://user-images.githubusercontent.com/61446939/126521684-669e4dd5-4263-4c5e-9cce-9c0e097759e3.png)

## What's new?

- Added window methods like alert, prompt, confirm
- Added Map Object
- Added setTimeout, setInterval, clearTimeout, clearInterval
