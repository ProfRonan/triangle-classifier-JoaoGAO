a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))

if a + b > c and a + c > b and b + c > a:
    if a == b and b == c:
        print("Equilátero")
    elif a == b or a == c or b == c:
        print("Isósceles")
    else:
        print("Escaleno")
else:
    print("Não é um triângulo.")
    