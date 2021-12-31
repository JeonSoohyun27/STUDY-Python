def outer(a,b):
    # print('a=',a)
    # print('b=',b)
    def plus(c,d):
        # print('c=',c)
        # print('d=',d)
        return c+d
    
    r1 = plus(a,b)
    r2 = plus(b,a)
    return r1 + r2

result = outer(int(input('one:')),int(input('two:')))
print(result)