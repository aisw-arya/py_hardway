import sys  # Importing sys
script, encoding, error = sys.argv


def main(language_file, encoding, errors):      #Fuction to get each line.
    line = language_file.readline()

    if line:                                # Condition to check whether  data is present.
        print_line(line, encoding,errors)     #Calling print_line function.
        return main(language_file, encoding, errors)     #Calling main function inside the function. 


def print_line(line, encoding, errors):
    next_lang = line.strip()  #Strippiing of the trailing \n.
    raw_bytes = next_lang.encode(encoding, errors=errors)   #Encoding the string.
    cooked_string = raw_bytes.decode(encoding, errors=errors)  #Decoding the raw bytes.

    print(raw_bytes, "<===>", cooked_string)


languages = open("languages.txt", encoding="utf-8")   #Opening the file.

main(languages, encoding, error)  #Calling main function.