import inventory

def addToInventory(inven, itemLst):
    itemLst.sort()
    for item in itemLst:
        if item in inven:
            inven[item] += 1
        else:
            inven[item] = itemLst.count(item)

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
inventory.displayInventory(stuff)
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
addToInventory(stuff, dragonLoot)
inventory.displayInventory(stuff)