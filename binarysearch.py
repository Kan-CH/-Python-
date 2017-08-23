#coding:utf-8
'''class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self"""
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
           Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'

    def intersect(self, other):
        return list(set(self.vals).intersection(set(other.vals)))

s1 = intSet([1,2,3])
s2 = [3,5]
print s1.intersect(s2)'''
'''
def generator1():
    if True:
        yield 1

def generator2():
    if False:
        yield 1

g1 = generator1()
g2 = generator2()

print type(g1)
print type(g2)
print g1.next()
print g2.next()
'''
'''
animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

print biggest(animals)
'''
def binarysearch(list,key):
    list.sort()
    lo = 0
    hi = len(list)-1
    while lo <= hi:
        mid = lo + (hi - lo)/2
        if key < list[mid]:
            hi = mid
        elif key > list[mid]:
            lo = mid
        else:
            return mid
    return -1



print(binarysearch([5, 2, 9, 6, 1], 6))
