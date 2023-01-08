def collatz(number):
    if (number % 2 == 0):
        print(number // 2)
        return number // 2
    else:
        print(3*number + 1)
        return 3*number + 1

while True:
    try: 
        n = int(input())
        while n != 1:
            n = collatz(n)
        else: break
    except ValueError:
        print("Invalid input, enter an integer.")