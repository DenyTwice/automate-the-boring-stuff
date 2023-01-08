def commaCode(lst):
    for i in range(len(lst)):
        if i == len(lst) - 1:
            print(f'and {lst[i]}')
        else:
            print(f'{lst[i]}, ', end="")


spam = ['apples', 'oranges', 'bananas', 'tofu', 'cats']
commaCode(spam)