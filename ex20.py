from sys import argv #import argv module.
script, input_file = argv #unpacking the command line argument.

def print_all(f):  #function to read.
    print(f.read())

def rewind(f):   #function to change file pointer to the begining of the file.
    f.seek(0)
    

def print_a_line(line_count,f):
    print(line_count,f.readline())   #to print each line.

current_file = open(input_file)    #opening the input_file.

print("First let's print the whole file:\n")

print_all(current_file)   #print content in the file.

print("Now let's rewind,  kind of like a tape.")

rewind(current_file)    #calling the second function 'rewind()'.passing current_file to the function.

print("Let's print three lines:")

current_line = 1                         #to print each lines
print_a_line(current_line,current_file)

current_line = current_line + 1
print_a_line(current_line,current_file)

current_line = current_line + 1
print_a_line(current_line,current_file)

