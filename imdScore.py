
def score(cp,op,bv,bu,sb,yd,om,dv,pe):

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
    elif cp < (0.505*op):
        pcs = 1
    elif cp < (0.895*op):
        pcs = 2
    elif cp < (0.995*op):
        pcs = 5
    elif cp > (0.9949*op) and cp < (1.0149*op):
        pcs = 6
    elif cp < (1.1049*op):
        pcs = 7
    elif cp < (1.9949*op):
        pcs = 9
    else:
        pcs = 10

    if bv < 1:
        bvs = 1
    elif bv < 2:
        bvs = 2
    elif bv < 5:
        bvs = 3
    elif bv < 10:
        bvs = 4
    elif bv < 15:
        bvs = 5
    elif bv < 20:
        bvs = 6
    elif bv < 30:
        bvs = 7
    elif bv < 50:
        bvs = 8
    elif bv < 100:
        bvs = 9
    else:
        bvs = 10

    if cp < (0.4949*bv):
        bps = 10
    elif cp < (0.895*bv):
        bps = 8
    elif cp < (0.995*bv):
        bps = 6
    elif cp < (1.0149*bv):
        bps = 4
    elif cp < (1.0949*bv):
        bps = 2
    elif cp < (1.4949*bv):
        bps = 1
    else:
        bps = 0

    if bu < 1:
        bus = 0
    elif bu < 2:
        bus = 2
    elif bu < 4:
        bus = 3
    elif bu < 6:
        bus = 4
    else:
        bus = 5

    if sb < 1:
        sbs = 0
    elif sb < 2:
        sbs = 3
    elif sb < 5:
        sbs = 4
    else:
        sbs = 5

    if yd == 0:
        yds = 0 
    elif yd < 1.5:
        yds = 1
    elif yd < 2.5:
        yds = 4
    elif yd < 4.5:
        yds = 6
    elif yd < 7.5:
        yds = 8
    elif yd < 10.5:
        yds = 10
    else:
        yds = 2

    if om < 1.49:
        oms = 0
    elif om < 4.5:
        oms = 1
    elif om < 9.5:
        oms = 2
    elif om < 14.5:
        oms = 3
    elif om < 19.5:
        oms = 4
    elif om < 29.5:
        oms = 5
    elif om < 49.5:
        oms = 6
    elif om < 69.5:
        oms = 8
    elif om < 79.5:
        oms = 9
    else:
        oms = 10
    
    if dv < 10001:
        dvs = 0
    elif dv < 30001:
        dvs = 1
    elif dv < 50001:
        dvs = 2
    elif dv < 100001:
        dvs = 3
    elif dv < 250001:
        dvs = 4 
    elif dv < 500001:
        dvs = 5
    elif dv < 750001:
        dvs = 6
    elif dv < 1000001:
        dvs = 8 
    elif dv < 2000001:
        dvs = 9
    else: 
        dvs = 10

    if pe < 1:
        pes = 0
    elif pe < 5.5:
        pes = 10
    elif pe < 15.5:
        pes = 9
    elif pe < 20.5:
        pes = 8
    elif pe < 25.5:
        pes = 7
    elif pe < 30.5:
        pes = 6
    elif pe < 35.5:
        pes = 5
    elif pe < 40.5:
        pes = 4
    elif pe < 100:
        pes = 2
    else:
        pes = 1

    total = cps + ops + pcs + bvs + bps + bus + sbs + yds + oms + dvs + pes
    return total
    
