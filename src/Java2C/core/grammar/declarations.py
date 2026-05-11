def p_function(p):
    'function : visibility type IDENTIFER LPAREN params RPAREN body'
    p[0] = {
        'type' : 'function',
        'visibility' : p[1],
        'return_type' : p[2],
        'name' : p[3],
        'params': p[5]
    }

def p_class(p):
    'class : visibility CLASS IDENTIFIER body'
    p[0] = {
        'type': 'class',
        'visibility': p[1],
        'name': p[3],
    }

def p_type(p):
    'type : INT | VOID'
    p[0] = p[1]

def p_visibility(p):
    'visibility : PUBLIC | PRIVATE | empty'
    p[0] = p[1]

def p_body(p):
    'body : LBRACES statements RBRACES'

# def p_class_body(p):
#     'class_body : LBRACES statements RBRACES'

def p_param(p):
    'param : type IDENTIFIER'
    p[0] = [(p[1], p[2])]
    
def p_params_empty(p):
    'params : empty'
    p[0] = []

def p_params_single(p):
    'params : param'
    p[0] = p[1]

def p_params_multiple(p):
    'params : param COMMA params'
    #NOTE: can mutate for larger input
    p[0] = [p[1]] + p[3]

def p_this(p):
    'this : THIS'
    #TODO: if there's a this the fn should take a ptr to an instance of the Object
    p[0] = p[1]