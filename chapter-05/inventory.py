def displayInventory(dict):
    print("Inventory:")
    total_items = 0
    for k, v in dict.items():
        print(f"{v} {k}")
        total_items += v
    print(f"Total number of items: {total_items}")

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

if __name__ == "__main__":
    displayInventory(stuff)