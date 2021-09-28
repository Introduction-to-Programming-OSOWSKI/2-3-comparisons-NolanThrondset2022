#WRITE YOUR CODE IN THIS FILE
def greaterThan(x,y):
    if x > y:
        return True
    else:
        return False
def lessThan(x,y):
    if x < y:
        return True
    else:
        return False
def equalTo(x,y):
    if x == y:
        return True
    else:
        return False
def greaterOrEqual(x,y):
    if x >= y:
        return True
    else:
        return False 
def lessOrEqual(x,y):
    if x <= y:
        return True
    else:
        return False

print(greaterThan(10,6))
print(lessThan(10,6))
print(equalTo(10,10))
print(greaterOrEqual(5,10))
print(lessOrEqual(7,7))