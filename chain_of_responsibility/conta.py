def formatar_moeda(valor):

    texto = f"{valor:,.2f}"
    texto = texto.replace(",", "X").replace(".", ",").replace("X", ".")
    return "R$ " + texto


class Conta:
    def __init__(self, titular, saldo, premium=False, bloqueio_judicial=False):
        self.titular = titular
        self.saldo = saldo
        self.premium = premium
        self.bloqueio_judicial = bloqueio_judicial

    def limite_por_transacao(self):
        return 10000.00 if self.premium else 1000.00