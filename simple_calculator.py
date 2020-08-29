def ingresa_num():
    a = True
    while a == True:
        try:
            num = input("Ingrese el un numero: ")
            num = int(num)
            a = False
        except ValueError:
            print("No es un numero valido ")

    return num

def suma(a, b):
    print("La suma es: ", a+b)

def resta(a, b):
    print("La resta es: ", a-b)

def mult(a, b):
    print("La Multiplicación es: ", a*b)

def div(a, b):
    try:
        if b == 0:
            print("Solo se permiten valores mayores a cero")
            div(ingresa_num(), ingresa_num())
        else:
            print("La División es: ", a/b)
    except ZeroDivisionError:
        print(":: División por Cero :: Operacion incorrecta ::")
        div(ingresa_num(), ingresa_num())

while True:
    print("\n1. Suma ")
    print("2. Resta ")
    print("3. Multiplicación ")
    print("4. División ")
    print("5. Salir\n ")

    try:
        opc = int(input( "Ingrese una opción: " ))
        if opc == 1:
            print("\nSuma")
            suma(ingresa_num(), ingresa_num())
        elif opc == 2:
            print("\nResta")
            resta(ingresa_num(), ingresa_num())
        elif opc == 3:
            print("\nMultiplicación")
            mult(ingresa_num(), ingresa_num())
        elif opc == 4:
            print("\nDivisión")
            div(ingresa_num(), ingresa_num())
        else:
            break

    except ValueError:
        print("La opción que marcó es incorrecta")