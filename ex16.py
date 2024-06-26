from sys import argv #Importing the `argv` module

script,filename = argv # Unpacking command-line arguments into variables

print(f"We're going to erase {filename}.")  # accessing filename using string formating
print("If you don't want that, hit CTRL-C(^C).")
print("If you do want that, hit RETURN.")

input("?")  #accessing user input

print("Opening the file...")
target = open (filename,'w')  #opening the file in w mode

print("Truncating the file. Goodbye!")
target.truncate()    #to remove data inside target

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ") #input from the user
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

# target.write(line1)  #writing the inputed data
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")

target.write(f"{line1}\n{line2}\n{line3}")

print("And finally, we close it.")
target.close()
target1 = open (filename,'r') #opening the file in read mode
print(target1.read()) #printing the contents inside the file
target1.close()