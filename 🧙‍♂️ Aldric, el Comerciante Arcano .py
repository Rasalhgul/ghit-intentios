# hare los diccionaroio (Mismos datos)

items = {
    "MAG001": ["Agonía de Escarcha", "Arma", "Legendaria", "Hielo"],
    "MAG002": ["Anillo de Sauron", "Accesorio", "Epica", "Magia"],
    "MAG003": ["Poción Curativa", "Consumible", "Comun", "Vida"],
    "MAG004": ["Corona Nemesis ", "Armadura", "Legendaria", "Dragon"],
    "MAG005": ["Baston Lunar de Lileath", "Arma", "Epica", "Hechizo"],
    "MAG006": ["Cristal de Hielo", "Material", "Rara", "hielo"],
}

inventario = {
    "MAG001": [5000, 3],
    "MAG002": [2500, 8],
    "MAG003": [100, 50],
    "MAG004": [10000, 1],
    "MAG005": [3500, 4],
    "MAG006": [800, 0],
}

# aqui pondre las funcione si falla caga el codgo 


# Opción 1 es para poder ver el Stock por categoría
def stock_categoria(categoria):
    # realise solo el uso de una linea  para sumar el stock poneindo todos los item aen el formato 
    total = sum(inventario[cod][1] for cod, datos in items.items() if datos[1].lower() == categoria.lower())
    print(f"El stock es: {total}")


# Opción 2 espara que se realize la  Búsqueda por precio
def busqueda_precio(p_min, p_max):
    # intente dejar la lista lo mas organizada posiblepara ver la listas y para filtrar de manera más avanzada y directa
    resultados = [
        f"{items[cod][2]}--{cod}" 
        for cod, (precio, stock) in inventario.items() 
        if p_min <= precio <= p_max and stock > 0
    ]
    resultados.sort()  # espero mantenga  el orden alfabético requerido sino se rompe 
    print(resultados)


# Opción 3 es para Actualizar el  precio 
def actualizar_precio(codigo, precio):
    # usare el .get() para verificar la existencia del código elegantemente para destacar 
    if inventario.get(codigo):
        inventario[codigo][0] = precio
        return True
    return False


# Opción 4: Buscar objeto por código
def buscar_codigo(codigo):
    if codigo in items:
        # estoy usando un solo print multilínea con formato limpio (\t) que es el que mejor entiendo 
        print(f"- Objeto encontrado -\n"
              f"Nombre:\t\t{items[codigo][0]}\n"
              f"Categoría:\t{items[codigo][1]}\n"
              f"Rareza:\t\t{items[codigo][2]}\n"
              f"Tipo magia:\t{items[codigo][3]}\n"
              f"Precio:\t\t{inventario[codigo][0]}\n"
              f"Stock:\t\t{inventario[codigo][1]}")
    else:
        print("El objeto mágico no existe!!")


#  Opción 5 tiene que  Mostrar todos los objetos
def mostrar_todos():
    print("=== CATÁLOGO DE OBJETOS ===")
    # rdta funcion deveria de realizar un Recorrido limpio utilizando desempaquetado 
    for cod, (nombre, cat, rareza, tipo) in items.items():
        precio, stock = inventario[cod]
        print(f"Código: {cod} | Nombre: {nombre} | Cat: {cat} | Rareza: {rareza} | Tipo: {tipo} | Precio: ${precio} | Stock: {stock}")
    print("-" * 40)


# aqui colocarle el PROGRAMA PRINCIPAL o el MENÚ ALTERNATIVO
def menu_principal():
    controlador = True
    while controlador:
        print("\n=== ALDRIC EL COMERCIANTE ARCANO ===")
        print("1. Stock por categoría.\n2. Búsqueda por precio.\n3. Actualizar precio.")
        print("4. Buscar objeto por código.\n5. Mostrar todos los objetos.\n6. Salir.")
        
        opcion = input("Ingrese opción: ")
        
        if opcion == "1":
            stock_categoria(input("Ingrese categoría: "))
            
        elif opcion == "2":
            # despues de aqui hare los Validadores de errores optimizada en un solo bloque repetitivo que no se rompa o me voy a la ctm 
            while True:
                try:
                    p_min = int(input("Ingrese precio mínimo: "))
                    p_max = int(input("Ingrese precio máximo: "))
                    busqueda_precio(p_min, p_max)
                    break
                except ValueError:
                    print("Error: Debe ingresar valores enteros!!")
            
        elif opcion == "3":
            interrumpir = False
            while not interrumpir:
                cod = input("Ingrese código del objeto: ")
                try:
                    nuevo_precio = int(input("Ingrese nuevo precio: "))
                    if actualizar_precio(cod, nuevo_precio):
                        print("Precio actualizado!!")
                    else:
                        print("El objeto mágico no existe!!")
                except ValueError:
                    print("Error: El precio debe ser un número entero.")
                
                if input("¿Desea actualizar otro precio? (s/n): ").lower() != 's':
                    interrumpir = True
                    
        elif opcion == "4":
            buscar_codigo(input("Ingrese código del objeto: "))
            
        elif opcion == "5":
            mostrar_todos()
            
        elif opcion == "6":
            print("El NPC ha cerrado su tienda. Hasta pronto, aventurero.")
            controlador = False # aqui estoy colocando la variable que deveria de Terminal el bucle usando la variable de control
            
        else:
            print("Debe seleccionar una opción válida!!")

if __name__ == "__main__":
    menu_principal()