# -----------------------------------------------------------------------------
# patito.py
#
# Un simple parser para la clase de compiladores.
# Basado en el ejemplo de calc.py de la libreria ply v 3.8
# -----------------------------------------------------------------------------

import sys
import pprint
pp = pprint.PrettyPrinter(indent=4)


# Cuando se revisa el archivo si la version
# de python es mayor a tres en lugar de raw_input
# se usa input
if sys.version_info[0] >= 3:
    raw_input = input

###############################################
## Tokens declarados                         ##
###############################################
tokens = (
    'VAR','FUNC','LIST','IF', 'ELSE',
    'FOR','NOT','AND','OR',
    'LENGTH','NOTA','PRINT',
    'CALL', 'RETURN', 'INT', 'CHAR', 'FLOAT',
    'BOOL','NOTEQ', 'LTHANEQ', 'MTHANEQ', 'EQ',
    'CTEF', 'CTEE', 'CTEBOOL', 'CTECHAR', 'ID',
    'CANCION','WHILE','PLAY','VOID'
    )

###############################################
## Literales aceptados                       ##
###############################################
literals = ['(',')',',',':',';', '{','}','*','/','',',',';','>','<','=','+','-','[',']','.']

###############################################
## Tokens desarrollados                      ##
###############################################

# La palabra PLAY literalmente, se usa para hacer la
# accion de tocar una nota
def t_PLAY(t):
    r'PLAY'
    return t

# La palabra VOID literalmente, se utiliza para declarar
# una funcion que no regresa nada
def t_VOID(t):
    r'VOID'
    return t

# La palabra WHILE literalmente, se utiliza para declarar
# ciclos de este tipo
def t_WHILE(t):
    r'WHILE'
    return t

# La palabra CANCION literalmente, se utiliza para declarar
# la funcion principal del programa que ira a ejecutarse
# primero
def t_CANCION(t):
    r'CANCION'
    return t

# La palabra VAR literalmente, se utiliza para declarar
# variables
def t_VAR(t):
    r'VAR'
    return t

# La palabra FUNC literalmente, se utiliza para declarar
# el inicio de una nueva funcion
def t_FUNC(t):
    r'FUNC'
    return t

# La palabra LIST literalmente, se utiliza para declarar
# que una variable es un arreglo
def t_LIST(t):
    r'LIST'
    return t

# La palabra IF literalmente, se utiliza para declarar el
# inicio de una condicional tipo if
def t_IF(t):
    r'IF'
    return t

# La palabra ELSE literalmente, se utiliza para definir
# el camino en falso de una condicional if
def t_ELSE(t):
    r'ELSE'
    return t

# La palabra FOR literalmente, se utiliza para declarar
# el inicio de un ciclo de este tipo
def t_FOR(t):
    r'FOR'
    return t

# La palabra NOT literalmente, se utiliza para negar
# una expresion tipo booleana
def t_NOT(t):
    r'NOT'
    return t

# La palabra AND literalmente, se utiliza para hacer una
# operacion and entre dos booleanos
def t_AND(t):
    r'AND'
    return t

# La palabra OR literalmente, se utiliza para hacer una
# operacion or entre dos booleanos
def t_OR(t):
    r'OR'
    return t

# La palabra LENGTH literalmente, se utiliza para sacar
# el tamano de una variable tipo lista o arreglo
def t_LENGTH(t):
    r'LENGTH'
    return t

# Las notas se definen entre una letra de la A a la G
# y con un numero del 1 al 7, estas se usan en el estatuto
# play
def t_NOTA(t):
    r'([A-G][1-7])|([A,C,D,F,G][#][1-7])'
    return t

# La palabra PRINT literalmente, se utilia para imprimir
# texto en la consola
def t_PRINT(t):
    r'PRINT'
    return t

# La palabra CALL literalmente, se utiliza para mandar a
# llamar una funcion
def t_CALL(t):
    r'CALL'
    return t

# La palabra RETURN literalmente, se utiliza para regresar
# respuesta en una funcion que no sea de tipo void
def t_RETURN(t):
    r'RETURN'
    return t

# La palabra INT literalmente, se utiliza para declarar el
# tipo entero
def t_INT(t):
    r'INT'
    return t

# La palabra CHAR literalmente, se utiliza para declarar el
# tipo caracter
def t_CHAR(t):
    r'CHAR'
    return t

# La palabra FLOAT literalmente, se utiliza para declarar
# el tipo flotante
def t_FLOAT(t):
    r'FLOAT'
    return t

# La palabra BOOL literalmente, se utiliza para declarar
# el tipo booleano
def t_BOOL(t):
    r'BOOL'
    return t

# El token NOTEQ se llena con la combinacion del !=, se
# utiliza para comparar dos valores y decir si no son iguales
# tienen que ser del mismo tipo
def t_NOTEQ(t):
    r'!='
    return t

# El token LTHANEQ se llena con la combinacion del <=, se
# utiliza para comparar dos valores y decir si es menor o
# igual el primero del segundo
def t_LTHANEQ(t):
    r'<='
    return t

# El token LTHANEQ se llena con la combinacion del >=, se
# utiliza para comparar dos valores y decir si es mayor o
# igual el primero del segundo
def t_MTHANEQ(t):
    r'>='
    return t

# El token EQ se llena con la combinacion del ==, se
# utiliza para comparar dos valores y decir si es
# igual el primero al segundo, tienen que ser del mismo tipo
def t_EQ(t):
    r'=='
    return t

# El token CTEF se llena con la combinacion de una serie de
# digitos, opcionalmente seguido por un punto y mas digitos
# junto con la opcion de poner exponencial, para ser una
# CTEF tiene que tener el . o la e para exponenciar.
# Este token se utiliza para asignar valores a operaciones
# de tipo flotante.
def t_CTEF(t):
    r'[0-9]+([eE]([+]|[-])?|[.][0-9]+[eE]([+]|[-])?|[.])[0-9]+'
    t.value = float(t.value)
    return t

# El token CTEE se llena con la combinacion de una serie
# de digitos. Este token se utiliza para asignar valores
# a operaciones de tipo enteras.
def t_CTEE(t):
    r'[0-9]+'
    t.value = int(t.value)
    return t

# El token CTECHAR consiste de cualquier caracter salvo
# el salto de linea \n que se encuentre entre dos comillas
# dobles "". Este token se utiliza para asignar valores
# a operaciones de tipo char
def t_CTECHAR(t):
    r'\"[^\n"]\"'
    return t

# El token CTEBOOL consiste de la palabra True o False.
# Este token se utiliza para asignar valores a operaciones
# de tipo boolenas
def t_CTEBOOL(t):
    r'True| False'
    t.value = bool(t.value)
    return t

# El token ID consiste de empezar con una letra seguida
# de un guion bajo _ y una serie opcional de caracteres
# alfanumericos. Este token entra siempre y cuando no
# choque con los tokens anteriores ya que los anteriores
# son palabras reservadas. Este token se usa para declarar
# nombres de variables y funciones.
def t_ID(t):
    r'[A-Za-z]([_]?([a-zA-Z]|[0-9]))*'
    return t

# Al final se ignoran los espacios en blanco, tabuladores \t
# y saltos de linea \n
t_ignore = " \t\n"

# Si existe un error de lexico se imprime el mensaje
# Caracter ilegal seguido del Caracter que no se acepta
# y termina la ejecucion de la compilacion
def t_error(t):
    print("Caracter ilegal '%s'" % t.value[0])
    t.lexer.skip(1)

# Construye el lexico con la libreria de ply.lex
import ply.lex as lex
lex.lex()



###############################################
## Codigos de Operacion                      ##
###############################################

# Multiplicacion
MULT = 1
# Division
DIV = 2
# And
AND = 3
# Or
OR = 4
# ==
EQEQ = 5
# !=
NOTEQ = 6
# >
GT = 7
# <
LT = 8
# >=
GTE = 9
# <=
LTE = 10
# Suma
PLUS = 11
# Resta
MINUS = 12
# Not (!)
NOT = 13
# Asignacion
EQ = 14
# Play
PLAY = 15
# Imprime
PRINT = 16
# Brinco
GOTO = 17
# Brinco en falso
GOTOF = 18
# Brinco en verdader
GOTOV = 19
# Cierra procedimiento
ENDPROC = 20
# Registro de activacion
ERA = 21
# Entrada de parametro
PARAMETRO = 22
# Arranca procedimiento
GOSUB = 23
# Verifica que este dentro de rango el arreglo
VERIFICA = 24
# Signo negativo
NEG = 25
# Error, usado para los errores en el cubo semantico
ERR = -1

###############################################
## Codigos de Tipos                          ##
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

# diccionarios para la permutacion entre los 4 y asi
# cubrir todos los posibles escenarios
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

### Caso especial para igualdad ya que solo
### se puede asignar un int a un float y no al
### reves
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

# Pila de Operandos:
## Se utiliza para saber las direcciones virtuales
## de los operandos que estan pendientes por transformar
## o utilizar
pilaO=[]
# Pila de Operadores:
## Se utiliza para saber los codigos de operacion
## de las operaciones pendientes en el codigo actual
pOper=[]
# Pila de Tipos:
## Se utiliza para saber cuales son los codigos de los
## tipos que corresponden a la pila de operandos
pTipos=[]

####################################
## CUADRUPLOS                     ##
####################################

# Diccionario de Cuadruplos:
## Este diccionario de listas se utiliza para ingresar los cuadruplos
## que el programa va ingresando (codigo intermedio) que tiene la
## siguiente organizacion:
## posicion0 = codigo de la operacion a realizar
## posicion1 = direccion virtual del operando izquierdo
## posicion2 = direccion virtual del operando derecho
## posicion3 = direccion virtual del resultado
cuadruplos={}

# Iniciamos el contador de cuadruplos en 0
contCuad = 1

# Variable que representa la posicion de la operacion
# en el diccionario de cuadruplos
pos_cuads_op = 0

# Variable que representa la posicion del operando izquierdo
# en el diccionario de cuadruplos
pos_cuads_opdoIzq = 1

# Variable que representa la posicion del operando derecho
# en el diccionario de cuadruplos
pos_cuads_opdoDer = 2

# Variable que representa la posicion del resultado
# en el diccionario de cuadruplos
pos_cuads_res = 3

####################################
## Variables globales enteras     ##
####################################

# Direccion virtual que representa el actual de variables
# globales enteras en el programa, empieza en 1000
var_glob_int = 1000

# Direccion virtual que representa el inicio de las variables
# globales enteras en el programa
var_glob_int_inicio = 1000

####################################
## Variables globales flotantes   ##
####################################

# Direccion virtual que representa el actual de variables
# globales flotantes en el programa, empieza en 3000
var_glob_float = 3000

# Direccion virtual que representa el inicio de las variables
# globales flotantes en el programa
var_glob_float_inicio = 3000

####################################
## Variables globales booleanas   ##
####################################

# Direccion virtual que representa el actual de variables
# globales booleanas en el programa, empieza en 5000
var_glob_bool = 5000

# Direccion virtual que representa el inicio de las variables
# globales booleanas en el programa
var_glob_bool_inicio = 5000

####################################
## Variables globales char        ##
####################################

# Direccion virtual que representa el actual de variables
# globales char en el programa, empieza en 7000
var_glob_char = 7000

# Direccion virtual que representa el inicio de las variables
# globales char en el programa
var_glob_char_inicio = 7000

####################################
## Variables locales enteras      ##
####################################

