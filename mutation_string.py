def mutate_string(string, position, character):
    if 0 <=position <len(string):
        return string[:position]+character+string[position+1:]
    else:
        return string
    

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)