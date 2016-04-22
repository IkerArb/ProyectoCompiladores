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
    'CANCION','WHILE','PLAY','VOID'
    )

literals = ['(',')',',',':',';', '{','}','*','/','',',',';','>','<','=','+','-','[',']','.']

# Tokens
def t_PLAY(t):
    r'PLAY'
    return t

def t_VOID(t):
    r'VOID'
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
    r'True| False'
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
## Operaciones                               ##
###############################################

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
GOTO = 17
GOTOF = 18
GOTOV = 19
ENDPROC = 20
ERA = 21
PARAMETRO = 22
GOSUB = 23
VERIFICA = 24
NEG = 25
ERR = -1
USELESS = -2

###############################################
## Tipos                                     ##
###############################################

INT = 100
CHAR = 200
FLOAT = 300
BOOL = 400

###############################################
## Cubo Semantico                            ##
###############################################

#diccionario padre
cubo_semantico = {}

#diccionario donde INT es el primer operando
cubo_semantico[INT] = {}

#diccionario donde CHAR es el primer operando
cubo_semantico[CHAR] = {}

#diccionario donde FLOAT es el primer operando
cubo_semantico[FLOAT] = {}

#diccionario donde BOOL es el primer operando
cubo_semantico[BOOL] = {}

#diccionarios vacios para cubo Semantico

cubo_semantico[INT][INT] = {}
cubo_semantico[INT][FLOAT] = {}
cubo_semantico[INT][CHAR] = {}
cubo_semantico[INT][BOOL] = {}
cubo_semantico[CHAR][CHAR] = {}
cubo_semantico[CHAR][FLOAT] = {}
cubo_semantico[CHAR][BOOL] = {}
cubo_semantico[FLOAT][FLOAT] = {}
cubo_semantico[FLOAT][BOOL] = {}
cubo_semantico[BOOL][BOOL] = {}

#####################################
## multiplication operation  cube  ##
#####################################
cubo_semantico[INT][INT][MULT]=INT
cubo_semantico[INT][CHAR][MULT]=ERR
cubo_semantico[INT][FLOAT][MULT]=FLOAT
cubo_semantico[INT][BOOL][MULT]=ERR
cubo_semantico[CHAR][CHAR][MULT]=ERR
cubo_semantico[CHAR][FLOAT][MULT]=ERR
cubo_semantico[CHAR][BOOL][MULT]=ERR
cubo_semantico[FLOAT][FLOAT][MULT]=FLOAT
cubo_semantico[FLOAT][BOOL][MULT]=ERR
cubo_semantico[BOOL][BOOL][MULT]=ERR

#####################################
## division operation cube         ##
#####################################
cubo_semantico[INT][INT][DIV]=INT
cubo_semantico[INT][CHAR][DIV]=ERR
cubo_semantico[INT][FLOAT][DIV]=FLOAT
cubo_semantico[INT][BOOL][DIV]=ERR
cubo_semantico[CHAR][CHAR][DIV]=ERR
cubo_semantico[CHAR][FLOAT][DIV]=ERR
cubo_semantico[CHAR][BOOL][DIV]=ERR
cubo_semantico[FLOAT][FLOAT][DIV]=FLOAT
cubo_semantico[FLOAT][BOOL][DIV]=ERR
cubo_semantico[BOOL][BOOL][DIV]=ERR

#####################################
## and operation cube              ##
#####################################
cubo_semantico[INT][INT][AND]=ERR
cubo_semantico[INT][CHAR][AND]=ERR
cubo_semantico[INT][FLOAT][AND]=ERR
cubo_semantico[INT][BOOL][AND]=ERR
cubo_semantico[CHAR][CHAR][AND]=ERR
cubo_semantico[CHAR][FLOAT][AND]=ERR
cubo_semantico[CHAR][BOOL][AND]=ERR
cubo_semantico[FLOAT][FLOAT][AND]=ERR
cubo_semantico[FLOAT][BOOL][AND]=ERR
cubo_semantico[BOOL][BOOL][AND]=BOOL

#####################################
## or  operation cube              ##
#####################################
cubo_semantico[INT][INT][OR]=ERR
cubo_semantico[INT][CHAR][OR]=ERR
cubo_semantico[INT][FLOAT][OR]=ERR
cubo_semantico[INT][BOOL][OR]=ERR
cubo_semantico[CHAR][CHAR][OR]=ERR
cubo_semantico[CHAR][FLOAT][OR]=ERR
cubo_semantico[CHAR][BOOL][OR]=ERR
cubo_semantico[FLOAT][FLOAT][OR]=ERR
cubo_semantico[FLOAT][BOOL][OR]=ERR
cubo_semantico[BOOL][BOOL][OR]=BOOL

#####################################
## ==  operation cube              ##
#####################################
cubo_semantico[INT][INT][EQEQ]=BOOL
cubo_semantico[INT][CHAR][EQEQ]=ERR
cubo_semantico[INT][FLOAT][EQEQ]=BOOL
cubo_semantico[INT][BOOL][EQEQ]=ERR
cubo_semantico[CHAR][CHAR][EQEQ]=BOOL
cubo_semantico[CHAR][FLOAT][EQEQ]=ERR
cubo_semantico[CHAR][BOOL][EQEQ]=ERR
cubo_semantico[FLOAT][FLOAT][EQEQ]=BOOL
cubo_semantico[FLOAT][BOOL][EQEQ]=ERR
cubo_semantico[BOOL][BOOL][EQEQ]=BOOL

#####################################
## notequals  operation cube       ##
#####################################
cubo_semantico[INT][INT][NOTEQ]=BOOL
cubo_semantico[INT][CHAR][NOTEQ]=ERR
cubo_semantico[INT][FLOAT][NOTEQ]=BOOL
cubo_semantico[INT][BOOL][NOTEQ]=ERR
cubo_semantico[CHAR][CHAR][NOTEQ]=BOOL
cubo_semantico[CHAR][FLOAT][NOTEQ]=ERR
cubo_semantico[CHAR][BOOL][NOTEQ]=ERR
cubo_semantico[FLOAT][FLOAT][NOTEQ]=BOOL
cubo_semantico[FLOAT][BOOL][NOTEQ]=ERR
cubo_semantico[BOOL][BOOL][NOTEQ]=BOOL


#####################################
## gt operation cube               ##
#####################################
cubo_semantico[INT][INT][GT]=BOOL
cubo_semantico[INT][CHAR][GT]=ERR
cubo_semantico[INT][FLOAT][GT]=BOOL
cubo_semantico[INT][BOOL][GT]=ERR
cubo_semantico[CHAR][CHAR][GT]=ERR
cubo_semantico[CHAR][FLOAT][GT]=ERR
cubo_semantico[CHAR][BOOL][GT]=ERR
cubo_semantico[FLOAT][FLOAT][GT]=BOOL
cubo_semantico[FLOAT][BOOL][GT]=ERR
cubo_semantico[BOOL][BOOL][GT]=ERR

#####################################
## lt operation cube               ##
#####################################
cubo_semantico[INT][INT][LT]=BOOL
cubo_semantico[INT][CHAR][LT]=ERR
cubo_semantico[INT][FLOAT][LT]=BOOL
cubo_semantico[INT][BOOL][LT]=ERR
cubo_semantico[CHAR][CHAR][LT]=ERR
cubo_semantico[CHAR][FLOAT][LT]=ERR
cubo_semantico[CHAR][BOOL][LT]=ERR
cubo_semantico[FLOAT][FLOAT][LT]=BOOL
cubo_semantico[FLOAT][BOOL][LT]=ERR
cubo_semantico[BOOL][BOOL][LT]=ERR

#####################################
## gte operation cube              ##
#####################################
cubo_semantico[INT][INT][GTE]=BOOL
cubo_semantico[INT][CHAR][GTE]=ERR
cubo_semantico[INT][FLOAT][GTE]=BOOL
cubo_semantico[INT][BOOL][GTE]=ERR
cubo_semantico[CHAR][CHAR][GTE]=ERR
cubo_semantico[CHAR][FLOAT][GTE]=ERR
cubo_semantico[CHAR][BOOL][GTE]=ERR
cubo_semantico[FLOAT][FLOAT][GTE]=BOOL
cubo_semantico[FLOAT][BOOL][GTE]=ERR
cubo_semantico[BOOL][BOOL][GTE]=ERR

#####################################
## lte operation cube              ##
#####################################
cubo_semantico[INT][INT][LTE]=BOOL
cubo_semantico[INT][CHAR][LTE]=ERR
cubo_semantico[INT][FLOAT][LTE]=BOOL
cubo_semantico[INT][BOOL][LTE]=ERR
cubo_semantico[CHAR][CHAR][LTE]=ERR
cubo_semantico[CHAR][FLOAT][LTE]=ERR
cubo_semantico[CHAR][BOOL][LTE]=ERR
cubo_semantico[FLOAT][FLOAT][LTE]=BOOL
cubo_semantico[FLOAT][BOOL][LTE]=ERR
cubo_semantico[BOOL][BOOL][LTE]=ERR

#####################################
## plus operation cube             ##
#####################################
cubo_semantico[INT][INT][PLUS]=INT
cubo_semantico[INT][CHAR][PLUS]=ERR
cubo_semantico[INT][FLOAT][PLUS]=FLOAT
cubo_semantico[INT][BOOL][PLUS]=ERR
cubo_semantico[CHAR][CHAR][PLUS]=ERR
cubo_semantico[CHAR][FLOAT][PLUS]=ERR
cubo_semantico[CHAR][BOOL][PLUS]=ERR
cubo_semantico[FLOAT][FLOAT][PLUS]=FLOAT
cubo_semantico[FLOAT][BOOL][PLUS]=ERR
cubo_semantico[BOOL][BOOL][PLUS]=ERR

#####################################
## minus operation cube            ##
#####################################
cubo_semantico[INT][INT][MINUS]=INT
cubo_semantico[INT][CHAR][MINUS]=ERR
cubo_semantico[INT][FLOAT][MINUS]=FLOAT
cubo_semantico[INT][BOOL][MINUS]=ERR
cubo_semantico[CHAR][CHAR][MINUS]=ERR
cubo_semantico[CHAR][FLOAT][MINUS]=ERR
cubo_semantico[CHAR][BOOL][MINUS]=ERR
cubo_semantico[FLOAT][FLOAT][MINUS]=FLOAT
cubo_semantico[FLOAT][BOOL][MINUS]=ERR
cubo_semantico[BOOL][BOOL][MINUS]=ERR

#####################################
## not operation cube              ##
#####################################
cubo_semantico[INT][NOT]=ERR
cubo_semantico[CHAR][NOT]=ERR
cubo_semantico[FLOAT][NOT]=ERR
cubo_semantico[BOOL][NOT]=BOOL

#####################################
## equals operation cube           ##
#####################################
cubo_semantico[INT][INT][EQ]=INT
cubo_semantico[INT][CHAR][EQ]=ERR
cubo_semantico[INT][FLOAT][EQ]=ERR
cubo_semantico[INT][BOOL][EQ]=ERR
cubo_semantico[CHAR][CHAR][EQ]=CHAR
cubo_semantico[CHAR][FLOAT][EQ]=ERR
cubo_semantico[CHAR][BOOL][EQ]=ERR
cubo_semantico[FLOAT][FLOAT][EQ]=FLOAT
cubo_semantico[FLOAT][BOOL][EQ]=ERR
cubo_semantico[BOOL][BOOL][EQ]=BOOL

### Caso especial para igualdad #####
cubo_semantico[FLOAT][INT] = {}
cubo_semantico[FLOAT][INT][EQ] = FLOAT


#####################################
## neg operation cube              ##
#####################################
cubo_semantico[INT][NEG]=INT
cubo_semantico[CHAR][NEG]=ERR
cubo_semantico[FLOAT][NEG]=FLOAT
cubo_semantico[BOOL][NEG]=ERR

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
## Variables globales enteras     ##
####################################
var_glob_int = 1000
var_glob_int_inicio = 1000

####################################
## Variables globales flotantes   ##
####################################
var_glob_float = 3000
var_glob_float_inicio = 3000

####################################
## Variables globales booleanas   ##
####################################
var_glob_bool = 5000
var_glob_bool_inicio = 5000

####################################
## Variables globales char        ##
####################################
var_glob_char = 7000
var_glob_char_inicio = 7000

####################################
## Variables locales enteras      ##
####################################
var_loc_int = 9000
var_loc_int_inicio = 9000

####################################
## Variables locales flotantes    ##
####################################
var_loc_float = 11000
var_loc_float_inicio = 11000

####################################
## Variables locales booleanas    ##
####################################
var_loc_bool = 13000
var_loc_bool_inicio = 13000

####################################
## Variables locales char         ##
####################################
var_loc_char = 15000
var_loc_char_inicio = 15000

##################################################
## Variables locales temporales enteras         ##
##################################################
var_loc_temp_int = 17000
var_loc_temp_int_inicio = 17000

##################################################
## Variables locales temporales flotantes       ##
##################################################
var_loc_temp_float = 21000
var_loc_temp_float_inicio = 21000

##################################################
## Variables locales temporales booleanas       ##
##################################################
var_loc_temp_bool = 25000
var_loc_temp_bool_inicio = 25000

##################################################
## Variables locales temporales char            ##
##################################################
var_loc_temp_char = 29000
var_loc_temp_char_inicio = 29000

################################
## Constantes enteras         ##
################################
cte_int = 33000
cte_int_inicio = 33000

################################
## Constantes flotantes       ##
################################
cte_float = 37000
cte_float_inicio = 37000

################################
## Constantes booleanas       ##
################################
cte_bool = 41000
cte_bool_inicio = 41000

################################
## Constantes char            ##
################################
cte_char = 45000
cte_char_inicio = 45000

################################
## Constantes notas            ##
################################
cte_nota = 49000
cte_nota_inicio = 49000

from collections import deque

#diccionario de listas, pos0 = tipo, pos1 = vars, pos2 = direccion inicio,
#                       pos3 = tam, pos4 = params,
dir_procs = {}
auxDic = {}
scope = []
pos_dics_tipo = 0
pos_dics_var = 1
pos_dics_dir_inicio = 2
pos_dics_tam = 3
pos_dics_params = 4

pos_vars_tipo = 0
pos_vars_dir_virtual = 1
pos_vars_dim = 2

pilaNumFuncs = []
pSaltos = deque([])
auxParamCount = 0
tempFunc = 0
currentFunc = 0
auxFuncDestinoDir = None
ctes = {}
pos_cuads_op = 0
pos_cuads_opdoIzq = 1
pos_cuads_opdoDer = 2
pos_cuads_res = 3
# Parsing rules

#estructura dir_proc = ["global",vars{}]

# ######################################
# ## maquina virtual                  ##
# ######################################
#
# def comienzaMaqVirtual():
#     print "comenzamos maq virtual"
#     return;



######################################
## programa                         ##
######################################

def p_programa(p):
    'programa : creadirprocglobal a neur22 c cancion'
    #dir_procs[scope[-1]][pos_dics_var] = {}

    print('done with file!\n')

    pp.pprint(dir_procs)
    pp.pprint(cuadruplos)
    print pOper
    print pilaO
    print pTipos
    print pSaltos
    pass

###########################################
## creadirprocglobal (punto neuralgico)  ##
###########################################

def p_creadirprocglobal(p):
    'creadirprocglobal : '
    dir_procs['global'] = ['global',{},None,{'vi':0,'vf':0,'vc':0,'vb':0,'ti':0,'tf':0,'tc':0,'tb':0},[]]
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

##########################
## punto neuralgico 22  ##
##########################

def p_neur22(p):
    'neur22 : '
    global contCuad
    op = GOTO
    cuadruplos[contCuad] = [op,None,None,None]
    contCuad+=1
    pSaltos.append(contCuad-1)
    pass


def p_c(p):
    '''c : empty
         | funcion d'''
    pass

def p_d(p):
    '''d : empty
         | c'''
    pass

######################################
## vars                             ##
######################################

