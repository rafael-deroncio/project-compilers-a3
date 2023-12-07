class ASTNode:
    """
    Representa um nó na árvore sintática abstrata (AST).

    Attributes:
        node_type (str): O tipo do nó na AST.
        value: O valor associado ao nó.
        children (list): Lista de nós filhos.
        expression: Expressão associada ao nó.
    """

    def __init__(self, node_type: str, value=None, children=None, expression=None):
        """
        Inicializa um nó da AST.

        Parameters:
            node_type (str): O tipo do nó na AST.
            value: O valor associado ao nó.
            children (list, optional): Lista de nós filhos.
            expression: Expressão associada ao nó.
        """
        self.node_type = node_type
        self.value = value
        self.children = children or []
        self.expression = expression

    def __repr__(self, level=0):
        """
        Retorna uma representação visual do nó e de seus filhos, indentados de acordo com o nível.

        Parameters:
            level (int, optional): O nível de indentação. Usado recursivamente para indentar os filhos.
        
        Returns:
            str: Representação visual do nó e de seus filhos.
        """
        ret = "\t" * level + f"{self.node_type} "
        if self.value is not None:
            ret += f"({self.value})"
        ret += "\n"
        for child in self.children:
            ret += child.__repr__(level + 1)
        return ret
