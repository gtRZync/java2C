import ply.yacc as yacc
import rich

from .tokens import tokens          #noqa : F401, #pyright: ignore[reportUnusedImport]
from .grammar.declarations import *  #noqa : F403
from .grammar.expressions import *   #noqa : F403
from .grammar.statements import *    #noqa : F403

def p_empty(p):
    'empty :'
    pass

def p_error(p):
    if p is None:
        rich.print('[red]Error:[/red] Unexpected end of input')
    else:
        rich.print(f'[red]Syntax Error[/red] at line {p.lineno!r}: {p.value!r}')


def main() -> None:
    parser = yacc.yacc()


if __name__ == '__main__':
    main()
