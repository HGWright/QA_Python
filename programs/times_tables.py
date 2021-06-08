no_for_tt = int(input("Please enter the number you would like to see the times tabls for: "))

for i in range(1, no_for_tt + 1):
    for j in range(1, no_for_tt + 1):
        print(i * j, end='\t')
    print('')