def p_vars(p):
    'vars : VAR v ":" tipo u ";"'
    global dir_procs
    global var_glob_int
    global var_glob_float
    global var_glob_float_inicio
    global var_glob_bool
    global var_glob_bool_inicio
    global var_glob_char
    global var_glob_char_inicio

    global var_loc_int
    global var_loc_int_inicio
    global var_loc_float
    global var_loc_float_inicio
    global var_loc_bool
    global var_loc_bool_inicio
    global var_loc_char
    global var_loc_char_inicio

    global var_loc_temp_int_inicio
    auxDic = dir_procs[scope[-1]][pos_dics_var]
    if p[2] in auxDic:
        print "Variable con ese ID ya existe en ese scope"
        exit()
    else:
        if p[5] == "NA":
            dim = 1
        elif p[5] <= 0:
            print "Dimension no valida"
            exit()
        else:
            dim = p[5]
        if dim == 1:
            auxDic[p[2]] = [p[4],None,None]
        else:
            auxDic[p[2]] = [p[4],None,[dim-1,0]]
        if p[4] == INT:
            dir_procs[scope[-1]][pos_dics_tam]['vi']+=dim
            if scope[-1] == 'global':
                if var_glob_int + dim < var_glob_float_inicio:
                    auxDic[p[2]][pos_vars_dir_virtual] = var_glob_int
                    var_glob_int += dim
                else:
                    print "Overflow de variables enteras globales"
                    exit()
            else:
                if var_loc_int + dim < var_loc_float_inicio:
                    auxDic[p[2]][pos_vars_dir_virtual] = var_loc_int
                    var_loc_int += dim
                else:
                    print "Overflow de variables enteras locales"
                    exit()
        elif p[4] == FLOAT:
            dir_procs[scope[-1]][pos_dics_tam]['vf']+=dim
            if scope[-1] == 'global':
                if var_glob_float + dim < var_glob_bool_inicio:
                    auxDic[p[2]][pos_vars_dir_virtual] = var_glob_float
                    var_glob_float += dim
                else:
                    print "Overflow de variables flotantes globales"
                    exit()
            else:
                if var_loc_float + dim < var_loc_bool_inicio:
                    auxDic[p[2]][pos_vars_dir_virtual] = var_loc_float
                    var_loc_float += dim
                else:
                    print "Overflow de variables flotantes locales"
                    exit()
        elif p[4] == CHAR:
            dir_procs[scope[-1]][pos_dics_tam]['vc']+=dim
            if scope[-1] == 'global':
                if var_glob_char + dim < var_loc_int_inicio:
                    auxDic[p[2]][pos_vars_dir_virtual] = var_glob_char
                    var_glob_char += dim
                else:
                    print "Overflow de variables char globales"
                    exit()
            else:
                if var_loc_char + dim < var_loc_temp_int_inicio:
                    auxDic[p[2]][pos_vars_dir_virtual] = var_loc_char
                    var_loc_char += dim
                else:
                    print "Overflow de variables char locales"
                    exit()
        else:
            dir_procs[scope[-1]][pos_dics_tam]['vb']+=dim
            if scope[-1] == 'global':
                if var_glob_bool + dim < var_glob_char_inicio:
                    auxDic[p[2]][pos_vars_dir_virtual] = var_glob_bool
                    var_glob_bool += dim
                else:
                    print "Overflow de variables booleanas globales"
                    exit()
            else:
                if var_loc_bool + dim < var_loc_char_inicio:
                    auxDic[p[2]][pos_vars_dir_virtual] = var_loc_bool
                    var_loc_bool += dim
                else:
                    print "Overflow de variables booleanas locales"
                    exit()
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

######################################
## funcion                          ##
######################################

def p_funcion(p):
    'funcion : FUNC z ID meterfuncion "(" params ")" f neur23 bloque'
    global contCuad
    global pos_dics_tipo
    global pos_dics_var
    if p[4] != -1:
        if (not(scope[-1] in dir_procs["global"][pos_dics_var]) and (dir_procs[scope[-1]][pos_dics_tipo] != None)):
            print "Falta regresar parametro de salida en funcion"
            exit()
        #dir_procs[scope[-1]][pos_dics_var] = {}
        var_loc_int = var_loc_int_inicio
        var_loc_float = var_loc_float_inicio
        var_loc_bool = var_loc_bool_inicio
        var_loc_char = var_loc_char_inicio
        var_loc_temp_int = var_loc_temp_int_inicio
        var_loc_temp_float = var_loc_temp_float_inicio
        var_loc_temp_bool = var_loc_temp_bool_inicio
        var_loc_temp_char = var_loc_temp_char_inicio
        scope.pop()
        op = ENDPROC
        cuadruplos[contCuad]=[op,None,None,None]
        contCuad += 1
    pass

def p_z(p):
    '''z : INT
         | CHAR
         | FLOAT
         | BOOL
         | VOID'''
    if p[1]=="INT" :
        p[0] = INT
    elif p[1]=="CHAR" :
        p[0] = CHAR
    elif p[1]=="FLOAT" :
        p[0] = FLOAT
    elif p[1]=="BOOL" :
        p[0] = BOOL
    else:
        p[0] = None
    pass

######################################
## meterfuncion (punto neuralgico)  ##
######################################

def p_meterfuncion(p):
    'meterfuncion : '
    global var_loc_int
    global var_loc_float
    global var_loc_bool
    global var_loc_char
    global var_loc_temp_int
    global var_loc_temp_float
    global var_loc_temp_bool
    global var_loc_temp_char
    if p[-1] in dir_procs:
        print "Funcion con ese ID ya existe en el programa"
        p[0] = -1
        exit()
    else:
        var_loc_int = var_loc_int_inicio
        var_loc_float = var_loc_float_inicio
        var_loc_bool = var_loc_bool_inicio
        var_loc_char = var_loc_char_inicio
        var_loc_temp_int = var_loc_temp_int_inicio
        var_loc_temp_float = var_loc_temp_float_inicio
        var_loc_temp_bool = var_loc_temp_bool_inicio
        var_loc_temp_char = var_loc_temp_char_inicio
        dir_procs[p[-1]] = [p[-2],{},None,{'vi':0,'vf':0,'vc':0,'vb':0,'ti':0,'tf':0,'tc':0,'tb':0},[]]
        scope.append(p[-1])
    pass

##########################
## punto neuralgico 23  ##
##########################

def p_neur23(p):
    'neur23 : '
    global dir_procs
    global contCuad
    dir_procs[scope[-1]][pos_dics_dir_inicio] = contCuad
    pass

def p_f(p):
    '''f : empty
         | vars g'''
    pass

def p_g(p):
    '''g : empty
         | f'''
    pass

######################################
## params                           ##
######################################

def p_params(p):
    '''params : empty
              | tipo ID meterparams h'''
    pass

######################################
## meterparams  (punto neuralgico)  ##
######################################

def p_meterparams(p):
    'meterparams : '
    global dir_procs

    global var_loc_int
    global var_loc_int_inicio
    global var_loc_float
    global var_loc_float_inicio
    global var_loc_bool
    global var_loc_bool_inicio
    global var_loc_char
    global var_loc_char_inicio

    global var_loc_temp_int_inicio
    auxDic = dir_procs[scope[-1]][pos_dics_var]
    if p[-1] in auxDic:
        print "Parametro con ese ID ya existe en ese scope"
        exit()
    else:
        auxDic[p[-1]] = [p[-2],None,None]
        dir_procs[scope[-1]][pos_dics_params].append(p[-2])
        if p[-2] == INT:
            dir_procs[scope[-1]][pos_dics_tam]['vi']+=1
            if var_loc_int + 1 < var_loc_float_inicio:
                auxDic[p[-1]][pos_vars_dir_virtual] = var_loc_int
                var_loc_int += 1
            else:
                print "Overflow de variables enteras locales"
                exit()
        elif p[-2] == FLOAT:
            dir_procs[scope[-1]][pos_dics_tam]['vf']+=1
            if var_loc_float + 1 < var_loc_bool_inicio:
                auxDic[p[-1]][pos_vars_dir_virtual] = var_loc_float
                var_loc_float += 1
            else:
                print "Overflow de variables flotantes locales"
                exit()
        elif p[-2] == CHAR:
            dir_procs[scope[-1]][pos_dics_tam]['vc']+=1
            if var_loc_char + 1 < var_loc_temp_int_inicio:
                auxDic[p[-1]][pos_vars_dir_virtual] = var_loc_char
                var_loc_char += 1
            else:
                print "Overflow de variables char locales"
                exit()
        else:
            dir_procs[scope[-1]][pos_dics_tam]['vb']+=1
            if var_loc_bool + 1 < var_loc_char_inicio:
                auxDic[p[-1]][pos_vars_dir_virtual] = var_loc_bool
                var_loc_bool += 1
            else:
                print "Overflow de variables booleanas locales"
                exit()
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

######################################
## bloque                           ##
######################################

def p_bloque(p):
    'bloque : "{" i "}"'
    pass

# estructura de dir_proc = ['CANCION',vars{},tempo]

######################################
## cancion                          ##
######################################

def p_cancion(p):
    'cancion : CANCION "(" CTEE ")" metercancion f bloque'
    #dir_procs[scope[-1]][pos_dics_var] = {}
    scope.pop()
    pass

######################################
## metercancion (punto neuralgico)  ##
######################################

def p_metercancion(p):
    'metercancion : '
    global contCuad
    scope.append(p[-4])
    global var_loc_int
    global var_loc_float
    global var_loc_bool
    global var_loc_char
    global var_loc_temp_int
    global var_loc_temp_float
    global var_loc_temp_bool
    global var_loc_temp_char
    var_loc_int = var_loc_int_inicio
    var_loc_float = var_loc_float_inicio
    var_loc_bool = var_loc_bool_inicio
    var_loc_char = var_loc_char_inicio
    var_loc_temp_int = var_loc_temp_int_inicio
    var_loc_temp_float = var_loc_temp_float_inicio
    var_loc_temp_bool = var_loc_temp_bool_inicio
    var_loc_temp_char = var_loc_temp_char_inicio
    dir_procs[p[-4]] = [p[-4],{},None,{'vi':0,'vf':0,'vc':0,'vb':0,'ti':0,'tf':0,'tc':0,'tb':0},[],p[-2]] #cancion tiene tempo como parametro extra en su lista
    saltoInicial = pSaltos.pop()
    cuadruplos[saltoInicial][3] = contCuad
    pass

#############################
## estatuto                ##
#############################

def p_estatuto(p):
    '''estatuto : asignacion
                | if
                | for
                | return
                | while
                | play
                | print
                | callvoidfunc'''
    pass

#############################
## asignacion              ##
#############################

def p_asignacion(p):
    'asignacion : ID asiglista "=" neur8  expresion ";"'
    global contCuad
    global dir_procs
    global scope
    if pOper[-1] == EQ:
        op = pOper.pop()
        opdoIzq = pilaO.pop()
        tipoIzq = pTipos.pop()
        igualdad = pilaO.pop()
        tipoIgualdad = pTipos.pop()
        if tipoIzq in cubo_semantico[tipoIgualdad] and op in cubo_semantico[tipoIgualdad][tipoIzq]:
            tipoRes = cubo_semantico[tipoIgualdad][tipoIzq][op]
        else:
            tipoRes = cubo_semantico[tipoIzq][tipoIgualdad][op]
        if tipoRes != ERR :
            cuadruplos[contCuad] = [op,opdoIzq,None,igualdad]
            contCuad+=1
        else:
            print("Type mismatch")
            exit()
    else:
        print("Asignacion mal terminada")
        exit()
    pass

#############################
## punto neuralgico 8      ##
#############################

def p_neur8(p):
    'neur8 : '
    auxDic = dir_procs[scope[-1]][pos_dics_var]
    if p[-2] == -1:
        if p[-3] in auxDic:
            pilaO.append(auxDic[p[-3]][pos_vars_dir_virtual])
            pTipos.append(auxDic[p[-3]][0])
        else:
            print "No existe tal variable a asignar"
            exit()
    pOper.append(EQ)
    pass


######################################
## asiglista                        ##
######################################

def p_asiglista(p):
    '''asiglista : empty
                 | accesoVarDim'''
    if p[1] == None:
        p[0] = -1
    else:
        p[0] = 1
    pass

######################################
## if                               ##
######################################

def p_if(p):
    'if : IF "(" expresion ")" neur13 bloque l ";" neur15'
    pass

#############################
## punto neuralgico 13     ##
#############################

def p_neur13(p):
    'neur13 : '
    global contCuad
    if pTipos[-1] == BOOL:
        pTipos.pop()
        opdoIzq = pilaO.pop()
        op = GOTOF
        cuadruplos[contCuad] = [op,opdoIzq,None,None]
        contCuad+=1
        pSaltos.append(contCuad-1)
    else:
        print ("Tiene que tener un booleano como resultado de expresion")
        exit()
    pass

def p_l(p):
    '''l : empty
         | ELSE neur14 bloque'''
    pass

#############################
## punto neuralgico 14     ##
#############################

def p_neur14(p):
    'neur14 : '
    global contCuad
    op = GOTO
    falso = pSaltos.pop()
    cuadruplos[contCuad] = [op,None,None,None]
    contCuad += 1
    pSaltos.append(contCuad-1)
    cuadruplos[falso][3] = contCuad
    pass

#############################
## punto neuralgico 15     ##
#############################

def p_neur15(p):
    'neur15 : '
    global contCuad
    falso = pSaltos.pop()
    cuadruplos[falso][3] = contCuad
    pass

######################################
## for                              ##
######################################

def p_for(p):
    'for : FOR "(" asignacion neur18 expresion ";" neur19 asignacion ")" neur21 bloque ";" neur20'
    pass

######################################
## punto neuralgico 18              ##
######################################

def p_neur18(p):
    'neur18 : '
    global contCuad
    pSaltos.append(contCuad)
    pass

######################################
## punto neuralgico 19              ##
######################################

def p_neur19(p):
    'neur19 : '
    global contCuad
    if pTipos[-1] == BOOL:
        pTipos.pop()
        opdoIzq = pilaO.pop()
        op = GOTOV
        cuadruplos[contCuad] = [op,opdoIzq,None,None]
        contCuad+=1
        pSaltos.append(contCuad-1)
        op = GOTOF
        cuadruplos[contCuad] = [op,opdoIzq,None,None]
        contCuad+=1
        pSaltos.append(contCuad-1)
        pSaltos.append(contCuad)
    else:
        print ("Tiene que tener un booleano como resultado de expresion")
        exit()
    pass


######################################
## punto neuralgico 21              ##
######################################

def p_neur21(p):
    'neur21 : '
    global contCuad
    op = GOTO
    auxPila = []
    i = 0
    while i < 3:
        auxPila.append(pSaltos.pop())
        i += 1
        pass
    ciclo = pSaltos.pop()
    cuadruplos[contCuad] = [op,None,None,ciclo]
    contCuad+=1
    verdadero = auxPila.pop()
    cuadruplos[verdadero][3] = contCuad
    pSaltos.append(auxPila.pop())
    pSaltos.append(auxPila.pop())
    pass

######################################
## punto neuralgico 20              ##
######################################

def p_neur20(p):
    'neur20 : '
    global contCuad
    op = GOTO
    asigna = pSaltos.pop()
    cuadruplos[contCuad] = [op,None,None,asigna]
    contCuad+=1
    falso = pSaltos.pop()
    cuadruplos[falso][3] = contCuad
    pass


######################################
## expresion                        ##
######################################

