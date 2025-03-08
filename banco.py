class ContaBancaria:
     def __init__(self, numero_conta):
          self.__saldo = 0
          self.numero_conta = numero_conta  
     def depositar(self,valor):
         if valor > 0:
              self.__saldo += valor
              print(f"Depósito de {valor} feito com sucesso!")
         else:
              print("valor inválido para depósiito!")

     def sacar(self, valor):
          if valor > 0:
             if valor <= self.__saldo:
                self.__saldo -= valor
                print(f"Saque de {valor} feito com sucesso!")
             else:
                  print("Valor insuficiente para saque!")
          else:
               print("Valor inválido para saque!")

     def get_saldo(self):
          return self.__saldo
     
numero_conta = input("Digite o número da conta: ")

conta = ContaBancaria(numero_conta)
valor_depositar = (float(input("Digite o valor que deseja depositar: ")))
conta.depositar(valor_depositar)
saldo_atual = conta.get_saldo()
print(f"O saldo atual é de {saldo_atual}")
valor_sacar = (float(input("Digite o valor que deseja sacar: ")))
conta.sacar(valor_sacar)
saldo_atual = conta.get_saldo()
print(f"O saldo atual é de {saldo_atual}")
