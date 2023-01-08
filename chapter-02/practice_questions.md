# Practice Questions

## 1. What are the two values of the Boolean data type? How do you write them?

---

The two values are True and False.

---

## 2. What are the three Boolean operators?

---

Not, And and Or.

---

## 3. Write out the truth tables of each Boolean operator (that is, every possible combination of Boolean values for the operator and what they evaluate to).

---

| p | q | not p | p and q | p or q|
|---|---| :---: |  :---:  | :---: |
| F | F |   T   |    F    |   F   |
| F | T |   T   |    F    |   T   |
| T | F |   F   |    F    |   T   |
| T | T |   F   |    T    |   T   |

---

## 4.What do the following expressions evaluate to?

(5 > 4) and (3 == 5)

not (5 > 4)

(5 > 4) or (3 == 5)

not ((5 > 4) or (3 == 5))

(True and True) and (True == False)

(not False) or (not True)

---

False

False

True

False

False

True

---

## 5. What are the six comparison operators?

---

The six comparison operators are: >, <, ==, !=, <= and >=

---

## 6. What is the difference between the equal to operator and the assignment operator?

---

The equal to operator (==) checks if the LHS and RHS are equal while the assignment operator (=) assigns the RHS to the variable on LHS.

---

## 7. Explain what a condition is and where you should use one.

---

A condition is used to allow the program to make pre-determined choices depending on the evaluation of the expression. The expression is called the condition.

---

## 8. Identify the three blocks in this code:

```py
spam = 0
if spam == 10:
    print('eggs')
    if spam > 5:
        print('bacon')
    else:
        print('ham')
    print('spam')
print('spam')
```

---

The first block has no indentation i.e it begins at line 1. Lines 3,4,6 and 8 are in the second block and every other line is in the third block.

---



