import pyinputplus as pyip

ingreds = []
bread = ['Wheat' ,'white', 'Sourdough']
meat = ['Chicken' , 'Turkey', 'Ham', 'Tofu']

ingreds.append(pyip.inputMenu(bread, "Choose the type of bread: \n"))
ingreds.append(pyip.inputMenu(meat, "Choose the type of meat: \n"))
cheese = (pyip.inputYesNo("Do you want cheese? "))

if cheese == "yes":
    ingreds.append(pyip.inputMenu(['Cheddar', 'Swiss', 'Mozzarella'], "Choose the type of cheese: \n"))

meh = ['Mayo', 'Lettuce', 'Tomato', 'Mustard']
for i in meh:
    inpt = pyip.inputYesNo(f"Do you want {i}? ")
    if inpt == "yes":
        ingreds.append(i)
    
num_sandwhich = pyip.inputInt("Enter number of sandwhiches: ", min=1)

prices = {"Wheat": 10, "White": 15, "Sourdough": 18, "Chicken": 20, "Turkey": 22, "Ham": 25, "Tofu": 18, 
            "Cheddar": 7, "Swiss": 9, "Mozzarella": 9, "Mayo": 3, "Lettuce": 5, "Tomato": 7, "Mustard": 3}
price = 0
for i in ingreds:
    if i in prices:
        price += prices[i]

    
print(price*num_sandwhich)