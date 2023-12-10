Pacientes = int(input( "Numero de Pacientes: "))
while Pacientes > 0:


 NombreDePersona = input ("Ingresa tu nombre: ")

 Edad = int (input("Ingresa tu Edad: "))
 Estatura = float(input("Ingresa tu altura: "))
 Peso = float (input("Ingresa tu peso en kg: "))
 IMC = Peso / Estatura**2    
 print ("TU indice de masa corporal es: " + str(IMC) )
 if IMC >= 0 and IMC <= 18.5 :
        print ("Delgadez severa")
 elif IMC >= 18.50 and IMC <= 24.99 :
        print ("Normal/saludable")
 elif IMC >= 25.0 and IMC <= 29.9 :
        print ("Usted tiene Sobrepeso")
 elif IMC >= 30.00 and IMC <= 34.99:
        print ("obesidad leve")
 elif IMC >= 35.00 and IMC <= 39.9:
        print ("obesidad grado 2")
 elif IMC >= 40.00:
        print ("obesidad grado 3")

 Pacientes = Pacientes - 1
         