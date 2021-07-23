n=int(input())
score=(list(map(int,input().split())))
max=score[0]
count=0
for i in range(n):
    if max<score[i]:
        max=score[i]

for i in range(n):
    score[i]=score[i]/max*100
    count=count+score[i]

print(count/n)