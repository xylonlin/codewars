#codewars link
#https://www.codewars.com/kata/546d15cebed2e10334000ed9/train/python
def solve_runes(runes):
    temp = runes
    print(temp)
    for i in "0123456789":
        if i in temp or i == '0' and (temp[0] in '0?' and \
           temp[1] in '?1234567890' or \
           any([ True for i,s in enumerate(temp) \
                 if s in '=+-*' and temp[i+1] == '?'and i+2 < len(temp) and temp[i+2] in '?0123456789'])):
            continue
        temp = temp.replace('?',i)
        temp = temp.replace('=','==')
        print(temp)
        if eval(temp):
            return int(i)
        temp = runes
    return -1
test = "?38???+595???=833444"
print(solve_runes(test))
        
            
            
    