def p_expresion(p):
    'expresion : m subexpresion'
    global contCuad

    global var_loc_temp_int
    global var_loc_temp_int_inicio
    global var_loc_temp_float
    global var_loc_temp_float_inicio
    global var_loc_temp_bool
    global var_loc_temp_bool_inicio
    global var_loc_temp_char
    global var_loc_temp_char_inicio

    global cte_int_inicio
    if pOper:
        if pOper[-1] == NOT:
            op = pOper.pop()
            opdoIzq = pilaO.pop()
            tipoIzq = pTipos.pop()
            tipoRes = cubo_semantico[tipoIzq][op]
            if tipoRes != ERR :
                if tipoRes == INT:
                    dir_procs[scope[-1]][pos_dics_tam]['ti']+=1
                    if var_loc_temp_int + 1 < var_loc_temp_float_inicio:
                        cuadruplos[contCuad] = [op,opdoIzq,None,var_loc_temp_int]
                        pilaO.append(var_loc_temp_int)
                        pTipos.append(tipoRes)
                        var_loc_temp_int += 1
                    else:
                        print "Overflow de temporales enteras"
                        exit()
                elif tipoRes == FLOAT:
                    dir_procs[scope[-1]][pos_dics_tam]['tf']+=1
                    if var_loc_temp_float + 1 < var_loc_temp_bool_inicio:
                        cuadruplos[contCuad] = [op,opdoIzq,None,var_loc_temp_float]
                        pilaO.append(var_loc_temp_float)
                        pTipos.append(tipoRes)
                        var_loc_temp_float += 1
                    else:
                        print "Overflow de temporales flotantes"
                        exit()
                elif tipoRes == CHAR:
                    dir_procs[scope[-1]][pos_dics_tam]['tc']+=1
                    if var_loc_temp_char + 1 < cte_int_inicio:
                        cuadruplos[contCuad] = [op,opdoIzq,None,var_loc_temp_char]
                        pilaO.append(var_loc_temp_char)
                        pTipos.append(tipoRes)
                        var_loc_temp_char += 1
                    else:
                        print "Overflow de temporales char"
                        exit()
                else:
                    dir_procs[scope[-1]][pos_dics_tam]['tb']+=1
                    if var_loc_temp_bool + 1 < var_loc_temp_char_inicio:
                        cuadruplos[contCuad] = [op,opdoIzq,None,var_loc_temp_bool]
                        pilaO.append(var_loc_temp_bool)
                        pTipos.append(tipoRes)
                        var_loc_temp_bool += 1
                    else:
                        print "Overflow de temporales bool"
                        exit()
                contCuad+=1
            else:
                print("Type mismatch")
                exit()
    pass

def p_m(p):
    '''m : empty
         | NOT'''
    if p[1] == "NOT":
        pOper.append(NOT)
    pass

######################################
## subexpresion                     ##
######################################

def p_subexpresion(p):
    'subexpresion : exp neur10 o'
    pass

#############################
## punto neuralgico 10     ##
#############################

def p_neur10(p):
    'neur10 : '
    global contCuad

    global var_loc_temp_int
    global var_loc_temp_int
    global var_loc_temp_float
    global var_loc_temp_float_inicio
    global var_loc_temp_bool
    global var_loc_temp_bool_inicio
    global var_loc_temp_char
    global var_loc_temp_char_inicio
    global cte_int_inicio
    if pOper:
        if pOper[-1] == AND or pOper[-1] == OR:
            op = pOper.pop()
            opdoDer = pilaO.pop()
            tipoDer = pTipos.pop()
            opdoIzq = pilaO.pop()
            tipoIzq = pTipos.pop()
            if tipoDer in cubo_semantico[tipoIzq] and op in cubo_semantico[tipoIzq][tipoDer]:
                tipoRes = cubo_semantico[tipoIzq][tipoDer][op]
            else:
                tipoRes = cubo_semantico[tipoDer][tipoIzq][op]
            if tipoRes != ERR :
                if tipoRes == INT:
                    dir_procs[scope[-1]][pos_dics_tam]['ti']+=1
                    if var_loc_temp_int + 1 < var_loc_temp_float_inicio:
                        cuadruplos[contCuad] = [op,opdoIzq,opdoDer,var_loc_temp_int]
                        pilaO.append(var_loc_temp_int)
                        pTipos.append(tipoRes)
                        var_loc_temp_int += 1
                    else:
                        print "Overflow de temporales enteras"
                        exit()
                elif tipoRes == FLOAT:
                    dir_procs[scope[-1]][pos_dics_tam]['tf']+=1
                    if var_loc_temp_float + 1 < var_loc_temp_bool_inicio:
                        cuadruplos[contCuad] = [op,opdoIzq,opdoDer,var_loc_temp_float]
                        pilaO.append(var_loc_temp_float)
                        pTipos.append(tipoRes)
                        var_loc_temp_float += 1
                    else:
                        print "Overflow de temporales flotantes"
                        exit()
                elif tipoRes == CHAR:
                    dir_procs[scope[-1]][pos_dics_tam]['tc']+=1
                    if var_loc_temp_char + 1 < cte_int_inicio:
                        cuadruplos[contCuad] = [op,opdoIzq,opdoDer,var_loc_temp_char]
                        pilaO.append(var_loc_temp_char)
                        pTipos.append(tipoRes)
                        var_loc_temp_char += 1
                    else:
                        print "Overflow de temporales char"
                        exit()
                else:
                    dir_procs[scope[-1]][pos_dics_tam]['tb']+=1
                    if var_loc_temp_bool + 1 < var_loc_temp_char_inicio:
                        cuadruplos[contCuad] = [op,opdoIzq,opdoDer,var_loc_temp_bool]
                        pilaO.append(var_loc_temp_bool)
                        pTipos.append(tipoRes)
                        var_loc_temp_bool += 1
                    else:
                        print "Overflow de temporales bool"
                        exit()
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


######################################
## exp                              ##
######################################

def p_exp(p):
    'exp : nexp p neur12'
    pass

#############################
## punto neuralgico 12     ##
#############################

def p_neur12(p):
    'neur12 : '
    global contCuad

    global var_loc_temp_int
    global var_loc_temp_int_inicio
    global var_loc_temp_float
    global var_loc_temp_float_inicio
    global var_loc_temp_bool
    global var_loc_temp_bool_inicio
    global var_loc_temp_char
    global var_loc_temp_char_inicio
    global cte_int_inicio
    if pOper:
        if pOper[-1] == EQEQ or pOper[-1] == NOTEQ or pOper[-1] == GT or pOper[-1] == LT or pOper[-1] == GTE or pOper[-1] == LTE:
            op = pOper.pop()
            opdoDer = pilaO.pop()
            tipoDer = pTipos.pop()
            opdoIzq = pilaO.pop()
            tipoIzq = pTipos.pop()
            if tipoDer in cubo_semantico[tipoIzq] and op in cubo_semantico[tipoIzq][tipoDer]:
                tipoRes = cubo_semantico[tipoIzq][tipoDer][op]
            else:
                tipoRes = cubo_semantico[tipoDer][tipoIzq][op]
            if tipoRes != ERR :
                if tipoRes == INT:
                    dir_procs[scope[-1]][pos_dics_tam]['ti']+=1
                    if var_loc_temp_int + 1 < var_loc_temp_float_inicio:
                        cuadruplos[contCuad] = [op,opdoIzq,opdoDer,var_loc_temp_int]
                        pilaO.append(var_loc_temp_int)
                        pTipos.append(tipoRes)
                        var_loc_temp_int += 1
                    else:
                        print "Overflow de temporales enteras"
                        exit()
                elif tipoRes == FLOAT:
                    dir_procs[scope[-1]][pos_dics_tam]['tf']+=1
                    if var_loc_temp_float + 1 < var_loc_temp_bool_inicio:
                        cuadruplos[contCuad] = [op,opdoIzq,opdoDer,var_loc_temp_float]
                        pilaO.append(var_loc_temp_float)
                        pTipos.append(tipoRes)
                        var_loc_temp_float += 1
                    else:
                        print "Overflow de temporales flotantes"
                        exit()
                elif tipoRes == CHAR:
                    dir_procs[scope[-1]][pos_dics_tam]['tc']+=1
                    if var_loc_temp_char + 1 < cte_int_inicio:
                        cuadruplos[contCuad] = [op,opdoIzq,opdoDer,var_loc_temp_char]
                        pilaO.append(var_loc_temp_char)
                        pTipos.append(tipoRes)
                        var_loc_temp_char += 1
                    else:
                        print "Overflow de temporales char"
                        exit()
                else:
                    dir_procs[scope[-1]][pos_dics_tam]['tb']+=1
                    if var_loc_temp_bool + 1 < var_loc_temp_char_inicio:
                        cuadruplos[contCuad] = [op,opdoIzq,opdoDer,var_loc_temp_bool]
                        pilaO.append(var_loc_temp_bool)
                        pTipos.append(tipoRes)
                        var_loc_temp_bool += 1
                    else:
                        print "Overflow de temporales bool"
                        exit()
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

######################################
## nexp                             ##
######################################

def p_nexp(p):
    'nexp : termino neur5 q'
    pass

#############################
## punto neuralgico 5      ##
#############################

def p_neur5(p):
    'neur5 : '
    global contCuad

    global var_loc_temp_int
    global var_loc_temp_int_inicio
    global var_loc_temp_float
    global var_loc_temp_float_inicio
    global var_loc_temp_bool
    global var_loc_temp_bool_inicio
    global var_loc_temp_char
    global var_loc_temp_char_inicio

    global cte_int_inicio
    if pOper:
        if pOper[-1] == PLUS or pOper[-1]== MINUS :
            op = pOper.pop()
            opdoDer = pilaO.pop()
            tipoDer = pTipos.pop()
            opdoIzq = pilaO.pop()
            tipoIzq = pTipos.pop()
            if tipoDer in cubo_semantico[tipoIzq] and op in cubo_semantico[tipoIzq][tipoDer]:
                tipoRes = cubo_semantico[tipoIzq][tipoDer][op]
            else:
                tipoRes = cubo_semantico[tipoDer][tipoIzq][op]
            if tipoRes != ERR :
                if tipoRes == INT:
                    dir_procs[scope[-1]][pos_dics_tam]['ti']+=1
                    if var_loc_temp_int + 1 < var_loc_temp_float_inicio:
                        cuadruplos[contCuad] = [op,opdoIzq,opdoDer,var_loc_temp_int]
                        pilaO.append(var_loc_temp_int)
                        pTipos.append(tipoRes)
                        var_loc_temp_int += 1
                    else:
                        print "Overflow de temporales enteras"
                        exit()
                elif tipoRes == FLOAT:
                    dir_procs[scope[-1]][pos_dics_tam]['tf']+=1
                    if var_loc_temp_float + 1 < var_loc_temp_bool_inicio:
                        cuadruplos[contCuad] = [op,opdoIzq,opdoDer,var_loc_temp_float]
                        pilaO.append(var_loc_temp_float)
                        pTipos.append(tipoRes)
                        var_loc_temp_float += 1
                    else:
                        print "Overflow de temporales flotantes"
                        exit()
                elif tipoRes == CHAR:
                    dir_procs[scope[-1]][pos_dics_tam]['tc']+=1
                    if var_loc_temp_char + 1 < cte_int_inicio:
                        cuadruplos[contCuad] = [op,opdoIzq,opdoDer,var_loc_temp_char]
                        pilaO.append(var_loc_temp_char)
                        pTipos.append(tipoRes)
                        var_loc_temp_char += 1
                    else:
                        print "Overflow de temporales char"
                        exit()
                else:
                    dir_procs[scope[-1]][pos_dics_tam]['tb']+=1
                    if var_loc_temp_bool + 1 < var_loc_char_inicio:
                        cuadruplos[contCuad] = [op,opdoIzq,opdoDer,var_loc_temp_bool]
                        pilaO.append(var_loc_temp_bool)
                        pTipos.append(tipoRes)
                        var_loc_temp_bool += 1
                    else:
                        print "Overflow de temporales bool"
                        exit()
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

######################################
## termino                          ##
######################################

def p_termino(p):
    'termino : meteneg factor neur4 n'
    pass

#############################
## punto neuralgico 4      ##
#############################

def p_neur4(p):
    'neur4 : '
    global contCuad
    global pOper

    global var_loc_temp_int
    global var_loc_temp_int_inicio
    global var_loc_temp_float
    global var_loc_temp_float_inicio
    global var_loc_temp_bool
    global var_loc_temp_bool_inicio
    global var_loc_temp_char
    global var_loc_temp_char_inicio

    global cte_int_inicio
    if pOper:
        if pOper[-1] == MULT or pOper[-1]== DIV :
            op = pOper.pop()
            opdoDer = pilaO.pop()
            tipoDer = pTipos.pop()
            opdoIzq = pilaO.pop()
            tipoIzq = pTipos.pop()
            if tipoDer in cubo_semantico[tipoIzq] and op in cubo_semantico[tipoIzq][tipoDer]:
                tipoRes = cubo_semantico[tipoIzq][tipoDer][op]
            else:
                tipoRes = cubo_semantico[tipoDer][tipoIzq][op]
            if tipoRes != ERR :
                if tipoRes == INT:
                    dir_procs[scope[-1]][pos_dics_tam]['ti']+=1
                    if var_loc_temp_int + 1 < var_loc_temp_float_inicio:
                        cuadruplos[contCuad] = [op,opdoIzq,opdoDer,var_loc_temp_int]
                        pilaO.append(var_loc_temp_int)
                        pTipos.append(tipoRes)
                        var_loc_temp_int += 1
                    else:
                        print "Overflow de temporales enteras"
                        exit()
                elif tipoRes == FLOAT:
                    dir_procs[scope[-1]][pos_dics_tam]['tf']+=1
                    if var_loc_temp_float + 1 < var_loc_temp_bool_inicio:
                        cuadruplos[contCuad] = [op,opdoIzq,opdoDer,var_loc_temp_float]
                        pilaO.append(var_loc_temp_float)
                        pTipos.append(tipoRes)
                        var_loc_temp_float += 1
                    else:
                        print "Overflow de temporales flotantes"
                        exit()
                elif tipoRes == CHAR:
                    dir_procs[scope[-1]][pos_dics_tam]['tc']+=1
                    if var_loc_temp_char + 1 < cte_int_inicio:
                        cuadruplos[contCuad] = [op,opdoIzq,opdoDer,var_loc_temp_char]
                        pilaO.append(var_loc_temp_char)
                        pTipos.append(tipoRes)
                        var_loc_temp_char += 1
                    else:
                        print "Overflow de temporales char"
                        exit()
                else:
                    dir_procs[scope[-1]][pos_dics_tam]['tb']+=1
                    if var_loc_temp_bool + 1 < var_loc_char_inicio:
                        cuadruplos[contCuad] = [op,opdoIzq,opdoDer,var_loc_temp_bool]
                        pilaO.append(var_loc_temp_bool)
                        pTipos.append(tipoRes)
                        var_loc_temp_bool += 1
                    else:
                        print "Overflow de temporales bool"
                        exit()
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

######################################
## factor                           ##
######################################

def p_factor(p):
    '''factor : "(" neur6 expresion ")" neur7
              | varcte'''
    global contCuad
    global pOper

    global var_loc_temp_int
    global var_loc_temp_int_inicio
    global var_loc_temp_float
    global var_loc_temp_float_inicio
    global var_loc_temp_bool
    global var_loc_temp_bool_inicio
    global var_loc_temp_char
    global var_loc_temp_char_inicio

    global cte_int_inicio
    if pOper:
        if pOper[-1] == NEG:
            op = pOper.pop()
            opdoIzq = pilaO.pop()
            tipoIzq = pTipos.pop()
            tipoRes = cubo_semantico[tipoIzq][op]
            if tipoRes != ERR :
                if tipoRes == INT:
                    dir_procs[scope[-1]][pos_dics_tam]['ti']+=1
                    if var_loc_temp_int + 1 < var_loc_temp_float_inicio:
                        cuadruplos[contCuad] = [op,opdoIzq,None,var_loc_temp_int]
                        pilaO.append(var_loc_temp_int)
                        pTipos.append(tipoRes)
                        var_loc_temp_int += 1
                    else:
                        print "Overflow de temporales enteras"
                        exit()
                elif tipoRes == FLOAT:
                    dir_procs[scope[-1]][pos_dics_tam]['tf']+=1
                    if var_loc_temp_float + 1 < var_loc_temp_bool_inicio:
                        cuadruplos[contCuad] = [op,opdoIzq,None,var_loc_temp_float]
                        pilaO.append(var_loc_temp_float)
                        pTipos.append(tipoRes)
                        var_loc_temp_float += 1
                    else:
                        print "Overflow de temporales flotantes"
                        exit()
                elif tipoRes == CHAR:
                    dir_procs[scope[-1]][pos_dics_tam]['tc']+=1
                    if var_loc_temp_char + 1 < cte_int_inicio:
                        cuadruplos[contCuad] = [op,opdoIzq,None,var_loc_temp_char]
                        pilaO.append(var_loc_temp_char)
                        pTipos.append(tipoRes)
                        var_loc_temp_char += 1
                    else:
                        print "Overflow de temporales char"
                        exit()
                else:
                    dir_procs[scope[-1]][pos_dics_tam]['tb']+=1
                    if var_loc_temp_bool + 1 < var_loc_char_inicio:
                        cuadruplos[contCuad] = [op,opdoIzq,None,var_loc_temp_bool]
                        pilaO.append(var_loc_temp_bool)
                        pTipos.append(tipoRes)
                        var_loc_temp_bool += 1
                    else:
                        print "Overflow de temporales bool"
                        exit()
                contCuad+=1
            else:
                print("Type mismatch")
                exit()
    pass

