import math

class Calculadora:
    def somar(self, num1, num2):
        return num1 + num2
    def subtrair(self, num1, num2):
        return num1 - num2
    def mult(self, num1, num2):
        return num1 * num2
    def div(self, num1, num2):
        if num2 == 0:
            return "ERRO!"
        return num1 / num2
    
calculadora = Calculadora()

print("Escolha uma operação: ")
print("1. Adição")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")

escolha = input("Escolha: ")

if escolha in ("1", "2", "3", "4"):
    num1 = float(input("Digite o seu primeiro número: "))
    num2 = float(input("Digite o seu segundo número: "))

    if escolha == "1":
        resultado = calculadora.somar(num1, num2)
        print(f"A soma é igual a {resultado}")

    if escolha == "2":
        resultado = calculadora.subtrair(num1, num2)
        print(f"A subtração é igual a {resultado}")

    if escolha == "3":
        resultado = calculadora.mult(num1, num2)
        print(f"A multiplicação é igual a {resultado}")

    if escolha == "4":
        resultado = calculadora.div(num1, num2)
        print(f"A divisão é igual a {resultado}")
