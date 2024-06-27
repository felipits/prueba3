import json
import datetime

ventas = []

vinilos_info = {
    "linda": {"precio": 5000, "artista": "miguel bose", "estilo": "romantica"},
    "atado a tu amor": {"precio": 6000, "artista": "chayanne", "estilo": "romantica"},
    "un verano sin ti": {"precio": 4990, "artista": "bad bunny", "estilo": "regaeton"},
    "el ultimo baile": {"precio": 3990, "artista": "trueno", "estilo": "rap"},
    "hagalo usted mismo": {"precio": 4990, "artista": "los tres", "estilo": "rock"},
    "la velocidad de la luz": {"precio": 4500, "artista": "los bunkers", "estilo": "rock"},
    "welcome to my world": {"precio": 2990, "artista": "cris mj", "estilo": "regaeton"},
    "amigos": {"precio": 9990, "artista": "pollo fuentes", "estilo": "romantica"},
    "grandes exitos zalo reyes": {"precio": 9990, "artista": "zalo reyes", "estilo": "romantica"},
    "un golpe de suerte": {"precio": 9990, "artista": "lucho jara", "estilo": "romantica"}
}

descuentos = {
    "regular": 0.90,
    "premium": 0.85,
}

def menu():
    print("\nMENÚ VINILOS DUOCUC: ")
    print("1. Registrar venta")
    print("2. Mostrar todas las ventas")
    print("3. Buscar venta por cliente")
    print("4. Guardar ventas en archivo")
    print("5. Cargar ventas desde un archivo")
    print("6. Generar factura")
    print("7. Salir del programa")
    opcion = input("\nSeleccione una opción: ")
    
    if opcion == "1":
        registrar_venta()
        return menu()
    elif opcion == "2":
        mostrar_ventas()
        return menu()
    elif opcion == "3":
        buscar_venta()
        return menu()
    elif opcion == "4":
        guardar_ventas()
        return menu()
    elif opcion == "5":
        cargar_ventas()
        return menu()
    elif opcion == "6":
        generar_factura()
        return menu()
    elif opcion == "7":
       print("Adios!")
    else:
        print("Opción no válida. Por favor, intente de nuevo.")
        return menu()
    
def registrar_venta():
    cliente = input("Ingrese nombre del cliente: ").lower()
    tipo_cliente = input("Ingrese tipo de cliente (regular / premium): ").lower()
    nombre_vinilo = input("Ingrese nombre del disco : ").lower()
    cantidad = int(input("Unidades deseadas: "))
    
    if tipo_cliente not in descuentos:
        print("Tipo de cliente no valido.")
        return
    
    if nombre_vinilo not in vinilos_info:
        print("Vinilo no encontrado en la base de datos.")
        return

    vinilo_info = vinilos_info[nombre_vinilo]
    precio_unitario = vinilo_info["precio"]
    descuento = descuentos[tipo_cliente]
    precio_total = precio_unitario * cantidad
    precio_final = precio_total * descuento
    
    venta = {
        "cliente": cliente,
        "tipo_cliente": tipo_cliente,
        "nombre_vinilo": nombre_vinilo,
        "artista": vinilo_info["artista"],
        "estilo": vinilo_info["estilo"],
        "cantidad": cantidad,
        "precio_total": precio_total,
        "precio_final": precio_final
    }
    
    ventas.append(venta)
    print("\nVenta registrada con exito!")

def mostrar_ventas():
    if ventas:
        for venta in ventas:
            print(venta)
    else:
        print("\nNo se han registrado ventas.")

def buscar_venta():
    cliente = input("\nIngrese el nombre del cliente: ")
    encontrado = False
    for venta in ventas:
        if venta["cliente"] == cliente:
            print(venta)
            encontrado = True
    if not encontrado:
            print("\nCliente no encontrado.")

def guardar_ventas():
    with open('data_ventas.json', 'w') as archivo:
        json.dump(ventas, archivo)
    print("\nArchivo creado con exito.")

def cargar_ventas():
    global ventas
    with open('data_ventas.json', 'r') as archivo:
        ventas = json.load(archivo)
    print("\nVentas cargadas con exito.")

def generar_factura():
    cliente = input("\nIngrese nombre del cliente: ")
    encontrado = False
    for venta in ventas:
        if venta["cliente"] == cliente:
            encontrado = True
   
            print("\n\t\tVINILOS DUOCUC")
            print("--------------------------------------------------")
            print("Ubicación: \t\t\tAv. España")
            print(f"Hora: \t\t\t\t{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            print("--------------------------------------------------")
            print(f"Nombre del cliente: \t\t{venta['cliente']}")
            print(f"Tipo de usuario: \t\t{venta['tipo_cliente']}")
            print(f"\nVinilo: {venta['nombre_vinilo']} \t\t${venta['precio_total']}")
            print(f"Precio total por {venta['cantidad']} unidade(s): \t\t${venta['precio_total']}")
            print(f"Precio final con dcto: \t\t\t${venta['precio_final']}")
            print("--------------------------------------------------")
            break

        if not encontrado:
            print("\nCliente no encontrado.")

menu()
