x=int(input())
y=0
while(x):
    y=y*10+x%10
    x//=10
print(y)