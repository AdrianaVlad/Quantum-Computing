a=int(input())
b=int(input())
c=int(input())
delta=b*b-4*a*c
import math
x1=(-b+math.sqrt(delta))/(2*a)
print(x1)
x2=(-b-math.sqrt(delta))/(2*a)
print(x2)