def collatz(x):
    return x//2 if x%2 == 0 else (x*3)+1

x=int(input())
while x!=1:
    print(x := collatz(x))
