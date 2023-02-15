# a = int(input("ENTER: "))
# for i in range(1,a+1):
#     for j in range(1,a+1-i):
#         print(' ',end=" ")
#     for j in range(1,i+1):
#         print(j,end=' ')
#     for j in range(i-1,0-1):
#         print(j,end='')
#
#     print()
# todo first method
# N=int(input())
# for i in range(1, N+1):
#     print([0, 1, 121, 12321, 1234321, 123454321, 12345654321, 1234567654321, 123456787654321, 12345678987654321][i])
# todo second method
# for i in range(1,int(input())+1):
#    print(int((10**i-1)/9)**2)

'''1 -> (   10 - 1) / 9 =    1,    1 *    1 = 1
2 -> (  100 - 1) / 9 =   11,   11 *   11 = 121
3 -> ( 1000 - 1) / 9 =  111,  111 *  111 = 12321
4 -> (10000 - 1) / 9 = 1111, 1111 * 1111 = 1234321'''
# todo third method
# a=lambda n:n and [a(n-1),print(int(10**n/9)**2),range(1,n)]
# a(5)
a=lambda n:n and [a(n-1),print(int(10**n/9)**2)];a(int(input()))

'''a=5 = n=5 = [a(4),1,range(1,5)] i = 1
   a=4 = n=4 = [a(3),121,range(1,4)] i = 2
   a=3 = n=3 = [a(2),12321,range(1,3)] i = 3
   a=2 = n=2 = [a(1),1234321,range(1,2)] i = 4
   a=1 = n=1 = [a(0),123454321,range(1,1)] i = 5
   a=0 = n=0 = [a(-1),1,range(1,5)] i = 1   terminate'''


# g=lambda X:X
# print(g(5))
