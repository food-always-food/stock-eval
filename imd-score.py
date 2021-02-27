
def score(cp,ob,bv,bu,sb,yd,om,dv,pe):
    calculated = 0

    if cp < 1:
        cps = 1
    elif cp < 2:
        cps = 2
    elif cp < 5:
        cps = 3
    elif cp < 10:
        cps = 4
    elif cp < 15:
        cps = 5
    elif cp < 20:
        cps = 6
    elif cp < 30:
        cps = 7
    elif cp < 50:
        cps = 8
    elif cp < 100:
        cps = 9
    else:
        cps = 10

     if op < 1:
        ops = 1
    elif op < 2:
        ops = 2
    elif op < 5:
        ops = 3
    elif op < 10:
        ops = 4
    elif op < 15:
        ops = 5
    elif op < 20:
        ops = 6
    elif op < 30:
        ops = 7
    elif op < 50:
        ops = 8
    elif op < 100:
        ops = 9
    else:
        ops = 10
    
    if op == 0:
        pcs = 0
    if cp < (.505*op):
        pcs = 1
    if cp <