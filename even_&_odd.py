a=int(input())
i=1
list=[]
while i<100:
    c=a%10
    a=a/10 
    if c == 0:
        break
    list.append(c)
    i=i+1

index=len(list)-1
while index>=0:
    if list[index]%2==0:
        print str(list[index]),"is even no"
    else:
        print str(list[index]),"is odd no"
    index=index-1