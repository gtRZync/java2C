from typing import Literal

import ply.lex as lex
import rich

reserved_keywords = {
    'class' : 'CLASS',
    'public' : 'PUBLIC',
    'private' : 'PRIVATE',
    'protected' : 'PROTECTED',
    'static' : 'STATIC',
    'new' : 'NEW',
    'this' : 'THIS',
    'void' : 'VOID',
    'int' : 'INT',
    'if' : 'IF',
    'else' : 'ELSE',
    'while' : 'WHILE'
}

tokens = (
    'NUMBER',
    'IDENTIFIER',
    'COMMENTS',
    'COMMA',
    'DOT',
    'EQUALS',
    'LPAREN',
    'RPAREN',
    'LBRACKET',
    'RBRACKET',
    'LBRACE',
    'RBRACE',
    'SEMICOLON',
    'MUL_DIV',
    'PLUS_MINUS',
) + tuple(reserved_keywords.values())

precedence = (
    
)

def print_token(token: lex.LexToken, style: Literal['default', 'type-only', 'type+token'] = 'default'):
    match style:
        case 'default':
            token_parts = str(token).split(',')
            token_parts[0] = f'{token_parts[0].split("(")[0]}(type={token_parts[0].split("(")[1]}'
            token_parts[1] = f'token={token_parts[1]}'
            token_parts[2] = f'line={token_parts[2]}'
            token_parts[3] = f'pos={token_parts[3]}'
            tok = ','.join(token_parts)
            print(tok)
        case 'type+token' | 'type-only':
            str_token = str(token).split('(', 1)[1]
            parts = str_token.split(',', 2)
            parts[:] = parts[:2 if style == 'type+token' else 1]
            f = parts[0] if style == 'type-only' else f'{parts[0]}({parts[1]})'
            print(f)
        case _:
            rich.print(f'[yellow]WARNING: Unknown style: {style}, defaulting to __repr__.[/yellow]')
            print(token)