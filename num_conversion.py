def print_formatted(number):
    i=1
    width=len(bin(number)[2:])
    for i in range(1,number+1):
        dec=str(i)
        b_con=bin(i)[2:]
        oc_con=oct(i)[2:]
        hx_con=hex(i)[2:].upper()
        # print(str(i+1)+" "+ str(oc_con)+" "+ str(hx_con)+" "+ str(b_con))
        print(dec.rjust(width),oc_con.rjust(width),hx_con.rjust(width),b_con.rjust(width))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)