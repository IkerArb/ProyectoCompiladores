class Memoria:
    def __init__(self, vi, vf, vb, vc, ti, tf, tb, tc, globalmem):
        aux = 0
        self.ints = {}
        self.floats = {}
        self.bools = {}
        self.chars = {}
        if globalmem:
            aux_vi = 1000
            aux_vf = 3000
            aux_vb = 5000
            aux_vc = 7000
        else:
            aux_vi = 9000
            aux_vf = 11000
            aux_vb = 13000
            aux_vc = 15000

        aux_ti = 17000
        aux_tf = 21000
        aux_tb = 25000
        aux_tc = 29000
        while aux < vi:
            self.ints[aux_vi]=0
            aux_vi += 1
            aux += 1
        aux = 0
        while aux < vf:
            self.floats[aux_vf]=0.0
            aux_vf += 1
            aux += 1
        aux = 0
        while aux < vb:
            self.bools[aux_vb] = True
            aux_vb += 1
            aux += 1
        aux = 0
        while aux < vc:
            self.chars[aux_vc] = ''
            aux_vc += 1
            aux += 1
        aux = 0
        while aux < ti:
            self.ints[aux_ti] = 0
            aux_ti += 1
            aux += 1
        aux = 0
        while aux < tf:
            self.floats[aux_tf] = 0.0
            aux_tf += 1
            aux += 1
        aux = 0
        while aux < tb:
            self.bools[aux_tb] = True
            aux_tb += 1
            aux += 1
        aux = 0
        while aux < tc:
            self.chars[aux_tc] = ''
            aux_tc += 1
            aux += 1
