from datetime import datetime

class Cliente:

    def __init__(self, endereco):
        self.endereco = endereco
        self.lista_contas= []

    def adicionar_contas(self, conta):
        self.lista_contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, endereco, cpf, nome, data_nascimento):
        super().__init__(endereco)
        self.cpf = cpf
        self.nome = nome 
        self.data_nascimento = data_nascimento
class Conta:
    numero_conta = 0
    limite_saque_diario = 500.0
    quantidade_saques = 0

    def __init__(self, cliente, saldo = 0.0, agencia = "001"):
        Conta.numero_conta += 1
        self._saldo = saldo
        self._numero_conta = Conta.numero_conta
        self.agencia = agencia 
        self.cliente = cliente
        self.historico = Historico()

    @classmethod
    def nova_conta(cls, cliente):
        return cls(cliente)
    
    def sacar(self,valor):
        if valor > self.limite_saque_diario:
            print("❌ Erro: O valor do saque excede o limite permitido de R$ 500.00!")
            self.historico.realizar_transacao("Saque Negado (Acima do Limite)", valor)
            return False

        if self.quantidade_saques > 3:
            print("❌ Erro: Número máximo de saques diários atingido (3 saques).")
            self.historico.realizar_transacao("Saque Negado (Excedeu o Limite Diário)", valor)
            return False

        if self._saldo < valor:
            print("❌ Erro: Saldo insuficiente!")
            self.historico.realizar_transacao("Saque Negado (Saldo Insuficiente)", valor)
            return False

        self._saldo -= valor
        self.quantidade_saques += 1
        self.historico.realizar_transacao("Saque", valor)
        print(f"✅ Saque de R${valor:.2f} realizado com sucesso!")
        return True

    def depositar(self, valor):
        self._saldo += valor
        self.historico.realizar_transacao("Depósito", valor)

    def saldo(self):
        return self._saldo

class ContaCorrente(Conta):
    pass

class Historico:
    def __init__(self):
        self.transacoes = []
    
    def realizar_transacao(self, tipo, valor):
        data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.transacoes.append(f"{data_hora} - {tipo}: R${valor:.2f}")

    def exibir_historico(self):
        for transacao in self.transacoes:
            print(transacao)

class Transacao: #interface
    pass

class SaqueDeposito(Transacao):
    pass

cliente1 = Cliente("Rua José 123")
conta1 = Conta(cliente1)

cliente1.adicionar_contas(conta1)

conta1.depositar(1000)
conta1.sacar(200)  


print(f"\n💰 Saldo final: R${conta1.saldo():.2f}")
conta1.historico.exibir_historico()