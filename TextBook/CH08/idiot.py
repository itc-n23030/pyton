import pyinputplus as pp

def idiot():
    while True:
        print('バカを何時間も忙しくさせておく方法を知りたいですか？')
        a = pp.inputYesNo()
        if ('n' or 'N') in a:
            print('ありがとう、ごきげんよう')
            break


idiot()
