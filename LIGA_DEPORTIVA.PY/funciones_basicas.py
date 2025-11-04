from tabulate import tabulate
from datetime import datetime
# =========================
# Utilidades comunes
# =========================

def generar_id(lista):
    if not lista:
        return 1
    return max(item["id"] for item in lista) + 1

def leer_texto(mensaje):
    while True:
        texto = input(mensaje).strip()
        if texto:
            return texto
        print("⚠️  No puede estar vacío.")

def leer_int(mensaje, minimo=None, maximo=None):
    while True:
        try:
            valor = int(input(mensaje))
            if (minimo is None or valor >= minimo) and (maximo is None or valor <= maximo):
                return valor
            print("Valor fuera de rango.")
        except ValueError:
            print("Introduce un número entero.")

def imprimir_tabla(filas, columnas, titulo=""):
    if not filas:
        print(f"\n{titulo} (sin datos)\n")
        return
    print("\n" + titulo)
    print(tabulate(filas, headers=columnas, tablefmt="grid"))

def leer_fecha_hora():
    while True:
        fecha = input("Fecha (YYYY-MM-DD): ")
        hora = input("Hora (HH:MM): ")
        try:
            datetime.strptime(f"{fecha} {hora}", "%Y-%m-%d %H:%M")
            return fecha, hora
        except ValueError:
            print("Hora invalida.")
