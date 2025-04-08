print("Olá, blz? Esse programa irá converter graus Celsius para Fahrenheit e vice-versa.")

resp = str(input("""Digite "C" para converter de Celsius para Fahrenheit, ou "F" para converter de Fahrenheit para Celsius: """))

while resp != "C" and resp != "F":
    print("Entrada inválida. Por favor, digite 'C' ou 'F'.")
    resp = str(input("""Digite "C" para Celsius ou "F" para Fahrenheit: """))

graus = float(input("Digite o valor da temperatura: "))

def celsius_para_fahrenheit(celsius):
    return celsius * 9/5 + 32

def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

if resp == "C":
    resposta = celsius_para_fahrenheit(graus)
    print(f"{graus}° Celsius é igual a {resposta:.2f}° Fahrenheit.")
