str0 = 'BWWWWWBWWWW'

def EnRunLength(str0):
    code = ''
    connect = 1

    for i in range(1, len(str0)):
        if str0[i] != str0[i-1]:
            code = code  + str(connect) + str0[i-1]
            connect = 1
        else:
            connect += 1

    code = code + str(connect) + str0[len(str0) - 1]
    return code

def DeRunLength(code):
    connect = ''
    str0 = ''

    for i in range(0, len(code)):
        if code[i].isalpha():
            for j in range(0 , int(connect)):
                str0 += code[i]
            connect = ''
        else:
            connect = connect + code[i]

    return str0

code = EnRunLength(str0)
print(code)
print(DeRunLength(code))
