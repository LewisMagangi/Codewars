def rot13(m):
    m = list(m)
    for i in range(len(m)):
        if ord(m[i]) < 110 and ord(m[i]) >= 97:
            m[i] = chr(ord(m[i]) + 13)
        elif ord(m[i]) >= 110 and ord(m[i]) <= 122:
            m[i] = chr(ord(m[i]) - 13)
        elif ord(m[i]) < 78 and ord(m[i]) >= 65:
            m[i] = chr(ord(m[i]) + 13)
        elif ord(m[i]) >= 78 and ord(m[i]) <= 90:
            m[i] = chr(ord(m[i]) - 13)
    return "".join(m)