# Direccion virtual que representa el actual de variables
# locales enteras en el contexto, empieza en 9000
var_loc_int = 9000

# Direccion virtual que representa el inicio de las variables
# locales char en el contexto
var_loc_int_inicio = 9000

####################################
## Variables locales flotantes    ##
####################################

# Direccion virtual que representa el actual de variables
# locales flotantes en el contexto, empieza en 11000
var_loc_float = 11000

# Direccion virtual que representa el inicio de las variables
# locales flotantes en el contexto
var_loc_float_inicio = 11000

####################################
## Variables locales booleanas    ##
####################################

# Direccion virtual que representa el actual de variables
# locales booleanas en el contexto, empieza en 13000
var_loc_bool = 13000

# Direccion virtual que representa el inicio de las variables
# locales booleanas en el contexto
var_loc_bool_inicio = 13000

####################################
## Variables locales char         ##
####################################

# Direccion virtual que representa el actual de variables
# locales char en el contexto, empieza en 15000
var_loc_char = 15000

# Direccion virtual que representa el inicio de las variables
# locales char en el contexto
var_loc_char_inicio = 15000

##################################################
## Variables locales temporales enteras         ##
##################################################

# Direccion virtual que representa el actual de temporales
# locales enteras en el contexto, empieza en 17000
var_loc_temp_int = 17000

# Direccion virtual que representa el inicio de las temporales
# locales enteras en el contexto
var_loc_temp_int_inicio = 17000

##################################################
## Variables locales temporales flotantes       ##
##################################################

# Direccion virtual que representa el actual de temporales
# locales float en el contexto, empieza en 17000
var_loc_temp_float = 21000

# Direccion virtual que representa el inicio de las temporales
# locales float en el contexto
var_loc_temp_float_inicio = 21000

##################################################
## Variables locales temporales booleanas       ##
##################################################

# Direccion virtual que representa el actual de temporales
# locales booleanas en el contexto, empieza en 25000
var_loc_temp_bool = 25000

# Direccion virtual que representa el inicio de las temporales
# locales booleanas en el contexto
var_loc_temp_bool_inicio = 25000

##################################################
## Variables locales temporales char            ##
##################################################

# Direccion virtual que representa el actual de temporales
# locales char en el contexto, empieza en 29000
var_loc_temp_char = 29000

# Direccion virtual que representa el inicio de las temporales
# locales char en el contexto
var_loc_temp_char_inicio = 29000

################################
## Constantes enteras         ##
################################

# Direccion virtual que representa el actual de constantes
# globales enteras en el programa, empieza en 33000
cte_int = 33000

# Direccion virtual que representa el inicio de las constantes
# globales enteras en el programa
cte_int_inicio = 33000

################################
## Constantes flotantes       ##
################################

# Direccion virtual que representa el actual de constantes
# globales flotantes en el programa, empieza en 37000
cte_float = 37000

# Direccion virtual que representa el inicio de las constantes
# globales flotantes en el programa
cte_float_inicio = 37000

################################
## Constantes booleanas       ##
################################

# Direccion virtual que representa el actual de constantes
# globales booleanas en el programa, empieza en 41000
cte_bool = 41000

# Direccion virtual que representa el inicio de las constantes
# globales booleanas en el programa
cte_bool_inicio = 41000

################################
## Constantes char            ##
################################

# Direccion virtual que representa el actual de constantes
# globales char en el programa, empieza en 41000
cte_char = 45000

# Direccion virtual que representa el inicio de las constantes
# globales char en el programa
cte_char_inicio = 45000

################################
## Constantes notas           ##
################################

# Direccion virtual que representa el actual de constantes
# globales nota en el programa, empieza en 49000
cte_nota = 49000

# Direccion virtual que representa el inicio de las constantes
# globales nota en el programa
cte_nota_inicio = 49000

# Se utiliza para tener una pila/queue al que se le pueden
# hacer pops y dequeues
from collections import deque

################################
## Procedimientos             ##
################################

# Diccionario de Procedimientos:
## Este diccionario de los procedimientos del programa
## es un diccionario de listas que tiene la siguiente
## organizacion:
## posicion0 = tipo del procedimiento
## posicion1 = diccionario de variables del procedimiento
## posicion2 = direccion cuadruplo inicio del procedimiento
## posicion3 = diccionario del tamano del procedimiento, representado en cada tipo y por variables y constantes
## posicion4 = lista de parametros que tiene el procedimiento
dir_procs = {}

# Diccionario Auxiliar:
## Utilizado para hacer operaciones sobre el diccionario
## de procedimientos sin modificar al mismo
auxDic = {}

# Pila de Scopes:
## Es una pila que representa el scope o funcion en la
## que nos encontramos actualmente en su tope y se van
## empujando a la pila las funciones que estan pendientes
## ya que llamaron a otras funciones y no queremos perderlas
scope = []

# Variable que representa la posicion del tipo en el
# diccionario de procedimientos
pos_dics_tipo = 0

# Variable que representa la posicion de las variables
# en el diccionario de procedimientos
pos_dics_var = 1

# Variable que representa la posicion de la direccion
# de inicio en el diccionario de procedimientos
pos_dics_dir_inicio = 2

# Variable que representa la posicion del tamano
# en el diccionario de procedimientos
pos_dics_tam = 3

# Variable que representa la posicion de los parametros
# en el diccionario de procedimientos
pos_dics_params = 4

################################
## Variables                  ##
################################

# Diccionario de Variables:
## Este diccionario es un diccionario de listas que tiene
## la siguiente organizacion:
## posicion0 = tipo de la variable
## posicion1 = direccion virtual de la variable
## posicion2 = lista de dimensiones de la variable (para variables de tipo lista)
### No esta declarada aqui porque se declara cada vez que se
### manda a crear un nuevo procedimiento y se crea adentro
### de la posicion de variables en el diccionario de procedimientos


# Variable que representa la posicion de las variables
# en el diccionario de variables
pos_vars_tipo = 0

# Variable que representa la posicion de la direccion virtual
# en el diccionario de variables
pos_vars_dir_virtual = 1

# Variable que representa la posicion de las dimensiones
# en el diccionario de variables
pos_vars_dim = 2

################################
## Llamadas a funciones       ##
################################

# Pila de Numero de Funciones:
## Esta pila se utiliza para llevar un registro de a que
## funciones se estan llamando para que cuando se mande
## a llamar una funcion adentro de otra entonces sepa a
## cual registrarle parametros, se utilizan numeros
## ya que puede mandarse a llamar la misma funcion adentro
## de la otra
pilaNumFuncs = []

# Pila auxParamCount:
## Esta pila se utiliza para llevar un registro de en que
## parametro se encuentran las funciones en pilaNumFuncs
## esto se utiliza para cuando se mande a llamar una funcion
## adentro de otra
pilaAuxParamCount = []

# Pila de Funciones:
## Esta pila se utiliza para llevar un registro de a que
## funciones se estan llamando para que cuando se mande
## a llamar una funcion adentro de otra entonces sepa a
## cual registrarle parametros a diferencia de la pilaNumFuncs
## esta es para saber el nombre de la funcion a la que se le
## estan enviando las cosas
pilaFuncs = []

# Pila de Saltos:
## Esta pila/queue se utiliza para llevar un registro de
## los saltos que tiene pendiente por rellenar el programa
## o por asignar mas adelante, se utilizo pila/queue para
## que se puedan sacar por ambos lados
pSaltos = deque([])

# Variable que representa el conteo de funciones que se han
# hecho calls en el programa esto para poder meterlas con su
# numero a la pilaNumFuncs
tempFunc = 0

# Variable que representa el numero de la funcion a la que
# se le esta haciendo call al momento
currentFunc = 0

# Representa la direccion de la funcion en el directorio de
# de procedimientos a la que se le esta haciendo el call
auxFuncDestinoDir = None

################################
## Constantes                 ##
################################

# Diccionario de constantes:
## Aqui se guardan las constantes que se van declarando
## la organizacion es que la llave es el valor de la constante
## y el valor es la direccion virtual para los cuadruplos
ctes = {}

#### Parseo comienza a partir de aqui  ######

###############################################
## programa                                  ##
### Regla inicial para todo el programa      ##
###############################################

def p_programa(p):
    'programa : creadirprocglobal a neur22 c cancion'

    ## Cuando acaba de parsear toda esta regla
    ## que es la regla de todo el programa entonces se
    ## ejecuta lo siguiente

    ## Vaciamos la tabla de variables
    #dir_procs[scope[-1]][pos_dics_var] = {}

    ## Imprimimos para debuggeo
    print('done with file!\n')
    pp.pprint(dir_procs)
    pp.pprint(cuadruplos)
    print pOper
    print pilaO
    print pTipos
    print pSaltos
    pass

#####################################################################
## creadirprocglobal (punto neuralgico)                            ##
### punto nueoralgico para crear el directorio de procedimientos   ##
### de tipo global                                                 ##
#####################################################################

def p_creadirprocglobal(p):
    'creadirprocglobal : '
    ## Creamos el directorio de procedimientos global con las variables vacias
    ## la direccion de inicio en None, el tamano en 0's y con los parametros vacios
    dir_procs['global'] = ['global',{},None,{'vi':0,'vf':0,'vc':0,'vb':0,'ti':0,'tf':0,'tc':0,'tb':0},[]]

    ## Agregamos a los scopes el scope global
    scope.append('global')
    pass

###################################################################
## Regla sintactica a para poder meter ninguna o una variable    ##
## seguida de regla a de nuevo                                   ##
###################################################################
def p_a(p):
    ''' a : empty
          | vars a'''
    pass

###################################################################
## punto neuralgico 22                                           ##
### Utilizado para generar el salto a cancion que representa     ##
### el main del programa                                         ##
###################################################################
def p_neur22(p):
    'neur22 : '
    ## Traer la global de cantidad de cuadruplos
    global contCuad

    ## Hacer operacion de Goto pero sin saber aun
    ## a donde vamos a brincar
    op = GOTO
    cuadruplos[contCuad] = [op,None,None,None]
    contCuad+=1

    ## Agregamos a pila de saltos lo que hay que rellenar
    pSaltos.append(contCuad-1)
    pass

###################################################################
## Regla sintactica c para poder meter ninguna o una funcion     ##
## y mandar a llamar a la regla c de nuevo                       ##
###################################################################
def p_c(p):
    '''c : empty
         | funcion c'''
    pass

