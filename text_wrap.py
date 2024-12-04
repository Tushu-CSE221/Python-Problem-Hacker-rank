#using for loop:

s=input()
n=int(input())
if(n>len(s)):
    exit()

for i in range(0,len(s),n):
    print(s[i:i+n])

# using textwrap function:
import textwrap

def wrap(string, max_width):
    res=textwrap.fill(string,max_width)
    return res
 
if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)