import shelve, pyperclip, sys

# mcb save <kw> - save new <kw>
# mcb del <kw> - delete <kw>
# mcb del - delete all saved keywords
# mcb list - list all keywords
# mcb <kw> - load and copy <kw>

agree = 'Yes, I agree. That sounds fine to me.'
busy = "Sorry, can we do this later this week or next week?"
upsell = "Would you ocnsider making this a monthly donation?"

shelfFile = shelve.open('mcb')
shelfFile['agree'] = agree
shelfFile['busy'] = busy
shelfFile['upsell'] = upsell

if len(sys.argv) < 2:
    print('Usage: python3 mclip.py [keyphrase] - copy phrase text')
    sys.exit()

if len(sys.argv) == 3:
    if sys.argv[1].lower() == "save":
        shelfFile[sys.argv[2]] = pyperclip.paste()
    elif sys.argv[1].lower() == "del":
        del shelfFile[sys.argv[2]]

elif len(sys.argv) == 2:
    if sys.argv[1] == "del":
        shelfFile.clear()
    elif sys.argv[1] == "list":
        print("\n".join(list(shelfFile.keys())))
    elif sys.argv[1] in shelfFile.keys():
        pyperclip.copy(shelfFile[sys.argv[1]])
        print(f"Copied {sys.argv[1]} phrase to clipboard!")
    else:
        print("Invalid argument.")