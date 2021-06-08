student_name = str(input("Please enter your name: "))
homework_mark = int(input("Please enter your homework mark out of 25: "))
assessment_mark = int(input("Please enter your assessment mark out of 50: "))
final_exam_mark = int (input("Please enter your final exam mark out of 100: "))

def total_raw_mark(mark_1, mark_2, mark_3):
    percentage = (homework_mark + assessment_mark + final_exam_mark)
    return percentage

total_percentage_mark = int((total_raw_mark(homework_mark, assessment_mark, final_exam_mark) / 175) * 100)

print(f"{student_name} your overall percentage for ICT is {total_percentage_mark}%")

if total_percentage_mark >= 70:
    print(f"You earned a grade of: A")
elif total_percentage_mark >= 60:
    print(f"You earned a grade of: B")
elif total_percentage_mark >= 50:
    print(f"You earned a grade of: C")
elif total_percentage_mark >= 40:
    print(f"You earned a grade of: D")
else:
    print("You Failed")