# -----------------------------------------------------------------------------
# patito.py
#
# Un simple parser para la clase de compiladores.
# Basado en el ejemplo de calc.py de la libreria ply v 3.8
# -----------------------------------------------------------------------------

import sys

if sys.version_info[0] >= 3:
    raw_input = input

tokens = (
    'PROG','IF','THEN','ELSE','PROC','END','INT','FLOAT',
    'WHILE','READ','PRINT','VAR','NOTEQ','LTEQ','GTEQ',
    'CTES','COMMENT','ID','CTEED','CTEEB','CTEEH','CTEF',
    )

literals = ['=','+','-','*','/', '(',')','{','}',':',',',';','>','<']

# Tokens

def t_IF(t):
    r'IF'
    return t

def t_THEN(t):
    r'THEN'
    return t

def t_ELSE(t):
    r'ELSE'
    return t

def t_PROC(t):
    r'PROC'
    return t

def t_END(t):
    r'END'
    return t

def t_INT(t):
    r'INT'
    return t

def t_FLOAT(t):
    r'FLOAT'
    return t

def t_WHILE(t):
    r'WHILE'
    return t

def t_READ(t):
    r'READ'
    return t

def t_PRINT(t):
    r'PRINT'
    return t

def t_VAR(t):
    r'VAR'
    return t

def t_NOTEQ(t):
    r'<>'
    return t

def t_LTEQ(t):
    r'<='
    return t

def t_GTEQ(t):
    r'>='
    return t

def t_PROG(t):
    r'PROG'
    return t

def t_CTEF(t):
    r'[0-9]+([eE]([+]|[-])?|[.][0-9]+[eE]([+]|[-])?|[.])[0-9]+'
    t.value = float(t.value)
    return t

def t_CTES(t):
    r'\"[^\n"]*\"'
    return t

t_ignore = " \t\n"

def t_COMMENT(t):
    r'\/\*([^*]|\n|[*][^\/])*\*\/'
    return t

def t_ID(t):
    r'[A-Za-z]([_]?([a-zA-Z]|[0-9]))*'
    return t

def t_CTEED(t):
    r'[0-9]+'
    t.value = int(t.value)
    return t

def t_CTEEB(t):
    r'(0|1)+b'
    return t

def t_CTEEH(t):
    r'[0-9]+[a-fA-F0-9]*[hH]'
    return t

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
import ply.lex as lex
lex.lex()

# Parsing rules

def p_programa(p):
    'programa : a c cancion'
    print('done with file!\n')
    pass

def p_a(p):
    ''' a : empty
          | vars b'''
    pass

def p_b(p):
    '''b : empty
         | a''''
    pass

def p_c(p):
    '''c : empty
         | funcion d''''
    pass

def p_d(p):
    '''d : empty
         | c''''
    pass

def p_vars(p):
    'vars : VAR v ":" tipo ";"'
    pass

def p_v(p):
    'v : ID e'
    pass

def p_e(p):
    '''e : empty
         | "," v'''
    pass

def p_funcion(p):
    'funcion : FUNC tipo ID "(" params ")" f bloque'
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
              | tipo ID h'''
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

def p_cancion(p):
    'cancion : "(" CTEE ")" bloque'
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
    'asignacion : ID "=" k ";"'
    pass

def p_k(p):
    '''k : expresion
         | asiglista'''
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
    pass

def p_m(p):
    '''m : empty
         | NOT'''
    pass

def p_termino(p):
    'termino : factor n'
    pass

def p_n(p):
    '''n : empty
         | "*" termino
         | "/" termino'''
    pass

def p_subexpresion(p):
    'subexpresion : exp o'
    pass

def p_o(p):
    '''o : empty
         | AND subexpresion
         | OR subexpresion'''
    pass

def p_exp(p):
    'exp : nexp p'
    pass

def p_p(p):
    '''p : empty
         | EQ nexp
         | NOTEQ nexp
         | ">" nexp
         | "<" nexp
         | GTEQ nexp
         | LTEQ nexp'''
    pass

def p_nexp(p):
    'nexp : termino q'
    pass

def p_q(p):
    '''q : empty
         | "+" nexp
         | "-" nexp'''
    pass

def p_factor(p):
    '''factor : "(" expresion ")"
              | w varcte'''
    pass

def p_w(p):
    '''w : empty
         | "-"'''
    pass

def p_varcte(p):
    '''varcte : ID r
              | CTEE
              | CTEF
              | CTEBOOL
              | callfunc
              | CHAR'''
    pass

def p_k(p):
    '''k : empty
         | oplista'''
    pass

def p_oplista(p):
    'oplista : ID "." x'
    pass

def p_x(p):
    '''x : inlistset
         | append
         | length
         | getlist
         | removelist'''
    pass

def p_inlistset(p):
    'inlistset : SET "(" CTEE "," expresion ")"'
    pass

def p_append(p):
    'append : APPEND "(" expresion ")"'
    pass

def p_length(p):
    'length : LENGTH "(" ")"'
    pass

def p_getlist(p):
    'getlist : GET "(" expresion ")"'
    pass

def p_removelist(p):
    'removelist : REMOVE "(" expresion ")"'
    pass

def p_while(p):
    'while : "(" expresion ")" bloque ";"'
    pass

def p_play(p):
    'play : "(" NOTA , CTEE ")" ";"'
    pass

def p_print(p):
    'print : PRINT expresion ";"'
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
    pass

def p_u(p):
    '''u : empty
         | LISTA'''
    pass

def p_y(p):
    '''y : INT
         | CHAR
         | FLOAT
         | BOOL'''
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
