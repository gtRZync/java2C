import ply.lex as lex
import rich
from .tokens import print_token, reserved_keywords, tokens #noqa: F401

t_ignore = ' \t'
t_COMMA = r'\,'
t_DOT = r'\.'
t_EQUALS = r'\='
t_MUL_DIV = r'(\*|/)'
t_PLUS_MINUS = r'(\+|-)'
t_SEMICOLON = r'\;'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'

def t_NUMBER(t):
    r'\d+(\.d+)?'
    parts = [p.strip() for p in t.value.split(sep='.', maxsplit=1)]

    if len(parts) < 2:
        t.value = int(t.value)
    else:
        t.value = float(t.value)
    return t

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved_keywords.get(t.value, 'IDENTIFIER')
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count('\n')

def t_error(t):
    rich.print(f'[red]Error:[/red] Unknown character: {t.value[0]!r}')
    t.lexer.skip(1)

def t_ignore_COMMENTS(t):
    '//.*'
    pass

def main() -> None:
    import sys
    from pathlib import Path

    if len(sys.argv) < 2:
        rich.print('[red]Error:[/red] [yellow]usage: python lexer.py filename[/yellow]')
    rich.print(f'[green]Input file:[/green] [magenta]{sys.argv[1]!r}[/magenta]\n')

    file = Path(sys.argv[1])
    data = file.read_text()

    lexer = lex.lex()
    lexer.input(data)
    while 1:
        token = lexer.token()

        if not token:
            break
        print_token(token, style='type+token')

if __name__ == '__main__':
    main()
