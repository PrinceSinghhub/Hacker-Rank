# a=set([161,182, 161 ,154 ,176 ,170, 167 ,171, 170 ,174 ])
# r=list(a)
# print(r)
# print(sum(r)/len(r))
def average(array):
    result1 = set(array)
    a=list(result1)
    b=len(a)
    c=sum(a)
    d=c/b
    return d


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    print(arr)
    result = average(arr)
    print(result)