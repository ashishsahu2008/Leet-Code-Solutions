import datetime
def fibonacci_gen(n):
    a = b = 1
    for i in range(n):
        yield a
        a,b = b, a+b

def fibonacci(n):
    lst = []
    a = b = 1
    for i in range(n):
        lst.append(a)
        x = b
        b = a+b
        a = x
    return lst

t1 = datetime.datetime.now()
fibonacci(10000)
print(datetime.datetime.now() - t1)

t2 = datetime.datetime.now()
lst1=[]
for x in fibonacci_gen(1000):
    lst1.append(x)
    #print(x)
print(datetime.datetime.now() - t2)
