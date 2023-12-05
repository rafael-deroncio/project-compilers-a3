## Analisador de Expressões Matemáticas

Este código implementa um analisador de expressões matemáticas simples, dividido em três etapas principais: análise léxica, análise sintática e análise semântica.

### Utilização

O código principal está contido no arquivo principal (`main.py`), que utiliza as funcionalidades definidas nos módulos localizados na pasta `utils`. Antes de executar o código, certifique-se de ter um arquivo de expressões matemáticas (por exemplo, `expressoes.txt`) no mesmo diretório.

Para executar o código, basta seguir estas etapas:

1. Importar as classes necessárias do módulo `utils`:

    ```python
    from utils.gerenciadores import Arquivo
    from utils.analisadores import Lexica, Sintatica, Semantica
    ```

2. Processar o arquivo de expressões:

    ```python
    conteudo_arquivo = Arquivo.processar('expressoes.txt')
    ```

3. Realizar a análise léxica:

    ```python
    tokens = Lexica.analisar(conteudo_arquivo, True)
    ```

4. Realizar a análise sintática:

    ```python
    arvore_sintatica = Sintatica.analisar(tokens, True)
    ```

5. Realizar a análise semântica:

    ```python
    analise_semantica = Semantica.analisar(arvore_sintatica, True)
    ```

### Módulo `Arquivo`

O módulo `utils.file_manager` fornece uma classe estática `FileManager` com um método para processar o conteúdo de um arquivo. Ele verifica se o arquivo existe e não está vazio antes de retornar o conteúdo.

### Módulo `Lexer`

O módulo `Lexer` é responsável pela análise léxica das expressões matemáticas. Ele divide as expressões em tokens e fornece métodos para exibir os resultados da análise léxica.

### Módulo `Syntactic`

O módulo `Syntactic` realiza a análise sintática da lista de tokens gerada pela análise léxica. Ele verifica a validade da estrutura das expressões matemáticas, identificando possíveis erros sintáticos, como parênteses mal posicionados.

### Módulo `Semantic`

O módulo `Semantic` realiza a análise semântica das expressões matemáticas, avaliando-as e identificando erros semânticos, como divisão por zero. Os resultados são exibidos, indicando se as expressões são válidas e seus respectivos valores.

### Módulo `CodeGenerator`

O módulo `CodeGenerator` realiza a análise de codigo e traduz ela para a linguagem Python.

### Módulo `Compiler`

O módulo `Compiler` realiza a compilação e execução do código.

### Exemplo de Arquivo de Expressões (`expressoes.txt`)

```plaintext
for i in range(5): print(i)
for i in 'uma string qualquer': print(i)
for i in 'COMPILADORES': print(i)
for i in %: print(i)
# for i in range(15): print(i)
((12 + 2 -1) + 1)
```

### Resultados da Execução

Os resultados da análise léxica, sintática e semântica serão exibidos no console, indicando se as expressões são válidas e, em caso afirmativo, qual é o resultado da avaliação.