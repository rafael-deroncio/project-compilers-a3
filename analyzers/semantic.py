from utils.syntax_tree import ASTNode
from utils.ast_nodes import ForLoopNode, PrintNode, RangeNode, IdentifierNode
from exceptions.semantic_exception import SemanticException
from typing import List, Dict, Union

class Semantic:
    """
    Classe responsável pela análise semântica da árvore sintática gerada pelo parser.
    """

    @staticmethod
    def analyze(tree: ASTNode, show_result: bool = False) -> List[Dict[str, Union[str, IdentifierNode, RangeNode]]]:
        """
        Analisa a árvore sintática e gera informações semânticas.

        Args:
            tree (ASTNode): A raiz da árvore sintática.
            show_result (bool, optional): Indica se os resultados devem ser exibidos. Padrão é False.

        Returns:
            List[Dict[str, Union[str, IdentifierNode, RangeNode]]]: Lista de informações semânticas.
        """
        instance = Semantic()
        instance.declared_variables = set()
        instance.analysis_result = []
        instance.__analyze_program(tree)
        tree = instance.analysis_result

        if show_result:
            print(repr(instance))

        return tree

    def __analyze_program(self, program_node: ASTNode) -> None:
        """
        Analisa um nó do programa na árvore sintática.

        Args:
            program_node (ASTNode): O nó do programa a ser analisado.
        """
        for statement in program_node.children:
            self.__analyze_statement(statement)

    def __analyze_statement(self, statement: Union[ForLoopNode, PrintNode]) -> None:
        """
        Analisa um nó de declaração na árvore sintática.

        Args:
            statement (Union[ForLoopNode, PrintNode]): O nó de declaração a ser analisado.
        """
        if isinstance(statement, ForLoopNode):
            self.__analyze_for_loop(statement)
        elif isinstance(statement, PrintNode):
            self.__analyze_print_statement(statement)
        else:
            raise SemanticException(f"Tipo de declaração não suportado: {type(statement).__name__}")

    def __analyze_for_loop(self, for_loop_node: ForLoopNode) -> None:
        """
        Analisa um nó de loop 'for' na árvore sintática.

        Args:
            for_loop_node (ForLoopNode): O nó de loop 'for' a ser analisado.
        """
        variable = for_loop_node.value
        if not self.__variable_declared(variable):
            raise SemanticException(f"Variável '{variable}' não declarada antes do loop.")

        loop_info = {
            'type': 'for_loop',
            'variable': variable,
            'iterable': for_loop_node.children[0],
            'body': for_loop_node.children[1]
        }
        self.analysis_result.append(loop_info)

        self.__analyze_expression(for_loop_node.children[0])
        self.__analyze_statement(for_loop_node.children[1])

    def __analyze_print_statement(self, print_node: PrintNode) -> None:
        """
        Analisa um nó de declaração 'print' na árvore sintática.

        Args:
            print_node (PrintNode): O nó de declaração 'print' a ser analisado.
        """
        self.__analyze_expression(print_node.children[0])

    def __analyze_expression(self, expression_node: Union[IdentifierNode, RangeNode]) -> None:
        """
        Analisa um nó de expressão na árvore sintática.

        Args:
            expression_node (Union[IdentifierNode, RangeNode]): O nó de expressão a ser analisado.
        """
        if isinstance(expression_node, IdentifierNode):
            variable = expression_node.value
            if not self.__variable_declared(variable):
                raise SemanticException(f"Variável '{variable}' não declarada.")
        elif isinstance(expression_node, RangeNode):
            for node in expression_node.children:
                self.__analyze_expression(node)

    def __variable_declared(self, variable: str) -> bool:
        """
        Verifica se uma variável foi declarada.

        Args:
            variable (str): O nome da variável.

        Returns:
            bool: True se a variável foi declarada, False caso contrário.
        """
        if not self.declared_variables:
            self.declared_variables.add(variable)

        return variable in self.declared_variables

    def __repr__(self) -> str:
        """
        Retorna uma representação em string da análise semântica.

        Returns:
            str: Uma string representando a análise semântica.
        """
        ret = "Análise Semântica:\n"
        for analysis_info in self.analysis_result:
            ret += f"Tipo: {analysis_info['type']}, Variável: {analysis_info['variable']}, Iteravél: {repr(analysis_info['iterable'])} Corpo: {repr(analysis_info['body'])}\n"
        return ret
