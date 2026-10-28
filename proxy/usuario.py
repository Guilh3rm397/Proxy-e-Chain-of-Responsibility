from abc import ABC, abstractmethod


class InterfaceUsuario(ABC):
    """Interface comum entre o objeto real e o Proxy."""

    @abstractmethod
    def obter_nome(self):
        pass

    @abstractmethod
    def obter_cpf(self):
        pass

    @abstractmethod
    def obter_endereco(self):
        pass


class Usuario(InterfaceUsuario):
    """Objeto real: devolve todos os dados sem nenhuma restrição."""

    def __init__(self, nome, cpf, endereco):
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco

    def obter_nome(self):
        return self.nome

    def obter_cpf(self):
        return self.cpf

    def obter_endereco(self):
        return self.endereco