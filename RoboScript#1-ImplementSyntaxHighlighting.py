#link
#https://www.codewars.com/kata/roboscript-number-1-implement-syntax-highlighting/train/python
def highlight(code):
    temp={'F':'<span style="color: pink">%s</span>',
          'L':'<span style="color: red">%s</span>',
          'R':'<span style="color: green">%s</span>',
          'D':'<span style="color: orange">%s</span>',
          }
    s = []
    j = 0
    for i in range(len(code)-1):
        if code[i] in '()':
            s.append(code[i])
            j = i+1
        elif code[i+1] !=code [i] and not code[i].isdigit():
            s.append(temp[code[i]] % code[j:i+1])
            j = i+1
        elif code[i].isdigit() and not code[i+1].isdigit() and code[j:i+1].isdigit():
            s.append(temp['D'] % code[j:i+1])
            j = i+1
    if code [j] in '()':
        s.append(code[j])
    elif code[j:i+2].isdigit():
        s.append(temp['D'] % code[j:i+2])
    else:
        s.append(temp[code[j]] % code[j:i+2])
    return(''.join(s))
print(highlight("FFFL12L(12R)"))
            
        
            
            