###################################################################
## vars                                                          ##
### Utilizada para declarar variables en cualquier funcion       ##
### o globalmente                                                ##
###################################################################
def p_vars(p):
    'vars : VAR ID ":" tipo u ";"'

    ## Una vez que se termina la declaracion de la variable ##

    ## Nos traemos todas las variables globales que usaremos
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

    ## Utilizamos el diccionario auxiliar
    auxDic = dir_procs[scope[-1]][pos_dics_var]

    ## Validamos que la variable exista
    if p[2] in auxDic:
        ## si exite salimos
        print "Variable con ese ID ya existe en ese scope"
        exit()
    else:
        ## Sino checamos si es dimensionada
        if p[5] == "NA":
            ## utilizamos una variable que nos ayuda con la
            ## dimension y la declaramos en 0
            dim = 1
        ## Si la dimension sale <= 0 hay un error
        elif p[5] <= 0:
            print "Dimension no valida"
            exit()
        ## Sino asignamos la dimension que nos mandaron
        else:
            dim = p[5]
        ## Si no hay dimension
        if dim == 1:
            ## Creamos el diccionario de la variable
            ## con solamente el tipo, dimension en None
            auxDic[p[2]] = [p[4],None,None]
        else:
            ## Creamos el diccionario de la variable con
            ## el tipo, y el arreglo de la dimension (dim sup, dim inf)
            auxDic[p[2]] = [p[4],None,[dim-1,0]]
        ## Si el tipo es INT
        if p[4] == INT:
            ## Aumenta la cantidad de variables enteras en la cantidad de dim
            dir_procs[scope[-1]][pos_dics_tam]['vi']+=dim
            ## Si es global el scope
            if scope[-1] == 'global':
                ## Checa si junto con la dimension caben en las direcciones virtuales
                if var_glob_int + dim < var_glob_float_inicio:
                    ## Si cabe, agrega a su diccionario de variable su direccion virtual
                    auxDic[p[2]][pos_vars_dir_virtual] = var_glob_int
                    ## Aumenta la cantidad en dim de variables globales enteras
                    var_glob_int += dim
                ## Si no cabe, hay overflow y salimos
                else:
                    print "Overflow de variables enteras globales"
                    exit()
            ## si no es global entonces es local
            else:
                ## Checa si junto con la dimension caben en las direcciones virtuales
                if var_loc_int + dim < var_loc_float_inicio:
                    ## Si cabe, agrega a su diccionario de variable su direccion virtual
                    auxDic[p[2]][pos_vars_dir_virtual] = var_loc_int
                    ## Aumenta la cantidad en dim de variables locales enteras
                    var_loc_int += dim
                ## Si no cabe, hay overflow y salimos
                else:
                    print "Overflow de variables enteras locales"
                    exit()
        ## Si el tipo es FLOAT
        elif p[4] == FLOAT:
            ## Aumenta la cantidad de variables flotantes en la cantidad de dim
            dir_procs[scope[-1]][pos_dics_tam]['vf']+=dim
            ## Si es global el scope
            if scope[-1] == 'global':
                ## Checa si junto con la dimension caben en las direcciones virtuales
                if var_glob_float + dim < var_glob_bool_inicio:
                    ## Si cabe, agrega a su diccionario de variable su direccion virtual
                    auxDic[p[2]][pos_vars_dir_virtual] = var_glob_float
                    ## Aumenta la cantidad en dim de variables globales flotantes
                    var_glob_float += dim
                ## Si no cabe, hay overflow y salimos
                else:
                    print "Overflow de variables flotantes globales"
                    exit()
            ## si no es global entonces es local
            else:
                ## Checa si junto con la dimension caben en las direcciones virtuales
                if var_loc_float + dim < var_loc_bool_inicio:
                    ## Si cabe, agrega a su diccionario de variable su direccion virtual
                    auxDic[p[2]][pos_vars_dir_virtual] = var_loc_float
                    ## Aumenta la cantidad en dim de variables locales flotantes
                    var_loc_float += dim
                ## Si no cabe, hay overflow y salimos
                else:
                    print "Overflow de variables flotantes locales"
                    exit()
        ## Si el tipo es CHAR
        elif p[4] == CHAR:
            ## Aumenta la cantidad de variables flotantes en la cantidad de dim
            dir_procs[scope[-1]][pos_dics_tam]['vc']+=dim
            ## Si es global el scope
            if scope[-1] == 'global':
                ## Checa si junto con la dimension caben en las direcciones virtuales
                if var_glob_char + dim < var_loc_int_inicio:
                    ## Si cabe, agrega a su diccionario de variable su direccion virtual
                    auxDic[p[2]][pos_vars_dir_virtual] = var_glob_char
                    ## Aumenta la cantidad en dim de variables globales char
                    var_glob_char += dim
                ## Si no cabe, hay overflow y salimos
                else:
                    print "Overflow de variables char globales"
                    exit()
            ## si no es global entonces es local
            else:
                ## Checa si junto con la dimension caben en las direcciones virtuales
                if var_loc_char + dim < var_loc_temp_int_inicio:
                    ## Si cabe, agrega a su diccionario de variable su direccion virtual
                    auxDic[p[2]][pos_vars_dir_virtual] = var_loc_char
                    ## Aumenta la cantidad en dim de variables locales char
                    var_loc_char += dim
                ## Si no cabe, hay overflow y salimos
                else:
                    print "Overflow de variables char locales"
                    exit()
        ## Si el tipo es BOOL
        else:
            ## Aumenta la cantidad de variables booleanas en la cantidad de dim
            dir_procs[scope[-1]][pos_dics_tam]['vb']+=dim
            ## Si es global el scope
            if scope[-1] == 'global':
                ## Checa si junto con la dimension caben en las direcciones virtuales
                if var_glob_bool + dim < var_glob_char_inicio:
                    ## Si cabe, agrega a su diccionario de variable su direccion virtual
                    auxDic[p[2]][pos_vars_dir_virtual] = var_glob_bool
                    ## Aumenta la cantidad en dim de variables globales booleanas
                    var_glob_bool += dim
                ## Si no cabe, hay overflow y salimos
                else:
                    print "Overflow de variables booleanas globales"
                    exit()
            ## si no es global entonces es local
            else:
                ## Checa si junto con la dimension caben en las direcciones virtuales
                if var_loc_bool + dim < var_loc_char_inicio:
                    ## Si cabe, agrega a su diccionario de variable su direccion virtual
                    auxDic[p[2]][pos_vars_dir_virtual] = var_loc_bool
                    ## Aumenta la cantidad en dim de variables locales booleanas
                    var_loc_bool += dim
                ## Si no cabe, hay overflow y salimos
                else:
                    print "Overflow de variables booleanas locales"
                    exit()
    pass

########################################################################
## funcion                                                            ##
### Utilizada para declarar cualquier funcion                         ##
########################################################################

def p_funcion(p):
    'funcion : FUNC z ID meterfuncion "(" params ")" f neur23 bloque'

    ## Una vez que se termina la declaracion de la funcion ##

    ## Nos traemos todas las variables globales que usaremos
    global contCuad
    global pos_dics_tipo
    global pos_dics_var

    ## Si no es global o no es una funcion void, tenemos un error
    if (not(scope[-1] in dir_procs["global"][pos_dics_var]) and (dir_procs[scope[-1]][pos_dics_tipo] != None)):
        ## Falto poner el return
        print "Falta regresar parametro de salida en funcion"
        exit()
    ## Borramos la tabla de variables de la funcion
    #dir_procs[scope[-1]][pos_dics_var] = {}

    ## Reiniciamos los valores de nuestros contadores de
    ## variables locales y temporales locales
    var_loc_int = var_loc_int_inicio
    var_loc_float = var_loc_float_inicio
    var_loc_bool = var_loc_bool_inicio
    var_loc_char = var_loc_char_inicio
    var_loc_temp_int = var_loc_temp_int_inicio
    var_loc_temp_float = var_loc_temp_float_inicio
    var_loc_temp_bool = var_loc_temp_bool_inicio
    var_loc_temp_char = var_loc_temp_char_inicio

    ## Sacamos el scope actual
    scope.pop()

    ## Terminamos el procedimiento con un cuadruplo
    op = ENDPROC
    cuadruplos[contCuad]=[op,None,None,None]
    contCuad += 1
    pass

###################################################################
## Regla sintactica z para poder acabar el definir el tipo de    ##
## variables, funciones o parametros                             ##
###################################################################
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

###################################################################
## meterfuncion (punto neuralgico)                               ##
### utilizado para preparar la semantica necesaria al momento    ##
### de ingresar una funcion al momento de la compilacion cuando  ##
### detecta su declaracion                                       ##
###################################################################
def p_meterfuncion(p):
    'meterfuncion : '

    ## Nos traemos las variables necesarias
    global var_loc_int
    global var_loc_float
    global var_loc_bool
    global var_loc_char
    global var_loc_temp_int
    global var_loc_temp_float
    global var_loc_temp_bool
    global var_loc_temp_char

    ## Revisamos que no exista una funcion con ese nombre
    if p[-1] in dir_procs:
        print "Funcion con ese ID ya existe en el programa"
        exit()
    else:
        ## Inicializamos todas las variables y temporales en
        ## las iniciales porque arranca una nueva funcion
        var_loc_int = var_loc_int_inicio
        var_loc_float = var_loc_float_inicio
        var_loc_bool = var_loc_bool_inicio
        var_loc_char = var_loc_char_inicio
        var_loc_temp_int = var_loc_temp_int_inicio
        var_loc_temp_float = var_loc_temp_float_inicio
        var_loc_temp_bool = var_loc_temp_bool_inicio
        var_loc_temp_char = var_loc_temp_char_inicio

        ## Lo damos de alta en el directorio de procedimientos con su tipo,
        ## vars vacias, direccion virtual inicial, tamano en ceros y params
        ## vacios
        dir_procs[p[-1]] = [p[-2],{},None,{'vi':0,'vf':0,'vc':0,'vb':0,'ti':0,'tf':0,'tc':0,'tb':0},[]]

        ## Agregamos el nuevo scope como el actual
        scope.append(p[-1])
    pass

#########################################################################
## punto neuralgico 23                                                 ##
### utilizado para ingresar el cuadruplo inicial de las instrucciones  ##
### de la funcion, se utiliza para saber su dir virtual                ##
#########################################################################
def p_neur23(p):
    'neur23 : '
    ## nos traemos las variables necesarias
    global dir_procs
    global contCuad

    ## rellenamos el directorio de procedimiento actual con el cuadruplo
    ## actual para definir su direccion virtual de inicio
    dir_procs[scope[-1]][pos_dics_dir_inicio] = contCuad
    pass

###################################################################
## Regla sintactica f para poder meter ninguna o una variable    ##
## y mandar a llamar a la regla g                                ##
###################################################################
def p_f(p):
    '''f : empty
         | vars f'''
    pass

##################################################################
## params                                                       ##
### utilizado para declarar los parametros en las funciones     ##
##################################################################
def p_params(p):
    '''params : empty
              | tipo ID meterparams h'''
    pass

##################################################################
## meterparams  (punto neuralgico)                              ##
### utilizado para meter cada parametro declarado en la funcion ##
### se toma en cuenta su tipo y que no se llame igual que una   ##
### variable local                                              ##
##################################################################
def p_meterparams(p):
    'meterparams : '

    ## nos traemos las variables necesarias
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

    ## usamos el diccionario auxiliar para que apunte al
    ## directorio de variables del scope
    auxDic = dir_procs[scope[-1]][pos_dics_var]

    ## si ya existe un parametro o variable con ese id
    ## se marca error
    if p[-1] in auxDic:
        print "Parametro con ese ID ya existe en ese scope"
        exit()
    else:
        ## lo agregamos como variable nueva con su tipo declarado
        auxDic[p[-1]] = [p[-2],None,None]
        ## al igual lo agregamos a los parametros necesarios
        ## para ejecutar la funcion, esto es para la validacion
        ## semantica
        dir_procs[scope[-1]][pos_dics_params].append(p[-2])

        ## Checamos el tipo y al encontrarlo lo agregamos a ese
        ## tipo de variable local, siempre y cuando quepa dentro
        ## de los limites para que no haya overflow
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


###################################################################
## Regla sintactica h para poder acabar el ciclo de params o     ##
## volver a mandar a params                                      ##
###################################################################
def p_h(p):
    '''h : empty
         | "," params'''
    pass

