# Variables globales
saldo = 1000.0  # El saldo inicial en la cuenta
historial = []  # Lista para guardar las transacciones realizadas
pin_actual = "1234"  # PIN inicial

def consultar_saldo():
    global saldo
    print(f"Tu saldo actual es: ${saldo:.2f}")

def depositar_dinero():
    global saldo
    cantidad = float(input("Ingresa la cantidad a depositar: $"))
    if cantidad > 0:
        saldo += cantidad
        historial.append(f"Depósito: +${cantidad:.2f}")
        print(f"Has depositado: ${cantidad:.2f}")
    else:
        print("La cantidad a depositar debe ser positiva.")

def retirar_dinero():
    global saldo
    cantidad = float(input("Ingresa la cantidad a retirar: $"))
    if 0 < cantidad <= saldo:
        saldo -= cantidad
        historial.append(f"Retiro: -${cantidad:.2f}")
        print(f"Has retirado: ${cantidad:.2f}")
    elif cantidad > saldo:
        print("No tienes suficiente saldo para retirar esa cantidad.")
    else:
        print("La cantidad a retirar debe ser positiva.")

def ver_historial():
    if historial:
        print("Historial de transacciones:")
        for transaccion in historial:
            print(transaccion)
    else:
        print("No hay transacciones realizadas.")

def cambiar_pin():
    global pin_actual
    pin_ingresado = input("Ingresa tu PIN actual: ")
    if pin_ingresado == pin_actual:
        nuevo_pin = input("Ingresa tu nuevo PIN: ")
        confirmar_pin = input("Confirma tu nuevo PIN: ")
        if nuevo_pin == confirmar_pin:
            pin_actual = nuevo_pin
            print("PIN cambiado con éxito.")
        else:
            print("Los PIN no coinciden. Intenta de nuevo.")
    else:
        print("PIN incorrecto. No se puede cambiar el PIN.")

def menu():
    while True:
        print("\nBienvenido al Cajero Automático")
        print("1. Consultar Saldo")
        print("2. Depositar Dinero")
        print("3. Retirar Dinero")
        print("4. Ver Historial de Transacciones")
        print("5. Cambiar PIN de Seguridad")
        print("6. Salir")
        
        opcion = input("Elige una opción: ")
        
        if opcion == '1':
            consultar_saldo()
        elif opcion == '2':
            depositar_dinero()
        elif opcion == '3':
            retirar_dinero()
        elif opcion == '4':
            ver_historial()
        elif opcion == '5':
            cambiar_pin()
        elif opcion == '6':
            print("Gracias por usar el Cajero Automático. ¡Hasta luego!")
            break
        else:
            print("Opción inválida, por favor elige nuevamente.")

# Llamada directa al menú
menu()
