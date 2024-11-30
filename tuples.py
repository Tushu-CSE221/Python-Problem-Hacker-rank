n=int(input())
tup=tuple(map(int,input().split()))
if(len(tup)!=n):
    exit

print(hash(tup))