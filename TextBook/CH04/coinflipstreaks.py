import random, time
count = 0
for i in range(10000):
    li100 = [random.randint(0, 1) for i in range(100)] 
    for x in li100:
        if li100[x: x+6] == [0 for _ in range(6)]:
            count += 1
        if li100[x: x+6] == [1 for _ in range(6)]:
            count += 1

print(f'裏表が６連続でる確率{(count/1000000)}%')
