# Javascript-like data types
# This is unfinished as of now

class Array(list):

    def __init__(self, *args, **kwargs):
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

    def copyWithin(self, target, start = 0, end = None):
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
            if not func(*[elem, i, self][:func.__code__.co_argcount]):
                return False
        return True

    def fill(self, value, start = 0, end = None):
        if end is None:
            end = len(self)

        for i in range(start, end):
            self[i] = value
        
        return self
        
    def filter(self, func):
        new = []
        for i, elem in enumerate(self):
            if func(*[elem, i, self][:func.__code__.co_argcount]):
                new.append(elem)
        return Array(new)
                    
    def find(self, func):
        for i, elem in enumerate(self):
            if func(*[elem, i, self][:func.__code__.co_argcount]):
                return elem
        return None

    def findIndex(self, func):
        for i, elem in enumerate(self):
            if func(*[elem, i, self][:func.__code__.co_argcount]):
                return i
        return -1         
    
    def flat(self, depth = 1):
        if depth == 0:
            return Array(self)
        new = Array()
        for elem in self:
            if isinstance(elem, list):
                new += Array(elem).flat(depth=depth-1)
            else:
                new.append(elem)
        
        return new

    def flatMap(self, func):
        # TODO
        pass

    def forEach(self, func):
        for i, elem in enumerate(self):
            func(*[elem, i, self][:func.__code__.co_argcount])

    @staticmethod
    def from_(array_like):
        return Array(array_like)

    def includes(self, element, fromIndex = 0):
        return element in self[fromIndex:]
    
    def indexOf(self, element, fromIndex = 0):
        return self.index(element, fromIndex) if self.includes(element, fromIndex) else -1

    @staticmethod
    def isArray(obj):
        return isinstance(obj, Array)

    def join(self, separator = ','):
        new = Array()
        for elem in self:
            new.append(str(elem if elem not in [None, []] else ''))
        return separator.join(new)

    def keys(self):
        return range(len(self))

    def lastIndexOf(self, element, fromIndex = None):
        length = len(self) - 1
        if fromIndex is None:
            fromIndex = length
        return (length - self[fromIndex::-1].index(element)) if self.includes(element, length - fromIndex) else -1

    def map(self, func):
        new = Array()
        for i, elem in enumerate(self):
            new.append(func(*[elem, i, self][:func.__code__.co_argcount]))
        return new        

    @staticmethod
    def of(*objs):
        return Array(objs)

    def pop(self):
        removed_element = self[-1] if self.length else None
        self = self[:-1]
        return removed_element