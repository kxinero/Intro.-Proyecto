from random import randint

max_videojuegos = 60
max_paises = 12
def cantidad_min_max(videojuegos):
    while videojuegos <= 0 or videojuegos > max_videojuegos:
        print("Cantidad incorrecta, intenta nuevamente.")
        videojuegos = int(input("Ingrese la cantidad de videojuegos: "))

    paises = int(input("Ingrese la cantidad de paises: "))

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

def crear_paises(paises):

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
            fila.append(randint(501, 44999))

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
        
def main():
    print("========================================")
    print("     SISTEMA DE MONITOREO DE VENTAS     ")
    print("========================================")

    print("Version: VG-26.2")

    print("CAPACIDAD MAXIMA")
    print(f"Videojuegos: {max_videojuegos}")
    print(f"Paises: {max_paises}")

    videojuegos = int(input("Ingrese la cantidad de videojuegos: "))
    
    videojuegos, paises = cantidad_min_max(videojuegos)
    
    print("Configuracion completada.")
    print(f"Videojuegos registrados: {videojuegos}")
    print(f"Paises registrados: {paises}")
    
    lista_videojuegos = crear_videojuegos(videojuegos)

    lista_paises = crear_paises(paises)

    ventas = generar_ventas(videojuegos, paises)
    
    print("VIDEOJUEGOS REGISTRADOS:")
    print(lista_videojuegos)
    print("PAISES REGISTRADOS:")
    print(lista_paises)
    
    print(" ")

    mostrar_ventas(ventas, lista_videojuegos, lista_paises)
main()