#############################
## meteneg                 ##
#############################

def p_meteneg(p):
    '''meteneg : empty
               | "-" '''
    if p[1] == "-":
        pOper.append(NEG)
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
        exit()
    pass

#############################
## punto neuralgico 1      ##
#############################

# def p_neur1(p):
#     'neur1 : '
#     pilaO.append(p[-1])
#     pass

######################################
## varcte                           ##
######################################

def p_varcte(p):
    '''varcte : ID r neurVar
              | CTEE neurCteE
              | CTEF neurCteF
              | CTEBOOL neurCteB
              | callreturnfunc
              | CTECHAR neurCteCh'''
    p[0] = p[1]
    pass

#############################
## punto neuralgico var    ##
#############################

def p_neurVar(p):
    'neurVar : '
    if p[-1] == -1:
        auxDic = dir_procs[scope[-1]][pos_dics_var]
        if p[-2] in auxDic:
            pTipos.append(auxDic[p[-2]][0])
            pilaO.append(auxDic[p[-2]][pos_vars_dir_virtual])
        else:
            print "No existe tal variable"
            exit()
    pass

#############################
## punto neuralgico int    ##
#############################

def p_neurCteE(p):
    'neurCteE : '
    global cte_int
    global cte_float_inicio
    global ctes
    pTipos.append(INT)
    if (not p[-1] in ctes):
        if cte_int + 1 < cte_float_inicio:
            ctes[p[-1]] = cte_int
            cte_int += 1
        else:
            print "Overflow de constantes enteras"
            exit()
    pilaO.append(ctes[p[-1]])
    pass

#############################
## punto neuralgico char   ##
#############################

def p_neurCteF(p):
    'neurCteF : '
    global cte_float
    global cte_bool_inicio
    global ctes
    pTipos.append(FLOAT)
    if (not p[-1] in ctes):
        if cte_float + 1 < cte_bool_inicio:
            ctes[p[-1]] = cte_float
            cte_float += 1
        else:
            print "Overflow de constantes flotantes"
            exit()
    pilaO.append(ctes[p[-1]])
    pass

#############################
## punto neuralgico bool   ##
#############################

def p_neurCteB(p):
    'neurCteB : '
    global cte_bool
    global cte_char_inicio
    global ctes
    pTipos.append(BOOL)

    #############################################
    # fix para que el True no lo confunda con 1 #
    #############################################
    if p[-1]:
        boolConst = 'tru'
    else:
        boolConst = 'fals'
    if (not boolConst in ctes):
        if cte_bool + 1 < cte_char_inicio:
            ctes[boolConst] = cte_bool
            cte_bool += 1
        else:
            print "Overflow de constantes booleanas"
            exit()
    pilaO.append(ctes[boolConst])
    pass

#############################
## punto neuralgico char   ##
#############################

def p_neurCteCh(p):
    'neurCteCh : '
    global cte_char
    global cte_nota_inicio
    global ctes
    pTipos.append(CHAR)
    if (not p[-1] in ctes):
        if cte_char + 1 < cte_nota_inicio:
            ctes[p[-1]] = cte_char
            cte_char += 1
        else:
            print "Overflow de constantes char"
            exit()
    pilaO.append(ctes[p[-1]])
    pass


def p_r(p):
    '''r : empty
         | oplista'''
    if p[1] == None:
        p[0] = -1
    else:
        p[0] = 1
    pass

######################################
## oplista                          ##
######################################

def p_oplista(p):
    '''oplista : accesoVarDim
               | length'''
    p[0] = p[1]
    pass

######################################
## accesoVarDim                     ##
######################################

def p_accesoVarDim(p):
    'accesoVarDim : "[" neur27 nexp "]"'
    p[0] = 1
    global contCuad
    global var_loc_temp_int
    global var_loc_temp_int
    global var_loc_temp_float
    global var_loc_temp_float_inicio
    global var_loc_temp_bool
    global var_loc_temp_bool_inicio
    global var_loc_temp_char
    global var_loc_temp_char_inicio
    global cte_int_inicio
    global cte_int
    global cte_float_inicio

    if p[-1] in dir_procs[scope[-1]][pos_dics_var]:
        if dir_procs[scope[-1]][pos_dics_var][p[-1]][pos_vars_dim] != None:
            if pTipos[-1] == INT:
                op = VERIFICA
                opdoIzq = pilaO[-1]
                opdoDer = dir_procs[scope[-1]][pos_dics_var][p[-1]][pos_vars_dim][1]
                res = dir_procs[scope[-1]][pos_dics_var][p[-1]][pos_vars_dim][0]
                cuadruplos[contCuad] = [op,opdoIzq,opdoDer,res]
                contCuad += 1
                op = PLUS
                opdoIzq = pilaO.pop()
                pTipos.pop()
                aux = dir_procs[scope[-1]][pos_dics_var][p[-1]][pos_vars_dir_virtual]
                if (not aux in ctes):
                    if cte_int + 1 < cte_float_inicio:
                        ctes[aux] = cte_int
                        cte_int += 1
                    else:
                        print "Overflow de constantes enteras"
                        exit()
                opdoDer = ctes[aux]
                dir_procs[scope[-1]][pos_dics_tam]['ti']+=1
                if var_loc_temp_int + 1 < var_loc_temp_float_inicio:
                    cuadruplos[contCuad] = [op,opdoIzq,opdoDer,var_loc_temp_int]
                    contCuad += 1
                    pilaO.append("("+str(var_loc_temp_int)+")")
                    var_loc_temp_int += 1
                else:
                    print "Overflow de temporales enteras"
                    exit()
                pTipos.append(dir_procs[scope[-1]][pos_dics_var][p[-1]][pos_vars_tipo])
                if pOper[-1] == '[':
                    pOper.pop()
            else:
                print "El indice que tratas de acccesar no es de tipo entero"
                exit()
        else:
            print "No es una variable dimensionada"
            exit()
    else:
        print "No existe tal variable"
        exit()

    pass


################################
## neur 27                    ##
################################

def p_neur27(p):
    'neur27 : '
    pOper.append('[')
    pass

######################################
## append                           ##
######################################

# def p_append(p):
#     'append : APPEND "(" expresion ")"'
#     p[0] = 2
#     pass

######################################
## length                           ##
######################################

def p_length(p):
    'length : "." LENGTH "(" ")"'
    p[0] = 3
    global pilaO
    global pTipos
    global cte_int
    global cte_float_inicio
    if p[-1] in dir_procs[scope[-1]][pos_dics_var]:
        if dir_procs[scope[-1]][pos_dics_var][p[-1]][pos_vars_dim] != None:
            pTipos.append(INT);
            dim = dir_procs[scope[-1]][pos_dics_var][p[-1]][pos_vars_dim][0]+1
            if (not dim in ctes):
                if cte_int + 1 < cte_float_inicio:
                    ctes[dim] = cte_int
                    cte_int += 1
                else:
                    print "Overflow de constantes enteras"
                    exit()
            pilaO.append(ctes[dim])
        else:
            print "No es una variable dimensionada"
            exit()
    else:
        print "No existe tal variable"
        exit()
    pass

######################################
## getlist                          ##
######################################

# def p_getlist(p):
#     'getlist : GET "(" expresion ")"'
#     p[0] = 4
#     pass

######################################
## removelist                       ##
######################################

# def p_removelist(p):
#     'removelist : REMOVE "(" expresion ")"'
#     p[0] = 5
#     pass

######################################
## while                            ##
######################################

def p_while(p):
    'while : WHILE "(" neur16 expresion ")" neur13 bloque ";" neur17'
    pass

#############################
## punto neuralgico 16     ##
#############################

def p_neur16(p):
    'neur16 : '
    global contCuad
    pSaltos.append(contCuad)
    pass

#############################
## punto neuralgico 17     ##
#############################

def p_neur17(p):
    'neur17 : '
    global contCuad
    op = GOTO
    falso = pSaltos.pop()
    ciclo = pSaltos.pop()
    cuadruplos[contCuad] = [op,None,None,ciclo]
    contCuad += 1
    cuadruplos[falso][3] = contCuad
    pass

######################################
## play                             ##
######################################

def p_play(p):
    'play : PLAY "(" NOTA "," CTEE ")" ";"'
    global contCuad
    global ctes
    global cte_nota
    global cte_int
    global cte_float_inicio
    op = PLAY
    if (not p[3] in ctes):
        ctes[p[3]] = cte_nota
        cte_nota += 1
    opdoIzq = ctes[p[3]]
    if(not p[5] in ctes):
        if cte_int + 1 < cte_float_inicio:
            ctes[p[5]] = cte_int
            cte_int +=1
        else:
            print "Overflow de constantes enteras"
            exit()
    opdoDer = ctes[p[5]]
    cuadruplos[contCuad] = [op,opdoIzq,opdoDer,None]
    contCuad+=1
    pass

######################################
## print                            ##
######################################

def p_print(p):
    'print : PRINT expresion ";"'
    global contCuad
    op = PRINT
    opdoIzq = pilaO.pop()
    pTipos.pop()
    cuadruplos[contCuad] = [op,opdoIzq,None,None]
    contCuad+=1
    pass

######################################
## callreturnfunc                   ##
######################################

def p_callreturnfunc(p):
    'callreturnfunc : CALL ID neur24 "(" s ")" neur26 ";"'
    global pos_dics_tipo
    global var_loc_temp_int
    global var_loc_temp_int_inicio
    global var_loc_temp_float
    global var_loc_temp_float_inicio
    global var_loc_temp_bool
    global var_loc_temp_bool_inicio
    global var_loc_temp_char
    global var_loc_temp_char_inicio
    global contCuad

    global cte_int_inicio
    dir_virtual = dir_procs['global'][pos_dics_var][p[2]][pos_vars_dir_virtual]
    tipo = dir_procs['global'][pos_dics_var][p[2]][pos_vars_tipo]
    op = EQ
    opdoIzq = dir_virtual
    if tipo == INT:
        dir_procs[scope[-1]][pos_dics_tam]['ti']+=1
        if var_loc_temp_int + 1 < var_loc_temp_float_inicio:
            cuadruplos[contCuad] = [op,opdoIzq,None,var_loc_temp_int]
            pilaO.append(var_loc_temp_int)
            pTipos.append(tipo)
            var_loc_temp_int += 1
        else:
            print "Overflow de temporales enteras"
            exit()
    elif tipo == FLOAT:
        dir_procs[scope[-1]][pos_dics_tam]['tf']+=1
        if var_loc_temp_float + 1 < var_loc_temp_bool_inicio:
            cuadruplos[contCuad] = [op,opdoIzq,None,var_loc_temp_float]
            pilaO.append(var_loc_temp_float)
            pTipos.append(tipo)
            var_loc_temp_float += 1
        else:
            print "Overflow de temporales flotantes"
            exit()
    elif tipo == CHAR:
        dir_procs[scope[-1]][pos_dics_tam]['tc']+=1
        if var_loc_temp_char + 1 < cte_int_inicio:
            cuadruplos[contCuad] = [op,opdoIzq,None,var_loc_temp_char]
            pilaO.append(var_loc_temp_char)
            pTipos.append(tipo)
            var_loc_temp_char += 1
        else:
            print "Overflow de temporales char"
            exit()
    else:
        dir_procs[scope[-1]][pos_dics_tam]['tb']+=1
        if var_loc_temp_bool + 1 < var_loc_temp_char_inicio:
            cuadruplos[contCuad] = [op,opdoIzq,None,var_loc_temp_bool]
            pilaO.append(var_loc_temp_bool)
            pTipos.append(tipo)
            var_loc_temp_bool += 1
        else:
            print "Overflow de temporales bool"
            exit()
    contCuad+=1
    pass

def p_s(p):
    '''s : empty
         | expresion neur25 t'''
    pass

#############################
## punto neuralgico 25     ##
#############################

def p_neur25(p):
    'neur25 : '
    global dir_procs
    global contCuad
    global auxParamCount
    global auxFuncDestinoDir
    global currentFunc
    print pilaNumFuncs
    if pOper != [] and currentFunc == pilaNumFuncs[-1]:
        print pOper
        if len(pilaO)>0 and pOper[-1] == PARAMETRO:
            argumento = pilaO.pop()
            tipoarg = pTipos.pop()
            print "parametros: "+repr(auxParamCount)
            print "funcion destino: "+repr(auxFuncDestinoDir)
            if tipoarg == dir_procs[auxFuncDestinoDir][pos_dics_params][auxParamCount] or (tipoarg == INT and dir_procs[auxFuncDestinoDir][pos_dics_params][auxParamCount]==FLOAT):
                op = PARAMETRO
                if tipoarg == INT:
                    cuadruplos[contCuad] = [op,argumento,None,var_loc_int_inicio + auxParamCount]
                elif tipoarg == FLOAT:
                    cuadruplos[contCuad] = [op,argumento,None,var_loc_float_inicio + auxParamCount]
                elif tipoRes == CHAR:
                    cuadruplos[contCuad] = [op,argumento,None,var_loc_char_inicio + auxParamCount]
                else:
                    cuadruplos[contCuad] = [op,argumento,None,var_loc_bool_inicio + auxParamCount]
                auxParamCount += 1
                contCuad+=1
            else:
                print "Error en declaracion de parametros"
                exit()
        else:
            argumento = None
            tipoarg = None
    else:
        argumento = None
        tipoarg = None
    # try:
    #     i = dir_procs[auxFuncDestinoDir][pos_dics_params][auxParamCount][auxParamCount]
    # except IndexError:
    #     print ""

    pass

def p_t(p):
    '''t : empty
         | "," s'''
    pass

#############################
## callvoidfunc            ##
#############################

def p_callvoidfunc(p):
    'callvoidfunc : CALL ID neur24 "(" s ")" neur26 ";"'
    pass

#############################
## punto neuralgico 24     ##
#############################

def p_neur24(p):
    'neur24 : '
    global contCuad
    global auxParamCount
    global auxFuncDestinoDir
    global tempFunc
    global currentFunc
    global pOper
    if p[-1] in dir_procs:

        auxFuncDestinoDir = p[-1]
        auxParamCount = 0
        op = ERA
        cuadruplos[contCuad] = [op,p[-1],None,None]
        contCuad += 1
        pOper.append(PARAMETRO)
        currentFunc = tempFunc
        pilaNumFuncs.append(tempFunc)
        tempFunc += 1
        print "entro funcion"+ repr(p[-1]) + " " + repr(auxParamCount)
        print pOper
    else:
        print "Funcion con ese id no existe"
        exit()
    pass

#############################
## punto neuralgico 26     ##
#############################

def p_neur26(p):
    'neur26 : '
    global auxParamCount
    global auxFuncDestinoDir
    global contCuad
    if auxParamCount != len(dir_procs[auxFuncDestinoDir][pos_dics_params]):
        print "Error en cantidad de parametros"
        exit()
    else:
        op = GOSUB
        if(pOper[-1] == PARAMETRO):
            pOper.pop()
            pilaNumFuncs.pop()
        else:
            print "Llamada a funcion con operaciones pendientes"
            exit()
        cuadruplos[contCuad] = [GOSUB,auxFuncDestinoDir,None,None]
        contCuad += 1

    pass

######################################
## return                           ##
######################################

