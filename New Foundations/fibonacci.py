'''
n=0  1  2  3  4  5  6  7
v=0, 1, 1, 2, 3, 5, 8, 13
'''

lst = []
new_lst = []
def fib(n):
    for i in range(n+1):
        lst.append(i)
    for x,y in enumerate(lst):
        if x < 2:
            new_lst.append(y)
            print(y)
        else:
            z = new_lst[x-1] + new_lst[x-2]
            new_lst.append(z)
    print(new_lst)

print(fib(10))
