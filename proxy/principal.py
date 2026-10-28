from usuario import Usuario
from proxy_usuario import ProxyUsuario


class Principal:
    def executar(self):
        usuario_real = Usuario("Maria Silva", "12345678900", "Rua das Flores, 123")
        proxy = ProxyUsuario(usuario_real)

        print("=== Padrão Proxy ===")
        print("Nome:", proxy.obter_nome())
        print("CPF:", proxy.obter_cpf())

        try:
            print("Endereço:", proxy.obter_endereco())
        except PermissionError as erro:
            print("Endereço:", erro)


if __name__ == "__main__":
    Principal().executar()
    
''' === Padrão Proxy ===
Nome: Maria Silva
CPF: ***45678**
Endereço: Acesso negado ao endereço. '''
