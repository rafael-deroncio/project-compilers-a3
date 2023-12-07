from analyzers.lexer import Lexer
from analyzers.syntactic import Syntactic
from analyzers.semantic import Semantic
from analyzers.code_generator import CodeGenerator
from compilers.compiler import Compiler
from utils.file_manager import FileManager

if __name__ == "__main__":
    # Carregar o código-fonte de um arquivo
    text = FileManager.process('expressions.txt').split('\n')[1]

    # Análise léxica
    tokens = Lexer.scanner(text, show_result=True)

    # Análise sintática
    syntax_tree = Syntactic.parse(tokens, show_result=True)

    # Análise semântica
    semantic_tree = Semantic.analyze(syntax_tree, show_result=True)

    # Geração de código
    generated_code = CodeGenerator.generate(semantic_tree, show_result=True)

    # Compilação e execução
    Compiler.run(generated_code)
