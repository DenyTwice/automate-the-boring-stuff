def printTable(lst):
    max = 0
    
    for i in range(len(lst)):
        for j in lst[i]:
            if len(j) > max:
                max = len(j)
    for i in range(len(lst[0])):
        for j in lst:
            print(j[i].rjust(max), end="")
        print()



tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)