###################################################################
## Regla sintactica i para poder meter ninguno o un estatuto     ##
## seguida de la regla i de nuevo                                ##
###################################################################
def p_i(p):
    '''i : empty
         | estatuto i'''
    pass

##################################################################
## bloque                                                       ##
### utilizado para hacer bloques de estatutos mandando a llamar ##
### el ciclo de los mismos con la regla i                       ##
##################################################################

def p_bloque(p):
    'bloque : "{" i "}"'
    pass

# estructura de dir_proc = ['CANCION',vars{},tempo]

##################################################################
## cancion                                                      ##
### regla utilizada para declarar la funcion "main" del         ##
### programa y se trata de una funcion que no recibe parametros ##
### pero si se declara un tempo al que tocara la melodia        ##
##################################################################
def p_cancion(p):
    'cancion : CANCION "(" CTEE ")" metercancion f bloque'
    ## vaciamos el diccionario de variables
    #dir_procs[scope[-1]][pos_dics_var] = {}

    ## sacamos el scope de la pila
    scope.pop()
    pass

#################################################################
## metercancion (punto neuralgico)                             ##
### utilizado para meter la semantica de la cancion creando    ##
### sus variables y su registro en el directorio de            ##
### procedimientos y se rellena el salto inicial del programa  ##
#################################################################

def p_metercancion(p):
    'metercancion : '

    ## nos traemos las variables necesarias
    global contCuad
    global var_loc_int
    global var_loc_float
    global var_loc_bool
    global var_loc_char
    global var_loc_temp_int
    global var_loc_temp_float
    global var_loc_temp_bool
    global var_loc_temp_char

    ## agregamos el scope acual de cancion
    scope.append(p[-4])

    ## inicializamos las variables con los valores de inicio
    var_loc_int = var_loc_int_inicio
    var_loc_float = var_loc_float_inicio
    var_loc_bool = var_loc_bool_inicio
    var_loc_char = var_loc_char_inicio
    var_loc_temp_int = var_loc_temp_int_inicio
    var_loc_temp_float = var_loc_temp_float_inicio
    var_loc_temp_bool = var_loc_temp_bool_inicio
    var_loc_temp_char = var_loc_temp_char_inicio

    ## creamos la entrada al directorio de procedimientos de cancion
    ## donde tiene el tipo, las variables en vacio, none para direccion
    ## de inicio del procedimiento, en 0's la cantidad de variables y temporales,
    ## las variables en vacio y al final lleva el tempo que se manda a la funcion
    dir_procs[p[-4]] = [p[-4],{},None,{'vi':0,'vf':0,'vc':0,'vb':0,'ti':0,'tf':0,'tc':0,'tb':0},[],p[-2]] #cancion tiene tempo como parametro extra en su lista

    ## se rellena con el salto inicial el cuadruplo de goto pendiente
    saltoInicial = pSaltos.pop()
    cuadruplos[saltoInicial][3] = contCuad
    pass

######################################################################
## estatuto                                                         ##
### regla que se utiliza para seleccionar el estatuto a desarrollar ##
######################################################################
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

######################################################################
## asignacion                                                       ##
### estatuto de menor jerarquia en las operaciones aritmeticas,     ##
### se utiliza para asignar un valor a una variable de lo que sale  ##
### de una expresion                                                ##
######################################################################
def p_asignacion(p):
    'asignacion : ID asiglista "=" neur8  expresion ";"'
    ## nos traemos las variables necesarias
    global contCuad
    global dir_procs
    global scope

    ## revisamos si el operando pendiente es el de asignacion
    if pOper[-1] == EQ:
        ## sacamos lo necesario de las pilas para el cuadruplo
        op = pOper.pop()
        opdoIzq = pilaO.pop()
        tipoIzq = pTipos.pop()
        igualdad = pilaO.pop()
        tipoIgualdad = pTipos.pop()
        ## revisamos los tipos en el cubo semantico
        if tipoIzq in cubo_semantico[tipoIgualdad] and op in cubo_semantico[tipoIgualdad][tipoIzq]:
            tipoRes = cubo_semantico[tipoIgualdad][tipoIzq][op]
        ## revisamos los tipos en el cubo semantico inversamente tambien
        else:
            tipoRes = cubo_semantico[tipoIzq][tipoIgualdad][op]
        ## si el tipo resultante en el cubo semantico no es error
        if tipoRes != ERR :
            ## genera el cuadruplo
            cuadruplos[contCuad] = [op,opdoIzq,None,igualdad]
            contCuad+=1
        else:
            print("Type mismatch")
            exit()
    ## si nos quedamos con operaciones pendientes es una asignacion mal terminada
    else:
        print("Asignacion mal terminada")
        exit()
    pass

#######################################################################
## punto neuralgico 8                                                ##
### usado para validar que la variable de asignacion existe          ##
### y la agregamos a la pilaO y la pila de tipos y agregamos         ##
### el operando tambien                                              ##
#######################################################################
def p_neur8(p):
    'neur8 : '
    ## utilizamos el diccionario adicional para apuntar a las variables
    auxDic = dir_procs[scope[-1]][pos_dics_var]
    ## si no es una lista lo que estamos agregando
    if p[-2] == -1:
        ## revisamos si existe una variable con ese id
        if p[-3] in auxDic:
            ## lo agregamos a la pilaO y a la pila de tipos
            pilaO.append(auxDic[p[-3]][pos_vars_dir_virtual])
            pTipos.append(auxDic[p[-3]][0])
        ## si no existe es un error
        else:
            print "No existe tal variable a asignar"
            exit()
    ## agregamos la operacion a la pOper tambien
    pOper.append(EQ)
    pass


#############################################################################
## asiglista                                                               ##
### utilizado para revisar si se quiere asignar un elemento                ##
### de tipo lista o no, si es empty entonces se regresa -1,                ##
### sino pues se regresa 1 y se realizan distintas acciones semanticas     ##
### en la asignacion                                                       ##
#############################################################################
def p_asiglista(p):
    '''asiglista : empty
                 | accesoVarDim'''

    ## en caso de que no haya asignacion de lista
    ## regresamos -1
    if p[1] == None:
        p[0] = -1
    ## en caso de que si haya regresamos 1 y nos
    ## vamos a la regla accesoVarDim
    else:
        p[0] = 1
    pass

##################################################################
## if                                                           ##
### regla responsable de encargarse del estatuto if en el que   ##
### se especifica la sintaxis del mismo estatuto y manda a      ##
### llamar las reglas correspondientes para hacer un estatuto   ##
### de control logico                                           ##
##################################################################
def p_if(p):
    'if : IF "(" expresion ")" neur13 bloque l ";" neur15'
    pass

##################################################################
## punto neuralgico 13                                          ##
### utilizado para meter las acciones correspondientes de los   ##
### brincos por el estatuto logico en caso de que sea falso     ##
### todo dependiendo del resultado de la expresion del estatuto ##
### de control                                                  ##
##################################################################

def p_neur13(p):
    'neur13 : '
    ## nos traemos las variables necesarias
    global contCuad

    ## checamos si la expresion nos dejo un tipo bool al final
    if pTipos[-1] == BOOL:
        ## sacamos de la pila de tipos, agarramos el opdoIzq
        ## que es el resultdado de la expresion anterior que esta
        ## en la pilaO
        pTipos.pop()
        opdoIzq = pilaO.pop()
        ## hacemos un goto en falso pero en el que ponemos el
        ## resultado de la expresion como lo que se va a evaluar
        ## todavia sin saber a donde brincaremos
        op = GOTOF
        cuadruplos[contCuad] = [op,opdoIzq,None,None]
        contCuad+=1
        ## agregamos a la pila de saltos el cuadruplo del GOTOF
        ## para saber a donde brincar en caso de ser falso
        pSaltos.append(contCuad-1)
    ## si el resultado de la expresion no es un booleano hay error
    else:
        print ("Tiene que tener un booleano como resultado de expresion")
        exit()
    pass

###################################################################
## Regla sintactica l para poder meter la opcion del else en un  ##
## if o que se quede el if sin else                              ##
###################################################################
def p_l(p):
    '''l : empty
         | ELSE neur14 bloque'''
    pass

##################################################################
## punto neuralgico 14                                          ##
### utilizado para hacer un salto en caso de que haya else      ##
### se utiliza porque si hay un else y entro al verdadero se    ##
### tiene que saltar las instrucciones del else y al igual es   ##
### el brinco que se hace para el GOTOF del if                  ##
##################################################################
def p_neur14(p):
    'neur14 : '
    ## nos traemos las variables necesarias
    global contCuad
    ## hacemos la operacion del goto y sacamos
    ## el brinco en falso que traiamos del if en la pila
    ## de saltos
    op = GOTO
    falso = pSaltos.pop()
    ## generamos el cuadruplo de goto pero sin saber a donde
    ## brincaremos porque no sabemos cuando se acaba el else
    cuadruplos[contCuad] = [op,None,None,None]
    contCuad += 1
    ## agregamos a la pila de saltos el brinco del else que
    ## esta pendiente por resolverse
    pSaltos.append(contCuad-1)
    ## rellenamos el cuadruplo del GOTOF que traia el if
    ## ya que ya sabemos a donde va a brincar, justo despues
    ## del GOTO generado por el else para que sepa
    ## que si es falso va directo al bloque del else
    cuadruplos[falso][3] = contCuad
    pass

########################################################################
## punto neuralgico 15                                                ##
### utilizado para cerrar el estatuto del if y generar                ##
### las acciones correspondientes semanticas, aqui lo importante      ##
### es que la pila de saltos ya se trabajo bien en los otros          ##
### puntos del if ya que no importa si fue if else o if solo          ##
########################################################################
def p_neur15(p):
    'neur15 : '
    ## nos traemos las variables que necesitamos
    global contCuad
    ## sacamos de la pila de salto el pendiente del GOTO del
    ## else o el pendiente del GOTOF si es un if sin else
    falso = pSaltos.pop()
    ## rellenamos el cuadruplo correspondiente con el numero
    ## de cuadruplo actual
    cuadruplos[falso][3] = contCuad
    pass

######################################################################
## for                                                              ##
### estatuto ciclico en el que se hace una asignacion una sola      ##
### vez seguido de una expresion que siempre se evalua en cada      ##
### pasada del ciclo y finalmente se hace una asignacion cada       ##
### vez que se vuelve termina de ejecutar el ciclo                  ##
######################################################################
def p_for(p):
    'for : FOR "(" asignacion neur18 expresion ";" neur19 asignacion ")" neur21 bloque ";" neur20'
    pass

######################################################################
## punto neuralgico 18                                              ##
### utilizado por el for para agregar a la pila de saltos           ##
### el punto inicial antes de la expresion que se evalua cada       ##
### vez que se ejecuta de nuevo el ciclo                            ##
######################################################################
def p_neur18(p):
    'neur18 : '
    ## nos traemos las variables necesarias
    global contCuad
    ## agregamos a la pila de saltos el cuadruplo siguiente
    ## para que sepamos a donde brincar al comienzo del ciclo
    pSaltos.append(contCuad)
    pass

