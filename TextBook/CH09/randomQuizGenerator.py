#! python3
# randomQuizGenerator.py - ランダム順に問題と答えを並べ問題集と解答集を作る

import random
import csv

# 都道府県の辞書を作る　keyが都道府県 valuesが県庁所在地
todoufuken_dict = {}
todoufuken_origin = open('./todoufuken.txt') # 同じフォルダ内に都道府県＋県庁所在地のcsvがある前提。どこかから適当にDLしてちょっと整形
todoufuken = csv.reader(todoufuken_origin)
for i in todoufuken:
    todoufuken_dict[i[0]] = i[1]

# 35個の問題集を作成する

for quiz_num in range(35):
    # 問題集と解答集のファイルを作成
    quiz_file = open(f'capitalsquiz{quiz_num+1}.txt', 'w')
    answer_key_file = open(f'capitalsquiz_answers{quiz_num+1}.txt', 'w')

    # 問題集のヘッダを書く
    quiz_file.write('名前：\n\n日付：\n\n学期：\n\n')
    quiz_file.write((' ' * 20) + f'都道府県県庁所在地クイズ（問題番号{quiz_num+1}）')
    quiz_file.write('\n\n')

    # 都道府県の順番をシャッフル
    prefectures = list(todoufuken_dict.keys())
    random.shuffle(prefectures)

    # 47都道府県をループして、それぞれ問題を作成
    for question_num in range(len(prefectures)):
        #正答と誤答を取得する
        correct_answer = todoufuken_dict[prefectures[question_num]]
        wrong_answers = list(todoufuken_dict.values())
        del wrong_answers[wrong_answers.index(correct_answer)]
        wrong_answers = random.sample(wrong_answers, 3)
        answer_options = wrong_answers + [correct_answer]
        random.shuffle(answer_options)
        #問題文と解答選択肢を問題ファイルに書く。fが使えないっぽいのでformatで書く。'ABCD'[i]はなんちゃってリスト作成テクニック
        quiz_file.write(f'{question_num+1}. {prefectures[question_num]}の都道府県庁所在地は？\n')
        for i in range(4):
            quiz_file.write(' {}. {}\n'.format('ABCD'[i], answer_options[i]))
        quiz_file.write('\n')
        #答えの選択肢をファイルに書く
        answer_key_file.write('{}. {}\n'.format(question_num+1, 'ABCD'[answer_options.index(correct_answer)]))
    quiz_file.close()
    answer_key_file.close()