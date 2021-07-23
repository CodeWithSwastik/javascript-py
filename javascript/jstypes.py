# Javascript-like data types
# This is unfinished as of now

# Ref: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects

import math

# Value Properties

Infinity = float("inf")
NaN = float("nan")

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
    DIGITS = "0123456789"
    if number[0] not in DIGITS + ".+-":
        return NaN

    f = ""
    encountered_period = False
    encountered_e = False
    encountered_plus_or_minus = False

    for char in number:
        if char == "." and encountered_period:
            break
        elif char == ".":
            encountered_period = True

        if char == "e" and encountered_e:
            break
        elif char == "e":
            encountered_e = True

        if char in "+-" and encountered_plus_or_minus:
            break
        else:
            encountered_plus_or_minus

        if char in "0123456789e.+-":
            f += char
        else:
            break
    try:
        return float(f)
    except ValueError:
        return NaN


def parseInt(number, radix=None):
    number = str(number).lower().strip()

    if radix is None:
        radix = 16 if (len(number) >= 2 and number[:2] == "0x") else 10
    else:
        radix = int(radix)

    if not number or radix < 2 or radix > 36:
        return NaN

    if radix == 16 and len(number) >= 2:
        if number[:2] == "0x":
            number = number[2:]
        elif number[:3] == "-0x":
            number = "-" + number[3:]

    DIGITS = "0123456789abcdefghijklmnopqrstuvwxyz"[:radix]
    if number[0] not in DIGITS + "+-":
        return NaN

    f = ""
    encountered_plus_or_minus = False
    for char in number:
        if char in "+-" and encountered_plus_or_minus:
            break
        else:
            encountered_plus_or_minus = True

        if char in DIGITS + "+-":
            f += char
        else:
            break

    if radix is None:
        radix = 16 if (len(f) > 2 and f[:2].lower() == "0x") else 10
    else:
        radix = int(radix)
    try:
        return int(f, radix)
    except:
        return NaN


class Object(object):
    def __init__(self, *args, **kwargs):
        for arg in args:
            self.__dict__.update(arg)
        self.__dict__.update(kwargs)

    def __getitem__(self, name):
        return self.__dict__.get(name, None)

    def __setitem__(self, name, val):
        return self.__dict__.__setitem__(name, val)

    def __delitem__(self, name):
        if self.__dict__.has_key(name):
            del self.__dict__[name]

    def __getattr__(self, name):
        return self.__getitem__(name)

    def __setattr__(self, name, val):
        return self.__setitem__(name, val)

    def __delattr__(self, name):
        return self.__delitem__(name)

    def __iter__(self):
        return self.__dict__.__iter__()

    def __repr__(self):
        return self.__dict__.__repr__()

    def __str__(self):
        return self.__dict__.__str__()

    def __add__(self, other):
        val = other.toString() if hasattr(other, "toString") else str(other)
        return self.toString() + val

    def hasOwnProperty(self, prop):
        return prop in self

    @staticmethod
    def assign(target, *sources):
        for source in sources:
            for key in iter(source):
                target[key] = source[key]

        return target

    @staticmethod
    def entries(obj):
        return iter(obj.__dict__.items())

    def toString(self):
        return "[object Object]"


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


class Map(dict):
    def __repr__(self):
        f = "{"
        for k, v in self.items():
            f += f" {k} => {v},"
        f = f[:-1] + " }"
        return f"Map({self.size}) {f}"

    def __getattr__(self, attr):
        try:
            return self[attr]
        except KeyError:
            raise None

    def clear(self):
        for key in self.keys():
            self.delete(key)

    def set(self, key, value):
        self[key] = value
        return self

    def delete(self, key):
        del self[key]

    def has(self, key):
        return key in self

    def forEach(self, func):
        for key, value in self.items():
            func(*[key, value])

    @classmethod
    def from_dict(cls, data: dict):
        self = cls.__new__(cls)
        for key, value in data.items():
            self[key] = value
        return self

    @property
    def size(self):
        return len(self)

    def entries(self):
        return iter([k, v] for k, v in self.items())


class Math:
    E = math.e
    LN2 = math.log(2)
    LN10 = math.log(10)
    LOG2E = math.log(math.e, 2)
    LOG10E = math.log(math.e, 10)
    PI = math.pi
    SQRT1_2 = math.sqrt(1 / 2)
    SQRT_2 = math.sqrt(2)

    @staticmethod
    def floor(x):
        return math.floor(x)

    @staticmethod
    def random():
        return __import__("random").random()


import datetime


class Date:
    def __init__(self, date=None):
        self.date = date or datetime.datetime.now()
        self.utc_date = datetime.datetime.utcfromtimestamp(self.date.timestamp())

    def getDate(self):
        return self.date.day

    def getDay(self):
        return self.date.weekday()

    def getFullYear(self):
        return self.date.year

    def getHours(self):
        return self.date.hour

    def getMilliseconds(self):
        return Math.floor(self.date.microsecond / 1000)

    def getMinutes(self):
        return self.date.minute

    def getMonth(self):
        return self.date.month

    def getSeconds(self):
        return self.date.second

    def getTime(self):
        return Math.floor(self.date.timestamp() * 1000)

    def getTimezoneOffset(self):
        seconds_offset = self.date - self.utc_date
        return int(seconds_offset.seconds / 60)

    def getUTCDate(self):
        return self.utc_date.day

    def getUTCDay(self):
        return self.utc_date.weekday()

    def getUTCFullYear(self):
        return self.utc_date.year

    def getUTCHours(self):
        return self.utc_date.hour

    def getUTCMilliseconds(self):
        return Math.floor(self.utc_date.microsecond / 1000)

    def getUTCMinutes(self):
        return self.utc_date.minute

    def getUTCMonth(self):
        return self.utc_date.month

    def getUTCSeconds(self):
        return self.utc_date.second

    @staticmethod
    def now():
        return Date().getTime()

    @staticmethod
    def parse(dateString):
        # TODO
        return Date(datetime.datetime.fromisoformat(dateString)).getTime()

    def toString(self):
        aware = self.date.replace(tzinfo=datetime.timezone.utc).astimezone(tz=None)
        return self.date.strftime('%a %b %d %Y %H:%M:%S ') + aware.strftime(f'GMT%z (%Z)')

    def __repr__(self):
        return self.toString()
    
    def __str__(self):
        return self.toString()

class JSON:
    @staticmethod
    def parse(jsonString):
        return __import__("json").loads(jsonString)

    @staticmethod
    def stringify(obj):
        return __import__("json").dumps(obj)


import re


class RegExp:
    def __init__(self, pattern, flags=""):
        self.source = pattern
        self.flags = flags.lower()

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f"/{self.source}/{self.flags}"

    @property
    def dotAll(self):
        return "s" in self.flags

    @property
    def global_(self):
        return "g" in self.flags

    @property
    def hasIndices(self):
        return "d" in self.flags

    @property
    def ignoreCase(self):
        return "i" in self.flags

    @property
    def unicode(self):
        return "u" in self.flags

    def test(self, string):
        return bool(re.search(self.source, string))

    def toString(self):
        return self.__str__()

    def exec(self, string):
        return re.findall(self.source, string)
