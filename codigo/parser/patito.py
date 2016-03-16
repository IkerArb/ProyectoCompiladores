# -----------------------------------------------------------------------------
# patito.py
#
# Un simple parser para la clase de compiladores.
# Basado en el ejemplo de calc.py de la libreria ply v 3.8
# -----------------------------------------------------------------------------

import sys
import pprint
pp = pprint.PrettyPrinter(indent=4)

if sys.version_info[0] >= 3:
    raw_input = input

tokens = (
    'VAR','FUNC','NEW','LIST','IF', 'ELSE',
    'FOR','NOT','AND','OR','SET','APPEND',
    'LENGTH','GET','REMOVE','NOTA','PRINT',
    'CALL', 'RETURN', 'INT', 'CHAR', 'FLOAT',
    'BOOL','NOTEQ', 'LTHANEQ', 'MTHANEQ', 'EQ',
    'CTEF', 'CTEE', 'CTEBOOL', 'CTECHAR', 'ID',
    'CANCION','WHILE','PLAY'
    )

literals = ['(',')',',',':',';', '{','}','*','/','',',',';','>','<','=','+']

# Tokens
def t_PLAY(t):
    r'PLAY'
    return t

def t_WHILE(t):
    r'WHILE'
    return t

def t_CANCION(t):
    r'CANCION'
    return t

def t_VAR(t):
    r'VAR'
    return t

def t_FUNC(t):
    r'FUNC'
    return t

def t_NEW(t):
    r'NEW'
    return t

def t_LIST(t):
    r'LIST'
    return t

def t_IF(t):
    r'IF'
    return t

def t_ELSE(t):
    r'ELSE'
    return t

def t_FOR(t):
    r'FOR'
    return t

def t_NOT(t):
    r'NOT'
    return t

def t_AND(t):
    r'AND'
    return t

def t_OR(t):
    r'OR'
    return t

def t_SET(t):
    r'SET'
    return t

def t_APPEND(t):
    r'APPEND'
    return t

def t_LENGTH(t):
    r'LENGTH'
    return t

def t_GET(t):
    r'GET'
    return t

def t_REMOVE(t):
    r'REMOVE'
    return t

def t_NOTA(t):
    r'([A-G][1-7])|([A,C,D,F,G][#][1-7])'
    return t

def t_PRINT(t):
    r'PRINT'
    return t

def t_CALL(t):
    r'CALL'
    return t

def t_RETURN(t):
    r'RETURN'
    return t

def t_INT(t):
    r'INT'
    return t

def t_CHAR(t):
    r'CHAR'
    return t

def t_FLOAT(t):
    r'FLOAT'
    return t

def t_BOOL(t):
    r'BOOL'
    return t

def t_NOTEQ(t):
    r'!='
    return t

def t_LTHANEQ(t):
    r'<='
    return t

def t_MTHANEQ(t):
    r'>='
    return t

def t_EQ(t):
    r'=='
    return t

def t_CTEF(t):
    r'[0-9]+([eE]([+]|[-])?|[.][0-9]+[eE]([+]|[-])?|[.])[0-9]+'
    t.value = float(t.value)
    return t

def t_CTEE(t):
    r'[0-9]+'
    t.value = int(t.value)
    return t

def t_CTECHAR(t):
    r'\"[^\n"]\"'
    return t

def t_CTEBOOL(t):
    r'\"true\"| \"false\"'
    t.value = bool(t.value)
    return t

def t_ID(t):
    r'[A-Za-z]([_]?([a-zA-Z]|[0-9]))*'
    return t

t_ignore = " \t\n"

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
import ply.lex as lex
lex.lex()


###############################################
## Cubo Semantico                            ##
###############################################
INT = 100
CHAR = 200
FLOAT = 300
BOOL = 400
MULT = 1
DIV = 2
AND = 3
OR = 4
EQEQ = 5
NOTEQ = 6
GT = 7
LT = 8
GTE = 9
LTE = 10
PLUS = 11
MINUS = 12
NOT = 13
EQ = 14
PLAY = 15
PRINT = 16
ERR = -1
USELESS = -2

cubo_semantico = {}

