import math
import random

class JogoDado:
     def lancar_dados(self):
          numero = random.randint(1,6)
          raiz = math.sqrt(numero)
          print(f"O número gerado é {numero}")
          print(f"A raiz quadrada desse número é {raiz}")

jogo = JogoDado()
jogo.lancar_dados()
