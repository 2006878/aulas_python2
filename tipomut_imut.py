'''d=[1,2,3,4,5]
print(d)
d[3] = 8
print(d)

a=3
b=a
print('a = ', a)
print('b = ', b)
a=6
print('a = ', a)
print('b = ', b)


a= [3,4,5]
b = a
print('a= ', a)
print('b= ', b)
b[1]=8
print('a= ', a)
print('b= ', b)
'''
def g(x):
    x=5

a=3
print(a)
g(a)
print(a)    

def h(lst):
    lst[0] = 5

mylist = [3,6,9,12]
print(mylist)
h(mylist)
print(mylist)
