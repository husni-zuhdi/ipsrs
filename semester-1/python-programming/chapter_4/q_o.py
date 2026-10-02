# o) Create a recursive function fibo(n) that returns the n -th element of the Fibonacci sequence.
def fibo(n):
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    while n > 1:
        return fibo(n - 2) + fibo(n - 1)


if __name__ == "__main__":
    print("Fibonacci of 3 is ", fibo(3))
    print("Fibonacci of 4 is ", fibo(4))
    print("Fibonacci of 5 is ", fibo(5))
    print("Fibonacci of 6 is ", fibo(6))
