datos = []
print ("cantidad de alumnos a calificaar")
cantAlu: int= int (input())
promedio=0
for i in range(1,cantAlu,+1):
    print("dicte las notas por alumno")
    aux= int( input( ))
    promedio = (promedio+aux)
    datos.append(aux)
print ("nota de alumnos es: ",datos,"el promedio es =",(promedio/(cantAlu-1)))



