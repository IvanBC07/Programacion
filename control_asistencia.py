#Definimos los dias de la semana.
Dias_semana = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"]

print (Dias_semana)

#Creamos las variables necesarias.
dias_asistidos = 0
dias_ausencia = 0
#Creamos el bucle for para que lea y detecte cuantos días ha asistido y faltado a clase.
for dias in Dias_semana:
    Asistencia=(input(f"Dime si ha asistido poniendo 's' o si ha faltado 'n' el dia {dias}:"))

    if Asistencia == "s":
        dias_asistidos += 1;

    elif Asistencia == "n":
        dias_ausencia += 1

#Vamos a calcular el porcentaje de asistencia en esos 5 dias.
Porcentaje_asistencia = (dias_asistidos/5)*100


# Escribimos el porcentaje de asistencia del alumno
print (f"El porcentaje de asistencia del usuario ha sido un {Porcentaje_asistencia}%")

# Escribimos los días que ha asistido y faltado el alumno
print (f"El alumno ha asistido {dias_asistidos} días.")
print (f"El alumno ha faltado {dias_ausencia} días.")