######################################################################
## punto neuralgico 19                                              ##
### utilizado por el for para revisar que la expresion sea de       ##
### tipo booleana y agregamos los brincos correspondientes en falso ##
### y verdadero de acuerdo al resultado de la misma ya que siempre  ##
### se debe dejar la segunda asignacion hasta el final del for      ##
######################################################################
def p_neur19(p):
    'neur19 : '
    ## nos traemos las variable necesarias
    global contCuad
    ## checamos que el tipo de la expresion sea BOOL
    if pTipos[-1] == BOOL:
        ## lo sacamos de la pila de tipos
        pTipos.pop()
        ## sacamos el opdoIzq que vendria a ser el resultado
        ## de la expresion para hacer los brincos en GOTOV y GOTOF
        opdoIzq = pilaO.pop()
        ## armamos el GOTOV todavia sin destino porque no sabemos
        ## aun en que punto arranca el bloque del for
        op = GOTOV
        cuadruplos[contCuad] = [op,opdoIzq,None,None]
        contCuad+=1
        ## agregamos a la pila de saltos el numero de cuadruplo
        ## del GOTOV que va a rellenar mas adelante cuando se encuentre
        ## el bloque del for
        pSaltos.append(contCuad-1)
        ## armamos el GOTOF todavia sin destino porque no sabemos
        ## aun en que punto termina el for
        op = GOTOF
        cuadruplos[contCuad] = [op,opdoIzq,None,None]
        contCuad+=1
        ## agregamos a la pila de saltos el numero de cuadruplo
        ## del GOTOF que va a rellenar mas adelante cuando se acabe
        ## el bloque del for
        pSaltos.append(contCuad-1)
        ## agregamos a la pila de saltos el siguiente cuadruplo que
        ## realiza la segunda asignacion del for y como se hace hasta el final
        ## este se va con un GOTO al final del bloque del for
        pSaltos.append(contCuad)
    ## si el resultado de la expresion no es bool hay un error
    else:
        print ("Tiene que tener un booleano como resultado de expresion")
        exit()
    pass


##################################################################
## punto neuralgico 21                                          ##
### se utiliza para hacer el salto despues de la segunda        ##
### asignacion ya que despues de ahi vuelve a evaluarse         ##
### la expresion anteriormente en el for y se usa para saber    ##
### que ya comienza el bloque entonces el salto del GOTOV       ##
### se rellena                                                  ##
##################################################################
def p_neur21(p):
    'neur21 : '
    ## nos traemos las variables necesarias
    global contCuad
    ## marcamos la operacion del GOTO
    op = GOTO
    ## utilizamos una pila auxiliar ya que el salto antes de la
    ## expresion no esta en el tope y se tiene que buscar
    auxPila = []
    ## se encuentra dos niveles anidado el salto en la pila
    i = 0
    while i < 3:
        ## se transfieren de los saltos a la auxiliar
        ## se utiliza una pila para respetar el orden que se tenia
        ## en la pila
        auxPila.append(pSaltos.pop())
        i += 1
        pass
    ## ya cuando llegamos al salto que queremos lo sacamos
    ## y ya hacemos la operacion del GOTO que nos permitira
    ## volver a comenzar el ciclo
    ciclo = pSaltos.pop()
    cuadruplos[contCuad] = [op,None,None,ciclo]
    contCuad+=1
    ## ahora se encuentra en la pila auxiliar el GOTOV de
    ## la expresion y como ya viene el bloque lo sacamos y
    ## rellenamos el GOTOV con el cuadruplo que viene
    verdadero = auxPila.pop()
    cuadruplos[verdadero][3] = contCuad
    ## restablecemos la pila de saltos para que sigan el
    ## GOTOF y el punto para el brinco a la segunda asignacion
    pSaltos.append(auxPila.pop())
    pSaltos.append(auxPila.pop())
    pass

##############################################################
## punto neuralgico 20                                      ##
### se utiliza para marcar el fin de la declaracion del     ##
### for y se utiliza para hacer el brinco a la segunda      ##
### asignacion y rellenar el GOTOF de la expresion          ##
##############################################################
def p_neur20(p):
    'neur20 : '
    ## nos traemos las variables necesarias
    global contCuad
    ## generamos la accion del GOTO que sera el
    ## salto a la segunda asignacion al final del for
    op = GOTO
    asigna = pSaltos.pop()
    cuadruplos[contCuad] = [op,None,None,asigna]
    contCuad+=1
    ## sacamos el numero de cuadruplo para el GOTOF
    ## de la expresion y lo rellenamos con el siguiente
    ## cuadruplo porque ahi ya termino el for
    falso = pSaltos.pop()
    cuadruplos[falso][3] = contCuad
    pass


##########################################################
## expresion                                            ##
### regla sintactica que se utiliza para hacer el NOT   ##
### a toda una expresion y marca la menor prioridad en  ##
### las expresiones, se hace hasta el final             ##
##########################################################
def p_expresion(p):
    'expresion : m subexpresion'
    ## nos traemos las variables necesarias
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
    ## checamos que la pila de operaciones no este vacia
    if pOper:
        ## checamos que el tope de la pila de operaciones
        ## sea un NOT
        if pOper[-1] == NOT:
            ## hacemos la operacion del NOT que solo usa un
            ## operando izquierdo y se guarda el resultado
            op = pOper.pop()
            opdoIzq = pilaO.pop()
            tipoIzq = pTipos.pop()
            ## checamos que no sea error el tipo resultante
            ## con el cubo semantico y realizamos el alta de
            ## la temporal local y su direccion virtual para
            ## la operacion y la agregamos a la pilaO y a la pTipos
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
            ## si el cubo semantico no acepta esa operacion con los tipos
            ## marca error de tipos
            else:
                print("Type mismatch")
                exit()
    pass

####################################################################
## Regla sintactica m para poder agregar ninguno, uno o mas NOT's ##
####################################################################
def p_m(p):
    '''m : empty
         | NOT m'''
    if p[1] == "NOT":
        pOper.append(NOT)
    pass

##################################################################
## subexpresion                                                 ##
### siguiente nivel en la jerarquia de expresiones que se       ##
### utilia para las operaciones de AND's y OR's                 ##
##################################################################
def p_subexpresion(p):
    'subexpresion : exp neur10 o'
    pass

##################################################################
## punto neuralgico 10                                          ##
### utilizado para evaluar los AND's y OR's pendientes y        ##
### agregar el resultado a la pilaO y a la pTipos el tipo       ##
##################################################################
def p_neur10(p):
    'neur10 : '
    ## nos traemos las variables necesarias
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
    ## si la pila de operandos no esta vacia
    if pOper:
        ## revisa si el tope es un AND o un OR
        if pOper[-1] == AND or pOper[-1] == OR:
            ## preparamos el and u or con sus operandos izquierdo
            ## y derecho correspondientes
            op = pOper.pop()
            opdoDer = pilaO.pop()
            tipoDer = pTipos.pop()
            opdoIzq = pilaO.pop()
            tipoIzq = pTipos.pop()
            ## checamos si los tipos no marcan error en el cubo semantico y lo
            ## hacemos inverso por si el cubo lo tiene al reves (derecho y luego izquierdo)
            if tipoDer in cubo_semantico[tipoIzq] and op in cubo_semantico[tipoIzq][tipoDer]:
                tipoRes = cubo_semantico[tipoIzq][tipoDer][op]
            else:
                tipoRes = cubo_semantico[tipoDer][tipoIzq][op]
            if tipoRes != ERR :
                ## si no fue error asignamos la temporal correspondiente al cuadruplo
                ## y agregamos a pilaO y pTipos
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
            ## si el cubo marca error en los operandos entonces marcamos
            ## error de tipos
            else:
                print("Type mismatch")
                exit()
    pass

###################################################################
## Regla sintactica o para poder meter el AND y el OR            ##
## seguido de la subexpresion otra vez o acabar con el ciclo de  ##
## ands y ors                                                    ##
###################################################################
def p_o(p):
    '''o : empty
         | AND neur9_1 subexpresion
         | OR neur9_2 subexpresion'''
    pass

##################################################################
## puntos neuralgico 9_1 y 9_2                                  ##
### se utiliza para agregar la operacion AND u OR a la pOper    ##
##################################################################
def p_neur9_1(p):
    'neur9_1 : '
    pOper.append(AND)
    pass

def p_neur9_2(p):
    'neur9_2 : '
    pOper.append(OR)
    pass


##################################################################
## exp                                                          ##
### se utiliza para el siguiente nivel de jerarquia en          ##
### expresiones que corresponde a las comparaciones(==,>,       ##
### >=,<=,!=)                                                   ##
##################################################################
def p_exp(p):
    'exp : nexp p neur12'
    pass

##################################################################
## punto neuralgico 12                                          ##
### se utiliza para evaluar las comparaciones y poner el        ##
### resultado en la pilaO y pTipos al igual hacer el cuadruplo  ##
##################################################################
def p_neur12(p):
    'neur12 : '
    ## nos traemos las variables necesarias
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
    ## si la pila de operaciones no esta vacia
    if pOper:
        ## revisamos si la operacione es alguna de las de comparacion
        if pOper[-1] == EQEQ or pOper[-1] == NOTEQ or pOper[-1] == GT or pOper[-1] == LT or pOper[-1] == GTE or pOper[-1] == LTE:
            ## armar la operacion con sus operando izquierdo y derecho
            op = pOper.pop()
            opdoDer = pilaO.pop()
            tipoDer = pTipos.pop()
            opdoIzq = pilaO.pop()
            tipoIzq = pTipos.pop()
            ## ver el resultado de los tipos en el cubo semantico e inverso tambien
            if tipoDer in cubo_semantico[tipoIzq] and op in cubo_semantico[tipoIzq][tipoDer]:
                tipoRes = cubo_semantico[tipoIzq][tipoDer][op]
            else:
                tipoRes = cubo_semantico[tipoDer][tipoIzq][op]
            ## si no es un error entonces damos de alta el temporal correspondiente
            ## armamos el cuadruplo y agregamos a la pilaO y a a pTipos
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
            ## si el cubo marco error entonces tenemos un error
            ## de tipos
            else:
                print("Type mismatch")
                exit()
    pass

####################################################################
## Regla sintactica p para poder agregar ninguno o uno de las     ##
## operaciones de comparacion seguido de una expresion de mas     ##
## alta jerarquia                                                 ##
####################################################################
def p_p(p):
    '''p : empty
         | EQ neur11_1 nexp
         | NOTEQ neur11_2 nexp
         | ">" neur11_3 nexp
         | "<" neur11_4 nexp
         | MTHANEQ neur11_5 nexp
         | LTHANEQ neur11_6 nexp'''
    pass

##################################################################
## puntos neuralgico 11                                         ##
### se utiliza para agregar la operacion correspondiente        ##
### de comparacion (==,>,>=,<=,<,!=)                            ##
##################################################################
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

##############################################################
## nexp                                                     ##
### siguiente nivel en la jerarquia de expresiones en el    ##
### que se pueden hacer sumas y restas                      ##
##############################################################
def p_nexp(p):
    'nexp : termino neur5 q'
    pass

