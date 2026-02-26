print("#################################")
print("######Calculadora de notas#######")
print("#################################")

numeronotas = float(input("ingrese el numero de notas a promediar: "))
Sumatoria = 0
i=1

while (i <= numeronotas) :
    
    print("ingrese la nota numero ",i)
    nota=float(input())
    Sumatoria = Sumatoria + nota
    i+=1

promedio = Sumatoria/numeronotas

print("el promedio de notas es ",promedio)
