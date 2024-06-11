import random

guess = ''

while guess not in ('表', '裏'): #whileがいらない
    print('コインの表裏を当ててください。表か裏を入力してください:')
    guess = input()

toss = random.randint(0, 1) #0,1が表か裏か決めるコードがない

if toss == guess:
    print('当たり')
else:
    print('ハズレ! もう１回当てて!')
    guess = input()
    if toss == guess:
        print('当たり')
    else:
        print('ハズレ。このゲームは苦手ですね')