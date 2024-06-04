import pyinputplus as pp

def idiot():
    while True:
        print('バカを何時間も忙しくさせておく方法を知りたいですか？')
        a = pp.inputYesNo()
        if a is 'no':
            print('ありがとう、ごきげんよう')
            break
        
idiot()
