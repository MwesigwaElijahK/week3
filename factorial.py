x=int(input("Enter number: "))

def factorial(x):
    if x < 0:
        return "Error"
    elif x == 0:
        return 1    
    else:
        factorial(x - 1)
    return x * factorial(x - 1) 

print (factorial(x))