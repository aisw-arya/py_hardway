def cheese_and_crackers(cheese_count, boxes_of_crackers): # defining a function 
    print(f"you have {cheese_count} cheese!") #accessing values using string formatting 
    print(f"You have {boxes_of_crackers} box of crackers!")
    print("Man that enough for a party!")
    print("Get a blanket.\n")


print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30) #function calling

print("Or, we can use variable from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers) #variables are used as arguments

print("We can even do math inside too:")
cheese_and_crackers(10+20,5+6) #doing math inside function call

print("and we can combine the two, variable and math:")
cheese_and_crackers(amount_of_cheese+100, amount_of_crackers+1000) #combing math and variable value inside function call