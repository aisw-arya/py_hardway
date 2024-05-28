def add(a, b):       #Created function for addition.
    print(f"ADDING {a} + {b}")
    return a + b


def subtract(a, b):            #Created function for subtarction.
    print(f"SUBTRACTING {a} - {b}")
    return a - b


def multiply(a, b):       #Created function for multiplying.
    print(f"MULTIPLYING {a} * {b}")
    return a * b


def divide(a, b):               #Created code for dividing.
    print(f"DIVIDING  {a} / {b}")
    return a / b


print("Let's do some math with just functions!")

age = add(30, 5)    #Calling add function and return the value to th variable 'age'.
height = subtract(78, 4)   #Calling substract function and return value to the variable 'height'.
weight = multiply(90, 2)    #Calling multiply function and return  value to the variable 'weight'.
iq = divide(100, 2)         #calling divide function and return value to the variable 'divide'.

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}") #printing the value inside the variable 
print("Here is a puzzle.")

what= add(age, subtract(height, multiply(weight, divide(iq, 2))))  #using one function as the argument of another function 

print("That becomes: ",what, "Can you do it by hand?")