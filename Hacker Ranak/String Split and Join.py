def split_and_join(line):
    String = line
    String1 = String.split()
    String2 = "-".join(String1)
    return String2

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)