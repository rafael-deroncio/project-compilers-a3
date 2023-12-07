from utils.syntax_tree import ASTNode
from utils.ast_nodes import RangeNode, PrintNode, IdentifierNode, IntegerNode, StringNode
from exceptions.semantic_exception import SemanticException

class CodeGenerator:
    """
    Classe responsável por gerar código a partir de uma árvore sintática.
    """

    @staticmethod
    def generate(tree, show_result=False):
        """
        Gera código a partir de uma árvore sintática.

        Args:
            tree: A árvore sintática.
            show_result (bool, optional): Indica se o resultado deve ser exibido. Padrão é False.

        Returns:
            str: O código gerado.
        """
        generator = CodeGenerator()
        generator.code = []

        # Verifica se tree é uma lista de dicionários
        if not isinstance(tree, list) or not all(isinstance(entry, dict) for entry in tree):
            raise SemanticException("A árvore fornecida para o CodeGenerator deve ser uma lista de dicionários.")

        # Gera o código para cada entrada na lista de dicionários
        for entry in tree:
            generator.__generate_entry(entry)

        code = '\n'.join(generator.code)

        if show_result:
            print("Código Gerado:\n", code)

        return code

    def __generate_entry(self, entry):
        """
        Gera código para uma entrada específica na árvore sintática.

        Args:
            entry (dict): A entrada da árvore sintática.
        """
        # Verifica se a entrada tem um tipo válido
        if 'type' not in entry:
            raise SemanticException("Cada entrada na lista de dicionários deve ter uma chave 'type' para indicar o tipo.")

        # Chama o método de geração correspondente com base no tipo da entrada
        if entry['type'] == 'for_loop':
            self.__generate_for_loop(entry)
        else:
            raise SemanticException(f"Tipo de entrada não suportado: {entry['type']}")

    def __generate_for_loop(self, for_loop_entry):
        """
        Gera código para um loop 'for' na árvore sintática.

        Args:
            for_loop_entry (dict): A entrada correspondente ao loop 'for'.
        """
        variable = for_loop_entry['variable']
        iterable = for_loop_entry['iterable']

        # Gera o código para o cabeçalho do loop
        self.code.append(f"for {variable} in {self.__generate_expression(iterable)}:")

        # Gera o código para o corpo do loop
        self.__generate_statement(for_loop_entry)

    def __generate_print_statement(self, print_entry):
        """
        Gera código para uma declaração 'print' na árvore sintática.

        Args:
            print_entry (dict): A entrada correspondente à declaração 'print'.
        """
        expression = print_entry['body']
        self.code.append(f"{' ' * 4}print({self.__generate_expression(expression)})")

    def __generate_expression(self, expression_node):
        """
        Gera código para uma expressão na árvore sintática.

        Args:
            expression_node: O nó correspondente à expressão.

        Returns:
            str: O código gerado para a expressão.
        """
        if isinstance(expression_node, IdentifierNode) or isinstance(expression_node, IntegerNode) or isinstance(
                expression_node, StringNode):
            return expression_node.value

        elif isinstance(expression_node, PrintNode):
            return ', '.join([expr.value for expr in expression_node.children])

        elif isinstance(expression_node, RangeNode):
            return f"range({', '.join([expr.value for expr in expression_node.children])})"
        else:
            raise SemanticException(f"Tipo de expressão não suportado: {type(expression_node).__name__}")

    def __generate_statement(self, entry):
        """
        Gera código para uma declaração na árvore sintática.

        Args:
            entry (dict): A entrada correspondente à declaração.
        """
        if isinstance(entry['body'], PrintNode):
            self.__generate_print_statement(entry)
        else:
            raise SemanticException(f"Tipo de declaração não suportado: {entry['body']}")

    def __repr__(self):
        """
        Retorna uma representação em string do código gerado.

        Returns:
            str: O código gerado.
        """
        return '\n'.join(self.code)