#####################################
## multiplication operation  cube  ##
#####################################
cubo_semantico[INT,INT,MULT]=INT
cubo_semantico[INT,CHAR,MULT]=ERR
cubo_semantico[INT,FLOAT,MULT]=FLOAT
cubo_semantico[INT,BOOL,MULT]=ERR
cubo_semantico[CHAR,CHAR,MULT]=ERR
cubo_semantico[CHAR,FLOAT,MULT]=ERR
cubo_semantico[CHAR,BOOL,MULT]=ERR
cubo_semantico[FLOAT,FLOAT,MULT]=FLOAT
cubo_semantico[FLOAT,BOOL,MULT]=ERR
cubo_semantico[BOOL,BOOL,MULT]=ERR

#####################################
## division operation cube         ##
#####################################
cubo_semantico[INT,INT,DIV]=INT
cubo_semantico[INT,CHAR,DIV]=ERR
cubo_semantico[INT,FLOAT,DIV]=FLOAT
cubo_semantico[INT,BOOL,DIV]=ERR
cubo_semantico[CHAR,CHAR,DIV]=ERR
cubo_semantico[CHAR,FLOAT,DIV]=ERR
cubo_semantico[CHAR,BOOL,DIV]=ERR
cubo_semantico[FLOAT,FLOAT,DIV]=FLOAT
cubo_semantico[FLOAT,BOOL,DIV]=ERR
cubo_semantico[BOOL,BOOL,DIV]=ERR

#####################################
## and operation cube              ##
#####################################
cubo_semantico[INT,INT,AND]=ERR
cubo_semantico[INT,CHAR,AND]=ERR
cubo_semantico[INT,FLOAT,AND]=ERR
cubo_semantico[INT,BOOL,AND]=ERR
cubo_semantico[CHAR,CHAR,AND]=ERR
cubo_semantico[CHAR,FLOAT,AND]=ERR
cubo_semantico[CHAR,BOOL,AND]=ERR
cubo_semantico[FLOAT,FLOAT,AND]=ERR
cubo_semantico[FLOAT,BOOL,AND]=ERR
cubo_semantico[BOOL,BOOL,AND]=BOOL

#####################################
## or  operation cube              ##
#####################################
cubo_semantico[INT,INT,OR]=ERR
cubo_semantico[INT,CHAR,OR]=ERR
cubo_semantico[INT,FLOAT,OR]=ERR
cubo_semantico[INT,BOOL,OR]=ERR
cubo_semantico[CHAR,CHAR,OR]=ERR
cubo_semantico[CHAR,FLOAT,OR]=ERR
cubo_semantico[CHAR,BOOL,OR]=ERR
cubo_semantico[FLOAT,FLOAT,OR]=ERR
cubo_semantico[FLOAT,BOOL,OR]=ERR
cubo_semantico[BOOL,BOOL,OR]=BOOL

#####################################
## ==  operation cube              ##
#####################################
cubo_semantico[INT,INT,EQEQ]=BOOL
cubo_semantico[INT,CHAR,EQEQ]=ERR
cubo_semantico[INT,FLOAT,EQEQ]=BOOL
cubo_semantico[INT,BOOL,EQEQ]=ERR
cubo_semantico[CHAR,CHAR,EQEQ]=BOOL
cubo_semantico[CHAR,FLOAT,EQEQ]=ERR
cubo_semantico[CHAR,BOOL,EQEQ]=ERR
cubo_semantico[FLOAT,FLOAT,EQEQ]=BOOL
cubo_semantico[FLOAT,BOOL,EQEQ]=ERR
cubo_semantico[BOOL,BOOL,EQEQ]=BOOL

#####################################
## notequals  operation cube       ##
#####################################
cubo_semantico[INT,INT,NOTEQ]=BOOL
cubo_semantico[INT,CHAR,NOTEQ]=ERR
cubo_semantico[INT,FLOAT,NOTEQ]=BOOL
cubo_semantico[INT,BOOL,NOTEQ]=ERR
cubo_semantico[CHAR,CHAR,NOTEQ]=BOOL
cubo_semantico[CHAR,FLOAT,NOTEQ]=ERR
cubo_semantico[CHAR,BOOL,NOTEQ]=ERR
cubo_semantico[FLOAT,FLOAT,NOTEQ]=BOOL
cubo_semantico[FLOAT,BOOL,NOTEQ]=ERR
cubo_semantico[BOOL,BOOL,NOTEQ]=BOOL


