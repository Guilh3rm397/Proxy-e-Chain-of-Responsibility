from usuario import InterfaceUsuario


class ProxyUsuario(InterfaceUsuario):
    """Controla o acesso aos dados do usuário real."""

    def __init__(self, usuario_real):
        self.usuario_real = usuario_real

    def obter_nome(self):
        # Nome liberado normalmente
        return self.usuario_real.obter_nome()

    def obter_cpf(self):
        # Oculta os 3 primeiros e os 2 últimos dígitos
        cpf = self.usuario_real.obter_cpf()
        return "***" + cpf[3:-2] + "**"

    def obter_endereco(self):
        # O endereço nunca é exibido
        raise PermissionError("Acesso negado ao endereço.")