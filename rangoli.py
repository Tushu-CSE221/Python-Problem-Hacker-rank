def print_rangoli(number):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    width = 4 * number - 3  # Total width of each line
    lines = []  # To store the rows of the pattern
    
    for i in range(number):
        # Generate the left part of the pattern
        l_part = '-'.join(alphabet[number-1:number-i-1:-1])
        # Add the central letter
        full_line = (l_part + ('-' if i > 0 else '') + '-'.join(alphabet[number-i-1:number])).center(width, '-')
        lines.append(full_line)
    
    # Print the rangoli by mirroring the list
    print('\n'.join(lines + lines[-2::-1]))
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)