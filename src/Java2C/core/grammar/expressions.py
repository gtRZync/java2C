operations = {
    '+' : lambda x, y: x+y,
    '-' : lambda x, y: x-y,
    '*' : lambda x, y: x*y,
    '/' : lambda x, y: x/y,
}

def p_expression_op_arithm(p):
    ''' expression : expression PLUS_MINUS expression |
        expression MUL_DIV expression'''
    p[0] = operations[p[2]](p[1], p[3])