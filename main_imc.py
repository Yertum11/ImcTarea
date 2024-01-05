# Pregunta al usuario el número de pacientes
while True:
    try:
        num_pacientes = int(input("Número de Pacientes: "))
        if num_pacientes > 0:
            break
        else:
            print("Lo siento, por favor ingresa un número válido mayor que 0.")
    except ValueError:
        print("Lo siento, por favor ingresa un número entero válido.")

# Bucle para ingresar los datos de cada paciente
while num_pacientes > 0:
    # Solicita el nombre de la persona
    nombre_persona = input("Ingresa tu nombre: ")

    # Solicita la edad de la persona
    while True:
        try:
            edad = int(input("Ingresa tu Edad: "))
            if edad > 0:
                break
            else:
                print("Lo siento, por favor ingresa una edad válida mayor que 0.")
        except ValueError:
            print("Lo siento, por favor ingresa un número entero válido para la edad.")

    # Solicita la estatura de la persona
    while True:
        try:
            estatura = float(input("Ingresa tu altura: "))
            if estatura > 0:
                break
            else:
                print("Lo siento, por favor ingresa una estatura válida mayor que 0.")
        except ValueError:
            print("Lo siento, por favor ingresa un número válido para la estatura.")

    # Solicita el peso de la persona en kg
    while True:
        try:
            peso = float(input("Ingresa tu peso en kg: "))
            if peso > 0:
                break
            else:
                print("Lo siento, por favor ingresa un peso válido mayor que 0.")
        except ValueError:
            print("Lo siento, por favor ingresa un número válido para el peso.")

    # Calcula el índice de masa corporal (IMC)
    imc = peso / estatura**2

    # Imprime el IMC calculado
    print("Tu índice de masa corporal es: " + str(imc))

    # Determina la categoría de peso según el IMC
    if 0 <= imc <= 18.5:
        print("Delgadez severa")
    elif 18.5 < imc <= 24.99:
        print("Normal/saludable")
    elif 25.0 <= imc <= 29.9:
        print("Usted tiene Sobrepeso")
    elif 30.0 <= imc <= 34.99:
        print("Obesidad leve")
    elif 35.0 <= imc <= 39.9:
        print("Obesidad grado 2")
    elif imc >= 40.0:
        print("Obesidad grado 3")

    # Reduce el contador de pacientes en 1
    num_pacientes -= 1
