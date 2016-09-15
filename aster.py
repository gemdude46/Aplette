import sys

class Token:
    def __init__(self, t, d=None):
        self.t=t
        self.d=d

icp = 0
code = sys.stdin.read()

tokens = []

while icp < len(code):
    c = code[icp]
    if c in '\n \r\t\a':
        icp+=1
        continue
    
    f = False
    for sym in ('++','--','+=','-=','*=','/=','%=','==','+','-','*','/'):
        if code[icp:icp+len(sym)] == sym:
            tokens.append(Token(sym))
            icp+=len(sym)
            f = True
            break
    if f: continue
    
    
