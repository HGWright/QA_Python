your_mark = int(input("Enter your mark here: "))

# With elif
if your_mark > 85:
    print("distinction")
elif your_mark > 65:
    print("pass")
else:
    print("fail")

# Without elif
if your_mark > 85:
    print("distinction")

if your_mark <= 85 and your_mark > 65:
    print("pass")

if your_mark <= 65:
    print("fail")
