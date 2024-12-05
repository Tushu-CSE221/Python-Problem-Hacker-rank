
n,m=map(int,input().split())

for i in range(int(n/2)): #upper part
    us='-'*(int(m/2)-1-3*i)
    sm='.|.'*(2*i+1)
    print(us+sm+us)



for i in range(1):#middle part
    us='-'*(int(m/2)-3-i)
    w="WELCOME"
    print(us+w+us)

for i in range(int(n/2)-1,-1,-1):#lower part
    us='-'*(int(m/2)-1-3*i)
    sm='.|.'*(2*i+1)
    print(us+sm+us)