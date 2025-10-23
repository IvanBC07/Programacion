
dias_semana = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]

suma_temperaturas = 0
dias_mas25 = 0
temp_max = -100
dia_temp_max = ""

for dia in dias_semana:
    temp_dia = float(input(f"Introduce la temperatura media de {dia}: "))
 
    suma_temperaturas += temp_dia
    if temp_dia > 25:
        dias_mas25 += 1
  
    if temp_dia > temp_max:
        temp_max = temp_dia
        dia_temp_max = dia

media = suma_temperaturas / len(dias_semana)

print(f"Temperatura media de todos los días = {media} Cº")
print(f"Hay una cantidad de {dias_mas25} días que hacen más de 25 Cº")
print(f"El día con la temperatura más alta es el {dia_temp_max}")