#############################################################
## punto neuralgico 5                                      ##
### se utiliza para hacer la operacion de suma o resta y   ##
### agregar el resultado a la pilaO y a la pTipos          ##
#############################################################
def p_neur5(p):
    'neur5 : '
    ## nos traemos las variables necesarias
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
    ## si la pila de operandos no esta vacia
    if pOper:
        ## revisamos si el tipo de la pila es una suma o resta
        if pOper[-1] == PLUS or pOper[-1]== MINUS :
            ## armamos la operacion con sus operandos derecho e izquierdo
            ## y los tipos para la validacion
            op = pOper.pop()
            opdoDer = pilaO.pop()
            tipoDer = pTipos.pop()
            opdoIzq = pilaO.pop()
            tipoIzq = pTipos.pop()
            ## revisamos el tipo resultante de la operacion e inverso
            if tipoDer in cubo_semantico[tipoIzq] and op in cubo_semantico[tipoIzq][tipoDer]:
                tipoRes = cubo_semantico[tipoIzq][tipoDer][op]
            else:
                tipoRes = cubo_semantico[tipoDer][tipoIzq][op]
            ## si el resultado no es un error entonces creamos la temporal
            ## correspondiente y su tipo todo agregando a la pilaO, pTipos y
            ## en el cuadruplo
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
            ## si el tipo nos marca error entonces marcamos error de tipos
            else:
                print("Type mismatch")
                exit()
    pass

######################################################################
## Regla sintactica q para poder agregar suma o resta seguido de    ##
## otro nexp para que puedan encadenar muchas operaciones de ese    ##
## tipo                                                             ##
######################################################################
def p_q(p):
    '''q : empty
         | "+" neur3_1 nexp
         | "-" neur3_2 nexp'''
    pass

######################################################################
## punto neuralgico 3                                               ##
### se utilizan para agregar la operacion de suma o resta a         ##
### la pOper                                                        ##
######################################################################
def p_neur3_1(p):
    'neur3_1 : '
    pOper.append(PLUS)
    pass

def p_neur3_2(p):
    'neur3_2 : '
    pOper.append(MINUS)
    pass

##################################################################
## termino                                                      ##
### es el siguiente nivel en la jerarquia de las expresiones    ##
### en este se pueden realizar multiplicaciones y divisiones    ##
### y meter el signo negativo                                   ##
##################################################################
def p_termino(p):
    'termino : meteneg factor neur4 n'
    pass

##################################################################
## punto neuralgico 4                                           ##
### utilizado para realizar la operacion de multiplicacion      ##
### o division del termino y agregando el resultado a la        ##
### pilaO y el tipo a la pTipos                                 ##
##################################################################
def p_neur4(p):
    'neur4 : '
    ## agregamos las variables necesarias
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

    ## si la pila de operaciones no esta vacia
    if pOper:
        ## revisamos si el tope es multiplicacion o division
        if pOper[-1] == MULT or pOper[-1]== DIV :
            ## armamos la operacion con sus operandos derecho e izquierdo y sus tipos
            op = pOper.pop()
            opdoDer = pilaO.pop()
            tipoDer = pTipos.pop()
            opdoIzq = pilaO.pop()
            tipoIzq = pTipos.pop()
            ## revisamos el tipo resultante en el cubo semantico y en busqueda inversa tambien
            if tipoDer in cubo_semantico[tipoIzq] and op in cubo_semantico[tipoIzq][tipoDer]:
                tipoRes = cubo_semantico[tipoIzq][tipoDer][op]
            else:
                tipoRes = cubo_semantico[tipoDer][tipoIzq][op]
            ## si el tipo resultante no es error entonces creamos el temporal correspondiente
            ## con su tipo, armamos el cuadruplo y agregamos a pilaO y a pTipos el tipo
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
            ## si el tipo resultante es error entonces marcamos error de tipos
            else:
                print("Type mismatch")
                exit()
    pass

######################################################################
## Regla sintactica n para poder agregar multiplicacion o division  ##
## seguido de otro termino para que puedan encadenar muchas         ##
## operaciones de ese tipo                                          ##
######################################################################
def p_n(p):
    '''n : empty
         | "*" neur2_1 termino
         | "/" neur2_2 termino'''
    pass

######################################################################
## punto neuralgico 2                                               ##
### se utiliza para agregar la operacion a la pOper de              ##
### multiplicacion o division segun sea el token leido              ##
######################################################################
def p_neur2_1(p):
    'neur2_1 : '
    pOper.append(MULT)
    pass

def p_neur2_2(p):
    'neur2_2 : '
    pOper.append(DIV)
    pass

######################################################################
## factor                                                           ##
### nivel mas alto en la jerarquia de expresiones en el que se      ##
### pueden utilizar parentesis y meter otra expresion para          ##
### poner esa expresion en mayor prioridad o asi bien meter         ##
### constantes o variables                                          ##
######################################################################
def p_factor(p):
    '''factor : "(" neur6 expresion ")" neur7
              | varcte'''

    ## nos traemos las variables necesarias
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

    ## si la pila de operaciones no esta vacia
    if pOper:
        ## revisa si el tope de la pila es negativo
        if pOper[-1] == NEG:
            ## armamos la operacion de hacer negativo con su operando izquierdo
            ## y su tipo correspondiente
            op = pOper.pop()
            opdoIzq = pilaO.pop()
            tipoIzq = pTipos.pop()
            tipoRes = cubo_semantico[tipoIzq][op]
            ## si el tipo resultante no es error entonces damos de alta la temporal
            ## correspondiente, lo agregamos a la pilaO su tipo a la pTipos y
            ## hacemos el cuadruplo
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
            ## si el tipo resultante marca error entonces marcamos error de tipos
            else:
                print("Type mismatch")
                exit()
    pass

##############################################################
## meteneg                                                  ##
### regla sintactica para dar la opcion de meter o no el    ##
### signo negativo en el termino y agregarlo a la pOper     ##
##############################################################
def p_meteneg(p):
    '''meteneg : empty
               | "-" '''
    if p[1] == "-":
        pOper.append(NEG)
    pass

##############################################################
## punto neuralgico 6                                       ##
### utilizado para meter el fondo falso a la pila de        ##
### operaciones para cuando se ingresa un parentesis        ##
### esto le da prioridad a las operaciones internas         ##
##############################################################
def p_neur6(p):
    'neur6 : '
    pOper.append("(")
    pass

##############################################################
## punto neuralgico 7                                       ##
### utilizado para sacar el fondo falso de la pila de       ##
### operaciones para cuando se termina la expreson          ##
### y se cierra parentesis y asi ya pueden continuar las    ##
### operaciones anteriores al parentesis                    ##
##############################################################
def p_neur7(p):
    'neur7 : '
    ## si la pila de operaciones es un parentesis lo sacamos
    if pOper[-1] == "(" :
        pOper.pop()
    ## sino marcamos error
    else:
        print("Missing opening parenthesis")
        exit()
    pass

##############################################################
## varcte                                                   ##
### utilizado para meter constantes, variables sencillas    ##
### y llamadas a funciones no void                          ##
##############################################################
def p_varcte(p):
    '''varcte : ID r neurVar
              | CTEE neurCteE
              | CTEF neurCteF
              | CTEBOOL neurCteB
              | callreturnfunc
              | CTECHAR neurCteCh'''
    p[0] = p[1]
    pass

######################################################
## punto neuralgico var                             ##
### utilizado para agregar la variable a la pilaO   ##
### y pTipos siempre y cuando exista en el          ##
### diccionario de variables del scope actual       ##
### y no sea una operacion length                   ##
######################################################
def p_neurVar(p):
    'neurVar : '
    ## si no es una operacion de length
    if p[-1] == -1:
        ## utilizamos el diccionario auxiliar para apuntar
        ## a las variables del scope
        auxDic = dir_procs[scope[-1]][pos_dics_var]
        ## revisamos que exista en el diccionario el ID y
        ## en caso de que si agregamos a la pTipos su tipo
        ## y su direccion virtual correspondiente
        if p[-2] in auxDic:
            pTipos.append(auxDic[p[-2]][0])
            pilaO.append(auxDic[p[-2]][pos_vars_dir_virtual])
        ## si no esta es por que no existe y marcamos error
        else:
            print "No existe tal variable"
            exit()
    pass

##############################################################
## punto neuralgico cte entera                              ##
### utilizado para agregar constantes enteras y como        ##
### las constantes estan en un diccionario entonces revisa  ##
### si ya existe esa constante y pone su direccion virtual  ##
### o si no la agrega                                       ##
##############################################################
def p_neurCteE(p):
    'neurCteE : '
    ## nos traemos las variables necesarias
    global cte_int
    global cte_float_inicio
    global ctes
    ## agregamos a la pila de tipos el tipo entero
    pTipos.append(INT)
    ## checamos si no existe en el diccionario de constantes
    if (not p[-1] in ctes):
        ## si no existe la agregamos sumando nuestra constante
        ## global de constantes enteras que tiene la direccion
        ## virtual de la siguiente constante entera a utilizar
        if cte_int + 1 < cte_float_inicio:
            ctes[p[-1]] = cte_int
            cte_int += 1
        else:
            print "Overflow de constantes enteras"
            exit()
    ## agregamos a pilaO la direccion virtual de la constante
    pilaO.append(ctes[p[-1]])
    pass

##############################################################
## punto neuralgico cte flotante                            ##
### utilizado para agregar constantes flotantes y como      ##
### las constantes estan en un diccionario entonces revisa  ##
### si ya existe esa constante y pone su direccion virtual  ##
### o si no la agrega                                       ##
##############################################################
def p_neurCteF(p):
    'neurCteF : '
    ## nos traemos las variables necesarias
    global cte_float
    global cte_bool_inicio
    global ctes
    ## agregamos el tipo float a la pila de tipos
    pTipos.append(FLOAT)
    ## checamos si no existe en el diccionario de constantes
    if (not p[-1] in ctes):
        ## si no existe la agregamos sumando nuestra constante
        ## global de constantes enteras que tiene la direccion
        ## virtual de la siguiente constante entera a utilizar
        if cte_float + 1 < cte_bool_inicio:
            ctes[p[-1]] = cte_float
            cte_float += 1
        else:
            print "Overflow de constantes flotantes"
            exit()
    ## agregamos a pilaO la direccion virtual de la constante
    pilaO.append(ctes[p[-1]])
    pass

##############################################################
## punto neuralgico cte booleana                            ##
### utilizado para agregar constantes booleanas y como      ##
### las constantes estan en un diccionario entonces revisa  ##
### si ya existe esa constante y pone su direccion virtual  ##
### o si no la agrega                                       ##
##############################################################
def p_neurCteB(p):
    'neurCteB : '
    ## nos traemos las variables necesarias
    global cte_bool
    global cte_char_inicio
    global ctes
    ## agregamos el tipo a la pila de tipos
    pTipos.append(BOOL)

    #####################################################
    # fix para que el True no lo confunda con 1         #
    # por cuestion de que python lo parsea directamente #
    # a 1 o 0 si es False                               #
    #####################################################

    ## cambiamos que ahora lo agregue como un string al
    ## diccionario de constantes y poderlo buscar asi despues
    if p[-1]:
        boolConst = 'tru'
    else:
        boolConst = 'fals'
    ## revisamos si existe en el diccionario de constantes
    if (not boolConst in ctes):
        ## si no existe la agregamos sumando nuestra constante
        ## global de constantes enteras que tiene la direccion
        ## virtual de la siguiente constante entera a utilizar
        if cte_bool + 1 < cte_char_inicio:
            ctes[boolConst] = cte_bool
            cte_bool += 1
        else:
            print "Overflow de constantes booleanas"
            exit()
    ## agregamos a pilaO la direccion virtual de la constante
    pilaO.append(ctes[boolConst])
    pass

