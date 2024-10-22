def fibonacci_iterative(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

def fibonacci_recursion(n):
    seq=[]
    if n <= 1:
        return [0][:n]
    elif n == 2:
        return [0, 1]
    else:
        seq = fibonacci_recursion(n - 1)
        seq.append(seq[-1] + seq[-2])
    return seq

def calculate_fibonacci():
    try:
        n = int(input("Enter a number to calculate Fibonacci sequence: "))
        if n < 0:
            print("Please enter a positive integer!")
            return
        
        print("Choose method:\n1. Iterative\n2. Recursive")
        choice = int(input("Enter 1 or 2: "))
        
        if choice == 1:
            result = fibonacci_iterative(n)
            print(f"Iterative Fibonacci sequence up to {n}: {result}")
        elif choice == 2:
            result = fibonacci_recursion(n)
            print(f"Recursive Fibonacci sequence up to {n}: {result}")
        else:
            print("Invalid choice!")
    except ValueError:
        print("Invalid input!")

calculate_fibonacci()
