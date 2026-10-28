from regra_transacao import RegraTransacao


class RegraSaldo(RegraTransacao):
    def validar(self, conta, valor):
        if conta.saldo < valor:
            return False, "Saldo insuficiente"
        return super().validar(conta, valor)


class RegraValorMaximo(RegraTransacao):
    def validar(self, conta, valor):
        if valor > conta.limite_por_transacao():
            return False, "Valor acima do limite da conta"
        return super().validar(conta, valor)


class RegraBloqueioJudicial(RegraTransacao):
    def validar(self, conta, valor):
        if conta.bloqueio_judicial:
            return False, "Conta com bloqueio judicial"
        return super().validar(conta, valor)