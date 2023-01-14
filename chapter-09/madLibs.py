import random

madFile = open('sampleMadLib.txt', 'r')
content = madFile.read()
words = []
toWrite = list.copy(content.split())
for indx, word in enumerate(content.split()):
    if word.isupper() and len(word) > 1:
        if word[-1] == '.':
            toWrite[indx] = input(f"Enter {word[:-1]}: ") + '.'
        else:
            toWrite[indx] = input(f"Enter {word}: ")
madFile.close()


num = random.randint(1,200)
with open('MadLib' + str(num) + '.txt', 'w') as madFile:
    madFile.write(" ".join(toWrite))

with open('MadLib' + str(num) + '.txt', 'r') as madFile:
    content = madFile.read()
    print(content)