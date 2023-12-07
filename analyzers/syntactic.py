from utils.syntax_tree import ASTNode
from utils.ast_nodes import ForLoopNode, PrintNode, RangeNode, IdentifierNode, IntegerNode, StringNode
from utils.token_type import TokenType
from utils.token import Token
from exceptions.token_exception import TokenException
from typing import List, Union, Tuple

class Syntactic:
    """
    Classe responsável pela análise sintática da sequência de tokens gerada pelo lexer.
    """

    @staticmethod
    def parse(tokens: List[Token], show_result: bool = False) -> ASTNode:
        """
        Analisa a sequência de tokens e gera a árvore sintática (AST).

        Args:
            tokens (List[Token]): A sequência de tokens gerada pelo lexer.
            show_result (bool, optional): Indica se os resultados devem ser exibidos. Padrão é False.

        Returns:
            ASTNode: A raiz da árvore sintática.
        """
        instance = Syntactic()
        instance.tokens = tokens
        instance.current_token_index = 0
        syntax_tree = instance.__parse_program()

        if show_result:
            print('Resultados da análise Sintática: (AST)')
            print(syntax_tree.__repr__(level=1))

        return syntax_tree

    def __parse_program(self) -> ASTNode:
        """
        Analisa o programa na sequência de tokens e gera o nó correspondente na árvore sintática.

        Returns:
            ASTNode: O nó correspondente ao programa na árvore sintática.
        """
        program_node = ASTNode("PROGRAM", children=[])

        while self.current_token_index < len(self.tokens):
            statement = self.__parse_statement()
            program_node.children.append(statement)

        return program_node

    def __parse_statement(self) -> Union[ForLoopNode, RangeNode, PrintNode]:
        """
        Analisa uma declaração na sequência de tokens e gera o nó correspondente na árvore sintática.

        Returns:
            Union[ForLoopNode, RangeNode, PrintNode]: O nó correspondente à declaração na árvore sintática.
        """
        current_token = self.tokens[self.current_token_index]

        if current_token.type == TokenType.FOR:
            return self.__parse_for_loop()
        elif current_token.type == TokenType.RANGE:
            return self.__parse_range_statement()
        elif current_token.type == TokenType.PRINT:
            return self.__parse_print_statement()
        else:
            raise TokenException(f"Token não esperado: {current_token}")

    def __match(self, expected_type: TokenType) -> Token:
        """
        Compara o tipo do token atual com um tipo esperado e avança o índice do token.

        Args:
            expected_type (TokenType): O tipo esperado do token.

        Returns:
            Token: O token atual.
        """
        current_token = self.tokens[self.current_token_index]

        if current_token.type == expected_type:
            self.current_token_index += 1
            return current_token
        else:
            raise TokenException(f"Token não esperado: {current_token.value}")

    def __parse_for_loop(self) -> ForLoopNode:
        """
        Analisa um loop 'for' na sequência de tokens e gera o nó correspondente na árvore sintática.

        Returns:
            ForLoopNode: O nó correspondente ao loop 'for' na árvore sintática.
        """
        self.__match(TokenType.FOR)
        variable = self.__match(TokenType.IDENTIFIER).value
        self.__match(TokenType.IN)

        start = None
        end = None

        if self.tokens[self.current_token_index].type == TokenType.RANGE:
            self.__match(TokenType.RANGE)
            start = self.__parse_expression()

            if isinstance(start, IntegerNode):
                end = start
                start = ASTNode(
                    node_type=TokenType.INTEGER.name,
                    value='0',
                    children=None,
                    expression=None)

            elif len(start) < 2:  # 2 argumentos no range
                self.__match(TokenType.COMMA)
            else:
                end = start[1]
                start = start[0]
        else:
            iterable = self.__parse_expression()

        self.__match(TokenType.COLON)
        body = self.__parse_statement()

        if start is not None and end is not None:
            return ForLoopNode(variable, RangeNode(start, end), body)
        else:
            return ForLoopNode(variable, iterable, body)

    def __parse_range_statement(self) -> RangeNode:
        """
        Analisa uma declaração 'range' na sequência de tokens e gera o nó correspondente na árvore sintática.

        Returns:
            RangeNode: O nó correspondente à declaração 'range' na árvore sintática.
        """
        self.__match(TokenType.RANGE)
        start = self.__parse_expression()
        self.__match(TokenType.COLON)
        end = self.__parse_expression()
        return RangeNode(start, end)

    def __parse_print_statement(self) -> PrintNode:
        """
        Analisa uma declaração 'print' na sequência de tokens e gera o nó correspondente na árvore sintática.

        Returns:
            PrintNode: O nó correspondente à declaração 'print' na árvore sintática.
        """
        self.__match(TokenType.PRINT)
        expression = self.__parse_expression()
        return PrintNode(expression=expression)

    def __parse_expression(self) -> Union[ASTNode, Tuple[ASTNode, ASTNode]]:
        """
        Analisa uma expressão na sequência de tokens e gera o nó correspondente na árvore sintática.

        Returns:
            Union[ASTNode, Tuple[ASTNode, ASTNode]]: O nó correspondente à expressão na árvore sintática.
        """
        current_token = self.tokens[self.current_token_index]

        if current_token.type == TokenType.LPAREN:
            return self.__parse_parenthesized_expression()
        elif current_token.type == TokenType.INTEGER:
            return self.__parse_integer()
        elif current_token.type == TokenType.STRING:
            return self.__parse_string()
        elif current_token.type == TokenType.IDENTIFIER:
            return self.__parse_identifier()
        elif current_token.type == TokenType.RANGE:
            return self.__parse_range()
        elif current_token.type == TokenType.PRINT:
            return self.__parse_print_statement()
        else:
            raise TokenException(f"Token não esperado em uma expressão: {current_token.value}")

    def __parse_parenthesized_expression(self) -> Union[ASTNode, Tuple[ASTNode, ASTNode]]:
        """
        Analisa uma expressão entre parênteses na sequência de tokens e gera o nó correspondente na árvore sintática.

        Returns:
            Union[ASTNode, Tuple[ASTNode, ASTNode]]: O nó correspondente à expressão entre parênteses na árvore sintática.
        """
        self.__match(TokenType.LPAREN)
        expression = self.__parse_expression()

        # Adicione a lógica para lidar com uma possível vírgula
        if self.tokens[self.current_token_index].type == TokenType.COMMA:
            self.__match(TokenType.COMMA)
            # Se houver uma vírgula, espera-se mais uma expressão
            second_expression = self.__parse_expression()
            expression = (expression, second_expression)

        self.__match(TokenType.RPAREN)
        return expression

    def __parse_integer(self) -> IntegerNode:
        """
        Analisa um literal inteiro na sequência de tokens e gera o nó correspondente na árvore sintática.

        Returns:
            IntegerNode: O nó correspondente ao literal inteiro na árvore sintática.
        """
        return IntegerNode(self.__match(TokenType.INTEGER).value)

    def __parse_string(self) -> StringNode:
        """
        Analisa um literal de string na sequência de tokens e gera o nó correspondente na árvore sintática.

        Returns:
            StringNode: O nó correspondente ao literal de string na árvore sintática.
        """
        return StringNode(self.__match(TokenType.STRING).value)

    def __parse_identifier(self) -> IdentifierNode:
        """
        Analisa um identificador (nome de variável) na sequência de tokens e gera o nó correspondente na árvore sintática.

        Returns:
            IdentifierNode: O nó correspondente ao identificador na árvore sintática.
        """
        return IdentifierNode(self.__match(TokenType.IDENTIFIER).value)

    def __parse_range(self) -> RangeNode:
        """
        Analisa uma expressão 'range' na sequência de tokens e gera o nó correspondente na árvore sintática.

        Returns:
            RangeNode: O nó correspondente à expressão 'range' na árvore sintática.
        """
        self.__match(TokenType.RANGE)
        start = self.__parse_expression()
        self.__match(TokenType.COLON)
        end = self.__parse_expression()

        return RangeNode(start, end)
