import numpy as np

a=np.array([1,2,3,4])               #array of rank 1
b=np.array([[1,2,3,4],[5,6,7,8]])   #array of rank 2
print(b)                            #access array
print(b[1,2])                       #access an element
print(b.ndim)                       #access the rank
print(b.shape)                      #access rows and coloumns
print(b.size)                       #access no. of elements
print(type(b))                      #access element type

c=np.ones((3,2))                    #array of 1's
print(c)
d=np.zeros((2,3))                   #array of 0's
print(d)
e=np.random.random((3,4))           #array of random values
print(e)
f=np.full((2,2),13,dtype=np.float32)                 #array filled with constants
print(f)
g=np.identity(3)                    #identity array
print(g)
h=np.empty((4,3))                   #array of uninitialised elements
print(h)
i=b.copy()                          #copy array
print(i)

j=np.arange(0,11,2)                 #np.arange(start,stop,step)
print(j)
k=np.arange(6)                      #np.arange(start=1,stop,step=1)
print(k)
l=np.linspace(0,10,8)               #np.linspace(start,end,numberofvaluesbetweenlimits)
print(l)

m=np.arange(10)
print(m.shape)                      #(10,)
print(m)                            #[0 1 2 3 4 5 6 7 8 9]
m.resize(2,5)                       #modifies the original array(resizes it)
print(m.shape)                      #(2,5)
print(m)                            #[0 1 2 3 4]
                                    #[5 6 7 8 9]
print(m.reshape(5,2))               #returns a new array with modified shape
print(m.shape)                      #(2,5)
print(m.ravel())                    #returns a new flattened array  [0 1 2 3 4 5 6 7 8 9]
print(m.shape)                      #(2,5)
print(m.transpose())                #retuurns a new transpose array

n=np.arange(8)
o=n[0:7:2]                          #n[start:stop:step]
print(o)
p=n[:5]                             #element 0 to element 5
print(p)
q=n[4:]                             #from element 4 on
print(q)
r=np.array([[1,2,3,4],[3,4,5,6]])
print(r[0:2,2])                     #returns third element in first two rows
print(r[...,1])                     #returns second element in all rows
print(r[:,3])                       #returns fourth element in all rows

s=np.array([[9,8,7,6],[7,6,5,4]])
print(np.add(r,s))
print(np.remainder(s,r))
print(np.subtract(s,r))
print(np.divide(s,r))               #returns quotient in decimal
print(np.power(s,r))
print(s>7)                          #returns true or false
print(np.exp(s))
print(np.sqrt(s))                   #np.around(), np.trunc(), np.floor(), np.ceil(), np.log()

print(np.sum(s))                    #52  , np.min(s), np.max(s), np.mean(s), np.median(s)
print(s.sum(axis=0))                #[16 14 12 10]   sum of all colomns and axis=1 for rows
print(np.corrcoef(s))               #correlation coefficient
print(np.cumsum(s))                 #cumilative sum  [ 9 17 24 30 37 43 48 52]
print(np.std(s))                    #standard deviation     1.5    s.std()

one_d=np.array([[10]])
two_d=np.array([[1,2,3,4],[5,6,7,8]])
three_d=np.ones((3,3))
print(np.add(one_d,two_d))          #[[11 12 13 14]
                                    # [15 16 17 18]]
print(np.add(one_d,three_d))        #[[11. 11. 11.]
                                    # [11. 11. 11.]
                                    # [11. 11. 11.]]










