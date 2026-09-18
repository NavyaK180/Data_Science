import numpy as np
N=np.array([1,2,3,4,5,6])
print(N)
P=np.array([[1,2,3],
           [4,5,6]])
print(P)
print(N.ndim)
#zeros and ones
P=np.zeros([1])
N=np.zeros([3,4])
print(N)
print(type(N))
#array indexing
a=np.array([12,23,34,45,56,67,78])
print(a[0])
print(a[5])
b=np.array([[1,2,3],
           [4,5,6]])

#negative indexing
P=np.array([1,2,3,4,5])
print(P[-1])
P=np.array([[1,2,3],
            [4,5,6]])
print(P[0,-1])
#array slicing
print(P[2:5])
print(P[:5])
print(P[4:])
#we can also include a step in array([start:end:step])
N=np.array([[1,2,3,4,5],
            [6,7,8,9,0]])
print(N[0,2:4])
P=np.array([[1,2,3,4,5,6],
            [7,8,9,3,2,1]])
print(P[0:2,2:5])
#array shape
N=np.array([1,2,3,4,5])
print(N)
print(N.ndim)
print(N.shape)
#array reshape
N=np.array([1,2,3,4,5,6])
a=N.shape
b=N.reshape(3,2)
print(a)
print(b)
#looping 1D array
n=np.array([1,2,3,4,5,6])
for x in n:
    print(x)
#looping 2D array
n=np.array([[1,2,3],
            [4,5,6],
            [7,8,9]])
for a in n:
    print(a)
#concatenation
n1=np.array([1,2,3,4])
n2=np.array([4,5,6,7])
n3=np.concatenate((n1,n2))
print(n3)
#splitting
print(np.array_split(n3,4))
sp=np.array_split(n3,4)
print(sp[0])
#searching
n1=np.array([4,2,3,4])
P=np.where(n1==4)
print(P)
#sorting
n1=np.array([4,2,3,1])
P=np.sort(n1)
print(P)
#sorting string array
n=np.array(['hi','java','pyth','app'])
print(np.sort(n))
#arithmetic operations
n1=np.array([1,2,3,4])
n2=np.array([4,5,6,7])
print(np.sum([n1,n2]))  # sum of 2 arrays
print(np.sum([n1,n2],axis=1))  # adds row wise elements
print(np.sum([n1,n2],axis=0)) # adds column wise elements
print(np.subtract(n1,n2)) #subtraction
print(np.multiply(n1,n2)) # multiplication
print(np.divide(n1,n2)) #division