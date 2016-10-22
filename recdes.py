from collections import deque
def RD(stream):
    S(stream)
    if len(stream) != 0:
        raise Exception('garbage found in the end')
def C(stream):
    #debug info
    print(C.__name__, ''.join(stream))
    S(stream)
    E(stream)
    return
    x = stream.popleft()
    if x == ']':
        return
    else:
        stream.appendleft(x)
    raise Exception('no rule found')
def Q(stream):
    #debug info
    print(Q.__name__, ''.join(stream))
    x = stream.popleft()
    if x == ',':
        A(stream)
        return
    else:
        stream.appendleft(x)
    x = stream.popleft()
    if x == '}':
        return
    else:
        stream.appendleft(x)
    raise Exception('no rule found')
def A(stream):
    #debug info
    print(A.__name__, ''.join(stream))
    x = stream.popleft()
    if x == 'x':
        x = stream.popleft()
        if x == ':':
            S(stream)
            Q(stream)
            return
        else:
            stream.appendleft(x)
    else:
        stream.appendleft(x)
    x = stream.popleft()
    if x == '}':
        return
    else:
        stream.appendleft(x)
    raise Exception('no rule found')
def E(stream):
    #debug info
    print(E.__name__, ''.join(stream))
    x = stream.popleft()
    if x == ',':
        C(stream)
        return
    else:
        stream.appendleft(x)
    x = stream.popleft()
    if x == ']':
        return
    else:
        stream.appendleft(x)
    raise Exception('no rule found')
def S(stream):
    #debug info
    print(S.__name__, ''.join(stream))
    if len(stream) == 0:
        return
    x = stream.popleft()
    if x == '{':
        A(stream)
        return
    else:
        stream.appendleft(x)
    x = stream.popleft()
    if x == '(':
        B(stream)
        return
    else:
        stream.appendleft(x)
    x = stream.popleft()
    if x == '[':
        C(stream)
        return
    else:
        stream.appendleft(x)
    x = stream.popleft()
    if x == 'x':
        return
    else:
        stream.appendleft(x)
    return
def W(stream):
    #debug info
    print(W.__name__, ''.join(stream))
    x = stream.popleft()
    if x == ',':
        B(stream)
        return
    else:
        stream.appendleft(x)
    x = stream.popleft()
    if x == ')':
        return
    else:
        stream.appendleft(x)
    raise Exception('no rule found')
def B(stream):
    #debug info
    print(B.__name__, ''.join(stream))
    S(stream)
    W(stream)
    return
    x = stream.popleft()
    if x == ')':
        return
    else:
        stream.appendleft(x)
    raise Exception('no rule found')
