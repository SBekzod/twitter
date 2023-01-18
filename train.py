
def powersum(power, *args):
    total = 0
    for i in args:
        total += pow(i, power)
    return total

print(powersum(2, 3, 4))
print('======================')

def myFun(**kwargs):
    print('KWARGS:', kwargs)
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))
 
 
# Driver code
myFun(first='Geeks', mid='for', last='Geeks')