from Funcion import Nota_estudiante

x = input("Ingrese la nota del estudiante: ")
notafinal = Nota_estudiante(x)

if x == "10" and notafinal == "D":

    print("la nota del estudiante es: ", x)
    print("Por lo que se le asignara: ", notafinal)

    print ("Programa ejecutado exitosamente")
else:
    print("error del programa")

