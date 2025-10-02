# Math Tutor - Project
# Multiplication tables
# Object: Create application to practice multiplication tables
# - User specifies number of random practice questions
# - User is presented with a prompt e.g. 5 X 5 = and inputs the answer for each question
# - When all questions are answered, print out the following info:
#       a. Some form of 'thanks for playing' greeting
#       b. Number of correct answers / total answers
#       c. % correct
#   Use different rows as you wish.
#   Remember \n (line break) or '' doesn’t work properly with Brython
# Bonus 1: Also measure / present the time it took to answer questions:
#          in total and per question
# Bonus 2: Show all questions and answers at the end
import string, random as r, time as t

questions_count = int(input("How many question do you require? "))
correct = 0
numbers = string.digits
question_data = []


def calculatetheresult(random_exprssion):
    random_exprssion = random_exprssion.split()
    first_num = int(random_exprssion[0])
    second_num = int(random_exprssion[-1])
    return first_num * second_num


start = t.time()
for i in range(questions_count):
    print(f"Question {i+1} :")
    exprssion = f"{r.choice(numbers)} * {r.choice(numbers)}"
    question = int(input(f"{exprssion} = "))
    result = calculatetheresult(exprssion)
    question_data.append(
        {i + 1: exprssion, "your awnser": question, "the correct awnser": result}
    )
    if result == question:
        correct = correct + 1
    else:
        None
end = t.time()


print("==== you are done =====")
print(f"correct awnsers : {correct}/{questions_count}")
print(
    f"percent correct : {(correct / questions_count) * 100:.2f}% in {round(end-start,1)} seconds ({round((end-start)/questions_count,1)}seconds/question)"
)
print("=== questions ====")
for item in question_data:
    for key, value in item.items():
        print(f"{key} : {value}\t")