#####################################
## gt operation cube               ##
#####################################
cubo_semantico[INT,INT,GT]=BOOL
cubo_semantico[INT,CHAR,GT]=ERR
cubo_semantico[INT,FLOAT,GT]=BOOL
cubo_semantico[INT,BOOL,GT]=ERR
cubo_semantico[CHAR,CHAR,GT]=ERR
cubo_semantico[CHAR,FLOAT,GT]=ERR
cubo_semantico[CHAR,BOOL,GT]=ERR
cubo_semantico[FLOAT,FLOAT,GT]=BOOL
cubo_semantico[FLOAT,BOOL,GT]=ERR
cubo_semantico[BOOL,BOOL,GT]=ERR

#####################################
## lt operation cube               ##
#####################################
cubo_semantico[INT,INT,LT]=BOOL
cubo_semantico[INT,CHAR,LT]=ERR
cubo_semantico[INT,FLOAT,LT]=BOOL
cubo_semantico[INT,BOOL,LT]=ERR
cubo_semantico[CHAR,CHAR,LT]=ERR
cubo_semantico[CHAR,FLOAT,LT]=ERR
cubo_semantico[CHAR,BOOL,LT]=ERR
cubo_semantico[FLOAT,FLOAT,LT]=BOOL
cubo_semantico[FLOAT,BOOL,LT]=ERR
cubo_semantico[BOOL,BOOL,LT]=ERR

#####################################
## gte operation cube              ##
#####################################
cubo_semantico[INT,INT,GTE]=BOOL
cubo_semantico[INT,CHAR,GTE]=ERR
cubo_semantico[INT,FLOAT,GTE]=BOOL
cubo_semantico[INT,BOOL,GTE]=ERR
cubo_semantico[CHAR,CHAR,GTE]=ERR
cubo_semantico[CHAR,FLOAT,GTE]=ERR
cubo_semantico[CHAR,BOOL,GTE]=ERR
cubo_semantico[FLOAT,FLOAT,GTE]=BOOL
cubo_semantico[FLOAT,BOOL,GTE]=ERR
cubo_semantico[BOOL,BOOL,GTE]=ERR

#####################################
## lte operation cube              ##
#####################################
cubo_semantico[INT,INT,LTE]=BOOL
cubo_semantico[INT,CHAR,LTE]=ERR
cubo_semantico[INT,FLOAT,LTE]=BOOL
cubo_semantico[INT,BOOL,LTE]=ERR
cubo_semantico[CHAR,CHAR,LTE]=ERR
cubo_semantico[CHAR,FLOAT,LTE]=ERR
cubo_semantico[CHAR,BOOL,LTE]=ERR
cubo_semantico[FLOAT,FLOAT,LTE]=BOOL
cubo_semantico[FLOAT,BOOL,LTE]=ERR
cubo_semantico[BOOL,BOOL,LTE]=ERR

#####################################
## plus operation cube             ##
#####################################
cubo_semantico[INT,INT,PLUS]=INT
cubo_semantico[INT,CHAR,PLUS]=ERR
cubo_semantico[INT,FLOAT,PLUS]=FLOAT
cubo_semantico[INT,BOOL,PLUS]=ERR
cubo_semantico[CHAR,CHAR,PLUS]=ERR
cubo_semantico[CHAR,FLOAT,PLUS]=ERR
cubo_semantico[CHAR,BOOL,PLUS]=ERR
cubo_semantico[FLOAT,FLOAT,PLUS]=FLOAT
cubo_semantico[FLOAT,BOOL,PLUS]=ERR
cubo_semantico[BOOL,BOOL,PLUS]=ERR

#####################################
## neg operation cube              ##
#####################################
cubo_semantico[INT,MINUS,USELESS]=INT
cubo_semantico[CHAR,MINUS,USELESS]=ERR
cubo_semantico[FLOAT,MINUS,USELESS]=FLOAT
cubo_semantico[BOOL,MINUS,USELESS]=ERR

