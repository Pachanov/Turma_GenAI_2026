class CPFInvalidoException(Exception):
    """Exceção customizada para CPF inválido."""

    def __init__(self, mensagem="CPF inválido. Informe 11 dígitos numéricos válidos."):
        super().__init__(mensagem)
