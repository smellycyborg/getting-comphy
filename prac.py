from array import *

values = array('i', [
    13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1
])

newArray = array(values.typecode, (a*a for a in values))

for e in newArray:
    print(e)
