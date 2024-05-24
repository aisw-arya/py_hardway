from sys import argv #Importing the `argv` module

script, filename = argv # Unpacking command-line arguments into variables

txt = open(filename) #opening inputed file and assigning it to the variable txt

print(f"Here's your life {filename}:")  
print(txt.read())#print content of the file  

print("Type the filename again")
file_again = input("> ") # Taking input from the user for the filename. 

txt_again = open(file_again)

print(txt_again.read())#print content of the file 