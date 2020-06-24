def presses(phrase):
    phrase = phrase.upper()
    keypads = ['1', 'ABC2', 'DEF3', 'GHI4', 'JKL5', 'MNO6', 'PQRS7', 'TUV8', 'WXYZ9', '*', ' 0', '#']
    res = 0
    for i in phrase:
        for j in keypads:
            if i in j:
                res += j.index(i) +1

    return res


print(presses("B19DN YZX37ERQ*68W5LH*EJ"))


OR


def presses(phrase):
    x = 0
    for letter in phrase:
        if letter.lower() in list('1*#adgjmptw '): x+= 1
        elif letter.lower() in list('0behknqux'): x+= 2
        elif letter.lower() in list('cfilorvy'): x+= 3
        elif letter.lower() in list('234568sz'): x+= 4
        elif letter.lower() in list('79'): x+= 5
    return x
        
        
        
 OR
 
 
 def presses(phrase):
    phrase = phrase.upper()
    counter = 0
    s = set(phrase)
    alphabet = [chr(x) for x in range(65,91)]
    for x in range(10):
        if x != 1:
            result = (3, 0, 4)[(not x) + (x in [7,9])*2]
            part = alphabet[:result] or [' ']
            part.append(str(x))
            alphabet = alphabet[result:]
            for i,c in enumerate(part, 1):
                if c in s:
                    res = phrase.count(c)
                    counter += res * i
                    s.remove(c)
        else:
            for ch in ['1', '*', '#']:
                counter += 1 * phrase.count(ch)
    return counter