def p_return(p):
    'return : RETURN "(" expresion ")" ";"'
    global pos_dics_tipo
    global pos_dics_var
    global contCuad
    global var_glob_int
    global var_glob_float
    global var_glob_float_inicio
    global var_glob_bool
    global var_glob_bool_inicio
    global var_glob_char
    global var_glob_char_inicio

    global var_loc_int_inicio
    retorno = pilaO.pop()
    tipoRetorno = pTipos.pop()
    op = EQ
    if tipoRetorno == dir_procs[scope[-1]][pos_dics_tipo] or (tipoRetorno == INT and dir_procs[scope[-1]][pos_dics_tipo] == FLOAT):
        if scope[-1] in dir_procs["global"][pos_dics_var]:
            var_aux = dir_procs["global"][pos_dics_var][scope[-1]][pos_vars_dir_virtual]
            cuadruplos[contCuad] = [op,retorno,None,var_aux]
        else:
            if dir_procs[scope[-1]][pos_dics_tipo] == INT:
                dir_procs["global"][pos_dics_tam]['vi']+=1
                if var_glob_int + 1 < var_glob_float_inicio:
                    dir_procs["global"][pos_dics_var][scope[-1]] = [dir_procs[scope[-1]][pos_dics_tipo],var_glob_int,None]
                    cuadruplos[contCuad] = [op,retorno,None,var_glob_int]
                    var_glob_int += 1
                else:
                    print "Overflow de variables enteras globales"
                    exit()
            elif dir_procs[scope[-1]][pos_dics_tipo] == FLOAT:
                dir_procs["global"][pos_dics_tam]['vf']+=1
                if var_glob_float + 1 < var_glob_bool_inicio:
                    dir_procs["global"][pos_dics_var][scope[-1]] = [dir_procs[scope[-1]][pos_dics_tipo],var_glob_float,None]
                    cuadruplos[contCuad] = [op,retorno,None,var_glob_float]
                    var_glob_float += 1
                else:
                    print "Overflow de variables enteras globales"
                    exit()
            elif dir_procs[scope[-1]][pos_dics_tipo] == CHAR:
                dir_procs["global"][pos_dics_tam]['vc']+=1
                if var_glob_char + 1 < var_loc_int_inicio:
                    dir_procs["global"][pos_dics_var][scope[-1]] = [dir_procs[scope[-1]][pos_dics_tipo],var_glob_char,None]
                    cuadruplos[contCuad] = [op,retorno,None,var_glob_char]
                    var_glob_char += 1
                else:
                    print "Overflow de variables enteras globales"
                    exit()
            else:
                dir_procs["global"][pos_dics_tam]['vb']+=1
                if var_glob_bool + 1 < var_glob_char_inicio:
                    dir_procs["global"][pos_dics_var][scope[-1]] = [dir_procs[scope[-1]][pos_dics_tipo],var_glob_bool,None]
                    cuadruplos[contCuad] = [op,retorno,None,var_glob_bool]
                    var_glob_bool += 1
                else:
                    print "Overflow de variables enteras globales"
                    exit()
        contCuad += 1
    else:
        print "Error en el tipo de retorno dado"
        exit()

    op = ENDPROC
    cuadruplos[contCuad]=[op,None,None,None]
    contCuad += 1
    pass

######################################
## tipo                             ##
######################################

def p_tipo(p):
    'tipo : y'
    p[0] = p[1]
    pass

def p_u(p):
    '''u : empty
         | LIST "(" CTEE ")"'''
    global cte_int
    global ctes
    if p[1] == None:
        p[0] = "NA"
    else:
        # if(not p[3] in ctes):
        #     if cte_int + 1 < cte_float_inicio:
        #         ctes[p[3]] = cte_int
        #         cte_int +=1
        #     else:
        #         print "Overflow de constantes enteras"
        #         exit()
        p[0] = p[3]
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
        exit()
    else:
        print("Syntax error at EOF")

import ply.yacc as yacc
yacc.yacc()

f = open(str(sys.argv[1]), 'r')
s = f.read()
f.close()
yacc.parse(s)

import memoria
###########################
## funcion search        ##
###########################
def search(values, searchFor):
    for k in values:
        if searchFor == values[k]:
            return k
    return None


