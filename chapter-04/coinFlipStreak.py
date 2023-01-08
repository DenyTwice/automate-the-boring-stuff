import random

totalStreaks = 0

for expNmbr in range(10000):    
    flag = 0
    
    tossLst = [random.randint(0,1) for i in range(100)]
    for toss in range(len(tossLst)):
        currentStreak = 0
        
        for i in range(1,6):
            try:
                if tossLst[toss+i] == tossLst[toss]:
                    currentStreak += 1

                if currentStreak == 5:
                    totalStreaks += 1
                    flag = 1
            except IndexError:
                break

        if flag:
            break

print(f"Chance of streak: {totalStreaks/100}%")