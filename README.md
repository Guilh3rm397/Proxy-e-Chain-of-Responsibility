# Padrões de Projeto: Proxy e Chain of Responsibility

Projeto acadêmico desenvolvido em Python para demonstrar dois padrões de projeto comportamentais: **Proxy** e **Chain of Responsibility**.

## Objetivos

- Aplicar o padrão **Proxy** para controlar a exibição de dados pessoais de um usuário.
- Aplicar o padrão **Chain of Responsibility** para validar transações bancárias em uma sequência de regras.
- Demonstrar os resultados por meio de uma classe `Principal` em cada exemplo.

## Tecnologias

- Python 3
- Bibliotecas padrão do Python
- Não é necessário instalar dependências externas.

## Estrutura do projeto

```text
Proxy e Chain of Responsibility/
├── proxy/
│   ├── principal.py
│   ├── proxy_usuario.py
│   └── usuario.py
└── chain_of_responsibility/
    ├── principal.py
    ├── conta.py
    ├── regra_transacao.py
    └── regras.py
```

## 1. Padrão Proxy

O exemplo de Proxy controla como os dados de um usuário são apresentados.

Regras implementadas:

- **Nome:** exibido normalmente.
- **CPF:** os três primeiros e os dois últimos dígitos são ocultados por asteriscos.
- **Endereço:** o acesso é bloqueado e uma mensagem de acesso negado é apresentada.

A classe `Usuario` representa o objeto real. A classe `ProxyUsuario` atua como intermediária e aplica as restrições de exibição. A classe `Principal` demonstra o comportamento.

### Como executar

Abra um terminal na pasta do projeto e execute:

```bash
cd proxy
python principal.py
```

Exemplo de saída:

```text
=== Padrão Proxy ===
Nome: Maria Silva
CPF: ***45678**
Endereço: Acesso negado ao endereço.
```

## 2. Padrão Chain of Responsibility

O exemplo bancário verifica uma transação por meio de uma cadeia de regras. A transação só é aprovada se passar por todas as validações.

As regras são executadas nesta ordem:

1. **Regra de saldo:** verifica se há saldo suficiente.
2. **Regra de valor máximo:** contas comuns podem realizar transações de até R$ 1.000,00; contas premium, de até R$ 10.000,00.
3. **Regra de bloqueio judicial:** impede a transação quando a conta possui bloqueio judicial.

A classe `RegraTransacao` define o mecanismo de encaminhamento para a próxima regra. As classes em `regras.py` implementam as validações. A classe `Principal` executa cenários aprovados e reprovados.

### Como executar

Abra um terminal na pasta do projeto e execute:

```bash
cd chain_of_responsibility
python principal.py
```

O programa apresenta diferentes testes, incluindo saldo insuficiente, valor acima do limite, bloqueio judicial e transações válidas.

## Conceitos demonstrados

| Padrão                  | Finalidade no projeto                                                |
| ----------------------- | -------------------------------------------------------------------- |
| Proxy                   | Intermediar o acesso aos dados do usuário e restringir sua exibição. |
| Chain of Responsibility | Encaminhar a transação por uma sequência de regras de validação.     |
