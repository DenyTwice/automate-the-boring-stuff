import re

def checkIfStronk(pswd):
    if len(pswd) < 8:
        return False
    upperReg = re.compile('[A-Z]')
    lowerReg = re.compile('[a-z]')
    numReg = re.compile('[0-9]')
    conditionOne = upperReg.search(pswd)
    conditionTwo = lowerReg.search(pswd)
    conditionThree = numReg.search(pswd)
    try:
        t1 = conditionOne.group()
        t2 = conditionTwo.group()
        t3 = conditionThree.group()
    except AttributeError:
        return False
    return True

print(checkIfStronk('passwordisweak'))
print(checkIfStronk('passw0rdIsStronk'))