#####################################
## not operation cube              ##
#####################################
cubo_semantico[INT,NOT,USELESS]=ERR
cubo_semantico[CHAR,NOT,USELESS]=ERR
cubo_semantico[FLOAT,NOT,USELESS]=ERR
cubo_semantico[BOOL,NOT,USELESS]=BOOL

#####################################
## equals operation cube           ##
#####################################
cubo_semantico[INT,INT,EQ]=INT
cubo_semantico[INT,CHAR,EQ]=ERR
cubo_semantico[INT,FLOAT,EQ]=ERR
cubo_semantico[INT,BOOL,PLUS]=ERR
cubo_semantico[CHAR,CHAR,PLUS]=CHAR
cubo_semantico[CHAR,FLOAT,PLUS]=ERR
cubo_semantico[CHAR,BOOL,PLUS]=ERR
cubo_semantico[FLOAT,FLOAT,PLUS]=FLOAT
cubo_semantico[FLOAT,BOOL,PLUS]=ERR
cubo_semantico[BOOL,BOOL,PLUS]=BOOL

####################################
## PILAS AUXILIARES               ##
####################################
pilaO=[]
pOper=[]
pTipos=[]

####################################
## CUADRUPLOS                     ##
####################################
cuadruplos={}
contCuad = 1

####################################
## TEMPORALES                     ##
####################################
contTemp=1001

#diccionario de listas, pos0 = tipo, pos1 = vars
dir_procs = {}
auxDic = {}
scope = []
pos_dics_var = 1
# Parsing rules

#estructura dir_proc = ["global",vars{}]
def p_programa(p):
    'programa : creadirprocglobal a c cancion'
    print('done with file!\n')

    pp.pprint(dir_procs)

    pass

def p_creadirprocglobal(p):
    'creadirprocglobal : '
    dir_procs['global'] = ['global',{}]
    scope.append('global')
    pass

def p_a(p):
    ''' a : empty
          | vars b'''
    pass

def p_b(p):
    '''b : empty
         | a'''
    pass

def p_c(p):
    '''c : empty
         | funcion d'''
    pass

def p_d(p):
    '''d : empty
         | c'''
    pass

def p_vars(p):
    'vars : VAR v ":" tipo ";"'
    auxDic = dir_procs[scope[-1]][pos_dics_var]
    print auxDic
    if p[2] in auxDic:
        print "Variable con ese ID ya existe en ese scope"
    else:
        auxDic[p[2]] = []
        auxDic[p[2]].append(p[4])
    pass

def p_v(p):
    'v : ID'
    p[0] = p[1]
    pass

#def p_e(p):
#    '''e : empty
#         | "," v'''
#    pass

# estructura de dir_proc = [tipo,vars{}]

def p_funcion(p):
    'funcion : FUNC tipo ID meterfuncion "(" params ")" f bloque'
    if p[4] != -1:
        scope.pop()
    pass

def p_meterfuncion(p):
    'meterfuncion : '
    if p[-1] in dir_procs:
        print "Funcion con ese ID ya existe en el programa"
        p[0] = -1
    else:
        dir_procs[p[-1]] = [p[-2],{}]
        scope.append(p[-1])
    pass

def p_f(p):
    '''f : empty
         | vars g'''
    pass

def p_g(p):
    '''g : empty
         | f'''
    pass

def p_params(p):
    '''params : empty
              | tipo ID meterparams h'''
    pass

def p_meterparams(p):
    'meterparams : '
    dic_var = dir_procs[scope[-1]][pos_dics_var]
    dic_var[p[-1]] = [p[-2]]
    pass

def p_h(p):
    '''h : empty
         | "," params'''
    pass

def p_i(p):
    '''i : empty
         | estatuto j'''
    pass

def p_j(p):
    '''j : empty
         | i'''
    pass

def p_bloque(p):
    'bloque : "{" i "}"'
    pass

# estructura de dir_proc = ['CANCION',vars{},tempo]

def p_cancion(p):
    'cancion : CANCION "(" CTEE ")" metercancion f bloque'
    scope.pop()
    pass

def p_metercancion(p):
    'metercancion : '
    scope.append(p[-4])
    dir_procs[p[-4]] = [p[-4],{},p[-2]] #cancion tiene tempo como parametro extra en su lista
    pass

