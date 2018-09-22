#https://www.codewars.com/kata/585b373ce08bae41b800006e/train/python
class Funnel(object):
    # Coding and coding...
    def __init__(self):
        self.len = 0
        self.arr = [[' ',]*i for i in range(1,6,)]
    def fill(self, *args):
        temp = list(args)
        for x in range(5):
            for y in range(x+1):
                if self.arr[x][y] != ' ':
                    continue
                self.arr[x][y] = str(temp.pop(0))
                self.len += 1
                if not temp:
                    return
    def drip(self):
        if self.len == 0:
            return None
        self.len -= 1
        re = self.arr[0][0]
        def weight(x,y):
            return len([True for i in range(1,5) for j in range(y,y+i+1)\
                        if x+i<5 and j<5 and self.arr[x+i][j]!=' '])+ 1 if self.arr[x][y] !=' 'else 0
        x = y = 0
        while x<4 and y<4 and self.arr[x][y]!=' ':
            if weight(x+1,y) >= weight(x+1,y+1):
                self.arr[x][y] = self.arr[x+1][y]
                x,y = x+1,y
            else:
                self.arr[x][y] = self.arr[x+1][y+1]
                x,y = x+1,y+1
        self.arr[x][y] = ' '
        return  int(re) if re.isdigit() else re
    
    def __str__(self):
        return '\n'.join(['{:>{i}s}{}{}'.format(\
            '\\',' '.join(s),'/',i=i+1) for i,s in enumerate(self.arr[::-1])])
funnel = Funnel()
funnel.fill(1,2,3)
print(funnel)
dropped = funnel.drip()
print(funnel,dropped)
funnel.fill(4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H')
print(funnel)
dropped = funnel.drip()
print(funnel,dropped)
dropped = funnel.drip()
print(funnel,dropped)
dropped = funnel.drip()
print(funnel,dropped)
dropped = funnel.drip()
print(funnel,dropped)
dropped = funnel.drip()
print(funnel,dropped)
dropped = funnel.drip()
print(funnel,dropped)
dropped = funnel.drip()
print(funnel,dropped)
dropped = funnel.drip()
print(funnel,dropped)
dropped = funnel.drip()
print(funnel,dropped)
dropped = funnel.drip()
print(funnel,dropped)
dropped = funnel.drip()
print(funnel,dropped)
dropped = funnel.drip()
print(funnel,dropped)
dropped = funnel.drip()
print(funnel,dropped)
dropped = funnel.drip()
print(funnel,dropped)
dropped = funnel.drip()
print(funnel,dropped)
dropped = funnel.drip()
print(funnel,dropped)

