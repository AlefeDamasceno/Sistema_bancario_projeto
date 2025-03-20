from datetime import datetime

class Cliente:

    def __init__(self, endereco, lista_contas):
        self.endereco = endereco
        self.lista_contas= []

    def adicionar_contas(self, conta):
        self.lista_contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, endereco, lista_contas, cpf, nome, data_nascimento):
        super().__init__(endereco, lista_contas)
        self.cpf = cpf
        self.nome = nome 
        self.data_nascimento = data_nascimento
class Conta:
    numero_conta = 0

    def __init__(self, cliente, saldo = 0.0, agencia = "001"):
        Conta.numero_conta += 1
        self._saldo = saldo
        self._numero_conta = Conta.numero_conta
        self.agencia = agencia 
        self.cliente = cliente
        self.historico = []

    def nova_conta(cliente):
        return Conta(cliente)
    
    def sacar(self,valor):
        if self._saldo >= valor:
            self._saldo -= valor
            self.historico.adicionar.append("Saque", valor)
            return True
        else:
            return False

    def depositar(self, valor):
        self._saldo += valor
        self.historico.adicionar.append("Deposito", valor)

    def saldo(self):
        return self._saldo

class ContaCorrente(Conta):
    pass

class Historico:
    
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

cliente1 = Cliente("Alefe", "Rua josé 123")
conta1 = Conta(cliente1)

cliente1.adicionar_contas(conta1)

conta1.depositar(1000)
conta1.sacar(300)

print(f"\n💰 Saldo final: R${conta1.saldo():.2f}")
conta1.historico.exibir_historico()