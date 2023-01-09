import itertools

def isValidChessBoard(dict):
    
    valid_rows = ['1', '2', '3', '4', '5', '6', '7', '8']
    valid_files = ['a', 'b',' c', 'd', 'e', 'f', 'g', 'h']
    chckr = list(itertools.product(valid_rows, valid_files))
    
    w_count, w_pcount, b_count, b_pcount = 0, 0, 0, 0

    for key in dict:
        row_file = tuple(key)
        if row_file not in list(chckr):
            return False
        
    for value in dict.values():
        if value[0] == "w":
            w_count += 1
            if value[1] == 'p':
                w_pcount += 1
        else:
            b_count += 1
            if value[1] == 'p':
                b_pcount += 1  
    if b_count > 16 or w_count > 16 or w_pcount > 8 or b_pcount > 8:
        return False

    if list(dict.values()).count("bking") > 1 or list(dict.values()).count("wking") > 1:
        return False
    
    return True
            

print(isValidChessBoard({'2a': 'bking'}))