import math

def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return recur_fibo(n - 1) + recur_fibo(n - 2)

def check():
    try:
        x = int(numb)

        print("Fibonacci sequence :")
        for i in range(x):
            print(recur_fibo(i))
        return math.factorial(x)
    except ValueError:
        print("Empty File or does not contain positive integer")
    except OverflowError:
        print("Value to great")
    finally:
        f.close()

try:
    with open("text.txt", 'r') as f:
        numb = (f.readline())
        check()
except FileNotFoundError:
    print("File not found, Dear")
    with open("text.txt", 'x+') as f:
        numb = (f.readline())
        check()