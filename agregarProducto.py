listaProductos = [
    {'codigo': '001', 'producto': 'PAN', 'descripcion': 'Descripción 1', 'cantidad':"10", 'precio': 10.0},
    {'codigo': '002', 'producto': 'LECHE', 'descripcion': 'Descripción 2', 'cantidad': "5", 'precio': 15.0},
    {'codigo': '003', 'producto': 'TORNILLO', 'descripcion': 'Descripción 3', 'cantidad': "8", 'precio': 20.0},
]

encabezado="############################### \n \tMENNU DE OPCIONES \n ##############################"

while True:
    print (encabezado)
    opcion = int(input("\nIngrese \n\n (1) Agregar un Nuevo Producto \n (2) Mostrar la lista de Productos \n (3) Salir del Menú \n"))

    match opcion:
        case 1:
            codigo = input("Ingrese un nuevo código: ").upper()
            # Si el codigo es numérico, para que le pongo UPPER??
            # Verifica si el código ya existe en la lista
            if codigo in [producto['codigo'] for producto in listaProductos]:
                print("El código ya existe, ingrese otro código.")
                codigo = input("Ingrese un nuevo código: ").upper()
            else:
                while True:
                    producto = input("Ingrese el nombre del producto: ").upper()
                    try:
                        precio = float(input("Ingrese el Precio del Producto: $ "))
                         # Verifica si el precio es un número positivo
                        if precio <= 0:
                            print("El precio debe ser un número positivo.")
                            
                    except ValueError:
                        print("Debe ingresar un precio válido.")
                        precio = float(input("Ingrese el Precio del Producto: $ "))

                    descripcion = (input("Ingrese descripción del producto: "))
                     # Verifica que sea texto
                    if not descripcion:
                        print("Ingrese una descripción, por favor")
                        cantidad_valida = False
                        cantidad_intentos = 0
                        while cantidad_intentos < 3:
                            try:
                                cantidad = int(input("Ingrese la cantidad adquirida: "))
                                if cantidad <= 0:
                                 print("La cantidad debe ser un número positivo. Intente nuevamente.")
                                else:
                                    cantidad_valida = True
                                    break
                            except ValueError:
                                print("Debe ingresar un número válido. Intente nuevamente.")
                                cantidad_intentos+= 1

                            try:
                                cantidad = int(input("Ingrese la cantidad adquirida: "))
                                if cantidad <= 0:
                                    print("La cantidad debe ser un número positivo. Intente nuevamente.")
                                    cantidad_valida = False
                                cantidad_intentos = 0
                                while cantidad_intentos < 3:
                                    try:
                                        cantidad = int(input("Ingrese la cantidad adquirida: "))
                                        if cantidad <= 0:
                                            print("La cantidad debe ser un número positivo. Intente nuevamente.")
                                        else:
                                            cantidad_valida = True
                                        break
                                    except ValueError:
                                        print("Debe ingresar un número válido. Intente nuevamente.")
                                        
                                     
                        
                # Agrega el nuevo producto a la lista de productos
                                nuevoProducto = {'codigo': codigo, 'producto': producto, 'precio': precio, 'descripcion': descripcion, 'cantidad': cantidad}
            
                                listaProductos.append(nuevoProducto)
                                print("El Producto se ingresó correctamente.\n")
                                
                                
        case 2:
            print("Lista de Productos:")
            for producto in listaProductos:
                print(f"Código: {producto['codigo']}\n Producto: {producto['producto']}\n Precio: ${producto['precio']}\n Descripción: {producto['descripcion']}\n Cantidad: {producto['cantidad']}")
            
            
        case 3:
            print("Usted eligió SALIR.\n")
            break

        case _:
            print("Ingresó una opción inválida.")