################################################
## funcion de operaciones maq virtual         ##
################################################
def func_maq_virtual():
    global current_cuad
    global memoriaGlobal
    global memoriaActiva
    global memoriaDormida
    op = cuadruplos[current_cuad][0]
    # print cuadruplos[current_cuad]
    opdoIzq = cuadruplos[current_cuad][1]
    if isinstance(opdoIzq,basestring) and opdoIzq[0] == '(' and opdoIzq[-1]==')':
        opdoIzq = int(opdoIzq[1:-1])
        if opdoIzq >= var_glob_int_inicio and opdoIzq < var_glob_float_inicio:
            opdoIzq = memoriaGlobal.ints[opdoIzq]
        elif opdoIzq >= var_glob_float_inicio and opdoIzq < var_glob_bool_inicio:
            opdoIzq = memoriaGlobal.floats[opdoIzq]
        elif opdoIzq >= var_glob_bool_inicio and opdoIzq < var_glob_char_inicio:
            opdoIzq = memoriaGlobal.bools[opdoIzq]
        elif opdoIzq >= var_glob_char_inicio and opdoIzq < var_loc_int_inicio:
            opdoIzq = memoriaGlobal.chars[opdoIzq]
        elif (opdoIzq >= var_loc_int_inicio and opdoIzq < var_loc_float_inicio) or (opdoIzq >= var_loc_temp_int_inicio and opdoIzq < var_loc_temp_float_inicio):
            opdoIzq = memoriaActiva.ints[opdoIzq]
        elif (opdoIzq >= var_loc_float_inicio and opdoIzq < var_loc_bool_inicio) or (opdoIzq >= var_loc_temp_float_inicio and opdoIzq < var_loc_temp_bool_inicio):
            opdoIzq = memoriaActiva.floats[opdoIzq]
        elif (opdoIzq >= var_loc_bool_inicio and opdoIzq < var_loc_char_inicio) or (opdoIzq >= var_loc_temp_bool_inicio and opdoIzq < var_loc_temp_char_inicio):
            opdoIzq = memoriaActiva.bools[opdoIzq]
        elif (opdoIzq >= var_loc_char_inicio and opdoIzq < var_loc_temp_int_inicio) or (opdoIzq >= var_loc_temp_char_inicio and opdoIzq < cte_int_inicio):
            opdoIzq = memoriaActiva.chars[opdoIzq]
        elif opdoIzq >= cte_int_inicio and opdoIzq < cte_float_inicio:
            opdoIzq = int(search(ctes,opdoIzq))
        elif opdoIzq >= cte_float_inicio and opdoIzq < cte_bool_inicio:
            opdoIzq = float(search(ctes,opdoIzq))
        elif opdoIzq >= cte_bool_inicio and opdoIzq < cte_char_inicio:
            if search(ctes,opdoIzq) == 'tru':
                opdoIzq = True
            else:
                opdoIzq = False
        elif opdoIzq >= cte_char_inicio:
            opdoIzq = search(ctes,opdoIzq)
    opdoDer = cuadruplos[current_cuad][2]
    if isinstance(opdoDer,basestring) and opdoDer[0] == '(' and opdoDer[-1]==')':
        opdoDer = int(opdoDer[1:-1])
        if opdoDer >= var_glob_int_inicio and opdoDer < var_glob_float_inicio:
            opdoDer = memoriaGlobal.ints[opdoDer]
        elif opdoDer >= var_glob_float_inicio and opdoDer < var_glob_bool_inicio:
            opdoDer = memoriaGlobal.floats[opdoDer]
        elif opdoDer >= var_glob_bool_inicio and opdoDer < var_glob_char_inicio:
            opdoDer = memoriaGlobal.bools[opdoDer]
        elif opdoDer >= var_glob_char_inicio and opdoDer < var_loc_int_inicio:
            opdoDer = memoriaGlobal.chars[opdoDer]
        elif (opdoDer >= var_loc_int_inicio and opdoDer < var_loc_float_inicio) or (opdoDer >= var_loc_temp_int_inicio and opdoDer < var_loc_temp_float_inicio):
            opdoDer = memoriaActiva.ints[opdoDer]
        elif (opdoDer >= var_loc_float_inicio and opdoDer < var_loc_bool_inicio) or (opdoDer >= var_loc_temp_float_inicio and opdoDer < var_loc_temp_bool_inicio):
            opdoDer = memoriaActiva.floats[opdoDer]
        elif (opdoDer >= var_loc_bool_inicio and opdoDer < var_loc_char_inicio) or (opdoDer >= var_loc_temp_bool_inicio and opdoDer < var_loc_temp_char_inicio):
            opdoDer = memoriaActiva.bools[opdoDer]
        elif (opdoDer >= var_loc_char_inicio and opdoDer < var_loc_temp_int_inicio) or (opdoDer >= var_loc_temp_char_inicio and opdoDer < cte_int_inicio):
            opdoDer = memoriaActiva.chars[opdoDer]
        elif opdoDer >= cte_int_inicio and opdoDer < cte_float_inicio:
            opdoDer = int(search(ctes,opdoDer))
        elif opdoDer >= cte_float_inicio and opdoDer < cte_bool_inicio:
            opdoDer = float(search(ctes,opdoDer))
        elif opdoDer >= cte_bool_inicio and opdoDer < cte_char_inicio:
            if search(ctes,opdoDer) == 'tru':
                opdoDer = True
            else:
                opdoDer = False
        elif opdoDer >= cte_char_inicio:
            opdoDer = search(ctes,opdoDer)
    resultado = cuadruplos[current_cuad][3]
    if isinstance(resultado,basestring) and resultado[0] == '(' and resultado[-1]==')':
        resultado = int(resultado[1:-1])
        if resultado >= var_glob_int_inicio and resultado < var_glob_float_inicio:
            resultado = memoriaGlobal.ints[resultado]
        elif resultado >= var_glob_float_inicio and resultado < var_glob_bool_inicio:
            resultado = memoriaGlobal.floats[resultado]
        elif resultado >= var_glob_bool_inicio and resultado < var_glob_char_inicio:
            resultado = memoriaGlobal.bools[resultado]
        elif resultado >= var_glob_char_inicio and resultado < var_loc_int_inicio:
            resultado = memoriaGlobal.chars[resultado]
        elif (resultado >= var_loc_int_inicio and resultado < var_loc_float_inicio) or (resultado >= var_loc_temp_int_inicio and resultado < var_loc_temp_float_inicio):
            resultado = memoriaActiva.ints[resultado]
        elif (resultado >= var_loc_float_inicio and resultado < var_loc_bool_inicio) or (resultado >= var_loc_temp_float_inicio and resultado < var_loc_temp_bool_inicio):
            resultado = memoriaActiva.floats[resultado]
        elif (resultado >= var_loc_bool_inicio and resultado < var_loc_char_inicio) or (resultado >= var_loc_temp_bool_inicio and resultado < var_loc_temp_char_inicio):
            resultado = memoriaActiva.bools[resultado]
        elif (resultado >= var_loc_char_inicio and resultado < var_loc_temp_int_inicio) or (resultado >= var_loc_temp_char_inicio and resultado < cte_int_inicio):
            resultado = memoriaActiva.chars[resultado]
        elif resultado >= cte_int_inicio and resultado < cte_float_inicio:
            resultado = int(search(ctes,resultado))
        elif resultado >= cte_float_inicio and resultado < cte_bool_inicio:
            resultado = float(search(ctes,resultado))
        elif resultado >= cte_bool_inicio and resultado < cte_char_inicio:
            if search(ctes,resultado) == 'tru':
                resultado = True
            else:
                resultado = False
        elif resultado >= cte_char_inicio:
            resultado = search(ctes,resultado)
    dato1 = None
    dato2 = None
    if op == MULT:

        if opdoIzq >= var_glob_int_inicio and opdoIzq < var_glob_float_inicio:
            dato1 = memoriaGlobal.ints[opdoIzq]
        elif opdoIzq >= var_glob_float_inicio and opdoIzq < var_glob_bool_inicio:
            dato1 = memoriaGlobal.floats[opdoIzq]
        elif (opdoIzq >= var_loc_int_inicio and opdoIzq < var_loc_float_inicio) or (opdoIzq >= var_loc_temp_int_inicio and opdoIzq < var_loc_temp_float_inicio):
            dato1 = memoriaActiva.ints[opdoIzq]
        elif (opdoIzq >= var_loc_float_inicio and opdoIzq < var_loc_bool_inicio) or (opdoIzq >= var_loc_temp_float_inicio and opdoIzq < var_loc_temp_bool_inicio):
            dato1 = memoriaActiva.floats[opdoIzq]
        elif opdoIzq >= cte_int_inicio and opdoIzq < cte_float_inicio:
            dato1 = int(search(ctes,opdoIzq))
        elif opdoIzq >= cte_float_inicio and opdoIzq < cte_bool_inicio:
            dato1 = float(search(ctes,opdoIzq))

        if opdoDer >= var_glob_int_inicio and opdoDer < var_glob_float_inicio:
            dato2 = memoriaGlobal.ints[opdoDer]
        elif opdoDer >= var_glob_float_inicio and opdoDer < var_glob_bool_inicio:
            dato2 = memoriaGlobal.floats[opdoDer]
        elif (opdoDer >= var_loc_int_inicio and opdoDer < var_loc_float_inicio) or (opdoDer >= var_loc_temp_int_inicio and opdoDer < var_loc_temp_float_inicio):
            dato2 = memoriaActiva.ints[opdoDer]
        elif (opdoDer >= var_loc_float_inicio and opdoDer < var_loc_bool_inicio) or (opdoDer >= var_loc_temp_float_inicio and opdoDer < var_loc_temp_bool_inicio):
            dato2 = memoriaActiva.floats[opdoDer]
        elif opdoDer >= cte_int_inicio and opdoDer < cte_float_inicio:
            dato2 = int(search(ctes,opdoDer))
        elif opdoDer >= cte_float_inicio and opdoDer < cte_bool_inicio:
            dato2 = float(search(ctes,opdoDer))


        res = dato1 * dato2

        if resultado >= var_glob_int_inicio and resultado < var_glob_float_inicio:
            memoriaGlobal.ints[resultado] = res
        elif resultado >= var_glob_float_inicio and resultado < var_glob_bool_inicio:
            memoriaGlobal.floats[resultado] = res
        elif (resultado >= var_loc_int_inicio and resultado < var_loc_float_inicio) or (resultado >= var_loc_temp_int_inicio and resultado < var_loc_temp_float_inicio):
            memoriaActiva.ints[resultado] = res
        elif (resultado >= var_loc_float_inicio and resultado < var_loc_bool_inicio) or (resultado >= var_loc_temp_float_inicio and resultado < var_loc_temp_bool_inicio):
            memoriaActiva.floats[resultado] = res

        current_cuad +=1

    elif op == DIV:
        if opdoIzq >= var_glob_int_inicio and opdoIzq < var_glob_float_inicio:
            dato1 = memoriaGlobal.ints[opdoIzq]
        elif opdoIzq >= var_glob_float_inicio and opdoIzq < var_glob_bool_inicio:
            dato1 = memoriaGlobal.floats[opdoIzq]
        elif (opdoIzq >= var_loc_int_inicio and opdoIzq < var_loc_float_inicio) or (opdoIzq >= var_loc_temp_int_inicio and opdoIzq < var_loc_temp_float_inicio):
            dato1 = memoriaActiva.ints[opdoIzq]
        elif (opdoIzq >= var_loc_float_inicio and opdoIzq < var_loc_bool_inicio) or (opdoIzq >= var_loc_temp_float_inicio and opdoIzq < var_loc_temp_bool_inicio):
            dato1 = memoriaActiva.floats[opdoIzq]
        elif opdoIzq >= cte_int_inicio and opdoIzq < cte_float_inicio:
            dato1 = int(search(ctes,opdoIzq))
        elif opdoIzq >= cte_float_inicio and opdoIzq < cte_bool_inicio:
            dato1 = float(search(ctes,opdoIzq))

        if opdoDer >= var_glob_int_inicio and opdoDer < var_glob_float_inicio:
            dato2 = memoriaGlobal.ints[opdoDer]
        elif opdoDer >= var_glob_float_inicio and opdoDer < var_glob_bool_inicio:
            dato2 = memoriaGlobal.floats[opdoDer]
        elif (opdoDer >= var_loc_int_inicio and opdoDer < var_loc_float_inicio) or (opdoDer >= var_loc_temp_int_inicio and opdoDer < var_loc_temp_float_inicio):
            dato2 = memoriaActiva.ints[opdoDer]
        elif (opdoDer >= var_loc_float_inicio and opdoDer < var_loc_bool_inicio) or (opdoDer >= var_loc_temp_float_inicio and opdoDer < var_loc_temp_bool_inicio):
            dato2 = memoriaActiva.floats[opdoDer]
        elif opdoDer >= cte_int_inicio and opdoDer < cte_float_inicio:
            dato2 = int(search(ctes,opdoDer))
        elif opdoDer >= cte_float_inicio and opdoDer < cte_bool_inicio:
            dato2 = float(search(ctes,opdoDer))

        res = dato1 / dato2

        if resultado >= var_glob_int_inicio and resultado < var_glob_float_inicio:
            memoriaGlobal.ints[resultado] = res
        elif resultado >= var_glob_float_inicio and resultado < var_glob_bool_inicio:
            memoriaGlobal.floats[resultado] = res
        elif (resultado >= var_loc_int_inicio and resultado < var_loc_float_inicio) or (resultado >= var_loc_temp_int_inicio and resultado < var_loc_temp_float_inicio):
            memoriaActiva.ints[resultado] = res
        elif (resultado >= var_loc_float_inicio and resultado < var_loc_bool_inicio) or (resultado >= var_loc_temp_float_inicio and resultado < var_loc_temp_bool_inicio):
            memoriaActiva.floats[resultado] = res

        current_cuad +=1

    elif op == AND:

        if opdoIzq >= var_glob_bool_inicio and opdoIzq < var_glob_char_inicio:
            dato1 = memoriaGlobal.bools[opdoIzq]
        elif (opdoIzq >= var_loc_bool_inicio and opdoIzq < var_loc_char_inicio) or (opdoIzq >= var_loc_temp_bool_inicio and opdoIzq < var_loc_temp_char_inicio):
            dato1 = memoriaActiva.bools[opdoIzq]
        elif opdoIzq >= cte_bool_inicio and opdoIzq < cte_char_inicio:
            if search(ctes,opdoIzq) == 'tru':
                dato1 = True
            else:
                dato1 = False

        if opdoDer >= var_glob_bool_inicio and opdoDer < var_glob_char_inicio:
            dato2 = memoriaGlobal.bools[opdoDer]
        elif (opdoDer >= var_loc_bool_inicio and opdoDer < var_loc_char_inicio) or (opdoDer >= var_loc_temp_bool_inicio and opdoDer < var_loc_temp_char_inicio):
            dato2 = memoriaActiva.bools[opdoDer]
        elif opdoDer >= cte_bool_inicio and opdoDer < cte_char_inicio:
            if search(ctes,opdoDer) == 'tru':
                dato2 = True
            else:
                dato2 = False


        res = dato1 and dato2

        if resultado >= var_glob_bool_inicio and resultado < var_glob_char_inicio:
            memoriaGlobal.bools[resultado] = res
        elif (resultado >= var_loc_bool_inicio and resultado < var_loc_char_inicio) or (resultado >= var_loc_temp_bool_inicio and resultado < var_loc_temp_char_inicio):
            memoriaActiva.bools[resultado] = res

        current_cuad +=1

    elif op == OR:

        if opdoIzq >= var_glob_bool_inicio and opdoIzq < var_glob_char_inicio:
            dato1 = memoriaGlobal.bools[opdoIzq]
        elif (opdoIzq >= var_loc_bool_inicio and opdoIzq < var_loc_char_inicio) or (opdoIzq >= var_loc_temp_bool_inicio and opdoIzq < var_loc_temp_char_inicio):
            dato1 = memoriaActiva.bools[opdoIzq]
        elif opdoIzq >= cte_bool_inicio and opdoIzq < cte_char_inicio:
            if search(ctes,opdoIzq) == 'tru':
                dato1 = True
            else:
                dato1 = False

        if opdoDer >= var_glob_bool_inicio and opdoDer < var_glob_char_inicio:
            dato2 = memoriaGlobal.bools[opdoDer]
        elif (opdoDer >= var_loc_bool_inicio and opdoDer < var_loc_char_inicio) or (opdoDer >= var_loc_temp_bool_inicio and opdoDer < var_loc_temp_char_inicio):
            dato2 = memoriaActiva.bools[opdoDer]
        elif opdoDer >= cte_bool_inicio and opdoDer < cte_char_inicio:
            if search(ctes,opdoDer) == 'tru':
                dato2 = True
            else:
                dato2 = False

        res = dato1 or dato2

        if resultado >= var_glob_bool_inicio and resultado < var_glob_char_inicio:
            memoriaGlobal.bools[resultado] = res
        elif (resultado >= var_loc_bool_inicio and resultado < var_loc_char_inicio) or (resultado >= var_loc_temp_bool_inicio and resultado < var_loc_temp_char_inicio):
            memoriaActiva.bools[resultado] = res

        current_cuad +=1

    elif op == EQEQ:

        if opdoIzq >= var_glob_int_inicio and opdoIzq < var_glob_float_inicio:
            dato1 = memoriaGlobal.ints[opdoIzq]
        elif opdoIzq >= var_glob_float_inicio and opdoIzq < var_glob_bool_inicio:
            dato1 = memoriaGlobal.floats[opdoIzq]
        elif opdoIzq >= var_glob_bool_inicio and opdoIzq < var_glob_char_inicio:
            dato1 = memoriaGlobal.bools[opdoIzq]
        elif opdoIzq >= var_glob_char_inicio and opdoIzq < var_loc_int_inicio:
            dato1 = memoriaGlobal.chars[opdoIzq]
        elif (opdoIzq >= var_loc_int_inicio and opdoIzq < var_loc_float_inicio) or (opdoIzq >= var_loc_temp_int_inicio and opdoIzq < var_loc_temp_float_inicio):
            dato1 = memoriaActiva.ints[opdoIzq]
        elif (opdoIzq >= var_loc_float_inicio and opdoIzq < var_loc_bool_inicio) or (opdoIzq >= var_loc_temp_float_inicio and opdoIzq < var_loc_temp_bool_inicio):
            dato1 = memoriaActiva.floats[opdoIzq]
        elif (opdoIzq >= var_loc_bool_inicio and opdoIzq < var_loc_char_inicio) or (opdoIzq >= var_loc_temp_bool_inicio and opdoIzq < var_loc_temp_char_inicio):
            dato1 = memoriaActiva.bools[opdoIzq]
        elif (opdoIzq >= var_loc_char_inicio and opdoIzq < var_loc_temp_int_inicio) or (opdoIzq >= var_loc_temp_char_inicio and opdoIzq < cte_int_inicio):
            dato1 = memoriaActiva.chars[opdoIzq]
        elif opdoIzq >= cte_int_inicio and opdoIzq < cte_float_inicio:
            dato1 = int(search(ctes,opdoIzq))
        elif opdoIzq >= cte_float_inicio and opdoIzq < cte_bool_inicio:
            dato1 = float(search(ctes,opdoIzq))
        elif opdoIzq >= cte_bool_inicio and opdoIzq < cte_char_inicio:
            if search(ctes,opdoIzq) == 'tru':
                dato1 = True
            else:
                dato1 = False
        elif opdoIzq >= cte_char_inicio:
            dato1 = search(ctes,opdoIzq)

        if opdoDer >= var_glob_int_inicio and opdoDer < var_glob_float_inicio:
            dato2 = memoriaGlobal.ints[opdoDer]
        elif opdoDer >= var_glob_float_inicio and opdoDer < var_glob_bool_inicio:
            dato2 = memoriaGlobal.floats[opdoDer]
        elif opdoDer >= var_glob_bool_inicio and opdoDer < var_glob_char_inicio:
            dato2 = memoriaGlobal.bools[opdoDer]
        elif opdoDer >= var_glob_char_inicio and opdoDer < var_loc_int_inicio:
            dato2 = memoriaGlobal.chars[opdoDer]
        elif (opdoDer >= var_loc_int_inicio and opdoDer < var_loc_float_inicio) or (opdoDer >= var_loc_temp_int_inicio and opdoDer < var_loc_temp_float_inicio):
            dato2 = memoriaActiva.ints[opdoDer]
        elif (opdoDer >= var_loc_float_inicio and opdoDer < var_loc_bool_inicio) or (opdoDer >= var_loc_temp_float_inicio and opdoDer < var_loc_temp_bool_inicio):
            dato2 = memoriaActiva.floats[opdoDer]
        elif (opdoDer >= var_loc_bool_inicio and opdoDer < var_loc_char_inicio) or (opdoDer >= var_loc_temp_bool_inicio and opdoDer < var_loc_temp_char_inicio):
            dato2 = memoriaActiva.bools[opdoDer]
        elif (opdoDer >= var_loc_char_inicio and opdoDer < var_loc_temp_int_inicio) or (opdoDer >= var_loc_temp_char_inicio and opdoDer < cte_int_inicio):
            dato2 = memoriaActiva.chars[opdoDer]
        elif opdoDer >= cte_int_inicio and opdoDer < cte_float_inicio:
            dato2 = int(search(ctes,opdoDer))
        elif opdoDer >= cte_float_inicio and opdoDer < cte_bool_inicio:
            dato2 = float(search(ctes,opdoDer))
        elif opdoDer >= cte_bool_inicio and opdoDer < cte_char_inicio:
            if search(ctes,opdoDer) == 'tru':
                dato2 = True
            else:
                dato2 = False
        elif opdoDer >= cte_char_inicio:
            dato2 = search(ctes,opdoDer)

        res = dato1 == dato2

        if resultado >= var_glob_bool_inicio and resultado < var_glob_char_inicio:
            memoriaGlobal.bools[resultado] = res
        elif (resultado >= var_loc_bool_inicio and resultado < var_loc_char_inicio) or (resultado >= var_loc_temp_bool_inicio and resultado < var_loc_temp_char_inicio):
            memoriaActiva.bools[resultado] = res

        current_cuad +=1

    elif op == NOTEQ:

        if opdoIzq >= var_glob_int_inicio and opdoIzq < var_glob_float_inicio:
            dato1 = memoriaGlobal.ints[opdoIzq]
        elif opdoIzq >= var_glob_float_inicio and opdoIzq < var_glob_bool_inicio:
            dato1 = memoriaGlobal.floats[opdoIzq]
        elif opdoIzq >= var_glob_bool_inicio and opdoIzq < var_glob_char_inicio:
            dato1 = memoriaGlobal.bools[opdoIzq]
        elif opdoIzq >= var_glob_char_inicio and opdoIzq < var_loc_int_inicio:
            dato1 = memoriaGlobal.chars[opdoIzq]
        elif (opdoIzq >= var_loc_int_inicio and opdoIzq < var_loc_float_inicio) or (opdoIzq >= var_loc_temp_int_inicio and opdoIzq < var_loc_temp_float_inicio):
            dato1 = memoriaActiva.ints[opdoIzq]
        elif (opdoIzq >= var_loc_float_inicio and opdoIzq < var_loc_bool_inicio) or (opdoIzq >= var_loc_temp_float_inicio and opdoIzq < var_loc_temp_bool_inicio):
            dato1 = memoriaActiva.floats[opdoIzq]
        elif (opdoIzq >= var_loc_bool_inicio and opdoIzq < var_loc_char_inicio) or (opdoIzq >= var_loc_temp_bool_inicio and opdoIzq < var_loc_temp_char_inicio):
            dato1 = memoriaActiva.bools[opdoIzq]
        elif (opdoIzq >= var_loc_char_inicio and opdoIzq < var_loc_temp_int_inicio) or (opdoIzq >= var_loc_temp_char_inicio and opdoIzq < cte_int_inicio):
            dato1 = memoriaActiva.chars[opdoIzq]
        elif opdoIzq >= cte_int_inicio and opdoIzq < cte_float_inicio:
            dato1 = int(search(ctes,opdoIzq))
        elif opdoIzq >= cte_float_inicio and opdoIzq < cte_bool_inicio:
            dato1 = float(search(ctes,opdoIzq))
        elif opdoIzq >= cte_bool_inicio and opdoIzq < cte_char_inicio:
            if search(ctes,opdoIzq) == 'tru':
                dato1 = True
            else:
                dato1 = False
        elif opdoIzq >= cte_char_inicio:
            dato1 = search(ctes,opdoIzq)

        if opdoDer >= var_glob_int_inicio and opdoDer < var_glob_float_inicio:
            dato2 = memoriaGlobal.ints[opdoDer]
        elif opdoDer >= var_glob_float_inicio and opdoDer < var_glob_bool_inicio:
            dato2 = memoriaGlobal.floats[opdoDer]
        elif opdoDer >= var_glob_bool_inicio and opdoDer < var_glob_char_inicio:
            dato2 = memoriaGlobal.bools[opdoDer]
        elif opdoDer >= var_glob_char_inicio and opdoDer < var_loc_int_inicio:
            dato2 = memoriaGlobal.chars[opdoDer]
        elif (opdoDer >= var_loc_int_inicio and opdoDer < var_loc_float_inicio) or (opdoDer >= var_loc_temp_int_inicio and opdoDer < var_loc_temp_float_inicio):
            dato2 = memoriaActiva.ints[opdoDer]
        elif (opdoDer >= var_loc_float_inicio and opdoDer < var_loc_bool_inicio) or (opdoDer >= var_loc_temp_float_inicio and opdoDer < var_loc_temp_bool_inicio):
            dato2 = memoriaActiva.floats[opdoDer]
        elif (opdoDer >= var_loc_bool_inicio and opdoDer < var_loc_char_inicio) or (opdoDer >= var_loc_temp_bool_inicio and opdoDer < var_loc_temp_char_inicio):
            dato2 = memoriaActiva.bools[opdoDer]
        elif (opdoDer >= var_loc_char_inicio and opdoDer < var_loc_temp_int_inicio) or (opdoDer >= var_loc_temp_char_inicio and opdoDer < cte_int_inicio):
            dato2 = memoriaActiva.chars[opdoDer]
        elif opdoDer >= cte_int_inicio and opdoDer < cte_float_inicio:
            dato2 = int(search(ctes,opdoDer))
        elif opdoDer >= cte_float_inicio and opdoDer < cte_bool_inicio:
            dato2 = float(search(ctes,opdoDer))
        elif opdoDer >= cte_bool_inicio and opdoDer < cte_char_inicio:
            if search(ctes,opdoDer) == 'tru':
                dato2 = True
            else:
                dato2 = False
        elif opdoDer >= cte_char_inicio:
            dato2 = search(ctes,opdoDer)

        res = dato1 != dato2

        if resultado >= var_glob_bool_inicio and resultado < var_glob_char_inicio:
            memoriaGlobal.bools[resultado] = res
        elif (resultado >= var_loc_bool_inicio and resultado < var_loc_char_inicio) or (resultado >= var_loc_temp_bool_inicio and resultado < var_loc_temp_char_inicio):
            memoriaActiva.bools[resultado] = res

        current_cuad +=1

    elif op == GT:

        if opdoIzq >= var_glob_int_inicio and opdoIzq < var_glob_float_inicio:
            dato1 = memoriaGlobal.ints[opdoIzq]
        elif opdoIzq >= var_glob_float_inicio and opdoIzq < var_glob_bool_inicio:
            dato1 = memoriaGlobal.floats[opdoIzq]
        elif (opdoIzq >= var_loc_int_inicio and opdoIzq < var_loc_float_inicio) or (opdoIzq >= var_loc_temp_int_inicio and opdoIzq < var_loc_temp_float_inicio):
            dato1 = memoriaActiva.ints[opdoIzq]
        elif (opdoIzq >= var_loc_float_inicio and opdoIzq < var_loc_bool_inicio) or (opdoIzq >= var_loc_temp_float_inicio and opdoIzq < var_loc_temp_bool_inicio):
            dato1 = memoriaActiva.floats[opdoIzq]
        elif opdoIzq >= cte_int_inicio and opdoIzq < cte_float_inicio:
            dato1 = int(search(ctes,opdoIzq))
        elif opdoIzq >= cte_float_inicio and opdoIzq < cte_bool_inicio:
            dato1 = float(search(ctes,opdoIzq))

        if opdoDer >= var_glob_int_inicio and opdoDer < var_glob_float_inicio:
            dato2 = memoriaGlobal.ints[opdoDer]
        elif opdoDer >= var_glob_float_inicio and opdoDer < var_glob_bool_inicio:
            dato2 = memoriaGlobal.floats[opdoDer]
        elif (opdoDer >= var_loc_int_inicio and opdoDer < var_loc_float_inicio) or (opdoDer >= var_loc_temp_int_inicio and opdoDer < var_loc_temp_float_inicio):
            dato2 = memoriaActiva.ints[opdoDer]
        elif (opdoDer >= var_loc_float_inicio and opdoDer < var_loc_bool_inicio) or (opdoDer >= var_loc_temp_float_inicio and opdoDer < var_loc_temp_bool_inicio):
            dato2 = memoriaActiva.floats[opdoDer]
        elif opdoDer >= cte_int_inicio and opdoDer < cte_float_inicio:
            dato2 = int(search(ctes,opdoDer))
        elif opdoDer >= cte_float_inicio and opdoDer < cte_bool_inicio:
            dato2 = float(search(ctes,opdoDer))

        res = dato1 > dato2

        if resultado >= var_glob_bool_inicio and resultado < var_glob_char_inicio:
            memoriaGlobal.bools[resultado] = res
        elif (resultado >= var_loc_bool_inicio and resultado < var_loc_char_inicio) or (resultado >= var_loc_temp_bool_inicio and resultado < var_loc_temp_char_inicio):
            memoriaActiva.bools[resultado] = res

        current_cuad +=1

    elif op == LT:

        if opdoIzq >= var_glob_int_inicio and opdoIzq < var_glob_float_inicio:
            dato1 = memoriaGlobal.ints[opdoIzq]
        elif opdoIzq >= var_glob_float_inicio and opdoIzq < var_glob_bool_inicio:
            dato1 = memoriaGlobal.floats[opdoIzq]
        elif (opdoIzq >= var_loc_int_inicio and opdoIzq < var_loc_float_inicio) or (opdoIzq >= var_loc_temp_int_inicio and opdoIzq < var_loc_temp_float_inicio):
            dato1 = memoriaActiva.ints[opdoIzq]
        elif (opdoIzq >= var_loc_float_inicio and opdoIzq < var_loc_bool_inicio) or (opdoIzq >= var_loc_temp_float_inicio and opdoIzq < var_loc_temp_bool_inicio):
            dato1 = memoriaActiva.floats[opdoIzq]
        elif opdoIzq >= cte_int_inicio and opdoIzq < cte_float_inicio:
            dato1 = int(search(ctes,opdoIzq))
        elif opdoIzq >= cte_float_inicio and opdoIzq < cte_bool_inicio:
            dato1 = float(search(ctes,opdoIzq))

        if opdoDer >= var_glob_int_inicio and opdoDer < var_glob_float_inicio:
            dato2 = memoriaGlobal.ints[opdoDer]
        elif opdoDer >= var_glob_float_inicio and opdoDer < var_glob_bool_inicio:
            dato2 = memoriaGlobal.floats[opdoDer]
        elif (opdoDer >= var_loc_int_inicio and opdoDer < var_loc_float_inicio) or (opdoDer >= var_loc_temp_int_inicio and opdoDer < var_loc_temp_float_inicio):
            dato2 = memoriaActiva.ints[opdoDer]
        elif (opdoDer >= var_loc_float_inicio and opdoDer < var_loc_bool_inicio) or (opdoDer >= var_loc_temp_float_inicio and opdoDer < var_loc_temp_bool_inicio):
            dato2 = memoriaActiva.floats[opdoDer]
        elif opdoDer >= cte_int_inicio and opdoDer < cte_float_inicio:
            dato2 = int(search(ctes,opdoDer))
        elif opdoDer >= cte_float_inicio and opdoDer < cte_bool_inicio:
            dato2 = float(search(ctes,opdoDer))

        res = dato1 < dato2

        if resultado >= var_glob_bool_inicio and resultado < var_glob_char_inicio:
            memoriaGlobal.bools[resultado] = res
        elif (resultado >= var_loc_bool_inicio and resultado < var_loc_char_inicio) or (resultado >= var_loc_temp_bool_inicio and resultado < var_loc_temp_char_inicio):
            memoriaActiva.bools[resultado] = res

        current_cuad +=1

    elif op == GTE:

        if opdoIzq >= var_glob_int_inicio and opdoIzq < var_glob_float_inicio:
            dato1 = memoriaGlobal.ints[opdoIzq]
        elif opdoIzq >= var_glob_float_inicio and opdoIzq < var_glob_bool_inicio:
            dato1 = memoriaGlobal.floats[opdoIzq]
        elif (opdoIzq >= var_loc_int_inicio and opdoIzq < var_loc_float_inicio) or (opdoIzq >= var_loc_temp_int_inicio and opdoIzq < var_loc_temp_float_inicio):
            dato1 = memoriaActiva.ints[opdoIzq]
        elif (opdoIzq >= var_loc_float_inicio and opdoIzq < var_loc_bool_inicio) or (opdoIzq >= var_loc_temp_float_inicio and opdoIzq < var_loc_temp_bool_inicio):
            dato1 = memoriaActiva.floats[opdoIzq]
        elif opdoIzq >= cte_int_inicio and opdoIzq < cte_float_inicio:
            dato1 = int(search(ctes,opdoIzq))
        elif opdoIzq >= cte_float_inicio and opdoIzq < cte_bool_inicio:
            dato1 = float(search(ctes,opdoIzq))

        if opdoDer >= var_glob_int_inicio and opdoDer < var_glob_float_inicio:
            dato2 = memoriaGlobal.ints[opdoDer]
        elif opdoDer >= var_glob_float_inicio and opdoDer < var_glob_bool_inicio:
            dato2 = memoriaGlobal.floats[opdoDer]
        elif (opdoDer >= var_loc_int_inicio and opdoDer < var_loc_float_inicio) or (opdoDer >= var_loc_temp_int_inicio and opdoDer < var_loc_temp_float_inicio):
            dato2 = memoriaActiva.ints[opdoDer]
        elif (opdoDer >= var_loc_float_inicio and opdoDer < var_loc_bool_inicio) or (opdoDer >= var_loc_temp_float_inicio and opdoDer < var_loc_temp_bool_inicio):
            dato2 = memoriaActiva.floats[opdoDer]
        elif opdoDer >= cte_int_inicio and opdoDer < cte_float_inicio:
            dato2 = int(search(ctes,opdoDer))
        elif opdoDer >= cte_float_inicio and opdoDer < cte_bool_inicio:
            dato2 = float(search(ctes,opdoDer))

        res = dato1 >= dato2

        if resultado >= var_glob_bool_inicio and resultado < var_glob_char_inicio:
            memoriaGlobal.bools[resultado] = res
        elif (resultado >= var_loc_bool_inicio and resultado < var_loc_char_inicio) or (resultado >= var_loc_temp_bool_inicio and resultado < var_loc_temp_char_inicio):
            memoriaActiva.bools[resultado] = res

        current_cuad +=1

    elif op == LTE:

        if opdoIzq >= var_glob_int_inicio and opdoIzq < var_glob_float_inicio:
            dato1 = memoriaGlobal.ints[opdoIzq]
        elif opdoIzq >= var_glob_float_inicio and opdoIzq < var_glob_bool_inicio:
            dato1 = memoriaGlobal.floats[opdoIzq]
        elif (opdoIzq >= var_loc_int_inicio and opdoIzq < var_loc_float_inicio) or (opdoIzq >= var_loc_temp_int_inicio and opdoIzq < var_loc_temp_float_inicio):
            dato1 = memoriaActiva.ints[opdoIzq]
        elif (opdoIzq >= var_loc_float_inicio and opdoIzq < var_loc_bool_inicio) or (opdoIzq >= var_loc_temp_float_inicio and opdoIzq < var_loc_temp_bool_inicio):
            dato1 = memoriaActiva.floats[opdoIzq]
        elif opdoIzq >= cte_int_inicio and opdoIzq < cte_float_inicio:
            dato1 = int(search(ctes,opdoIzq))
        elif opdoIzq >= cte_float_inicio and opdoIzq < cte_bool_inicio:
            dato1 = float(search(ctes,opdoIzq))

        if opdoDer >= var_glob_int_inicio and opdoDer < var_glob_float_inicio:
            dato2 = memoriaGlobal.ints[opdoDer]
        elif opdoDer >= var_glob_float_inicio and opdoDer < var_glob_bool_inicio:
            dato2 = memoriaGlobal.floats[opdoDer]
        elif (opdoDer >= var_loc_int_inicio and opdoDer < var_loc_float_inicio) or (opdoDer >= var_loc_temp_int_inicio and opdoDer < var_loc_temp_float_inicio):
            dato2 = memoriaActiva.ints[opdoDer]
        elif (opdoDer >= var_loc_float_inicio and opdoDer < var_loc_bool_inicio) or (opdoDer >= var_loc_temp_float_inicio and opdoDer < var_loc_temp_bool_inicio):
            dato2 = memoriaActiva.floats[opdoDer]
        elif opdoDer >= cte_int_inicio and opdoDer < cte_float_inicio:
            dato2 = int(search(ctes,opdoDer))
        elif opdoDer >= cte_float_inicio and opdoDer < cte_bool_inicio:
            dato2 = float(search(ctes,opdoDer))

        res = dato1 <= dato2

        if resultado >= var_glob_bool_inicio and resultado < var_glob_char_inicio:
            memoriaGlobal.bools[resultado] = res
        elif (resultado >= var_loc_bool_inicio and resultado < var_loc_char_inicio) or (resultado >= var_loc_temp_bool_inicio and resultado < var_loc_temp_char_inicio):
            memoriaActiva.bools[resultado] = res

        current_cuad +=1

    elif op == PLUS:

        if opdoIzq >= var_glob_int_inicio and opdoIzq < var_glob_float_inicio:
            dato1 = memoriaGlobal.ints[opdoIzq]
        elif opdoIzq >= var_glob_float_inicio and opdoIzq < var_glob_bool_inicio:
            dato1 = memoriaGlobal.floats[opdoIzq]
        elif (opdoIzq >= var_loc_int_inicio and opdoIzq < var_loc_float_inicio) or (opdoIzq >= var_loc_temp_int_inicio and opdoIzq < var_loc_temp_float_inicio):
            dato1 = memoriaActiva.ints[opdoIzq]
        elif (opdoIzq >= var_loc_float_inicio and opdoIzq < var_loc_bool_inicio) or (opdoIzq >= var_loc_temp_float_inicio and opdoIzq < var_loc_temp_bool_inicio):
            dato1 = memoriaActiva.floats[opdoIzq]
        elif opdoIzq >= cte_int_inicio and opdoIzq < cte_float_inicio:
            dato1 = int(search(ctes,opdoIzq))
        elif opdoIzq >= cte_float_inicio and opdoIzq < cte_bool_inicio:
            dato1 = float(search(ctes,opdoIzq))

        if opdoDer >= var_glob_int_inicio and opdoDer < var_glob_float_inicio:
            dato2 = memoriaGlobal.ints[opdoDer]
        elif opdoDer >= var_glob_float_inicio and opdoDer < var_glob_bool_inicio:
            dato2 = memoriaGlobal.floats[opdoDer]
        elif (opdoDer >= var_loc_int_inicio and opdoDer < var_loc_float_inicio) or (opdoDer >= var_loc_temp_int_inicio and opdoDer < var_loc_temp_float_inicio):
            dato2 = memoriaActiva.ints[opdoDer]
        elif (opdoDer >= var_loc_float_inicio and opdoDer < var_loc_bool_inicio) or (opdoDer >= var_loc_temp_float_inicio and opdoDer < var_loc_temp_bool_inicio):
            dato2 = memoriaActiva.floats[opdoDer]
        elif opdoDer >= cte_int_inicio and opdoDer < cte_float_inicio:
            dato2 = int(search(ctes,opdoDer))
        elif opdoDer >= cte_float_inicio and opdoDer < cte_bool_inicio:
            dato2 = float(search(ctes,opdoDer))

        res = dato1 + dato2

        if resultado >= var_glob_int_inicio and resultado < var_glob_float_inicio:
            memoriaGlobal.ints[resultado] = res
        elif resultado >= var_glob_float_inicio and resultado < var_glob_bool_inicio:
            memoriaGlobal.floats[resultado] = res
        elif (resultado >= var_loc_int_inicio and resultado < var_loc_float_inicio) or (resultado >= var_loc_temp_int_inicio and resultado < var_loc_temp_float_inicio):
            memoriaActiva.ints[resultado] = res
        elif (resultado >= var_loc_float_inicio and resultado < var_loc_bool_inicio) or (resultado >= var_loc_temp_float_inicio and resultado < var_loc_temp_bool_inicio):
            memoriaActiva.floats[resultado] = res

        current_cuad +=1

    elif op == MINUS:

        if opdoIzq >= var_glob_int_inicio and opdoIzq < var_glob_float_inicio:
            dato1 = memoriaGlobal.ints[opdoIzq]
        elif opdoIzq >= var_glob_float_inicio and opdoIzq < var_glob_bool_inicio:
            dato1 = memoriaGlobal.floats[opdoIzq]
        elif (opdoIzq >= var_loc_int_inicio and opdoIzq < var_loc_float_inicio) or (opdoIzq >= var_loc_temp_int_inicio and opdoIzq < var_loc_temp_float_inicio):
            dato1 = memoriaActiva.ints[opdoIzq]
        elif (opdoIzq >= var_loc_float_inicio and opdoIzq < var_loc_bool_inicio) or (opdoIzq >= var_loc_temp_float_inicio and opdoIzq < var_loc_temp_bool_inicio):
            dato1 = memoriaActiva.floats[opdoIzq]
        elif opdoIzq >= cte_int_inicio and opdoIzq < cte_float_inicio:
            dato1 = int(search(ctes,opdoIzq))
        elif opdoIzq >= cte_float_inicio and opdoIzq < cte_bool_inicio:
            dato1 = float(search(ctes,opdoIzq))

        if opdoDer >= var_glob_int_inicio and opdoDer < var_glob_float_inicio:
            dato2 = memoriaGlobal.ints[opdoDer]
        elif opdoDer >= var_glob_float_inicio and opdoDer < var_glob_bool_inicio:
            dato2 = memoriaGlobal.floats[opdoDer]
        elif (opdoDer >= var_loc_int_inicio and opdoDer < var_loc_float_inicio) or (opdoDer >= var_loc_temp_int_inicio and opdoDer < var_loc_temp_float_inicio):
            dato2 = memoriaActiva.ints[opdoDer]
        elif (opdoDer >= var_loc_float_inicio and opdoDer < var_loc_bool_inicio) or (opdoDer >= var_loc_temp_float_inicio and opdoDer < var_loc_temp_bool_inicio):
            dato2 = memoriaActiva.floats[opdoDer]
        elif opdoDer >= cte_int_inicio and opdoDer < cte_float_inicio:
            dato2 = int(search(ctes,opdoDer))
        elif opdoDer >= cte_float_inicio and opdoDer < cte_bool_inicio:
            dato2 = float(search(ctes,opdoDer))

        res = dato1 - dato2

        if resultado >= var_glob_int_inicio and resultado < var_glob_float_inicio:
            memoriaGlobal.ints[resultado] = res
        elif resultado >= var_glob_float_inicio and resultado < var_glob_bool_inicio:
            memoriaGlobal.floats[resultado] = res
        elif (resultado >= var_loc_int_inicio and resultado < var_loc_float_inicio) or (resultado >= var_loc_temp_int_inicio and resultado < var_loc_temp_float_inicio):
            memoriaActiva.ints[resultado] = res
        elif (resultado >= var_loc_float_inicio and resultado < var_loc_bool_inicio) or (resultado >= var_loc_temp_float_inicio and resultado < var_loc_temp_bool_inicio):
            memoriaActiva.floats[resultado] = res

        current_cuad +=1

    elif op == NOT:

        if opdoIzq >= var_glob_bool_inicio and opdoIzq < var_glob_char_inicio:
            dato1 = memoriaGlobal.bools[opdoIzq]
        elif (opdoIzq >= var_loc_bool_inicio and opdoIzq < var_loc_char_inicio) or (opdoIzq >= var_loc_temp_bool_inicio and opdoIzq < var_loc_temp_char_inicio):
            dato1 = memoriaActiva.bools[opdoIzq]
        elif opdoIzq >= cte_bool_inicio and opdoIzq < cte_char_inicio:
            if search(ctes,opdoIzq) == 'tru':
                dato1 = True
            else:
                dato1 = False

        res = not dato1

        if resultado >= var_glob_bool_inicio and resultado < var_glob_char_inicio:
            memoriaGlobal.bools[resultado] = res
        elif (resultado >= var_loc_bool_inicio and resultado < var_loc_char_inicio) or (resultado >= var_loc_temp_bool_inicio and resultado < var_loc_temp_char_inicio):
            memoriaActiva.bools[resultado] = res

        current_cuad +=1

    elif op == EQ:

        if opdoIzq >= var_glob_int_inicio and opdoIzq < var_glob_float_inicio:
            dato1 = memoriaGlobal.ints[opdoIzq]
        elif opdoIzq >= var_glob_float_inicio and opdoIzq < var_glob_bool_inicio:
            dato1 = memoriaGlobal.floats[opdoIzq]
        elif opdoIzq >= var_glob_bool_inicio and opdoIzq < var_glob_char_inicio:
            dato1 = memoriaGlobal.bools[opdoIzq]
        elif opdoIzq >= var_glob_char_inicio and opdoIzq < var_loc_int_inicio:
            dato1 = memoriaGlobal.chars[opdoIzq]
        elif (opdoIzq >= var_loc_int_inicio and opdoIzq < var_loc_float_inicio) or (opdoIzq >= var_loc_temp_int_inicio and opdoIzq < var_loc_temp_float_inicio):
            dato1 = memoriaActiva.ints[opdoIzq]
        elif (opdoIzq >= var_loc_float_inicio and opdoIzq < var_loc_bool_inicio) or (opdoIzq >= var_loc_temp_float_inicio and opdoIzq < var_loc_temp_bool_inicio):
            dato1 = memoriaActiva.floats[opdoIzq]
        elif (opdoIzq >= var_loc_bool_inicio and opdoIzq < var_loc_char_inicio) or (opdoIzq >= var_loc_temp_bool_inicio and opdoIzq < var_loc_temp_char_inicio):
            dato1 = memoriaActiva.bools[opdoIzq]
        elif (opdoIzq >= var_loc_char_inicio and opdoIzq < var_loc_temp_int_inicio) or (opdoIzq >= var_loc_temp_char_inicio and opdoIzq < cte_int_inicio):
            dato1 = memoriaActiva.chars[opdoIzq]
        elif opdoIzq >= cte_int_inicio and opdoIzq < cte_float_inicio:
            dato1 = int(search(ctes,opdoIzq))
        elif opdoIzq >= cte_float_inicio and opdoIzq < cte_bool_inicio:
            dato1 = float(search(ctes,opdoIzq))
        elif opdoIzq >= cte_bool_inicio and opdoIzq < cte_char_inicio:
            if search(ctes,opdoIzq) == 'tru':
                dato1 = True
            else:
                dato1 = False
        elif opdoIzq >= cte_char_inicio:
            dato1 = search(ctes,opdoIzq)

        res = dato1


        if resultado >= var_glob_int_inicio and resultado < var_glob_float_inicio:
            memoriaGlobal.ints[resultado] = res
        elif resultado >= var_glob_float_inicio and resultado < var_glob_bool_inicio:
            memoriaGlobal.floats[resultado] = res
        elif resultado >= var_glob_bool_inicio and resultado < var_glob_char_inicio:
            memoriaGlobal.bools[resultado] = res
        elif resultado >= var_glob_char_inicio and resultado < var_loc_int_inicio:
            memoriaGlobal.chars[resultado] = res
        elif (resultado >= var_loc_int_inicio and resultado < var_loc_float_inicio) or (resultado >= var_loc_temp_int_inicio and resultado < var_loc_temp_float_inicio):
            memoriaActiva.ints[resultado] = res
        elif (resultado >= var_loc_float_inicio and resultado < var_loc_bool_inicio) or (resultado >= var_loc_temp_float_inicio and resultado < var_loc_temp_bool_inicio):
            memoriaActiva.floats[resultado] = res
        elif (resultado >= var_loc_bool_inicio and resultado < var_loc_char_inicio) or (resultado >= var_loc_temp_bool_inicio and resultado < var_loc_temp_char_inicio):
            memoriaActiva.bools[resultado] = res
        elif (resultado >= var_loc_char_inicio and resultado < var_loc_temp_int_inicio) or (resultado >= var_loc_temp_char_inicio and resultado < cte_int_inicio):
            memoriaActiva.chars[resultado] = res

        current_cuad +=1

    elif op == PLAY:
        ##TODO: Robi sabe como se construye este pedo
        print "pase play"
        current_cuad +=1

    elif op == PRINT:
        if opdoIzq >= var_glob_int_inicio and opdoIzq < var_glob_float_inicio:
            dato1 = memoriaGlobal.ints[opdoIzq]
        elif opdoIzq >= var_glob_float_inicio and opdoIzq < var_glob_bool_inicio:
            dato1 = memoriaGlobal.floats[opdoIzq]
        elif opdoIzq >= var_glob_bool_inicio and opdoIzq < var_glob_char_inicio:
            dato1 = memoriaGlobal.bools[opdoIzq]
        elif opdoIzq >= var_glob_char_inicio and opdoIzq < var_loc_int_inicio:
            dato1 = memoriaGlobal.chars[opdoIzq]
        elif (opdoIzq >= var_loc_int_inicio and opdoIzq < var_loc_float_inicio) or (opdoIzq >= var_loc_temp_int_inicio and opdoIzq < var_loc_temp_float_inicio):
            dato1 = memoriaActiva.ints[opdoIzq]
        elif (opdoIzq >= var_loc_float_inicio and opdoIzq < var_loc_bool_inicio) or (opdoIzq >= var_loc_temp_float_inicio and opdoIzq < var_loc_temp_bool_inicio):
            dato1 = memoriaActiva.floats[opdoIzq]
        elif (opdoIzq >= var_loc_bool_inicio and opdoIzq < var_loc_char_inicio) or (opdoIzq >= var_loc_temp_bool_inicio and opdoIzq < var_loc_temp_char_inicio):
            dato1 = memoriaActiva.bools[opdoIzq]
        elif (opdoIzq >= var_loc_char_inicio and opdoIzq < var_loc_temp_int_inicio) or (opdoIzq >= var_loc_temp_char_inicio and opdoIzq < cte_int_inicio):
            dato1 = memoriaActiva.chars[opdoIzq]
        elif opdoIzq >= cte_int_inicio and opdoIzq < cte_float_inicio:
            dato1 = int(search(ctes,opdoIzq))
        elif opdoIzq >= cte_float_inicio and opdoIzq < cte_bool_inicio:
            dato1 = float(search(ctes,opdoIzq))
        elif opdoIzq >= cte_bool_inicio and opdoIzq < cte_char_inicio:
            if search(ctes,opdoIzq) == 'tru':
                dato1 = True
            else:
                dato1 = False
        elif opdoIzq >= cte_char_inicio:
            dato1 = search(ctes,opdoIzq)

        print dato1
        current_cuad += 1

    elif op == GOTO:
        current_cuad = resultado

    elif op == GOTOF:

        if opdoIzq >= var_glob_bool_inicio and opdoIzq < var_glob_char_inicio:
            dato1 = memoriaGlobal.bools[opdoIzq]
        elif (opdoIzq >= var_loc_bool_inicio and opdoIzq < var_loc_char_inicio) or (opdoIzq >= var_loc_temp_bool_inicio and opdoIzq < var_loc_temp_char_inicio):
            dato1 = memoriaActiva.bools[opdoIzq]
        elif opdoIzq >= cte_bool_inicio and opdoIzq < cte_char_inicio:
            if search(ctes,opdoIzq) == 'tru':
                dato1 = True
            else:
                dato1 = False

        if not dato1:
            current_cuad = resultado
        else:
            current_cuad +=1

    elif op == GOTOV:

        if opdoIzq >= var_glob_bool_inicio and opdoIzq < var_glob_char_inicio:
            dato1 = memoriaGlobal.bools[opdoIzq]
        elif (opdoIzq >= var_loc_bool_inicio and opdoIzq < var_loc_char_inicio) or (opdoIzq >= var_loc_temp_bool_inicio and opdoIzq < var_loc_temp_char_inicio):
            dato1 = memoriaActiva.bools[opdoIzq]
        elif opdoIzq >= cte_bool_inicio and opdoIzq < cte_char_inicio:
            if search(ctes,opdoIzq) == 'tru':
                dato1 = True
            else:
                dato1 = False

        if dato1:
            current_cuad = resultado
        else:
            current_cuad +=1

    elif op == ENDPROC:
        current_cuad = pSaltos.pop() + 1
        if memoriaDormida != []:
            memoriaActiva = memoriaDormida.pop()

    elif op == ERA:
        global memoriaAux
        memoriaAux = memoria.Memoria(dir_procs[opdoIzq][pos_dics_tam]['vi'], dir_procs[opdoIzq][pos_dics_tam]['vf'], dir_procs[opdoIzq][pos_dics_tam]['vb'], dir_procs[opdoIzq][pos_dics_tam]['vc'], dir_procs[opdoIzq][pos_dics_tam]['ti'], dir_procs[opdoIzq][pos_dics_tam]['tf'], dir_procs[opdoIzq][pos_dics_tam]['tb'], dir_procs[opdoIzq][pos_dics_tam]['tc'], False)
        current_cuad +=1

    elif op == PARAMETRO:
        if opdoIzq >= var_glob_int_inicio and opdoIzq < var_glob_float_inicio:
            dato1 = memoriaGlobal.ints[opdoIzq]
        elif opdoIzq >= var_glob_float_inicio and opdoIzq < var_glob_bool_inicio:
            dato1 = memoriaGlobal.floats[opdoIzq]
        elif opdoIzq >= var_glob_bool_inicio and opdoIzq < var_glob_char_inicio:
            dato1 = memoriaGlobal.bools[opdoIzq]
        elif opdoIzq >= var_glob_char_inicio and opdoIzq < var_loc_int_inicio:
            dato1 = memoriaGlobal.chars[opdoIzq]
        elif (opdoIzq >= var_loc_int_inicio and opdoIzq < var_loc_float_inicio) or (opdoIzq >= var_loc_temp_int_inicio and opdoIzq < var_loc_temp_float_inicio):
            dato1 = memoriaActiva.ints[opdoIzq]
        elif (opdoIzq >= var_loc_float_inicio and opdoIzq < var_loc_bool_inicio) or (opdoIzq >= var_loc_temp_float_inicio and opdoIzq < var_loc_temp_bool_inicio):
            dato1 = memoriaActiva.floats[opdoIzq]
        elif (opdoIzq >= var_loc_bool_inicio and opdoIzq < var_loc_char_inicio) or (opdoIzq >= var_loc_temp_bool_inicio and opdoIzq < var_loc_temp_char_inicio):
            dato1 = memoriaActiva.bools[opdoIzq]
        elif (opdoIzq >= var_loc_char_inicio and opdoIzq < var_loc_temp_int_inicio) or (opdoIzq >= var_loc_temp_char_inicio and opdoIzq < cte_int_inicio):
            dato1 = memoriaActiva.chars[opdoIzq]
        elif opdoIzq >= cte_int_inicio and opdoIzq < cte_float_inicio:
            dato1 = int(search(ctes,opdoIzq))
        elif opdoIzq >= cte_float_inicio and opdoIzq < cte_bool_inicio:
            dato1 = float(search(ctes,opdoIzq))
        elif opdoIzq >= cte_bool_inicio and opdoIzq < cte_char_inicio:
            if search(ctes,opdoIzq) == 'tru':
                dato1 = True
            else:
                dato1 = False
        elif opdoIzq >= cte_char_inicio:
            dato1 = search(ctes,opdoIzq)

        res = dato1

        if (resultado >= var_loc_int_inicio and resultado < var_loc_float_inicio) or (resultado >= var_loc_temp_int_inicio and resultado < var_loc_temp_float_inicio):
            memoriaAux.ints[resultado] = res
        elif (resultado >= var_loc_float_inicio and resultado < var_loc_bool_inicio) or (resultado >= var_loc_temp_float_inicio and resultado < var_loc_temp_bool_inicio):
            memoriaAux.floats[resultado] = res
        elif (resultado >= var_loc_bool_inicio and resultado < var_loc_char_inicio) or (resultado >= var_loc_temp_bool_inicio and resultado < var_loc_temp_char_inicio):
            memoriaAux.bools[resultado] = res
        elif (resultado >= var_loc_char_inicio and resultado < var_loc_temp_int_inicio) or (resultado >= var_loc_temp_char_inicio and resultado < cte_int_inicio):
            memoriaAux.chars[resultado] = res

        current_cuad +=1

    elif op == GOSUB:
        if memoriaActiva != None:
            memoriaDormida.append(memoriaActiva)
        memoriaActiva = memoriaAux
        pSaltos.append(current_cuad)
        current_cuad = dir_procs[opdoIzq][pos_dics_dir_inicio]

    elif op == VERIFICA:
        if opdoIzq >= var_glob_int_inicio and opdoIzq < var_glob_float_inicio:
            dato1 = memoriaGlobal.ints[opdoIzq]
        elif (opdoIzq >= var_loc_int_inicio and opdoIzq < var_loc_float_inicio) or (opdoIzq >= var_loc_temp_int_inicio and opdoIzq < var_loc_temp_float_inicio):
            dato1 = memoriaActiva.ints[opdoIzq]
        elif opdoIzq >= cte_int_inicio and opdoIzq < cte_float_inicio:
            dato1 = int(search(ctes,opdoIzq))
        if dato1 < opdoDer or dato1 > resultado:
            print "Indice fuera de rango"
            exit()
        current_cuad += 1

    elif op == NEG:

        if opdoIzq >= var_glob_int_inicio and opdoIzq < var_glob_float_inicio:
            dato1 = memoriaGlobal.ints[opdoIzq]
        elif opdoIzq >= var_glob_float_inicio and opdoIzq < var_glob_bool_inicio:
            dato1 = memoriaGlobal.floats[opdoIzq]
        elif (opdoIzq >= var_loc_int_inicio and opdoIzq < var_loc_float_inicio) or (opdoIzq >= var_loc_temp_int_inicio and opdoIzq < var_loc_temp_float_inicio):
            dato1 = memoriaActiva.ints[opdoIzq]
        elif (opdoIzq >= var_loc_float_inicio and opdoIzq < var_loc_bool_inicio) or (opdoIzq >= var_loc_temp_float_inicio and opdoIzq < var_loc_temp_bool_inicio):
            dato1 = memoriaActiva.floats[opdoIzq]
        elif opdoIzq >= cte_int_inicio and opdoIzq < cte_float_inicio:
            dato1 = int(search(ctes,opdoIzq))
        elif opdoIzq >= cte_float_inicio and opdoIzq < cte_bool_inicio:
            dato1 = float(search(ctes,opdoIzq))

        res = -dato1

        if resultado >= var_glob_int_inicio and resultado < var_glob_float_inicio:
            memoriaGlobal.ints[resultado] = res
        elif resultado >= var_glob_float_inicio and resultado < var_glob_bool_inicio:
            memoriaGlobal.floats[resultado] = res
        elif (resultado >= var_loc_int_inicio and resultado < var_loc_float_inicio) or (resultado >= var_loc_temp_int_inicio and resultado < var_loc_temp_float_inicio):
            memoriaActiva.ints[resultado] = res
        elif (resultado >= var_loc_float_inicio and resultado < var_loc_bool_inicio) or (resultado >= var_loc_temp_float_inicio and resultado < var_loc_temp_bool_inicio):
            memoriaActiva.floats[resultado] = res

        current_cuad +=1

