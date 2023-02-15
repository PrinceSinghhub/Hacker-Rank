def print_formatted(number):
    x=len(bin(number)[2:])
    print(x)
    for i in range(1, number + 1):
        print(f"{str(i).rjust(x,' ')} {oct(i)[2:].rjust(x,' ')} {hex(i)[2:].upper().rjust(x,' ')} {bin(i)[2:].rjust(x,' ')}")


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
