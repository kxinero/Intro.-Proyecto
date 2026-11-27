from random import randint

max_videojuegos = 60
max_paises = 12
VERSION_SISTEMA = "VG-26.2"

def cantidad_min_max(videojuegos, paises):
    while videojuegos <= 0 or videojuegos > max_videojuegos:
        print("Cantidad incorrecta, intenta nuevamente.")
        videojuegos = int(input("Ingrese la cantidad de videojuegos: "))

    while paises <= 0 or paises > max_paises:
        print("Cantidad incorrecta, intenta nuevamente.")
        paises = int(input("Ingrese la cantidad de paises: "))
    return videojuegos, paises

def crear_videojuegos(videojuegos):

    lista_videojuegos = []
    for i in range(videojuegos):
        nombre = input("Ingrese nombre del videojuego: ")
        lista_videojuegos.append(nombre)
    return lista_videojuegos

def crear_paises_vg(paises):
    lista_paises = []
    for i in range(paises):
        nombre = input("Ingrese nombre del pais: ")
        lista_paises.append(nombre)
        
    return lista_paises

def generar_ventas(videojuegos, paises):
    ventas = []
    
    for f in range(videojuegos):
        fila = []
        for c in range(paises):
            fila.append(randint(500, 45000))
        ventas.append(fila)
        
    return ventas

def mostrar_ventas(ventas, lista_videojuegos, lista_paises):
    ancho = 15
    
    print("================ MATRIZ DE VENTAS ================")
    print()
    
    print("VIDEOJUEGO". center(ancho), end="")
    
    for pais in lista_paises:
        print(pais.center(ancho), end=" ")
    print()
    print("-" * ancho * (len(lista_paises) + 1))
    
    for f in range(len(lista_videojuegos)):
        print(lista_videojuegos[f].center(ancho), end=" ")
        for c in range(len(lista_paises)):
            print(str(ventas[f][c]).center(ancho), end=" ")
        print()
    
def calcular_totales(ventas):
    totales = []
    
    for f in range(len(ventas)):
        suma = 0
        for c in range (len(ventas[f])):
            suma += ventas[f][c]
        totales.append(suma)
    
    return totales

def titulo_mas_vendido_total (ventas, lista_videojuegos):
    totales = calcular_totales(ventas)
    mayor = totales[0]
    for i in range (1,len(totales)):
        if totales [i] > mayor:
            mayor = totales[i]
    
    print("\n=== TÍTULO MÁS VENDIDO EN TOTAL ===")
    
    for i in range(len(totales)):
        if totales[i] == mayor:
            print(f"{lista_videojuegos[i]} - {mayor} unidades")

def titulo_mas_vendido_por_pais(ventas, lista_videojuegos, lista_paises):
    print("\n=== TÍTULO MÁS VENDIDO POR PAÍS ===")
    for c in range(len(lista_paises)):
        mayor = ventas[0][c]
        for f in range(1, len(ventas)):
            if ventas[f][c] > mayor:
                mayor = ventas[f][c]
        
        print(f"\nPaís: {lista_paises[c]}")
        
        for f in range(len(ventas)):
            if ventas [f][c] == mayor:
                print(f"{lista_videojuegos[f]} - {mayor} unidades")

def pais_menor_ventas_titulo(ventas, lista_videojuegos, lista_paises):
    print("\n=== PAÍS CON MENOS VENTAS POR TÍTULO ===")
    
    for f in range(len(ventas)):
        menor = ventas[f][0]
        for c in range(1, len(ventas[f])):
            if ventas [f][c] < menor:
                menor = ventas [f][c]
        print(f"\nVideojuego: {lista_videojuegos[f]}")
        
        for c in range(len(ventas[f])):
            if ventas[f][c] == menor:
                print(f"{lista_paises[c]} - {menor} unidades")

