lambda functions or anynmous functions
minus= lambda x,y:x-y
print(minus(9,5))
plus = lambda x,y: x+y
print(plus(3,5))
divide= lambda x,y: x/y
print(divide(9,3))
multiply= lambda x,y: x*y
print(multiply(4,6))
def a_first(a):
     return a[1]
a=[[1,14],[5,6],[8,23]]
a.sort(key=a_first)
print(a)
