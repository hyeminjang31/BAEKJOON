n=int(input())
for _ in range(n):
    score_list=list(map(int,input().split()))
    sum=0
    num=score_list[0]
    for i in range(num-1):
        sum+=score_list[i+1]
    everage=sum/num
    count=0
    for i in range(num-1):
        if score_list[i+1]>everage:
            count+=1
    print("{:.3f}%".format(count/num*100))
    
