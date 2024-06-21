import pickle
import sys
import os
import random

def limpiar_pantalla():
    if os.name == 'posix': 
        _ = os.system('clear')
    else:  
        _ = os.system('cls')

def generar_numero_ticket():
    return random.randrange(1000, 9999)

def guardar_ticket(ticket, archivo):
    with open(archivo, "wb") as f:
        pickle.dump(ticket, f)

def cargar_ticket(archivo):
    if os.path.isfile(archivo):
        with open(archivo, "rb") as f:
            return pickle.load(f)
    else:
        return {}

def menu_principal():
    limpiar_pantalla()
    while True:
        print("Bienvenido al sistema de tickets")
        print("1. Alta ticket")
        print("2. Leer ticket")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            alta_ticket()
        elif opcion == '2':
            leer_ticket()
        elif opcion == '3':
            confirmacion_salida = input("¿Está seguro que desea salir? (s/n): ")
            if confirmacion_salida.lower() == 's':
                sys.exit()
        else:
            input("Opción no válida. Presione Enter para continuar.")

def alta_ticket():
    limpiar_pantalla()
    nombre = input("Ingrese su nombre: ")
    sector = input("Ingrese el sector: ")
    asunto = input("Ingrese el asunto: ")
    problema = input("Describa el problema: ")

    numero_ticket = generar_numero_ticket()

    ticket = {
        'Numero': numero_ticket,
        'Nombre': nombre,
        'Sector': sector,
        'Asunto': asunto,
        'Problema': problema
    }

    print("\nTicket creado exitosamente:")
    mostrar_ticket(ticket)

    guardar = 'tickets.pkl'
    guardar_ticket(ticket, guardar)

    opcion = input("\n¿Desea crear otro ticket? (s/n): ")
    if opcion.lower() == 's':
        alta_ticket()

def mostrar_ticket(ticket):
    print(f"Numero de Ticket: {ticket['Numero']}")
    print(f"Nombre: {ticket['Nombre']}")
    print(f"Sector: {ticket['Sector']}")
    print(f"Asunto: {ticket['Asunto']}")
    print(f"Problema: {ticket['Problema']}")
    print("Recuerde el número de ticket.")

def leer_ticket():
    limpiar_pantalla()
    archivo = 'tickets.pkl'
    ticket = cargar_ticket(archivo)

    if not ticket:
        print("No hay tickets almacenados.")
        input("\nPresione Enter para continuar.")
        return

    numero_ticket = input("Ingrese el número de ticket que desea leer: ")

    if int(numero_ticket) == ticket['Numero']:
        print("\nTicket encontrado:")
        mostrar_ticket(ticket)
    else:
        print("\nTicket no encontrado.")

    opcion = input("\n¿Desea leer otro ticket? (s/n): ")
    if opcion.lower() == 's':
        leer_ticket()

if __name__ == "__main__":
    menu_principal()
