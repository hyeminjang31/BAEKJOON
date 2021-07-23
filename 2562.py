
list=[0]*9

for i in range (9):
    list[i]=int(input())


max=list[0]
index=0
for i in range (9):
    if max<list[i]:
        max=list[i]
        index=i

print(max)
print(index+1)