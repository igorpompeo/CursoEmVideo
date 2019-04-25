def formatar(v):
    f = format(v, '.2f')
    return 'R$ ' + f

def aumentar(v, n):
    a = (v + (v * (n/100)) * 1)
    return a

def dobro(v):
    d = v * 2
    return d

def metade(v):
    m = v / 2
    return m

def reduzir(v, n):
    r = (v - (v * (n/100)) * 1)
    return r