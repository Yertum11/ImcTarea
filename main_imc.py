# Pregunta al usuario el número de pacientes
num_pacientes = int(input("Número de Pacientes: "))

# Bucle para ingresar los datos de cada paciente
while num_pacientes > 0:
    # Solicita el nombre de la persona
    nombre_persona = input("Ingresa tu nombre: ")

    # Solicita la edad de la persona
    edad = int(input("Ingresa tu Edad: "))

    # Solicita la estatura de la persona
    estatura = float(input("Ingresa tu altura: "))

    # Solicita el peso de la persona en kg
    peso = float(input("Ingresa tu peso en kg: "))

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
