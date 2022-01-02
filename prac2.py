from array import *

values = array('i', [
    13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1
])

for i in range(len(values)):
    print(values[i])
# [12:51 PM]
# works same as above
from array import *

values = array('i', [
    13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1
])

for e in values:
    print(e)
# [12:54 PM]
# how to get first and last elements of python list https://www.askpython.com/python/list/get-first-last-elements-python-list
# [1:00 PM]
# duplicating an array
from array import *

values = array('i', [
    13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1
])

newArray = array(values.typecode, (a*a for a in values))

for e in newArray:
    print(e)

# squid — Yesterday at 2:34 PM
from array import *

values = array('i', [])

lengthOfArray = int(input("enter the length of the array"))

for i in range(lengthOfArray):
    value = int(input("enter the value"))
    values.append(value)

print(values)

valueToSearch = int(input("enter value you want to search for"))
count = 0

for e in values:
    if e==valueToSearch:
        print(count)
        break

    count+=1
# [2:37 PM]
# start of video https://www.youtube.com/watch?v=kQDxmjfkIKY&ab_channel=CodDevX

#string
x = 'cookie'
#list
x = ['joe', 'bobby', 'tasha']
print(x[1])
# tuple
x = ('barbra', 'banana', 'bonbon')
# (edited)
# [2:41 PM]
x = 'thatsexymilf'
print(x[3:]) # goes until nothing or the last item
print(x[:4]) # goes until the beginning or the first item
# [2:45 PM]
x = 'bug'
print('u' in x) # returns boolean

y = ['tasha', 'is', 'sexyaf']
print('is' not in y)

z = ('mary', 'is', 'tightaf')
print('is' in z)
# [2:49 PM]
# go through items in sequence
x=[4,9,2]
for item in x: print(item)

# get both the item and index of the item
y=[2,9,8]
for index, item in enumerate(y): print(index, item)
# [2:53 PM]
# gets the length of items
y=[1,4,2]
print(len(y))

# gets the smallest
x=[9,10,3]
print(min(x))

# gets the biggest
a=[34, 42, 1034]
print(max(a))

# squid — Yesterday at 3:08 PM
y=[5,3,9,6]
print(sum(y))
print(sum(y[3:])) # combine sum with slice
# [3:10 PM]
# prints the sorted 
# does not return the same list, created a new list with sorted

x='bug'
print(sorted(x))

y=['tasha', 'fuck', 'me']
print(sorted(y))
#
# [3:14 PM]
# sorts by the 1 indez of each item
z=('tasha', 'cum', 'you')
print(sorted(z, key=lambda y: y[1]))
# [3:16 PM]
# gets the count
x='tashafuckme'
print(x.count('a'))

y=['tasha', 'cum', 'cum', 'onme']
print(y.count('cum'))
# [3:18 PM]
# gets idex
x='hippopot'
print(x.index('p'))

y=['tasha', 'wtf', 'udoing']
print(y.index('wtf'))
# [3:19 PM]
# unpacking into variables
x=['my', 'yams', 'ishott']
a, b, c = x
# [3:23 PM]
# unpacking into variables
x=['my', 'yams', 'ishott']
a, b, c = x
print(b)

# squid — Yesterday at 3:32 PM
# list comprehension
a=[m for m in range(8)] # counts from 0 to 7
print(a)
b=[i**2 for i in range(10) if i>4] # goes until 10 for every number after 4
print(b)
# [3:35 PM]
# deletes item from list
x=[5,4,10,9]
del(x[3])
print(x)

# adds item onto list
y=[45,2,9]
y.append(84)
print(y)

# squid — Yesterday at 3:45 PM
# extend - append a sequence to a list
m=[4,56,109]
j=[42,56,123,4]
m.extend(j)
print(m)
# [3:52 PM]
# inserts at said index
b=[5,2,0,9]
b.insert(1, 943)
print(b)
b.insert(1, [
    'a',
    'b',
    'c'
])
print(b)
# [3:53 PM]
# pops off the last item
x=[45,6,90,20]
x.pop()
print(x)
print(x.pop())
# [3:56 PM]
# removes the first spesified but not all
x=[5,3,3,45,9]
x.remove(3)
print(x)

