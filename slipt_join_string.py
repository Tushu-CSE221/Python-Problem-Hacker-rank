def split_and_join(line):
    a=line.split()

    b=("-").join(a)
    return b

str=input()
print(split_and_join(str))