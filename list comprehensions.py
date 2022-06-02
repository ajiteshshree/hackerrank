x = int(input())
y = int(input())
z = int(input())
n = int(input())
i=0
j=0
k=0
principle_list=[]
while i is not x+1:
    while j is not y+1:
        while k is not z+1:
            principle_list.append([i,j,k])
            k +=1
        k=0
        j+=1
    j=0
    i +=1
required_list=[x for x in principle_list if x[0]+x[1]+x[2] != n]
print(required_list)
#1
# print(principle_list)