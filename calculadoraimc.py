#calculadora imc
def calcular_imc (peso , altura):
    imc = peso / (altura ** 2)
    return imc 
peso = float(input("digite o seu peso (kg):"))
altura = float(input("digite a sua altura(m):"))

imc = calcular_imc(peso, altura)
print("seu imc é: ", imc )
