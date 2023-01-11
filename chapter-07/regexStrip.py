import re
# ....string....
    # ....
# ... ...string... ...
    #...
#      str   str     
def regexStrip(strng, strp):

    startStrip = re.compile("^("+strp+"*)")
    print("^"+strp+"*")
    res = startStrip.search(strng)
    bruh = res.group()
    print(bruh)


regexStrip(".....okay", ".")