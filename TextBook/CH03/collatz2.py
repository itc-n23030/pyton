x = int(input())
while x!=1:
    collatz = lambda x : x//2 if x%2==0 else (3*x)+1
    print(collatz(x))
    x = collatz(x)


