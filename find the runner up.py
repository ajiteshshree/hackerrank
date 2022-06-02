n=int(input())
a=input().split()
max=-999
for i in a:
    i=int(i)
    if i>max:
        max=i
b=[x for x in a if int(x) != max]
max=-999
for k in b:
    k=int(k)
    if k>max:
        max=k
print(max)

