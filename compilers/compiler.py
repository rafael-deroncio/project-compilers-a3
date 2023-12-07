import ast

class Compiler:
    @staticmethod
    def run(code, mode='exec', filename="<string>"):
        """
        Executa o código fornecido após compilá-lo usando o módulo ast.

        Args:
            code (str): O código-fonte a ser compilado e executado.
            mode (str, optional): O modo de compilação ('exec', 'eval' ou 'single'). Padrão é 'exec'.
            filename (str, optional): O nome do arquivo para fins de exibição de erros. Padrão é "<string>".

        Raises:
            SyntaxError: Se houver um erro de sintaxe no código.
        """
        try:
            compiled_code = compile(source=ast.parse(code, mode=mode), filename=filename, mode=mode)
            exec(compiled_code)
        except SyntaxError as e:
            print(f"Erro de sintaxe: {e}")
