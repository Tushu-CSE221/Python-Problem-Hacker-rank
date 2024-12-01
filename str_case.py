# def swap_case(s):
#     re=s.swapcase()
#     res=print(re)
#     return res 



def swap_case(s):
    x=""
    for i in s:
        if i.isupper():
            i=i.lower()
        else:
            i=i.upper()
        x+="".join(i)
    return x
str=input()
print(swap_case(str))
