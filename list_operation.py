n=int(input())
mylist=[]
ll=[]
while(n!=0):
    data=input().split()
    op=data[0]
    ll=list(map(int,data[1:]))
    if(op=="insert"):
        mylist.insert(ll[0],ll[1])
    elif(op=="append"):
        mylist.append(ll[0])
    elif(op=="remove"):
        mylist.remove(ll[0])
    elif(op=="print"):
        print(mylist)
    elif(op=="sort"):
        mylist.sort()
    elif(op=="pop"):
        mylist.pop()
    elif(op=="reverse"):
        mylist.reverse()
    n-=1