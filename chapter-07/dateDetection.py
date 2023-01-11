import re

inpt_date = input("Enter date: ")

dateRegex = re.compile('([0-9]{2})/([0-9]{2})/([1-9][0-9]{3})')
date = dateRegex.search(inpt_date)

day = date.group(1)
month = date.group(2)
year = int(date.group(3))

match month:
    case '04' | '06' | '09' | '11':
        if not int(day) or int(day) > 30:
            print("Invalid day")
    case '02':
        if (year%4==0):
            if (year % 100):
                if (year%400):
                    pass
                else: 
                    print("Invalid day")
        else:
            print("Invalid day")
    case '01' | '03' | '05' | '07' | '08' | '10' | '12':
        if not int(day) or int(day) > 31:
            print("Invalid day")
    case _:
        print("Invalid month")
