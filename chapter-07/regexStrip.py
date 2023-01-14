import re

def regexStrip(strng, strp="\s"):
    mod_strng = re.sub(f"^{strp}+", string=strng, repl="")
    mod_strng = re.sub(f"{strp}+$", string=mod_strng, repl="")
    print(mod_strng)

regexStrip("    ## ## aosdk ## ##    ##", "#")