##############################################################
## punto neuralgico cte char                                ##
### utilizado para agregar constantes char y como           ##
### las constantes estan en un diccionario entonces revisa  ##
### si ya existe esa constante y pone su direccion virtual  ##
### o si no la agrega                                       ##
##############################################################
def p_neurCteCh(p):
    'neurCteCh : '
    ## nos traemos las variables necesarias
    global cte_char
    global cte_nota_inicio
    global ctes
    ## agregamos el tipo a la pila de tipos
    pTipos.append(CHAR)
    ## revisamos si existe en el diccionario de constantes
    if (not p[-1] in ctes):
        ## si no existe la agregamos sumando nuestra constante
        ## global de constantes enteras que tiene la direccion
        ## virtual de la siguiente constante entera a utilizar
        if cte_char + 1 < cte_nota_inicio:
            ctes[p[-1]] = cte_char
            cte_char += 1
        else:
            print "Overflow de constantes char"
            exit()
    ## agregamos a pilaO la direccion virtual de la constante
    pilaO.append(ctes[p[-1]])
    pass

######################################################################
## Regla sintactica n para poder agregar una operacion de lista     ##
## con una variable dimensionada (length o acceso)                  ##
######################################################################
def p_r(p):
    '''r : empty
         | oplista'''
    ## si esta vacio regresamos que no hubo operacion
    if p[1] == None:
        p[0] = -1
    ## sino regresamos que si hubo
    else:
        p[0] = 1
    pass

##############################################################
## oplista                                                  ##
### utilizada para escoger la operacion que se va utilizar  ##
### de lista                                                ##
##############################################################
def p_oplista(p):
    '''oplista : accesoVarDim
               | length'''
    p[0] = p[1]
    pass

##############################################################
## accesoVarDim                                             ##
### utilizado para accesar el valor de una cassilla de      ##
### la variable dimensionada para esto se puede utilizar    ##
### expresion numerica entera para ingresar el indice       ##
### de la casilla a la que se quiere acceder                ##
##############################################################
def p_accesoVarDim(p):
    'accesoVarDim : "[" neur27 nexp "]"'
    ## regresamos que hicimos una operacion de lista
    p[0] = 1

    ## nos traemos las variables necesarias
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

    ## revisamos si la variable existe en el diccionario de variables
    if p[-1] in dir_procs[scope[-1]][pos_dics_var]:
        ## revisamos que sea una variable dimensionada por su campo de dimension
        ## en el diccionario
        if dir_procs[scope[-1]][pos_dics_var][p[-1]][pos_vars_dim] != None:
            ## revisamos que sea un entero el resultado de la expresion
            ## de acceso al indice
            if pTipos[-1] == INT:
                ## hacemos la operacion para verificar que este
                ## dentro del rango de la dimension y que lo revise en
                ## ejecucion y para eso hacemos este cuadruplo
                op = VERIFICA
                opdoIzq = pilaO[-1]
                opdoDer = dir_procs[scope[-1]][pos_dics_var][p[-1]][pos_vars_dim][1]
                res = dir_procs[scope[-1]][pos_dics_var][p[-1]][pos_vars_dim][0]
                cuadruplos[contCuad] = [op,opdoIzq,opdoDer,res]
                contCuad += 1
                ## vamos a hacer la operacion de suma del resultado de la operacion
                ## interna con la direccion virtual base de la variable dimensionada
                ## opdoIzq es el resultado de la operacion y el opdoDer es la direccion
                ## base de la variable convertida en direccion virtual de constante
                op = PLUS
                opdoIzq = pilaO.pop()
                pTipos.pop()
                ## aqui saco la direccion base con la direccion virtual
                aux = dir_procs[scope[-1]][pos_dics_var][p[-1]][pos_vars_dir_virtual]
                ## aqui lo agregue a las constantes si no estaba
                if (not aux in ctes):
                    if cte_int + 1 < cte_float_inicio:
                        ctes[aux] = cte_int
                        cte_int += 1
                    else:
                        print "Overflow de constantes enteras"
                        exit()
                ## aqui ya definimos el opdoDer para el cuadruplo
                opdoDer = ctes[aux]
                dir_procs[scope[-1]][pos_dics_tam]['ti']+=1
                if var_loc_temp_int + 1 < var_loc_temp_float_inicio:
                    ## se genera el cuadruplo
                    cuadruplos[contCuad] = [op,opdoIzq,opdoDer,var_loc_temp_int]
                    contCuad += 1
                    ## aqui agrego la direccion representada como meter el numero
                    ## de la direccion virtual entre parentesis para que de esta manera
                    ## lo trate como apuntador la maquina virtual y de esta manera
                    ## encuentra el valor de la casilla
                    pilaO.append("("+str(var_loc_temp_int)+")")
                    var_loc_temp_int += 1
                else:
                    print "Overflow de temporales enteras"
                    exit()
                ## aqui agrego el tipo de la variable dimensionada
                pTipos.append(dir_procs[scope[-1]][pos_dics_var][p[-1]][pos_vars_tipo])
                ## aqui saco el fondo falso que se mete cuando se manda a llamar la
                ## expresion interna para saber el desplazamiento que se quiere hacer
                if pOper[-1] == '[':
                    pOper.pop()
            ## si no es entera la expresion interna entonces es un error
            else:
                print "El indice que tratas de acccesar no es de tipo entero"
                exit()
        ## si la variable no es dimensionada entonces es un error
        else:
            print "No es una variable dimensionada"
            exit()
    ## si no existe la variable es un error
    else:
        print "No existe tal variable"
        exit()

    pass


##################################################################
## punto neuralgico 27                                          ##
### se utiliza para meter un fondo falso al momento de buscar   ##
### el indice que se desea acceder mediante una expresion       ##
### asi dejamos en pausa todas las operaciones pendientes que   ##
### teniamos en la expresion que tiene el acceso a la variable  ##
##################################################################
def p_neur27(p):
    'neur27 : '
    pOper.append('[')
    pass

##################################################################
## length                                                       ##
### se utiliza para saber el tamano declarado de una variable   ##
### dimensionada, regresa un entero metiendolo a la pilaO       ##
### y metiendo un entero a la pila de tipos                     ##
##################################################################
def p_length(p):
    'length : "." LENGTH "(" ")"'
    ## marcamos que no es una variable sencilla
    p[0] = 3
    ## nos traemos las variables necesarias
    global pilaO
    global pTipos
    global cte_int
    global cte_float_inicio
    ## checamos que la variable haya sido declarada en el scope
    if p[-1] in dir_procs[scope[-1]][pos_dics_var]:
        ## checamos que sea una variable dimensionada
        if dir_procs[scope[-1]][pos_dics_var][p[-1]][pos_vars_dim] != None:
            ## agregamos a la pila de tipos el tipo entero
            pTipos.append(INT);
            ## checamos la dimension al agregarle 1 al limite superior
            ## porque empieza desde 0
            dim = dir_procs[scope[-1]][pos_dics_var][p[-1]][pos_vars_dim][0]+1
            ## convertimos la dimension a una constante
            if (not dim in ctes):
                if cte_int + 1 < cte_float_inicio:
                    ctes[dim] = cte_int
                    cte_int += 1
                else:
                    print "Overflow de constantes enteras"
                    exit()
            ## y agregamos a la pilaO el resultado
            pilaO.append(ctes[dim])
        ## error si no es dimensionada la variable
        else:
            print "No es una variable dimensionada"
            exit()
    ## error si no habia sido declarada la variable en el scope o globalmente
    else:
        print "No existe tal variable"
        exit()
    pass

##################################################################
## while                                                        ##
### estatuto ciclico en el que se realiza el bloque de          ##
### instrucciones siempre y cuando siga siendo verdadera la     ##
### condicion interna, la diferencia del for es que no hay      ##
### asignacion pre ciclo y post-vuelta                          ##
##################################################################
def p_while(p):
    'while : WHILE "(" neur16 expresion ")" neur13 bloque ";" neur17'
    pass

##################################################################
## punto neuralgico 16                                          ##
### se utiliza en el while para definir el punto de brinco que  ##
### va a tener el ciclo para siempre evaluar la condicion cada  ##
### vez que termina una vuelta                                  ##
##################################################################
def p_neur16(p):
    'neur16 : '
    global contCuad
    pSaltos.append(contCuad)
    pass

##################################################################
## punto neuralgico 17                                          ##
### se utiliza en while para cuando terminamos el ciclo que     ##
### realice el GOTO al principio y vuelva a evaluar la          ##
### condicion para ver si vuelve a dar otra vuelta o no y       ##
### despues rellenamos el cuadruplo de GOTOF para saber a donde ##
### se va a ir el apuntador de instruccion si la condicion es   ##
### falsa                                                       ##
##################################################################
def p_neur17(p):
    'neur17 : '
    ## nos traemos las variables necesarias
    global contCuad
    ## realizamos el goto para ir al inicio
    op = GOTO
    ## sacamos primero la del GOTOF pendiente
    falso = pSaltos.pop()
    ## sacamos el punto antes de la condicion a usar
    ## en el goto
    ciclo = pSaltos.pop()
    cuadruplos[contCuad] = [op,None,None,ciclo]
    contCuad += 1
    ## rellenamos el GOTOF
    cuadruplos[falso][3] = contCuad
    pass

##########################################################
## play                                                 ##
### estatuto que se utiliza para sacar un sonido o      ##
### un silencio y que al final de programa se reunan    ##
### y se arme la melodia segun fue encontrando estos    ##
### estatutos                                           ##
##########################################################
def p_play(p):
    'play : PLAY "(" NOTA "," CTEE ")" ";"'
    ## nos traemos las variables necesarias
    global contCuad
    global ctes
    global cte_nota
    global cte_int
    global cte_float_inicio
    ## definimos el tipo de operacion
    op = PLAY
    ## checamos si la nota ya existe como constante
    ## sino la agregamos
    if (not p[3] in ctes):
        ctes[p[3]] = cte_nota
        cte_nota += 1
    opdoIzq = ctes[p[3]]
    ## checamos si el entero que define la duracion
    ## existe como constante sino la agregamos
    if(not p[5] in ctes):
        if cte_int + 1 < cte_float_inicio:
            ctes[p[5]] = cte_int
            cte_int +=1
        else:
            print "Overflow de constantes enteras"
            exit()
    opdoDer = ctes[p[5]]
    ## generamos el cuadruplo
    cuadruplos[contCuad] = [op,opdoIzq,opdoDer,None]
    contCuad+=1
    pass

##############################################################
## print                                                    ##
### estatuto que permite al usuario imprimir el resultado   ##
### de una expresion en consola                             ##
##############################################################
def p_print(p):
    'print : PRINT expresion ";"'
    ## nos traemos las variables necesarias
    global contCuad
    ## generamos el cuadruplo de impresion con lo que este
    ## en la pilaO
    op = PRINT
    opdoIzq = pilaO.pop()
    pTipos.pop()
    cuadruplos[contCuad] = [op,opdoIzq,None,None]
    contCuad+=1
    pass

