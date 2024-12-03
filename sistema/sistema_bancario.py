import random

class ContaCorrente:
    def __init__(self, nome_titular, senha):
        self.nome_titular = nome_titular
        self.numero_conta = random.randint(100, 999)
        self.__senha = senha
        self.__saldo_corrente = 0.0
        self.bloqueada = False
        self.tentativas = 0

    def verificar_senha(self, senha):
        if self.bloqueada:
            print("Conta bloqueada. Dirija-se à agência para desbloqueio.")
            return False
        if senha == self.__senha:
            self.tentativas = 0
            return True
        else:
            self.tentativas += 1
            print(f"Senha incorreta. Tentativa {self.tentativas} de 3.")
            if self.tentativas >= 3:
                self.bloqueada = True
                print("Conta bloqueada após 3 tentativas incorretas.")
            return False

    def set_saldo(self, saldo):
        if saldo >= 0:
            self.__saldo_corrente = saldo

    def get_saldo(self):
        return self.__saldo_corrente

    def depositar(self, valor):
        if valor > 0:
            self.__saldo_corrente += valor
            print("Depósito efetuado com sucesso!")
        else:
            print("Valor inválido para depósito.")

    def sacar(self, valor, senha):
        if not self.verificar_senha(senha):
            return
        if valor > 0 and valor <= self.__saldo_corrente:
            self.__saldo_corrente -= valor
            print("Saque efetuado com sucesso!")
        else:
            print("Saldo insuficiente ou valor inválido.")

    def aplicar(self, valor, conta_poupanca, senha):
        if not self.verificar_senha(senha):
            return
        if valor > 0 and valor <= self.__saldo_corrente:
            self.__saldo_corrente -= valor
            conta_poupanca.depositar(valor)
            print("Aplicação efetuada com sucesso!")
        else:
            print("Saldo insuficiente ou valor inválido.")


class ContaPoupanca(ContaCorrente):
    def __init__(self, nome_titular, senha):
        super().__init__(nome_titular, senha)
        self.__saldo_poupanca = 0.0

    def depositar(self, valor):
        if valor > 0:
            self.__saldo_poupanca += valor

    def resgatar(self, valor, conta_corrente, senha):
        if not self.verificar_senha(senha):
            return
        if valor > 0 and valor <= self.__saldo_poupanca:
            self.__saldo_poupanca -= valor
            conta_corrente.set_saldo(conta_corrente.get_saldo() + valor)
            print("Resgate efetuado com sucesso!")
        else:
            print("Saldo insuficiente na poupança.")

    def extrato(self):
        # Usando `self` para acessar a classe base
        print(f"Titular: {self.nome_titular}")
        print(f"Número da conta: {self.numero_conta}")
        print(f"Saldo da Conta Corrente: R$ {self.get_saldo():.2f}")
        print(f"Saldo da Conta Poupança: R$ {self.__saldo_poupanca:.2f}")


# Simulação do sistema bancário
print("Bem-vindo ao Banco Recife!")
nome = input("Digite o nome do titular da conta: ")
senha = input("Crie uma senha numérica de 4 dígitos: ")

# Cadastro da conta
conta_corrente = ContaCorrente(nome, senha)
conta_poupanca = ContaPoupanca(nome, senha)

print("Realize seu primeiro depósito de no mínimo R$ 10,00!")
while True:
    valor_inicial = float(input("Valor do depósito: "))
    if valor_inicial >= 10:
        conta_corrente.depositar(valor_inicial)
        print(f"Conta criada! Número da conta: {conta_corrente.numero_conta}")
        break
    else:
        print("O depósito inicial deve ser de no mínimo R$ 10,00.")

# Operações
while True:
    print("\nMenu de Operações:")
    print("1. Extrato")
    print("2. Depositar na Conta Corrente")
    print("3. Sacar da Conta Corrente")
    print("4. Aplicar na Poupança")
    print("5. Resgatar da Poupança")
    print("6. Sair")
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        conta_poupanca.extrato()
    elif opcao == 2:
        valor = float(input("Digite o valor a depositar: "))
        conta_corrente.depositar(valor)
    elif opcao == 3:
        valor = float(input("Digite o valor a sacar: "))
        senha = input("Digite sua senha: ")
        conta_corrente.sacar(valor, senha)
    elif opcao == 4:
        valor = float(input("Digite o valor a aplicar na poupança: "))
        senha = input("Digite sua senha: ")
        conta_corrente.aplicar(valor, conta_poupanca, senha)
    elif opcao == 5:
        valor = float(input("Digite o valor a resgatar da poupança: "))
        senha = input("Digite sua senha: ")
        conta_poupanca.resgatar(valor, conta_corrente, senha)
    elif opcao == 6:
        print("Obrigado por usar o Banco Recife! Até logo!")
        break
    else:
        print("Opção inválida.")
