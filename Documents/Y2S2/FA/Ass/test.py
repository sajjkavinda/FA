t = int(input("how many times: "))
i = 0
j = 0

for n in range(t):
    a = int(input("a: "))
    b = int(input("b: "))
    k = int(input("k: "))

    x = [a, a+b]

    while (i<100):
        y = a+(i*b)
        x.append(y)
        i = i+1
    while (j<100):
        m = b+(i*a)
        x.append(m)
        j = j+1
    pp = (''.join(map(str, x)))
    #print(x)
    print(pp[k+1])
    i = 0
    j = 0