######################################
## maquina virtual                  ##
######################################
print "comienza maquina virtual"
print ctes
global current_cuad
current_cuad = 1
memoriaGlobal = memoria.Memoria(dir_procs['global'][pos_dics_tam]['vi'], dir_procs['global'][pos_dics_tam]['vf'], dir_procs['global'][pos_dics_tam]['vb'], dir_procs['global'][pos_dics_tam]['vc'], dir_procs['global'][pos_dics_tam]['ti'], dir_procs['global'][pos_dics_tam]['tf'], dir_procs['global'][pos_dics_tam]['tb'], dir_procs['global'][pos_dics_tam]['tc'], True)
memoriaActiva = memoria.Memoria(dir_procs['CANCION'][pos_dics_tam]['vi'], dir_procs['CANCION'][pos_dics_tam]['vf'], dir_procs['CANCION'][pos_dics_tam]['vb'], dir_procs['CANCION'][pos_dics_tam]['vc'], dir_procs['CANCION'][pos_dics_tam]['ti'], dir_procs['CANCION'][pos_dics_tam]['tf'], dir_procs['CANCION'][pos_dics_tam]['tb'], dir_procs['CANCION'][pos_dics_tam]['tc'], False)
memoriaDormida = []
while current_cuad < contCuad:
    func_maq_virtual()
