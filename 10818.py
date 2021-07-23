n=int(input())

list=(list(map(int,input().split())))
min=list[0]
max=list[0]
for i in range(n):
    if list[i]<min:
        min=list[i]
    if list[i]>max:
        max=list[i]

print(min ,max)