def p_estatuto(p):
    '''estatuto : asignacion
                | if
                | for
                | return
                | while
                | play
                | print'''
    pass

def p_asignacion(p):
    'asignacion : ID "=" neur8  k ";"'
    if pOper[-1] == EQ:
        op = pOper.pop()
        opdoDer = pilaO.pop()
        tipoDer = pTipos.pop()
        opdoIzq = pilaO.pop()
        tipoIzq = pTipos.pop()
        tipoRes = cubo_semantico[tipoIzq,tipoDer,op]
        if tipoRes != ERR :
            cuadruplos[contCuad] = [op,opdoIzq,opdoDer,contTemp]
            contTemp+=1
            contCuad+=1
        else:
            print("Type mismatch")
            exit()
    else:
        print("Asignacion mal terminada")
    pass

#############################
## punto neuralgico 8      ##
#############################

def p_neur8(p):
    'neur8 : '
    auxDic = dir_procs[scope[-1]][pos_dics_var]
    print auxDic
    if p[-2] in auxDic:
        pilaO.append(p[-2])
        pTipos.append(auxDic[p[-2]])
        pOper.append(EQ)
    else:
        print "No existe tal variable a asignar"
        exit()
    pass

def p_k(p):
    '''k : expresion
         | asiglista'''
    pass

def p_asiglista(p):
    'asiglista : NEW LIST "(" ")"'
    pass

def p_if(p):
    'if : IF "(" expresion ")" bloque l ";"'
    pass

def p_l(p):
    '''l : empty
         | ELSE bloque'''
    pass

def p_for(p):
    'for : FOR "(" asignacion expresion asignacion ")" bloque ";"'
    pass

def p_expresion(p):
    'expresion : m subexpresion'
    if pOper[-1] == NOT:
        op = pOper.pop()
        opdoIzq = pilaO.pop()
        tipoIzq = pTipos.pop()
        tipoRes = cubo_semantico[tipoIzq,op,USELESS]
        if tipoRes != ERR :
            cuadruplos[contCuad] = [op,opdoIzq,"",contTemp]
            pilaO.append(contTemp)
            pTipos.append(tipoRes)
            contTemp+=1
            contCuad+=1
        else:
            print("Type mismatch")
            exit()
    pass

def p_m(p):
    '''m : empty
         | NOT'''
    pOper.append(NOT)
    pass

def p_subexpresion(p):
    'subexpresion : exp neur10 o'
    pass

#############################
## punto neuralgico 10      ##
#############################

def p_neur10(p):
    'neur10 : '
    if pOper[-1] == AND or pOper[-1] == OR:
        op = pOper.pop()
        opdoDer = pilaO.pop()
        tipoDer = pTipos.pop()
        opdoIzq = pilaO.pop()
        tipoIzq = pTipos.pop()
        tipoRes = cubo_semantico[tipoIzq,tipoDer,op]
        if tipoRes != ERR :
            cuadruplos[contCuad] = [op,opdoIzq,opdoDer,contTemp]
            pilaO.append(contTemp)
            pTipos.append(tipoRes)
            contTemp+=1
            contCuad+=1
        else:
            print("Type mismatch")
            exit()
    pass

def p_o(p):
    '''o : empty
         | AND neur9_1 subexpresion
         | OR neur9_2 subexpresion'''
    pass

#############################
## punto neuralgico 9      ##
#############################

def p_neur9_1(p):
    'neur9_1 : '
    pOper.append(AND)
    pass

def p_neur9_2(p):
    'neur9_2 : '
    pOper.append(OR)
    pass


def p_exp(p):
    'exp : nexp neur12 p'
    pass

#############################
## punto neuralgico 12     ##
#############################

