def p_statement_decl(p):
    'statement: type IDENTIFIER SEMICOLON'
    p[0] = (p[1], p[2], p[3])
    #NOTE: maybe switch to using dict[str, value] to make ur life easier instead of using tuples

def p_statement_if(p):
    ...
    
def p_statement_while(p):
    ...

def p_statements_single(p):
    'statements: statement'
    p[0] = [p[1]]
    
def p_statements_multiple(p):
    'statements: statement statements'
    p[0] = [p[1]] + p[2]