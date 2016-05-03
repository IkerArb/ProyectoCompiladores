## clase de memoria la que se utiliza para pedir memoria
## cuando llamas a una nueva funcion, la global o la de
## cancion, nos ayuda a definir el tamano en variables
## del elemento y las casillas y los valores de ejecucion
## que agarra cada casilla, inicialmente arrancan en 0
class Memoria:
    ## unica funcion de la clase memoria en la que recibe la cantidad
    ## de variables por tipo y temporales por tipo y un booleano
    ## que dice si es global o no
    def __init__(self, vi, vf, vb, vc, ti, tf, tb, tc, globalmem):
        ## contador que empieza en 0 para cada ciclo
        aux = 0
        ## creamos los diccionarios para cada tipo de dato
        self.ints = {}
        self.floats = {}
        self.bools = {}
        self.chars = {}
        ## si es global los iniciales son distintos de los
        ## locales
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

        ## solo hay temporales locales por lo que no importa
        ## si es global o local
        aux_ti = 17000
        aux_tf = 21000
        aux_tb = 25000
        aux_tc = 29000
        ## hacemos las casillas para todas las variables
        ## enteras
        while aux < vi:
            ## inicialmente las declaramos en 0
            self.ints[aux_vi]=0
            ## sumamos el numero de casilla
            aux_vi += 1
            ## sumamos el contador para el ciclo
            aux += 1
        ## reiniciamos el contador de ciclo
        aux = 0
        ## hacemos las casillas para todas las variables
        ## flotantes
        while aux < vf:
            ## inicialmente las declaramos en 0.0
            self.floats[aux_vf]=0.0
            ## sumamos el numero de casilla
            aux_vf += 1
            ## sumamos el contador para el ciclo
            aux += 1
        ## reiniciamos el contador del ciclo
        aux = 0
        ## hacemos las casillas para todas las variables
        ## booleanas
        while aux < vb:
            ## inicialmente las declaramos en True
            self.bools[aux_vb] = True
            ## sumamos el numero de casilla
            aux_vb += 1
            ## sumamos el contador para el ciclo
            aux += 1
        ## reiniciamos el contador de ciclo
        aux = 0
        ## hacemos las casillas para todas las variables
        ## char
        while aux < vc:
            ## inicialmente las declaramos en ''
            self.chars[aux_vc] = ''
            ## sumamos el numero de casilla
            aux_vc += 1
            ## sumamos el contador para el ciclo
            aux += 1
        ## reiniciamos el contador de ciclo
        aux = 0
        ## hacemos las casillas para todas las temporales
        ## enteras
        while aux < ti:
            ## inicialmente las declaramos en 0
            self.ints[aux_ti] = 0
            ## sumamos el numero de casilla
            aux_ti += 1
            ## sumamos el contador de ciclo
            aux += 1
        ## reiniciamos el contador de ciclo
        aux = 0
        ## hacemos las casillas para todas las temporales
        ## flotantes
        while aux < tf:
            ## inicialmente las declaramos en 0.0
            self.floats[aux_tf] = 0.0
            ## sumamos el numero de casilla
            aux_tf += 1
            ## sumamos el contador de ciclo
            aux += 1
        ## reiniciamos el contador de ciclo
        aux = 0
        ## hacemos las casillas para todas las temporales
        ## booleanas
        while aux < tb:
            ## inicialmente las declaramos en True
            self.bools[aux_tb] = True
            ## sumamos el numero de casilla
            aux_tb += 1
            ## sumamos el contador de ciclo
            aux += 1
        ## reiniciamos el contador de ciclo
        aux = 0
        ## hacemos las casillas para todas las temporales
        ## char
        while aux < tc:
            ## inicialmente las declaramos en ''
            self.chars[aux_tc] = ''
            ## sumamos el numero de casilla
            aux_tc += 1
            ## sumamos el contador de ciclo
            aux += 1