# reverses the list
x.reverse()
print(x)

# sorting list
x.sort()
print(x)
# sorts and reverses
x.sort(reverse=True)
print(x)
# [4:00 PM]
# tuples - cannot be changed or add items
# useful for fixed data
x=()
x=1,2,3
x=2, 
print(x, type(x))

myList=[2,3,4]
x=tuple(myList)
print(x, type(x))
# [4:02 PM]
y=([1,2], 3)
del(y[0][0]) # deletes first index of list in the first index of tuple

# squid — Yesterday at 4:15 PM
# example of recurssion
def getNthFib(n):
    if n==1:
        return 0
    if n<=3:
        return 1

    return getNthFib(n-1) + getNthFib(n-2)

print(getNthFib(1))
print(getNthFib(2))
print(getNthFib(3))
print(getNthFib(4))
print(getNthFib(5))
print(getNthFib(6))
#  (edited)

# squid — Yesterday at 4:23 PM
def getNthFib(n, calculated={1:0, 2:1., 3:1}):
    # storing values into new hash table or dictionary
    if n in calculated:
        return calculated[n]

    calculated[n]=getNthFib(n-1, calculated)+getNthFib(n-2, calculated)
    return calculated[n]

# squid — Yesterday at 5:48 PM
# sets
# - store non-duplicate items
# - very fast access vs lists
# - math set ops (union, intersect)
# - sets are unorded 

x={3,5,2,9, 35, 35}
print(x)

y=set()
y.add(9)
y.add(7)
b=1,34,4,5
y.remove(7)
y.add(b)

print(y)

list1=[1,2,3,4]
z=set(list1)
print(z)
# [5:55 PM]
# mathematical set operations
# and: &
# or: |
# symmetric difference: ^
# subset: <=
# superset: >=

s1={1,2,3,4}
s2={4,6,7,8}
print(s1 & s2) # they both have of value of
print(s1 | s2) # all the items in either set
print(s1 ^ s2) # in one set or the other but not in both
print(s1 - s2) 
print(s1 <= s2) 
print(s1 >= s2)

# squid — Yesterday at 6:06 PM
# dictionaries
# - key and value pairs
# - associate array, like java hashmap
# - dicts are unordered

x={'pork': 25.72, 'pocketpussy': 78.91, 'bananas': 1.99}

# print key
for i in x.keys():
    print(i)

# way 1 of print key and value
for key in x:
    print(key, x[key])
# way 2 of printing key and value
for key, value in x.items():
    print(key, value)
# [6:06 PM]
# loop through dictionary https://www.makeuseof.com/how-to-loop-through-a-python-dictionary/#:~:text=%20How%20to%20Loop%20Through%20a%20Dictionary%20in,iterative%20equivalent%20to%20using%20the%20sum...%20More%20

# squid — Yesterday at 8:05 PM
x={'pork': 25.72, 'pocketpussy': 78.91, 'bananas': 1.99}
# add item to
x['srhrimp']=38.72
print(x)
# delete item from 
del(x['pocketpussy'])
# delete all items from
x.clear()
print(x)
# delete
del(x)
# [8:06 PM]
x={'pork': 25.72, 'pocketpussy': 78.91, 'bananas': 1.99}
# keys
print(x.keys())
# values
print(x.values())
# items
print(x.items())
# [8:08 PM]
x={'pork': 25.72, 'pocketpussy': 78.91, 'bananas': 1.99}
# iterate through items

for key in x:
    print(key, x[key])

for k, v in x.items():
    print(k, v)

# squid — Yesterday at 8:24 PM
# get values within a range
under_10=[x for x in range(10)]
print('under_10: '+str(under_10))

# get squared values
squares=[x**2 for x in under_10]
print('squares: '+str(squares))

# get odd numbers using mod
odds=[x for x in range(10) if x%2==1]
print('odds: '+str(odds))

# get multiples of 10
ten_x=[x * 10 for x in range(10)]
print('ten_x'+str(ten_x))

