# -*- coding: utf-8 -*-
"""cs361python.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rbJzUQlieWT8ot8d487WHBhgkfJd78WO
"""

5/3

5%3

5.0/3

5/3.0

5.2%3

2000.3**200

1.0+1.0-1.0

1.0+1.0e20-1.0e20

x= float(123)
print(x)

float('123')

float('123.23')

int(123.23)

int(float('123.23'))

int('123.23')

str(12)

str(12.2)

bool('a')

bool(0)

bool(0.1)

range(5)

type(range(5))

number_found=0
x=11
while number_found < 20:
  if x%5 ==0 and x%7 == 0 and x%11==0:
    print (x)
    number_found+=1
  x+=1

def  is_prime(n):
  if n<1:
    return False
  for x in range(2,n):
    if n%x==0:
      return False
  return True

is_prime(3)

is_prime(121)

def is_prime_new(n):
  if n<1:
    return False
  if n==2 or n==3:
    return True
  return ((n+1)/6)%1==0.0 or ((n-1)/6)%1==0.0

is_prime_new(100)

is_prime_new(131)

def range_prime(n):
  count=2
  if n<=1:
    return None
  while count<=n:
    bol= True
    for s in range (2,count):
      if count%s==0:
        bol=False
    if bol==True:
      print(count)
    count+=1

range_prime(60)

range_prime(9)

def num_prime(n):
  count=0
  max=999999
  for x in range(2,max):
    if count<n:
      bol =True
      for s in range(2,x):
        if x%s==0:
          bol=False
      if bol==True:
        print(x)
        count+=1

num_prime(16)

def print_list(n):
  for i in range(len(n)):
    print(n[i])

a=[1,2,3,4,5,6]
print_list(a)

def print_reverse_list(n):
  n.reverse()
  for i in range(len(n)):
    print(n[i])

a=[1,2,3,4,5,6,7]
print_reverse_list(a)

def length(n):
  num_length=0
  for x in n:
    num_length+=1
  print(num_length)

a=[]
length(a)

b=[1,2,3,4,5,6,7]
length(b)

a=[3,20,57,9,32]
b=a
b[1]=4
print(a[0])
print(a[1])
c=a[:]
c[2]=9
print(a[2])

def set_first_elem_to_zero(l):
  temp=l
  temp[0]=0
  return l

a=[3,5,6,90,78]
set_first_elem_to_zero(a)

def list_sublists(x):
  arr=[]
  for s in range(len(x)):
    for r in range(len(x[s])):
      arr.append(x[s][r])   
  return arr

a=[[2,3],[3,4]]
list_sublists(a)

import matplotlib.pyplot as plt
import math
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Function')
plt.axis([0,2,0,2])
X=[]
Y=[]
for i in range(3):
  X.append(i)
  Y.append(math.sin((math.degrees(i-2)))*math.sin((math.degrees(i-2)))
  *(math.e**-(i**2)))
plt.plot(X,Y,color='purple',linewidth=3)

def iteration_product(n):
  if n==[]:
    return None
  product=n[0]
  for i in range(1, len(n)):
    product*=n[i]
  return product

a=[5]
iteration_product(a)

def recursion_product(n):
  temp=n[:]
  if n==[]:
    return None
  if len(n)==1:
    return n[0]
  else:
    temp.pop()
    return n[len(n)-1]*recursion_product(temp)

a=[8]
recursion_product(a)

def fib(n):
  if n<=0:
    return 0
  if n==1:
    return 1
  else:
    return fib(n-1)+fib(n-2)

fib(6)

import re
file=open(r"C:\Users\xxlal\OverDrive\Desktop\testing.txt","r")
matches=re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+",text)
print (matches)

