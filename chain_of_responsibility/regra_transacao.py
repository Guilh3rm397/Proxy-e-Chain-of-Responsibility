class RegraTransacao:

    def __init__(self):
        self.proxima_regra = None

    def definir_proxima(self, proxima_regra):
        self.proxima_regra = proxima_regra
        return proxima_regra  

    def validar(self, conta, valor):

        if self.proxima_regra is None:
            return True, "Transação aprovada"
        return self.proxima_regra.validar(conta, valor)