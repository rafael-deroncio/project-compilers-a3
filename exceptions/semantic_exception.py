class SemanticException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)

    def __traceback__(self):
        return None