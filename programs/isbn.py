isbn_12 = str(input("Please insert the first 12 digits of the required ISBN number without hyphens: "))

for i in range (12):
    exec(f'digit_{i} = int(isbn_12[i])')

digit_12 = 10 - ((digit_0 + (3 * digit_1) + digit_2 + (3 * digit_3) + digit_4 + (3 * digit_5) + digit_6 + (3 * digit_7) + digit_8 + (3 * digit_9) + digit_10 + (3 * digit_11)) % 10)


ISBN = f"{digit_0}{digit_1}{digit_2}-{digit_3}-{digit_4}{digit_5}{digit_6}-{digit_7}{digit_8}{digit_9}{digit_10}{digit_11}-{digit_12}"

print(ISBN)