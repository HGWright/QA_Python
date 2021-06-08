print("Welcome to the Grade Calculator")

maths_mark = int(input("Please enter your Maths mark: "))
chemistry_mark = int(input("Please enter your Chemistry mark: "))
physics_mark = int(input("Please enter your Physics mark: "))

total_mark = (maths_mark + chemistry_mark + physics_mark)/3

print(f"Your overall percentage is {total_mark}%")

if total_mark >= 70:
    print(f"You earned a grade of: A")
elif total_mark >= 60:
    print(f"You earned a grade of: B")
elif total_mark >= 50:
    print(f"You earned a grade of: C")
elif total_mark >= 40:
    print(f"You earned a grade of: D")
else:
    print("You Failed")