import sys

if len(sys.argv) < 3:
    print('Usage:')
    print('python algs.py grammar input')
    sys.exit()


'''
def getFIRST(grammar):
    FIRST = {x:set() for x in grammar}
    changed = True
    while changed:
        changed = False
        for left, alts in grammar.items():
            for right in alts:
                if right == "":
                    continue
                prev_len = len(FIRST[left])
                if right[0].isupper():
                    FIRST[left] = FIRST[left].union(FIRST[right[0]])
                else:
                    FIRST[left].add(right[0])                    
                if(len(FIRST[left]) != prev_len):
                    changed = True
    return FIRST
'''
def left(line):
    return line.split()[0]
     
def right(line):
    right = line.split()[1].split('|')
    def f(x):
        if x == 'eps':
            return ''
        return x
    return [f(x) for x in right]

grammar = {left(line.strip()):right(line.strip()) for line in open(sys.argv[1]) if line.strip() != ""}
print(grammar)


'''
FIRST = getFIRST(grammar)
print('FIRST')

for nonterm, first in FIRST.items():
    print(nonterm, ':', first)
'''



def rec(gen):
    try:
        ch = next(gen)
    except Exception:
        return ["return"]        

    if ch.isupper():  
        body = []
        body.append("{}(stream)".format(ch))
        
        for line in rec(gen):
            body.append(line)

    else:     
        body = ["x = stream.popleft()"]   
        body.append("if x == '{}':".format(ch))
        for line in rec(gen):
            body.append("    " + line)
        body.append("else:".format(ch))
        body.append("    stream.appendleft(x)")
    return body
        

with open("recdes.py", 'w') as file:
    file.write("from collections import deque\n".format(left))
    file.write("def RD(stream):\n")
    file.write("    S(stream)\n")
    file.write("    if len(stream) != 0:\n")
    file.write("        raise Exception('garbage found in the end')\n")



    for left, alts in grammar.items():
        file.write("def {}(stream):\n".format(left))
        file.write("    #debug info\n")
        file.write("    print({}.__name__, ''.join(stream))\n".format(left))

        if "" in alts:
            file.write("    if len(stream) == 0:\n")
            file.write("        return\n")
    
        has_eps = False
        for right in alts:
            line = []
            if right == "":
                has_eps = True
                continue
            
            pad = []
            
            for line in rec(iter(right)):
                file.write("".join(["    ", line, "\n"]))



        if has_eps:
            file.write("    return\n")
        else:
            file.write("    raise Exception('no rule found')\n")
            
        


import recdes
from collections import deque
print()
for line in open(sys.argv[2]):
    line = line.strip()
    print(deque(line))
    try:
        recdes.RD(deque(line))
    except Exception as e:
        print('False')
        print(e)
    else:
        print('True')
    


