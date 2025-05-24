import os

categorias = ["Alimentación", "Transporte", "Entretenimiento", "Salud", "Ropa", "Hogar", "Educación", "Viajes", "Mascotas"]
saldo = 0.0
transacciones = []

def limpiarConsola():
    os.system("cls" if os.name == "nt" else "clear")

def Enter():
    input("Presione Enter para continuar...")



def guardarTransaccion(tipo, monto, categoria):

    global saldo

    transaccion = {
        "tipo": tipo,
        "monto": monto,
        "categoria": categoria
    }

    transacciones.append(transaccion)

    if tipo == "+":
        saldo += monto
    elif tipo == "-":
        saldo -= monto



def agregarGasto():
    
    monto = float(input("Ingrese el monto: "))
    print("Categorías disponibles:")

    for i in range(len(categorias)):
        print(f"{i + 1}. {categorias[i]}")

    try:
        
        categoria = int(input("Seleccione la categoría (número): ")) - 1
            

        if categoria < 0 or categoria >= len(categorias):
            print("Categoría no válida.")
            return
        else:
            print(f"Monto: {monto}\nCategoría: {categorias[categoria]}")

        guardarTransaccion("-", monto, categorias[categoria])
        Enter()

    except ValueError:
        print("Solo se permiten números 👀")
        Enter()
        



def agregarIngreso():
    monto = float(input("Ingrese el monto: "))
    print(f"Monto: {monto}")
    guardarTransaccion("+", monto, "Ingreso")
    Enter()



def consultarSaldo():
    global saldo

    limpiarConsola()
    if saldo < 0:
        print(f"Pilas, debes ${abs(saldo)} 👀")
    else:
        print(f"Saldo actual: ${saldo}")
    Enter()


def historial(tipo):

    limpiarConsola()

    global transacciones

    if tipo == "-":
        tipoTransaccion = "Gastos"
    elif tipo == "+":
        tipoTransaccion = "Ingresos"

    print(f"\n---✨ Historial de {tipoTransaccion} ✨---\n")
    for transaccion in transacciones:
        if transaccion["tipo"] == tipo:
            print(f"🔸 Categoría: {transaccion['categoria']}, Monto: {transaccion['monto']}")

    Enter()



def verHistorial():

    limpiarConsola()    
    
    global transacciones

    print("---✨ Historial de Transacciones ✨---\n")
    print("1. Gastos\n2. Ingresos\n3. General")

    try:
        
        opcion = int(input("Seleccione una opción: "))
        if opcion < 1 or opcion > 3:
            print("Opción no válida.")
            return
        elif opcion == 1:
            historial("-")
        elif opcion == 2:
            historial("+")
        elif opcion == 3:
            limpiarConsola()
            print("\n---✨ Historial General ✨---")
            for transaccion in transacciones:
                print(f"🔸 Categoría: {transaccion['categoria']}, Monto: {transaccion['monto']}")
            Enter()

    except ValueError:
        print("Solo se permiten números 👀")  
        Enter()      


def agregarCategoria():
    limpiarConsola()
    global categorias
    print("Categorías disponibles:")
    for i in categorias:
        print(f"🔸 {i}")


    categoria = input("Agregue la categoría: ")
    while categoria == "":
        categoria = input("Categoría inválida ✖️, intente de nuevo: ")
    
    categorias.append(categoria)
    print("Categoría agregada exitosamente")
    Enter()



def menu():

    global categorias

    
    while True:
        try:
            limpiarConsola()
            print("\n---✨ Menú Principal ✨---")
            print("1. Agregar gasto\n2. Agregar ingreso\n3. Consultar saldo actual\n4. Ver historial\n5. Agregar Categoría\n6. Salir")


            opcion = int(input("Seleccione una opción: "))

            if opcion < 1 or opcion > 6:
                print("Opción no válida.")
                Enter()

            elif opcion == 1:
                agregarGasto()
            elif opcion == 2:
                agregarIngreso()
            elif opcion == 3:
                consultarSaldo()
            elif opcion == 4:
                verHistorial()
            elif opcion == 5:
                agregarCategoria()
            elif opcion == 6:
                print("Saliendo del programa...")
                exit(0)
        except ValueError:
            print("Solo se aceptan números 👀")
            Enter()
            
menu()