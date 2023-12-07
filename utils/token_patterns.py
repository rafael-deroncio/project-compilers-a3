from enum import Enum

class TokenPatterns(Enum):
    """
    Enumeração que define padrões de expressões regulares para tokens em um código.
    """

    @staticmethod
    def get_patterns():
        """
        Obtém uma lista de padrões de expressões regulares para tokens.

        Returns:
            List[Tuple[str, str]]: Lista de tuplas contendo padrões e os respectivos nomes de tokens.
        """
        return [
            (r'\bpara\b', 'FOR'),                           # Padrão para a palavra-chave 'for'
            (r'\bno\b', 'IN'),                              # Padrão para a palavra-chave 'in'
            (r'\bintervalo\b', 'RANGE'),                    # Padrão para a palavra-chave 'range'
            (r'\bescreva\b', 'PRINT'),                      # Padrão para a palavra-chave 'print'
            (r'\b[a-zA-Z_][a-zA-Z0-9_]*\b', 'IDENTIFIER'),  # Padrão para identificadores válidos
            (r'\d+', 'INTEGER'),                            # Padrão para números inteiros
            (r',', 'COMMA'),                                # Padrão para a vírgula
            (r"'[^']*'", 'STRING'),                         # Padrão para strings entre aspas simples
            (r'"[^"]*"', 'STRING'),                         # Padrão para strings entre aspas duplas
            (r'\(', 'LPAREN'),                              # Padrão para o parêntese esquerdo
            (r'\)', 'RPAREN'),                              # Padrão para o parêntese direito
            (r':', 'COLON'),                                # Padrão para dois pontos
            (r'[^a-zA-Z0-9_ \t\n,\'"]', 'UNKNOWN'),         # Padrão para caracteres desconhecidos
        ]
