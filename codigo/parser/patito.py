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
    'VAR','FUNC','NEW','LIST','IF', 'ELSE',
    'FOR','NOT','AND','OR','SET','APPEND',
    'LENGTH','GET','REMOVE','NOTA','PRINT',
    'CALL', 'RETURN', 'INT', 'CHAR', 'FLOAT',
    'BOOL','NOTEQ', 'LTHANEQ', 'MTHANEQ', 'EQ',
    'CTEF', 'CTEE', 'CTEBOOL', 'CTECHAR', 'ID',
    )

literals = ['(',')',',',':',';', '{','}','*','/','',',',';','>','<']

# Tokens

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

# Parsing rules

def p_programa(p):
    'programa : PROG ID ";" v bloque'
    print('done with file!\n')
    pass

def p_v(p):
    ''' v : empty
          | vars'''
    pass

def p_vars(p):
    'vars : VAR a'
    pass

def p_a(p):
    'a : b ":" tipo ";" f'
    pass

def p_f(p):
    ''' f : empty
          | a'''
    pass

def p_b(p):
    'b : ID c'
    pass

def p_c(p):
    '''c : empty
         | "," b '''
    pass

def p_tipo(p):
    '''tipo : INT
            | FLOAT'''
    pass

def p_bloque(p):
    'bloque : "{" d "}"'
    print('bloque codificado exitosamente\n')
    pass

def p_d(p):
    '''d : empty
         | estatuto d'''
    pass

def p_estatuto(p):
    '''estatuto : asignacion
                | condicion
                | escritura'''
    pass

def p_asignacion(p):
    'asignacion : ID "=" expresion ";"'
    print('se asigno la variable '+ p[1])
    pass

def p_expresion(p):
    'expresion : exp i'
    pass

def p_i(p):
    '''i : empty
         | ">" exp
         | "<" exp
         | NOTEQ exp'''
    pass

def p_escritura(p):
    'escritura : PRINT "(" g ")" ";"'
    pass

def p_g(p):
    '''g : expresion h
         | CTES h'''
    pass

def p_h(p):
    '''h : empty
        | "," g'''
    pass

def p_exp(p):
    'exp : termino k'
    pass

def p_k(p):
    '''k : empty
         | "+" exp
         | "-" exp'''
    pass

def p_factor(p):
    '''factor : "(" expresion ")"
              | m varcte'''
    pass

def p_m(p):
    '''m : empty
         | "+"
         | "-"'''
    pass

def p_condicion(p):
    'condicion : IF "(" expresion ")" bloque j ";"'
    pass

def p_j(p):
    '''j : empty
         | ELSE bloque'''
    pass

def p_termino(p):
    'termino : factor l'
    pass

def p_l(p):
    '''l : empty
         | "*" termino
         | "/" termino'''
    pass

def p_varcte(p):
    '''varcte : ID
              | CTEED
              | CTEF'''
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
