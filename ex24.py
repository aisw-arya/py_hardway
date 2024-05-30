print("Let's practice everything.")
print('you\'d need to know \'bout escape with \\ that do:')
print('\n newlines and \t tabs.')

poem = """
\t The lovely world
with logic so firmly planted
cannot discern \n the needs of love 
nor comprehend passion from instution 
and requires an explanation 
\n\twhere there is none.
"""

print("--------------")
print(poem)
print("--------------")


five = 10 - 2 + 3 -6
print(f"This should be five: {five}")     #Print the value inside the variable 'five' using string formatting.

def secret_formula(started):    # Function to calcluate jelly beans, jars, crates and returns the value.          
    jelly_beans = started * 500   
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point)    #Function call and returning the value to the variables

#remember that this is another way to format a string 
print("With a starting point of: {}".format(start_point))
#it's just like with an f"" string
print(f"We'd have {beans} beans, {jars} jars, and {crates} cractes.")

start_point = start_point / 10

print("We can also do that this way:")
fromula = secret_formula(start_point)
# this is  an easy wayto apply a list to a format string
print("we'd have {} beans, {} jars, and {} cractes.".format(*fromula))