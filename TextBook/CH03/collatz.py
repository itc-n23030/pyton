collatz = lambda x : x//2 if x%2 == 0 else (x*3)+1

n=int(input())

while n!=1 :
    print(collatz(n))
    n = collatz(n)
