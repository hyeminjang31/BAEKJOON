n=int(input())
count=0
N=n
while True:  
    if(n<10):
        n=10*n+n
        
        count+=1
          
    else:
        a=n//10
        b=n%10
        c=a+b
        n=10*b+c%10        
        count+=1
        
    if n==N:
        break

print(count)