##########################################################
## callreturnfunc                                       ##
### es mandado a llamar por varcte que se encuentra     ##
### en la jerarquia mas alta de la expresion donde se   ##
### cambia el scope de ejecucion y al final se tiene    ##
### un resultado que se puede utilizar en cualquier     ##
### expresion, este siempre tiene un tipo de retorno    ##
### y la funcion destino tiene sus propias variables    ##
### y expresiones para al final tener su instruccion    ##
### de retorno                                          ##
##########################################################
def p_callreturnfunc(p):
    'callreturnfunc : CALL ID neur24 "(" s ")" neur26 ";"'
    ## nos traemos las variables necesarias
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
    ## en el scope global en el diccionario de procedimientos se declara una
    ## variable que representa el resultado de la funcion en donde se le asigna
    ## una direccion virtual, por medio de esta instruccion se recupera la
    ## direccion virtual y poder igualar una temporal y meterla a la pilaO
    ## para que siga con el resto de la expresion

    ## sacamos la direccion virtual de la variable global
    dir_virtual = dir_procs['global'][pos_dics_var][p[2]][pos_vars_dir_virtual]
    ## sacamos el tipo de retorno que da que esta tambien en ese registro
    ## del diccionario de variable global
    tipo = dir_procs['global'][pos_dics_var][p[2]][pos_vars_tipo]
    ## hacemos una operacion de asignacion
    op = EQ
    opdoIzq = dir_virtual

    ## revisamos que tipo es y en base a eso le asignamos
    ## el valor de la variable global ahora a una temporal para
    ## el scope que mando a llamar la funcion al igual la metemos
    ## a la pilaO y su tipo a la pila de tipos
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

##################################################################
## Regla sintactica s para poder meter los valores de los       ##
## parametros por medio de expresiones ya que la funcion puede  ##
## o no tener parametros y puede tener uno o muchos por eso se  ##
## hace tambien un ciclo con la regla t                         ##
##################################################################
def p_s(p):
    '''s : empty
         | expresion neur25 t'''
    pass

##########################################################
## punto neuralgico 25                                  ##
### se utiliza cada vez que se termina la expresion de  ##
### un parametro en la llamada a una funcion, sea void  ##
### o con un tipo y se realiza una validacion para ver  ##
### si el parametro es del mismo tipo y los esta        ##
### ingresando en el orden correcto                     ##
##########################################################
def p_neur25(p):
    'neur25 : '
    ## nos traemos las variables necesarias
    global dir_procs
    global contCuad
    global auxFuncDestinoDir
    global currentFunc
    global pilaAuxParamCount

    ## como permitimos la llamada de una funcion como parametro
    ## de otra funcion tenemos que manejar una pila en la que
    ## el tope es a la funcion a la que se desea llamar y para
    ## eso utilizamos un auxiliar
    auxFuncDestinoDir = pilaFuncs[-1]
    ## checamos que el pOper no este vacio y que la pila
    ## que marca que numero de funcion a la que estamos llamando
    ## sea la misma a la que tenemos en el tope, esto se hace
    ## para cuando el parametro de una funcion es si misma
    if pOper != [] and currentFunc == pilaNumFuncs[-1]:
        ## checamos que la pilaO no este vacia y que la operacion
        ## pendiente o la pila del pOper sea el fondo falso de
        ## parametro
        if len(pilaO)>0 and pOper[-1] == PARAMETRO:
            ## sacamos el argumento que es el resultado de la
            ## expresion
            argumento = pilaO.pop()
            ## sacamos el tipo de la pila de tipos
            tipoarg = pTipos.pop()
            ## checamos si es el mismo tipo el que mandamos que el numero de parametro
            ## al que se lo estamos mandando, esto se debe al tope de la pilaAuxParamCount que nos dice
            ## que numero de parametro estamos llamando y hacemos el caso especial que si
            ## nos manda un int en la llamada a un float en el destino se la aceptamos
            if tipoarg == dir_procs[auxFuncDestinoDir][pos_dics_params][pilaAuxParamCount[-1]] or (tipoarg == INT and dir_procs[auxFuncDestinoDir][pos_dics_params][pilaAuxParamCount[-1]]==FLOAT):
                ## hacemos la operacion parametro y dependendo del tipo entonces
                ## utilizamos la variable local correspondiente
                op = PARAMETRO
                if tipoarg == INT:
                    cuadruplos[contCuad] = [op,argumento,None,var_loc_int_inicio + pilaAuxParamCount[-1]]
                elif tipoarg == FLOAT:
                    cuadruplos[contCuad] = [op,argumento,None,var_loc_float_inicio + pilaAuxParamCount[-1]]
                elif tipoRes == CHAR:
                    cuadruplos[contCuad] = [op,argumento,None,var_loc_char_inicio + pilaAuxParamCount[-1]]
                else:
                    cuadruplos[contCuad] = [op,argumento,None,var_loc_bool_inicio + pilaAuxParamCount[-1]]
                ## sumamos la cantidad de parametros
                pilaAuxParamCount[-1] += 1
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

    pass

######################################################################
## Regla sintactica t que permite seguir el ciclo de parametros     ##
## en el call de una funcion void o no void                         ##
######################################################################
def p_t(p):
    '''t : empty
         | "," s'''
    pass

##########################################################
## callvoidfunc                                         ##
### estatuto que permite al usuario cambiar al scope    ##
### de una funcion de tipo void enviandole parametros   ##
### y ejecutando instrucciones dentreo del scope de la  ##
### funcion                                             ##
##########################################################
def p_callvoidfunc(p):
    'callvoidfunc : CALL ID neur24 "(" s ")" neur26 ";"'
    pass

##############################################################
## punto neuralgico 24                                      ##
### se utiliza en cualquier call a una funcion, genera      ##
### un era para la nueva funcion a la que desea ir,         ##
### agrega a la pila de funciones, a la pila de numero      ##
### de funcion y finalmente deja todo listo para empezar    ##
### a ingresar los parametros                               ##
##############################################################
def p_neur24(p):
    'neur24 : '

    ## nos traemos las variables necesarias
    global contCuad
    global auxFuncDestinoDir
    global tempFunc
    global currentFunc
    global pOper
    global pilaFuncs

    ## revisamos que exista la funcion a la que se quiere
    ## llamar
    if p[-1] in dir_procs:
        ## lo agregamos a la pila de funciones y agregamos
        ## el numero de parametros dados de alta en 0's
        pilaFuncs.append(p[-1])
        auxFuncDestinoDir = p[-1]
        pilaAuxParamCount.append(0)
        ## generamos la operacion de era
        op = ERA
        cuadruplos[contCuad] = [op,p[-1],None,None]
        contCuad += 1
        ## metemos el fondo falso representado por el parametro
        pOper.append(PARAMETRO)
        ## apuntamos al numero de funcion corrrespondiente
        currentFunc = tempFunc
        ## agregamos ese numero de funcion a la pila de numero de
        ## funciones
        pilaNumFuncs.append(tempFunc)
        ## aumentamos el numero temporal
        tempFunc += 1
    ## marcamos error si no esta en el directorio de procedimiento
    else:
        print "Funcion con ese id no existe"
        exit()
    pass

##########################################################
## punto neuralgico 26                                  ##
### se utilia en cualquier llamada a funcion para       ##
### revisar que se hayan dado el numero de parametros   ##
### correctos y genera el GOSUB que ya cambia el scope  ##
##########################################################

def p_neur26(p):
    'neur26 : '
    ## nos traemos las variables necesarias
    global auxFuncDestinoDir
    global contCuad
    global pilaFuncs
    global currentFunc

    ## definimos la funcion destino
    auxFuncDestinoDir = pilaFuncs[-1]

    ## revisamos que el numero de parametros dados de alta sean iguales a la
    ## longitud de el arreglo de parametros en el diccionario de procedimientos
    ## no vaya a ser que dio parametros de menos
    if pilaAuxParamCount[-1] != len(dir_procs[auxFuncDestinoDir][pos_dics_params]):
        print "Error en cantidad de parametros"
        exit()
    else:
        ## si no fallo el pasado entonces ya damos de alta el GOSUB
        op = GOSUB
        ## checamos si esta el fondo falso
        if(pOper[-1] == PARAMETRO):
            ## sacamos fondo falso, la funcion y el numero de parametros
            ## y al final cambiamos la funcion actual
            pOper.pop()
            pilaNumFuncs.pop()
            pilaAuxParamCount.pop()
            if pilaNumFuncs != []:
                currentFunc = pilaNumFuncs[-1]
        ## se quedo con operaciones pendientes en los parametros
        else:
            print "Llamada a funcion con operaciones pendientes"
            exit()

        ## generamos el GOSUB
        cuadruplos[contCuad] = [op,auxFuncDestinoDir,None,None]
        contCuad += 1
        ## sacamos la funcion
        pilaFuncs.pop()


    pass

##############################################################
## return                                                   ##
### se utiliza en las funciones que no son de tipo void     ##
### esto marca que ya se asigna la variable global que      ##
### corresponde a la funcion y se le asigna el resultado    ##
### de la expresion                                         ##
##############################################################
def p_return(p):
    'return : RETURN "(" expresion ")" ";"'
    ## nos traemos las variables necesarias
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

    ## sacamo el resultado de la expresion y sera el retorno
    ## tambien sacamos el tipo resultante
    retorno = pilaO.pop()
    tipoRetorno = pTipos.pop()
    ## preparamos una asignacion ya que el return eso es lo que hace
    op = EQ
    ## checamos si el retorno corresponde con el que se declaron en la variable
    ## vuelve a pasar el caso especial con regresar un entero cuando es flotante
    if tipoRetorno == dir_procs[scope[-1]][pos_dics_tipo] or (tipoRetorno == INT and dir_procs[scope[-1]][pos_dics_tipo] == FLOAT):
        ## revisamos si ya existe la variable global para el scope
        if scope[-1] in dir_procs["global"][pos_dics_var]:
            ## si ya esta sacamos la direccion virtual y hacemos el cuadruplo de asignacion
            var_aux = dir_procs["global"][pos_dics_var][scope[-1]][pos_vars_dir_virtual]
            cuadruplos[contCuad] = [op,retorno,None,var_aux]
        ## si aun  no existe
        else:
            ## agregamos de acuerdo al tipo y luego armamos el cuadruplo
            ## de asignacion con la direccion virtual nueva
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

    ## generamos el fin del procedimiento que al final cambia
    ## el socpe actual y vuelve a pasar a control de la funcion
    ## que lo llamo
    op = ENDPROC
    cuadruplos[contCuad]=[op,None,None,None]
    contCuad += 1
    pass

##################################################################
## tipo                                                         ##
### se utiliza para definir el tipo de la variable o funcion    ##
### que se esta declarando                                      ##
##################################################################
def p_tipo(p):
    '''tipo : INT
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

######################################################################
## Regla sintactica u que permite declarar o no si la variable      ##
## es dimensionada o no                                             ##
######################################################################
def p_u(p):
    '''u : empty
         | LIST "(" CTEE ")"'''
    ## nos traemos las variables necesarias
    global cte_int
    global ctes
    ## si es vacio entonces no es dimensionada
    if p[1] == None:
        p[0] = "NA"
    ## si es dimensionada pasamos el entero que
    ## representa la dimension
    else:
        p[0] = p[3]
    pass

######################################################################
## Regla sintactica empty que permite indicar que esta vacio        ##
######################################################################
def p_empty(t):
    'empty : '
    pass

######################################################################
## Regla sintactica error que viene con ply que es a donde se va    ##
## cuando encuentra un error de sintaxis                            ##
######################################################################
def p_error(p):
    if p:
        print("Syntax error at '%s'" % p.value)
        exit()
    else:
        print("Syntax error at EOF")

## imports necesarios para ply
import ply.yacc as yacc
yacc.yacc()

## instrucciones para abrir el archivo que nos
## pasan como argumento en la consola
f = open(str(sys.argv[1]), 'r')
s = f.read()
f.close()
## comenzamos a parsearlo
yacc.parse(s)

## hacemos el import de la clase memoria
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