# get all numbers from a string
# TODO: figure out why it's not printing anything
s='i love jennifers pussy'
nums=[x for x in s if x.isnumeric()]
print('nums: '+''.join(nums))
# [8:28 PM]
# get index of a list item
names=['cosby','fluff','milk']
idx=[k for k, v in enumerate(names) if v=='fluff']
print('index = '+str(idx[0]))

# delete item from list
letters=[x for x in 'abcdefg']
random.shuffle(letters)
leters=[a for a in letters if a!='c']
print(letters,leters)

# squid — Yesterday at 8:36 PM
# stacks
# - can only access from from the top
# OPERATIONS
# -> pop: pop item off top of stack
# -> push: push item ontop of stack
# -> peek: get item on top of stack without removing it
# -> clear: remove all items from stack, empty it out

myStack=list()
myStack.append(4)
myStack.append(9)
myStack.append(3)
print(myStack)
# [8:41 PM]
class Stack():
    def __init__(self):
        self.stack=list()
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        if len(self.stack)>0:
            return self.stack.pop()
        else:
            return None
    def peek(self):
        if len(self.stack)>0:
            return self.stack[len(self.stack)-1]
        else:
            return None
    def __str__(self):
        return str(self.stack)

stack=Stack()
stack.push(1)
stack.push(3)
stack.push(9)
print(stack)
print(stack.pop())
print(stack.peek())
print(stack.pop())

# squid — Yesterday at 11:07 PM
# day 2 python complete.

# squid — Yesterday at 11:36 PM
# basic class
class Fruit:
    def __init__(self):
        self.name = 'appple'
        self.color = 'red'

fruit=Fruit()
print(fruit.color)
#  (edited)

# squid — Yesterday at 11:45 PM
class Fruit:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    def details(self):
        print('my '+self.name+' is '+self.color)

fruit=Fruit('kiwi', 'green')
fruit.details()
# January 2, 2022

# squid — Today at 12:06 AM
# class practice, gettin it
class Foo:
    def show(self):
        print('hi')

def addAttribute(self, num):
    self.z=num

Test=type('Test', (Foo,), {'x':5, 'addAttribute': addAttribute})
t=Test()
t.addAttribute(4)
print(t.z)
t.show()
# [12:12 AM]
class Foo:
    def show(self, string):
        print(string)

    def addNumber(self, number):
        self.z=number

Test=type('Test', (Foo,), {'x':5,})
t=Test()
t.addNumber(4)
print(t.z)
t.show('bitcheslovemebuttheysorry')
# [12:18 AM]
class Foo:
    def show(self, string1, string2):
        print(string1 + string2)

    def addNumber(self, number):
        self.z=number

Test=type('Test', (Foo,), {'x':5,})
t=Test()
t.addNumber(4)
print(t.z)
t.show('bitcheslovemebuttheysorry ', 'tashaiwanfuk')

# squid — Today at 12:31 AM
class Meta(type):
    def __new__(self, className, bases, attributes):
        print(attributes)

        a={}
        for name, value in attributes.items():
            if name.startswith('__'):
                a[name]=value
            else:
                a[name.upper()]=value
        print(a)
        return type(className, bases, a)

class Dog(metaclass=Meta):
    x=5
    y=8

    def hello(self, string):
        print(string)

d=Dog()
print(d.HELLO('bitchesLoveME'))

# squid — Today at 12:41 AM
# my class i created from scratch lets go
class Sword():
    def __init__(self, str, dur, pow, cha):
        self.str=str
        self.dur=dur
        self.pow=pow
        self.cha=cha

myFairLady=Sword(110, 6, 55, 25)
def addPower(self):
    if self.str>=6:
        print('myballsisonmydick')
addPower(myFairLady)

# squid — Today at 12:50 AM
# oh wow
import time

class Sword():
    def __init__(self, str, dur, pow, cha):
        self.str=str
        self.dur=dur
        self.pow=pow
        self.cha=cha

myFairLady=Sword(110, 6, 55, 25)
def addPower(self):
    if self.dur>=6:
        self.str+=self.pow
        print(self.str)
        time.sleep(6)
        self.str-=self.pow
        print(self.str)

addPower(myFairLady)