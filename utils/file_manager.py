class FileManager:
    """
    Uma classe utilitária para processar arquivos de texto.
    """

    @staticmethod
    def process(filepath: str) -> str:
        """
        Lê o conteúdo de um arquivo de texto.

        Parameters:
            filepath (str): O caminho do arquivo.

        Returns:
            str: O conteúdo do arquivo.

        Raises:
            FileNotFoundError: Se o arquivo não for encontrado.
            ValueError: Se o arquivo estiver vazio.
        """       
        try:
            with open(filepath, 'r') as file:
                content: str = file.read()
                if not content:
                    raise ValueError(f"Erro: Arquivo '{filepath}' está vazio.")
                return content
        except FileNotFoundError:
            raise FileNotFoundError(f"Erro: Arquivo '{filepath}' não encontrado.")
