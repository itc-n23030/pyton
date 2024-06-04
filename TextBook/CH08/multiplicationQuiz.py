import random
import time
import pyinputplus as pp

number_of_questions = 10
correct_answers = 0

for question_number in range(number_of_questions):
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)
    answer = num1 * num2
    prompt = f'#{question_number+1}: {num1} x {num2} = '

    attempts = 0
    while attempts < 3:
        user_answer = pp.inputInt(prompt)
    
        if user_answer == answer:
            print('正解')
            correct_answers += 1
            time.sleep(1) 
            break
        else:
            print('不正解')
            attempts += 1

        if attempts == 3:
            print('試行回数がありません')
            time.sleep(1)

print(f'Score: {correct_answers} / {number_of_questions}')
