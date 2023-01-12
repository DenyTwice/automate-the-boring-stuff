import random
import time
correct_ans = 0
for i in range(10):
    tries = 0
    operandOne = random.randint(0,9)
    operandTwo = random.randint(0,9)
    start = time.time()
    # while True:
    while tries < 3:
        answer = int(input(f"{operandOne} x {operandTwo} = "))
        if answer == operandOne * operandTwo:
            end = time.time()
            if end - start > 8:
                print("Time out")
                time.sleep(1)
                break
            print("Correct")
            correct_ans += 1
            time.sleep(1)
            break
        else:
            print("Wrong")
            tries += 1

print(correct_ans)