def p_neur12(p):
    'neur12 : '
    if pOper[-1] == EQEQ or pOper[-1] == NOTEQ or pOper[-1] == GT or pOper[-1] == LT or pOper[-1] == GTE or pOper[-1] == LTE:
        op = pOper.pop()
        opdoDer = pilaO.pop()
        tipoDer = pTipos.pop()
        opdoIzq = pilaO.pop()
        tipoIzq = pTipos.pop()
        tipoRes = cubo_semantico[tipoIzq,tipoDer,op]
        if tipoRes != ERR :
            cuadruplos[contCuad] = [op,opdoIzq,opdoDer,contTemp]
            pilaO.append(contTemp)
            pTipos.append(tipoRes)
            contTemp+=1
            contCuad+=1
        else:
            print("Type mismatch")
            exit()
    pass

def p_p(p):
    '''p : empty
         | EQ neur11_1 nexp
         | NOTEQ neur11_2 nexp
         | ">" neur11_3 nexp
         | "<" neur11_4 nexp
         | MTHANEQ neur11_5 nexp
         | LTHANEQ neur11_6 nexp'''
    pass

#############################
## punto neuralgico 11     ##
#############################

def p_neur11_1(p):
    'neur11_1 : '
    pOper.append(EQEQ)
    pass

def p_neur11_2(p):
    'neur11_2 : '
    pOper.append(NOTEQ)
    pass

def p_neur11_3(p):
    'neur11_3 : '
    pOper.append(GT)
    pass

def p_neur11_4(p):
    'neur11_4 : '
    pOper.append(LT)
    pass

def p_neur11_5(p):
    'neur11_5 : '
    pOper.append(GTE)
    pass

def p_neur11_6(p):
    'neur11_6 : '
    pOper.append(LTE)
    pass

def p_nexp(p):
    'nexp : termino neur5 q'
    pass

#############################
## punto neuralgico 5      ##
#############################

def p_neur5(p):
    'neur5 : '
    if pOper[-1] == PLUS or pOper[-1]== MINUS :
        op = pOper.pop()
        opdoDer = pilaO.pop()
        tipoDer = pTipos.pop()
        opdoIzq = pilaO.pop()
        tipoIzq = pTipos.pop()
        tipoRes = cubo_semantico[tipoIzq,tipoDer,op]
        if tipoRes != ERR :
            cuadruplos[contCuad] = [op,opdoIzq,opdoDer,contTemp]
            pilaO.append(contTemp)
            pTipos.append(tipoRes)
            contTemp+=1
            contCuad+=1
        else:
            print("Type mismatch")
            exit()
    pass


def p_q(p):
    '''q : empty
         | "+" neur3_1 nexp
         | "-" neur3_2 nexp'''
    pass

#############################
## punto neuralgico 3      ##
#############################
def p_neur3_1(p):
    'neur3_1 : '
    pOper.append(PLUS)
    pass

def p_neur3_2(p):
    'neur3_2 : '
    pOper.append(MINUS)
    pass

def p_termino(p):
    'termino : factor neur4 n'
    pass

#############################
## punto neuralgico 4      ##
#############################

def p_neur4(p):
    'neur4 : '
    if pOper[-1] == MULT or pOper[-1]== MULT :
        op = pOper.pop()
        opdoDer = pilaO.pop()
        tipoDer = pTipos.pop()
        opdoIzq = pilaO.pop()
        tipoIzq = pTipos.pop()
        tipoRes = cubo_semantico[tipoIzq,tipoDer,op]
        if tipoRes != ERR :
            cuadruplos[contCuad] = [op,opdoIzq,opdoDer,contTemp]
            pilaO.append(contTemp)
            pTipos.append(tipoRes)
            contTemp+=1
            contCuad+=1
        else:
            print("Type mismatch")
            exit()
    pass

def p_n(p):
    '''n : empty
         | "*" neur2_1 termino
         | "/" neur2_2 termino'''
    pass

#############################
## punto neuralgico 2      ##
#############################

def p_neur2_1(p):
    'neur2_1 : '
    pOper.append(MULT)
    pass

def p_neur2_2(p):
    'neur2_2 : '
    pOper.append(DIV)
    pass

def p_factor(p):
    '''factor : "(" neur6 expresion ")" neur7
              | varcte neur1'''
    pass

#############################
## punto neuralgico 6      ##
#############################

def p_neur6(p):
    'neur6 : '
    pOper.append("(")
    pass

#############################
## punto neuralgico 7      ##
#############################

