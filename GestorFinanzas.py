import os #para usarla en la funcoión de limpiarConsola

#Categorías para gastos
categorias = ["Alimentación", "Transporte", "Entretenimiento", "Salud", "Ropa", "Hogar", "Educación", "Viajes", "Mascotas"]
saldo = 0.0

#Lista para guardar las transacciones que se hacen (guarda diccionarios)
transacciones = []

# Limpia la consola dependiendo del sistema operativo
# 'cls' para Windows, 'clear' para Unix (Linux/macOS)
def limpiarConsola():
    os.system("cls" if os.name == "nt" else "clear")   

def Enter():
    input("Presione Enter para continuar...")



def guardarTransaccion(tipo, monto, categoria):

    global saldo

    #definimos el diccionario
    transaccion = {
        "tipo": tipo,
        "monto": monto,
        "categoria": categoria
    }

    #Guardamos el diccionario transaccion a la lista transacciones
    transacciones.append(transaccion)

    #Según el tipo de transacción (ingreso/gasto) se le aumenta o descuenta al saldo
    if tipo == "+":
        saldo += monto
    elif tipo == "-":
        saldo -= monto



def agregarGasto():

    limpiarConsola()
    print("---✨ Agregar Gasto ✨---\n")

    while True:
        try:
            monto = float(input("Ingrese el monto: "))
            if monto < 0: #Se verifica que el usuario ponga valores positivos
                print("✖️ Solo se aceptan valores positivos")
            else:
                break
        except ValueError:
            print("Solo se permiten números 👀")


    print("Categorías disponibles:")

    #imprime la lista que tenemos de categorias
    for i in range(len(categorias)):
        print(f"{i + 1}. {categorias[i]}")


    while True:
    
        try:
            categoria = int(input("Seleccione la categoría (número): ")) - 1 #restamos 1 porque en el momento que mostramos las categorías con su respectivo número le sumamos 1, entonces se le resta 1 para acceder a la posición correcta de la lista categorias

            if categoria < 0 or categoria >= len(categorias): #Verificamos que el usuario ponga una categoría existente
                print("Categoría no válida. Intentelo de nuevo")
              
            else:
                #imprimimos el monto y la categoría
                print(f"Monto: {monto}\nCategoría: {categorias[categoria]}")

                #Guardamos la transacción
                guardarTransaccion("-", monto, categorias[categoria])
                Enter()
                break

        except ValueError:
            #Verificamos que el usuario solo ponga números
            print("Solo se permiten números 👀")
            Enter()
        


def agregarIngreso():

    limpiarConsola()

    print("---✨ Agregar Ingreso ✨---\n")

    while True:
        try:
            monto = float(input("Ingrese el monto: "))
            if monto < 0: #Se verifica que el usuario ponga valores positivos
                print("✖️ Solo se aceptan valores positivos")
            else:
                #Mostramos el monto y guardamos la transacción
                print(f"Monto: {monto}")
                guardarTransaccion("+", monto, "Ingreso")
                Enter()
                break
        except ValueError:
            #Verificamos que el usuario solo ponga números
            print("Solo se permiten números 👀")

    



def consultarSaldo():
    global saldo

    limpiarConsola()
    if saldo < 0:
        #Significa que el usuario debe dinero, la función abs muestra el valor absoluto del saldo
        print(f"Pilas, debes ${abs(saldo)} 👀")
    else:
        print(f"Saldo actual: ${saldo}")
    Enter()


def historial(tipo):

    limpiarConsola()

    global transacciones

    #Definimos el título del historial dependiendo del tipo de transacción
    if tipo == "-":
        tipoTransaccion = "Gastos"
    elif tipo == "+":
        tipoTransaccion = "Ingresos"

    print(f"---✨ Historial de {tipoTransaccion} ✨---")

    #recorremos la lista de transacciones para filtrar solo las del tipo solicitado
    for transaccion in transacciones:

        #acá mostramos el tipo de transacción dependiendo de lo que tenemos en el diccionario si el tipo de la transacción coincide con el tipo recibido (gasto o ingreso)
        if transaccion["tipo"] == tipo:
            print(f"🔸 Categoría: {transaccion['categoria']}, Monto: {transaccion['monto']}")

    Enter()



def verHistorial():
    
    global transacciones

    while True:
        try:
            limpiarConsola()
            print("---✨ Historial de Transacciones ✨---\n")
            print("1. Gastos\n2. Ingresos\n3. General\n4. Volver al menú principal")
            opcion = int(input("Seleccione una opción: "))
            
            #Llamamos la funcion historial con su parámetro correspondiente
            if opcion == 1:
                historial("-")
            elif opcion == 2:
                historial("+")
            elif opcion == 3:
                limpiarConsola()
                print("\n---✨ Historial General ✨---")

                #mostramos todas las transacciones de la lista
                for transaccion in transacciones:
                    print(f"🔸 Categoría: {transaccion['categoria']}, Monto: {transaccion['monto']}")
                Enter()
            elif opcion == 4:
                #Salimos del bucle para vovler al menu principal
                break
            else:
                print("✖️ Opción no válida. Ingrese un número del 1 al 4.")
                Enter()

        except ValueError:
            #Verificamos que el usuario ponga solo números
            print("👀 Solo se permiten números.")
            Enter()



def Categorias():
    global categorias
    while True:
        limpiarConsola()
        print("\n---✨ Categorias ✨---")
        print("1. Ver categorías\n2. Agregar Categoría\n3. Volver al menú principal")
        try:
            opcion = int(input("Seleccione una opción: "))
            if opcion == 1:
                limpiarConsola()
                #imprimimos todas las categorias de la lista
                print("Categorías disponibles:")
                for categoria in categorias:
                    print(f"🔸 {categoria}")
                Enter()

            elif opcion == 2:
                agregarCategoria() 

            elif opcion == 3:
                break  
            else:
                print("✖️ Opción no válida. Ingrese un número del 1 al 3")
                Enter()

        except ValueError:
            print("Solo se permiten números 👀")
            Enter()   


def agregarCategoria():
    limpiarConsola()

    #imprimimos todas las categorías 
    global categorias
    print("Categorías disponibles:")
    for i in categorias:
        print(f"🔸 {i}")

    while True:
        categoria = input("Ingrese el nombre de la nueva categoría: ")

        #verificamos que no sea una cadena vacía
        if categoria == "":
            print("✖️ Categoría inválida. No puede estar vacía.")

        #verificamos que no ponga una categoría existente
        elif categoria in categorias:
            print("⚠️ Esa categoría ya existe. Intente con otro nombre.")

        #Guardamos la categoría nueva en la lista categorías
        else:
            categorias.append(categoria)
            print(f"✅ Categoría '{categoria}' agregada exitosamente.")
            Enter()
            break  # Salimos del bucle solo si todo salió bien

        Enter()



def menu():

    global categorias

    while True:
        try:
            limpiarConsola()
            print("\n---✨ Menú Principal ✨---")
            print("1. Agregar gasto\n2. Agregar ingreso\n3. Consultar saldo actual\n4. Ver historial\n5. Categorías\n6. Salir")


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
                Categorias()
            elif opcion == 6:
                print("Saliendo del programa...")
                exit(0)
        except ValueError:
            print("Solo se aceptan números 👀")
            Enter()
            
menu()