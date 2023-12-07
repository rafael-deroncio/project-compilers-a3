import re
from typing import List, Optional
from utils.token import Token
from utils.token_type import TokenType
from utils.token_patterns import TokenPatterns
from exceptions.token_exception import TokenException

class Lexer:
    @staticmethod
    def scanner(expression: str, show_result: bool = False) -> List[Token]:
        """
        Realiza a análise léxica da expressão fornecida e retorna a lista de tokens.

        Args:
            expression (str): A expressão a ser analisada.
            show_result (bool, optional): Se True, exibe os resultados da análise léxica.

        Returns:
            List[Token]: Lista de tokens gerados pela análise léxica.
        """
        tokens = []

        # Combina os padrões de expressões regulares para formar um padrão combinado
        combined_pattern = '|'.join('(?P<%s_%s>%s)' % (name, i, pattern) for i, (pattern, name) in enumerate(TokenPatterns.get_patterns(), start=1))
        regex = re.compile(combined_pattern)

        try:
            # Itera sobre todas as correspondências na expressão
            for match in regex.finditer(expression):
                for name, value in match.groupdict().items():
                    if value is not None:
                        # Verifica se o token é desconhecido
                        if name.startswith('UNKNOWN'):
                            raise TokenException(f"Token não reconhecido '{value}'")

                        # Obtém o tipo do token com base no nome e cria um objeto Token
                        token_type = TokenType[name.split('_')[0].upper()]  
                        tokens.append(Token(token_type, value))
                        break
        except TokenException as e:
            print(f"Erro Léxico: {e.message}")
        except Exception as e:
            print(f"Erro Inesperado: {e.message}")

        # Exibe os resultados se show_result for True
        if show_result:
            print("Resultados da análise Léxica: ")
            for token in tokens:
                print(token.__repr__(level=1))
            print()

        return tokens
