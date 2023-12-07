class Token:
    """
    Classe que representa um token resultante da análise léxica.

    Attributes:
        type (TokenType): O tipo do token.
        value (str): O valor associado ao token.
    """

    def __init__(self, type, value):
        """
        Inicializa uma instância de Token com o tipo e o valor fornecidos.

        Parameters:
            type (TokenType): O tipo do token.
            value (str): O valor associado ao token.
        """
        self.type = type
        self.value = value

    def __repr__(self, level=0) -> str:
        """
        Retorna uma representação de string do objeto Token.

        Parameters:
            level (int): O nível de indentação para melhor formatação (opcional).

        Returns:
            str: Uma representação de string do objeto Token.
        """
        ret = "\t" * level + f"Token(type={self.type.name}, value='{self.value}')"
        return ret