def p_neur7(p):
    'neur7 : '
    if pOper[-1] == "(" :
        pOper.pop()
    else:
        print("Missing opening parenthesis")
    pass

#############################
## punto neuralgico 1      ##
#############################

def p_neur1(p):
    'neur1 : '
    pilaO.append(p[-1])
    pass

def p_varcte(p):
    '''varcte : ID r neurVar
              | CTEE neurCteE
              | CTEF neurCteF
              | CTEBOOL neurCteB
              | callfunc
              | CTECHAR neurCteCh'''
    pass

#############################
## punto neuralgico var    ##
#############################

def p_neurVar(p):
    'neurVar : '
    if pOper[-1] == -1:
        auxDic = dir_procs[scope[-1]][pos_dics_var]
        if p[-2] in auxDic:
            pTipos.append(auxDic[p[-2]])
        else:
            print "No existe tal variable"
            exit()
    pass

#############################
## punto neuralgico int    ##
#############################

def p_neurCteE(p):
    'neurCteE : '
    pTipos.append(INT)
    pass

#############################
## punto neuralgico char   ##
#############################

def p_neurCteF(p):
    'neurCteF : '
    pTipos.append(FLOAT)
    pass

#############################
## punto neuralgico bool   ##
#############################

def p_neurCteB(p):
    'neurCteB : '
    pTipos.append(BOOL)
    pass

#############################
## punto neuralgico char   ##
#############################

def p_neurCteCh(p):
    'neurCteCh : '
    pTipos.append(CHAR)
    pass


def p_r(p):
    '''r : empty
         | oplista'''
    if p[1] == "":
        p[0] = -1
    else:
        p[0] = 1
    pass

def p_oplista(p):
    'oplista : ID "." x'
    p[0] = p[3]
    pass

def p_x(p):
    '''x : inlistset
         | append
         | length
         | getlist
         | removelist'''
    p[0] = p[1]
    pass

def p_inlistset(p):
    'inlistset : SET "(" CTEE "," expresion ")"'
    p[0] = 1
    pass

def p_append(p):
    'append : APPEND "(" expresion ")"'
    p[0] = 2
    pass

def p_length(p):
    'length : LENGTH "(" ")"'
    p[0] = 3
    pass

def p_getlist(p):
    'getlist : GET "(" expresion ")"'
    p[0] = 4
    pass

def p_removelist(p):
    'removelist : REMOVE "(" expresion ")"'
    p[0] = 5
    pass

def p_while(p):
    'while : WHILE "(" expresion ")" bloque ";"'
    pass

def p_play(p):
    'play : PLAY "(" NOTA "," CTEE ")" ";"'
    op = PLAY
    opdoIzq = p[3]
    opdoDer = p[5]
    cuadruplos[contCuad] = [op,opdoIzq,opdoDer,""]
    contCuad+=1
    pass

def p_print(p):
    'print : PRINT expresion ";"'
    op = PRINT
    opdoIzq = p[2]
    cuadruplos[contCuad] = [op,opdoIzq,"",""]
    contCuad+=1
    pass

def p_callfunc(p):
    'callfunc : CALL ID "(" s ")" ";"'
    pass

def p_s(p):
    '''s : empty
         | expresion t'''
    pass

def p_t(p):
    '''t : empty
         | "," s'''
    pass

def p_return(p):
    'return : RETURN "(" expresion ")" ";"'
    pass

def p_tipo(p):
    'tipo : u y'
    p[0] = p[2]
    pass

def p_u(p):
    '''u : empty
         | LIST'''
    pass

def p_y(p):
    '''y : INT
         | CHAR
         | FLOAT
         | BOOL'''
    if p[1]=="INT" :
        p[0] = INT
    elif p[1]=="CHAR" :
        p[0] = CHAR
    elif p[1]=="FLOAT" :
        p[0] = FLOAT
    elif p[1]=="BOOL" :
        p[0] = BOOL
    pass

def p_empty(t):
    'empty : '
    pass

def p_error(p):
    if p:
        print("Syntax error at '%s'" % p.value)
    else:
        print("Syntax error at EOF")

import ply.yacc as yacc
yacc.yacc()

f = open(str(sys.argv[1]), 'r')
s = f.read()
f.close()
yacc.parse(s)
