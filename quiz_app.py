# Main program
print("=" * 40)
print("WELCOME TO MECHATRONICS QUIZ APP")
print("=" * 40)

name = input("Enter your name: ")

# Get the number of questions from the user
while True:
    try:
        question_count = int(input("How many questions (1-10)? "))

        if 1 <= question_count <= 10:
            break
        else:
            print("Please enter a number from 1 to 10.")
    except ValueError:
        print("Invalid input! Enter a number.")

score = 0
wrong_answers = []

# Loop through the selected questions
for i in range(question_count):
    result = ask_question(i)

    if result == True:
        score += 1
    else:
        wrong_answers.append(i)

# Calculate percentage
percentage = (score / question_count) * 100

print("\n" + "=" * 40)
print("QUIZ RESULT")
print("=" * 40)

print("Student:", name)
print("Total Questions:", question_count)
print("Correct Answers:", score)
print("Wrong Answers:", len(wrong_answers))
print("Percentage:", percentage, "%")

# Grade the student
if percentage >= 80:
    print("Grade: A - Excellent!")
elif percentage >= 60:
    print("Grade: B - Very Good!")
elif percentage >= 50:
    print("Grade: C - Good!")
elif percentage >= 40:
    print("Grade: D - Fair!")
else:
    print("Grade: F - Try Again!")

# Extra feature: Review wrong answers
print("\nREVIEW OF WRONG ANSWERS")

if len(wrong_answers) == 0:
    print("Excellent! You got everything correct.")
else:
    for i in wrong_answers:
        print("\nQuestion:", questions[i])
        print("Correct answer:", answers[i])

print("\nThank you for using Mechatronics Quiz App!")
