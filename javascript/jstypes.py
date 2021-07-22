# Javascript-like data types
# This is unfinished as of now

# Ref: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects

import math

# Value Properties

Infinity = float('inf')
NaN = float('nan')

# Built-in methods

def isFinite(number):
    if number is None:
        return True
    number = float(number)
    return not (abs(number) == Infinity or number == NaN)
    
def isNaN(number):
    math.isnan(number)

def parseFloat(number):
    number = str(number).strip()
    if not number:
        return NaN
    DIGITS = '0123456789'
    if number[0] not in DIGITS+'.+-':
        return NaN

    f = ''
    encountered_period = False
    encountered_e = False
    encountered_plus_or_minus = False


    for char in number:
        if char == '.' and encountered_period:
            break
        elif char == '.':
            encountered_period = True

        if char == 'e' and encountered_e:
            break
        elif char == 'e':
            encountered_e = True

        if char in "+-" and encountered_plus_or_minus:
            break
        else:
            encountered_plus_or_minus

        if char in '0123456789e.+-':
            f += char
        else:
            break
    try:
        return float(f)
    except ValueError:
        return NaN

def parseInt(number, radix = None):
    number = str(number).lower().strip()

    if radix is None:
        radix = 16 if (len(number) >= 2 and number[:2] == '0x') else 10
    else:
        radix = int(radix)

    if not number or radix < 2 or radix > 36:
        return NaN

    if radix == 16 and len(number) >= 2:
        if number[:2] == '0x':
            number = number[2:]
        elif number[:3] == '-0x':
            number = '-' + number[3:]
        
    DIGITS = '0123456789abcdefghijklmnopqrstuvwxyz'[:radix]
    if number[0] not in DIGITS+'+-':
        return NaN

    f = ''
    encountered_plus_or_minus = False
    for char in number:
        if char in "+-" and encountered_plus_or_minus:
            break
        else:
            encountered_plus_or_minus = True

        if char in DIGITS+'+-':
            f += char
        else:
            break

    if radix is None:
        radix = 16 if (len(f) > 2 and f[:2].lower() == '0x') else 10
    else:
        radix = int(radix)
    try:
        return int(f, radix)
    except:
        return NaN

class Array(list):
    def __init__(self, *args, **kwargs):
        if len(args) > 1:
            super().__init__(args, **kwargs)
        else:
            super().__init__(*args, **kwargs)
            
        

    @property
    def length(self):
        return self.__len__()

    def at(self, index: int):
        return self[index]

    def concat(self, *args):
        new = self
        for arg in args:
            new += arg
        return Array(new)

    def copyWithin(self, target, start=0, end=None):
        if end is None:
            end = len(self)
        i = target
        for j in range(start, end):
            self[i] = self[j]
            i += 1

        return self

    def entries(self):
        return enumerate(self)

    def every(self, func):
        for i, elem in enumerate(self):
            if not func(*[elem, i, self][: func.__code__.co_argcount]):
                return False
        return True

    def fill(self, value, start=0, end=None):
        if end is None:
            end = len(self)

        for i in range(start, end):
            self[i] = value

        return self

    def filter(self, func):
        new = []
        for i, elem in enumerate(self):
            if func(*[elem, i, self][: func.__code__.co_argcount]):
                new.append(elem)
        return Array(new)

    def find(self, func):
        for i, elem in enumerate(self):
            if func(*[elem, i, self][: func.__code__.co_argcount]):
                return elem
        return None

    def findIndex(self, func):
        for i, elem in enumerate(self):
            if func(*[elem, i, self][: func.__code__.co_argcount]):
                return i
        return -1

    def flat(self, depth=1):
        if depth == 0:
            return Array(self)
        new = Array()
        for elem in self:
            if isinstance(elem, list):
                new += Array(elem).flat(depth=depth - 1)
            else:
                new.append(elem)

        return Array(new)

    def flatMap(self, func):
        new = self
        return new.map(func).flat()

    def forEach(self, func):
        for i, elem in enumerate(self):
            func(*[elem, i, self][: func.__code__.co_argcount])

    @staticmethod
    def from_(array_like):
        return Array(array_like)

    def includes(self, element, fromIndex=0):
        return element in self[fromIndex:]

    def indexOf(self, element, fromIndex=0):
        return (
            self.index(element, fromIndex) if self.includes(element, fromIndex) else -1
        )

    @staticmethod
    def isArray(obj):
        return isinstance(obj, Array)

    def join(self, separator=","):
        new = Array()
        for elem in self:
            new.append(str(elem if elem not in [None, []] else ""))
        return separator.join(new)

    def keys(self):
        return range(len(self))

    def lastIndexOf(self, element, fromIndex=None):
        length = len(self) - 1
        if fromIndex is None:
            fromIndex = length
        return (
            (length - self[fromIndex::-1].index(element))
            if self.includes(element, length - fromIndex)
            else -1
        )

    def map(self, func):
        new = Array()
        for i, elem in enumerate(self):
            new.append(func(*[elem, i, self][: func.__code__.co_argcount]))
        return new

    @staticmethod
    def of(*objs):
        return Array(objs)

    def pop(self):
        removed_element = self[-1] if self.length else None
        self = self[:-1]
        return removed_element

    def push(self, *elems):
        for elem in elems:
            self.append(elem)

        return self.length

    def reduce(self, func, initialValue=None):
        if len(self) == 0 and initialValue is None:
            raise TypeError("Reduce of empty array with no initial value")

        acc = initialValue or self[0]
        if len(self) == 0:
            return acc
        curVal = 1 if acc == self[0] else 0
        for i, elem in enumerate(self[curVal:]):
            acc = func(*[acc, elem, i + curVal, self][: func.__code__.co_argcount])
        return acc

    def reduceRight(self, func, initialValue=None):
        if len(self) == 0 and initialValue is None:
            raise TypeError("Reduce of empty array with no initial value")

        acc = initialValue or self[-1]
        if len(self) == 0:
            return acc
        curVal = -2 if acc == self[-1] else -1
        for i, elem in enumerate(self[curVal::-1]):
            acc = func(
                *[acc, elem, self.length - i + curVal, self][
                    : func.__code__.co_argcount
                ]
            )
        return acc

    def reverse(self):
        super().reverse()
        return self

    def shift(self):
        removed_element = self[0] if self.length else None
        self = self[1:]
        return removed_element

    def slice(self, start=0, end=None):
        if end is None:
            end = self.length
        return self[start:end]

    def some(self, func):
        for i, elem in enumerate(self):
            if func(*[elem, i, self][: func.__code__.co_argcount]):
                return True
        return False

    def sort(self, func):
        # TODO
        super().sort()
        return self

    def splice(self, start, delCount=None, *items):

        deleted = Array()
        if delCount is None or delCount > self.length - start:
            delCount = self.length - start

        for _ in range(delCount):
            deleted.append(super().pop(start))

        for i, item in enumerate(items):
            super().insert(i + start, item)

        return deleted

    def toString(self):
        return self.join()

    def unshift(self, *items):
        self = Array(items) + self
        return self.length

    def values(self):
        return iter(self)

class Math:
    E = math.e
    LN2 = math.log(2)
    LN10 = math.log(10)
    LOG2E = math.log(math.e, 2)
    LOG10E = math.log(math.e, 10)
    PI = math.pi
    SQRT1_2 = math.sqrt(1/2)
    SQRT_2 = math.sqrt(2)

    @staticmethod
    def floor(x):
        return math.floor(x)

    @staticmethod
    def random():
        return __import__('random').random()