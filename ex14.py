from sys import argv   #import argv
script, user_name = argv   #Unpacking command-line arguments into variables `script` and `user_name
prompt = '> '  # Assigning the prompt symbol to the variable `prompt`.
print(f"Hi {user_name}, I'm the {script} script.") # Printing a greeting message with the script name and user's name
print("I'd like to ask you a few questions")
print(f"Do you like me {user_name}?")
likes=input(prompt) #Taking input from the user for whether they like the script author.
print(f"where do you live{user_name}?")
lives=input(prompt)
print("What kind of computer do you have?")
computer=input(prompt)
print(f"""Alright, so you said {likes} about liking me. You live in {lives}. Not sure where that is. And you have a {computer} computer. Nice.""")