def mostrar_ranking(ventas, lista_videojuegos):
    totales = calcular_totales(ventas)
    nombres = []
    
    for i in range(len(lista_videojuegos)):
        nombres.append(lista_videojuegos[i])
    
    for i in range(len(totales) - 1):
        for j in range(len(totales) - 1 - i):
            if totales[j] < totales [j + 1]:
                auxiliar = totales[j]
                totales[j] = totales[j + 1]
                totales[j + 1] = auxiliar
                
                auxiliar = nombres[j]
                nombres[j] = nombres[j + 1]
                nombres[j + 1] = auxiliar
                
    print("\n=== RANKING DE VIDEOJUEGOS ===")
    print("Método utilizado: ORDENAMIENTO BURBUJA")
    print()
    
    for i in range(len(totales)):
        print(f"{i + 1}. {nombres[i]} - {totales[i]} unidades")

def buscar_titulo(nombre, lista_videojuegos):
    pass

def consultar_ventas(ventas, lista_videojuegos, lista_paises):
    pass

def intercambiar_ventas(ventas, lista_videojuegos, lista_paises):
    pass

def acumulado_recursivo(fila, posicion):
    if posicion == len(fila):
        return 0
    
    return fila[posicion] + acumulado_recursivo(fila, posicion + 1)

def reporte_recursivo(ventas, lista_videojuegos):
    print("\n=== REPORTE RECURSIVO DE VENTAS ===")
    
    for i in range(len(ventas)):
        total = acumulado_recursivo(ventas[i], 0)
        
        print(f"{lista_videojuegos[i]} - {total} unidades")

def mostrar_menu ():
    print("========================================")
    print("     SISTEMA DE MONITOREO DE VENTAS     ")
    print("========================================")
    
    print(f"Versión: {VERSION_SISTEMA}")
    print()
    print("1. Mostrar matriz de ventas")
    print("2. Titulo mas vendido en total")
    print("3. Titulo mas vendido por pais")
    print("4. Pais con menos ventas por titulo")
    print("5. Ranking de titulos (metodo: Burbuja)")
    print("6. Consultar ventas de un titulo en un pais")
    print("7. Intercambiar ventas de dos titulos en un pais")
    print("8. Funcionalidad recursiva")
    print("9. Salir")
    print()
    
    opcion = int(input("Elige una opción (1 - 9): "))
    
    return opcion

def main():
    print("----------------------------------------")
    print("      CAPACIDAD MÁXIMA DEL SISTEMA      ")
    
    print(f"Videojuegos: {max_videojuegos}")
    print(f"Países: {max_paises}")
    
    videojuegos = int(input("Ingrese la cantidad de videojuegos: "))
    paises = int(input("Ingrese la cantidad de paises: "))
    
    videojuegos, paises = cantidad_min_max(videojuegos)
    
    print("\nConfiguración completada.")
    print(f"Videojuegos registrados: {videojuegos}")
    print(f"Países registrados: {paises}")
    
    lista_videojuegos = crear_videojuegos(videojuegos)

    lista_paises = crear_paises_vg(paises)

    ventas = generar_ventas(videojuegos, paises)
    
    print("\nVIDEOJUEGOS REGISTRADOS:")
    print(lista_videojuegos)
    print("\nPAÍSES REGISTRADOS:")
    print(lista_paises)
    
    print(" ")
    
    #MENU PRINCIPAL
    opcion = 0
    
    while opcion != 9:
        opcion = mostrar_menu()
        
        if opcion == 1:
            mostrar_ventas(ventas, lista_videojuegos, lista_paises)
            
        elif opcion == 2:
            titulo_mas_vendido_total(ventas, lista_videojuegos)
        
        elif opcion == 3:
            titulo_mas_vendido_por_pais(ventas, lista_videojuegos, lista_paises)
        
        elif opcion == 4: 
            pais_menor_ventas_titulo(ventas, lista_videojuegos, lista_paises)
            
        elif opcion == 5: 
            mostrar_ranking(ventas, lista_videojuegos)
        
        elif opcion == 6:
            consultar_ventas(ventas, lista_videojuegos, lista_paises)
    
        elif opcion == 7: 
            intercambiar_ventas(ventas, lista_videojuegos, lista_paises)
        
        elif opcion == 8:
            reporte_recursivo(ventas, lista_videojuegos)
        
        elif opcion == 9:
            print("SE CERRÓ EL PROGRAMA CORRECTAMENTE")
        
        else:
            print("Opción incorrecta. Seleccione entre 1 y 9")
            
main()
