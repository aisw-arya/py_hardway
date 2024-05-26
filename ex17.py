from sys import argv  #import 'argv' module
from os.path import exists #import exists function from os.path module

script,from_file,to_file = argv #unpacking the command line argument

print(f"Copying from {from_file} to {to_file}") #printing the variables in argv

in_file = open(from_file)  #opening file in 'r' mode 
indata = in_file.read() #stored data to the variable

print(f"The input file is {len(indata)} bytes long") #len() function used to show the length of the data in file

print(f"Does the output file exist? {exists(to_file)}") #accessed 'exists()' function
print("Ready, hi RETURN to , CTRL-C to abort.")
input()

out_file = open(to_file,'w') #opening file in 'w' mode
out_file.write(indata) #copyimg the content in one file to another

print("Alright,all done.")

out_file.close()
in_file.close()