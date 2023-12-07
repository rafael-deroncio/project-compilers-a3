from utils.syntax_tree import ASTNode

class ForLoopNode(ASTNode):
    """
    Representa um nó específico na AST para uma instrução de loop for.

    Attributes:
        variable (str): O nome da variável do loop.
        iterable: A expressão ou intervalo a ser iterado.
        body: O corpo do loop.
    """

    def __init__(self, variable: str, iterable, body):
        """
        Inicializa um nó ForLoopNode na AST.

        Parameters:
            variable (str): O nome da variável do loop.
            iterable: A expressão ou intervalo a ser iterado.
            body: O corpo do loop.
        """
        super().__init__("FOR_LOOP", value=variable, children=[iterable, body])

class PrintNode(ASTNode):
    """
    Representa um nó específico na AST para uma instrução de impressão.

    Attributes:
        expression: A expressão a ser impressa.
    """

    def __init__(self, expression):
        """
        Inicializa um nó PrintNode na AST.

        Parameters:
            expression: A expressão a ser impressa.
        """
        super().__init__("PRINT", children=[expression])

class RangeNode(ASTNode):
    """
    Representa um nó específico na AST para uma expressão de intervalo.

    Attributes:
        start: O início do intervalo.
        end: O final do intervalo.
    """

    def __init__(self, start, end):
        """
        Inicializa um nó RangeNode na AST.

        Parameters:
            start: O início do intervalo.
            end: O final do intervalo.
        """
        super().__init__("RANGE", children=[start, end])

class IdentifierNode(ASTNode):
    """
    Representa um nó específico na AST para um identificador (variável).

    Attributes:
        name (str): O nome do identificador.
    """

    def __init__(self, name: str):
        """
        Inicializa um nó IdentifierNode na AST.

        Parameters:
            name (str): O nome do identificador.
        """
        super().__init__("IDENTIFIER", value=name)

class IntegerNode(ASTNode):
    """
    Representa um nó específico na AST para um valor inteiro.

    Attributes:
        value: O valor inteiro.
    """

    def __init__(self, value):
        """
        Inicializa um nó IntegerNode na AST.

        Parameters:
            value: O valor inteiro.
        """
        super().__init__("INTEGER", value=value)

class StringNode(ASTNode):
    """
    Representa um nó específico na AST para uma string.

    Attributes:
        value: O valor da string.
    """

    def __init__(self, value):
        """
        Inicializa um nó StringNode na AST.

        Parameters:
            value: O valor da string.
        """
        super().__init__("STRING", value=value)
