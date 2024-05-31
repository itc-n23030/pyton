import pyinputplus as pp

def sandwich():
    pan = pp.inputMenu(['小麦パン', '白パン', 'サワー種'], "パンの種類を選んでください\n")
    tanpaku = pp.inputMenu(['チキン', 'ターキー', 'ハム', '豆腐'], 'タンパク質を選んでください\n')
    cheese = pp.inputYesNo('チーズは必要ですか？')
    c = 0
    if cheese is 'yes' :
        c = pp.inputMenu(['チェダー', 'スイス', 'モッツァレラ'], 'チーズの種類を選んでください\n')
    topping = {'マヨネーズ': 50, 'からし': 50, 'レタス': 50, 'トマト': 50}
    t = []
    for k, v in topping.items():
        topp = pp.inputYesNo(f'{k}は必要ですか')
        if topp is 'yes':
            t.append(v)
    sandwich = pp.inputInt('サンドウィッチはいくつほしいですか？')
    dpan = {'小麦パン': 200, '白パン': 250, 'サワー種': 300}
    dtanpaku = {'チキン': 250, 'ターキー': 200, 'ハム': 150, '豆腐': 100}
    dc = {'チェダー': 100, 'スイス': 200, 'モッツァレラ': 250}
    print(f'合計で{(dpan[pan]+dtanpaku[tanpaku]+dc[c]+sum(t))*sandwich}円です')

sandwich()