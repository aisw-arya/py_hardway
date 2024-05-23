formatter = "{} {} {} {}" #creates four placeholders
print(formatter.format(1,2,3,4))# to add numbers to the placeholders of the formatter string template using the format()
print(formatter.format("one","two","three","four"))# to add string to the placeholders of the formatter string template using the format()
print(formatter.format("True","False","False","True")) # to add boolean value to the placeholders of the formatter string template using the format()
print(formatter.format(formatter,formatter,formatter,formatter))  #substitutes the formatter string template itself into each placeholder of the formatter string template and then prints the result.
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))