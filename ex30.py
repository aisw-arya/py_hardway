people = 30
cars = 40
trucks = 15


if cars > people:     #Check the condition1
    print("We should take the cars.")
elif cars < people:     # check the condition if the condition1 fail
    print("We should not take the cars.")
else:           #execute only when both conditions fail
    print("We can't decide.")

if trucks > cars:
    print("That's too many trucks.")
elif trucks < cars:
    print("Maybe we could take the trucks.")
else:
    print("We still can't decide.")

if people > trucks:
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's stay home then.")