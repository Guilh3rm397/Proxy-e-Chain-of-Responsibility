from conta import Conta, formatar_moeda
from regras import RegraSaldo, RegraValorMaximo, RegraBloqueioJudicial


class Principal:
    def montar_cadeia(self):
        regra_saldo = RegraSaldo()
        regra_valor_maximo = RegraValorMaximo()
        regra_bloqueio = RegraBloqueioJudicial()

        regra_saldo.definir_proxima(regra_valor_maximo).definir_proxima(regra_bloqueio)
        return regra_saldo

    def executar(self):
        cadeia = self.montar_cadeia()

        testes = [
            ("Conta comum, transação válida",
             Conta("Ana", 5000.00), 500.00),
            ("Conta comum, saldo insuficiente",
             Conta("Bruno", 100.00), 500.00),
            ("Conta comum, acima do limite de R$ 1.000,00",
             Conta("Carla", 5000.00), 2000.00),
            ("Conta premium, transação válida",
             Conta("Diego", 20000.00, premium=True), 8000.00),
            ("Conta premium, acima do limite de R$ 10.000,00",
             Conta("Elisa", 20000.00, premium=True), 12000.00),
            ("Conta premium, com bloqueio judicial",
             Conta("Fábio", 20000.00, premium=True, bloqueio_judicial=True), 500.00),
        ]

        print("=== Padrão Chain of Responsibility ===")
        for numero, (descricao, conta, valor) in enumerate(testes, start=1):
            aprovada, motivo = cadeia.validar(conta, valor)
            resultado = "APROVADA" if aprovada else "REPROVADA"

            print(f"\nTeste {numero}: {descricao}")
            print(f"  Titular: {conta.titular} | Saldo: {formatar_moeda(conta.saldo)} "
                  f"| Valor: {formatar_moeda(valor)}")
            print(f"  Resultado: {resultado} - {motivo}")


if __name__ == "__main__":
    Principal().executar()