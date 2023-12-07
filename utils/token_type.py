from enum import Enum, auto

class TokenType(Enum):
    """
    Enumeração que define os tipos de tokens reconhecidos pelo analisador léxico.
    Cada tipo de token é associado a um valor único.
    """

    FOR = auto()        # Token 'for'
    IN = auto()         # Token 'in'
    RANGE = auto()      # Token 'range'
    PRINT = auto()      # Token 'print'
    IDENTIFIER = auto() # Identificadores (nomes de variáveis)
    INTEGER = auto()    # Números inteiros
    STRING = auto()     # Strings delimitadas por aspas simples ou duplas
    PLUS = auto()       # Operador de adição '+'
    ASSIGN = auto()     # Operador de atribuição '='
    LPAREN = auto()     # Parêntese esquerdo '('
    RPAREN = auto()     # Parêntese direito ')'
    COLON = auto()      # Dois pontos ':'
    COMMA = auto()      # Vírgula ','
