import random

class JogoAdivinhacao:
     def __init__(self):
          self.numero =  random.randint(1,100)
    
     def jogar(self):
          tentativas = 0
          while True:
               palpite = int(input("Digite um número de 1 a 100:  "))
               tentativas +=1
               
               if palpite < self.numero:
                    print("O seu número é menor que o valor secreto, tente um número maior!")
               elif palpite > self.numero:
                    print("O seu número é maior que o valor secreto, tente um número menor!")
               else:
                    print(f"Parabéns!! Você acertou em {tentativas} tentativas")
                    break

jogo = JogoAdivinhacao()
jogo.jogar()
