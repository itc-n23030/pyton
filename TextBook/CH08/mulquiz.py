import pyinputplus as pp
import random, time

def multiplication():
    number_of_questions = 10
    correct_answers = 0
    for question_number in range(number_of_questions):
        num1 = random.randint(0,9)
        num2 = random.randint(0,9)
        prompt = f'#{question_number + 1}: {num1}✕{num2} = '
        try:
            pp.inputStr(prompt, allowRegexes=[f'^{num1*num2}$'], blockRegexes=[('.*', '不正解！')],timeout=8, limit=3)
        
        except pp.TimeoutException:
            print('時間切れ！')
        except pp.RetryLimitException:
            print('回数制限超え！')
        
        else:
            print('正解')
            correct_answers += 1
        
        time.sleep(1)
    print(f'得点: {correct_answers}/{number_of_questions}')

multiplication()
