string_1 = str(input("Please input the first string of letters: "))
string_2 = str(input("Please input the second string of letters: "))

mod_string_1 = ""

if len(string_1) != (len(string_2) + 1):
    print(False)
else:
    number_of_characters = len(string_1)

    for i in range (number_of_characters):
        mod_string_1 = string_1[0 : i : ] + string_1[i + 1 : :]
        if mod_string_1 == string_2:
            print(True)
            break

if mod_string_1 != string_2 and (len(string_1)) == (len(string_2) +1):
    print(False)
