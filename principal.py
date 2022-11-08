import controlador

while True:
    print("\n+-------------------------------------------+")
    print("|         DISQUERÍA FORMOSA MUSICAL         |")
    print("+-------------------------------------------+\n")
    print("")
    print("MENÚ PRINCIPAL\n")
    print("1 - DAR DE ALTA UN ÁLBUM") 
    print("2 - DAR DE BAJA UN ÁLBUM") 
    print("3 - MODIFICAR UN ÁLBUM")
    print("4 - LISTADO DE ÁLBUMES POR ARTISTAS")
    print("5 - LISTADO DE ÁLBUMES POR GÉNERO MUSICAL")
    print("6 - ELIMINAR INTERPRETE")
    print("7 - INSERTAR INTERPRETE")
    print("8 - SALIR")
    print("\n")
    opcion = int(input("Ingrese su opción: "))

    if opcion == 1:
        controlador.InsertarAlbum()
    elif opcion == 2:
        controlador.EliminarAlbum()
    elif opcion == 3:
        controlador.modificar_album()
    elif opcion == 4:
        controlador.ListarAlbumesPorArtistas()
    elif opcion == 5:
        controlador.ListarAlbumesPorGenero()
    elif opcion == 6:
        None
    elif opcion == 7:
        None
    elif opcion == 8:
        break
    else:
        print("¡Opción incorrecta!")
