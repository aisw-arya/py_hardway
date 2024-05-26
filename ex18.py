def print_two(*agrs):  #function with two argument 
    arg1, arg2 = agrs
    print(f"arg1: {arg1}, arg2: {arg2}")


def print_two_again(arg1,arg2):  #function with two argument
    print(f"arg1: {arg1}, arg2: {arg2}")


def print_one(arg1):#function with one argument
    print(f"arg1: {arg1}")


def print_none():  #function without argument
    print("I got nothin'.")


print_two('aiswarya','s')
print_two_again('aiswarya','s')
print_one('First!')
print_none()