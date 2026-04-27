import sys
def add(num1, num2):
    sum = num1 + num2 
    return sum

def sub(num1, num2):
    sub = num1 - num2
    return sub

def multi(num1, num2):
    mul=num1 * num2
    return mul

num1 = int(sys.argv[1])
operation = sys.argv[2]
num2 = int(sys.argv[3])

if operation == "add":
    output = add(num1, num2)
    print(output)

elif operation == "sub":
    output = sub(num1, num2)
    print(output)

elif operation == "multi":
    output = multi(num1, num2)
    print(output)
  
