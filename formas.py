import math

class Forma:
     def __init__(self, base, altura):
        self.base = base
        self.altura = altura
     def area(self):
        pass

     def perimetro(self):
        pass

class Retangulo(Forma):

     def area(self):
         return self.base * self.altura
     
     def perimetro(self):
         return 2 * (self.base + self.altura)
     
class Triangulo(Forma):
     def __init__(self, base, altura, l1, l2):
         self.base = base
         self.altura = altura
         self.l1 = l1
         self.l2 = l2

     def area(self):
         return (self.base * self.altura) / 2
     
     def perimetro(self):
         return self.base + self.l1 +self.l2
     
class Circulo(Forma):
     def __init__(self, raio):
         self.raio = raio

     def area(self):
         return math.pi * self.raio **2
     
     def perimetro(self):
         return 2 * math.pi *self.raio
     

def escolher_figura():
     print("Escolha a sua figura: ")
     print("1. Retângulo")
     print("2. Triângulo")
     print("3. Circulo")

     figura = int(input("Escolha a sua figura: "))
     if figura == 1:
         base = float(input("Digite a base do retângulo: "))
         altura = float(input("Digite a altura do retângulo: "))
         retangulo = Retangulo(base, altura)
         print(f"A área do retângulo é: {retangulo.area()}")
         print(f"O perimetro do retângulo é: {retangulo.perimetro()}")

     elif figura == 2:
           base = float(input("Digite a base do triângulo: "))
           altura = float(input("Digite a altura do triângulo: "))
           l1 = float(input("Digite o lado 1 do triângulo: "))
           l2 = float(input("Digite o lado 2 do triângulo: "))
           triangulo = Triangulo(base, altura, l1, l2)
           print(f"A área do triângulo é {triangulo.area()}")
           print(f"O perimetro do triângulo é {triangulo.perimetro()}")

     elif figura == 3:
          raio = float(input("Digite o raio do circulo: "))
          circulo = Circulo(raio)
          print(f"A área do circulo é {circulo.area()}")
          print(f"O perimetro do circulo é {circulo.perimetro()}")

escolher_figura()
