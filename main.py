from funciones import *
from consultas import *
import time
import os


def main(stdscr):
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    current_row_idx = 0
    print_menu(stdscr, current_row_idx)

    while 1:

        key = stdscr.getch()

        stdscr.clear()

        if key == curses.KEY_UP and current_row_idx > 0:
            current_row_idx = current_row_idx - 1
        elif key == curses.KEY_DOWN and current_row_idx < len(opciones_menu) - 1:
            current_row_idx = current_row_idx + 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            stdscr.refresh()
            curses.endwin()
            os.system('clear')

            if current_row_idx == 0:    # Agregar cliente
                cliente = agregar_cliente()
                if not cliente_existe(cliente):
                    print("\nCliente añadido con exito!\n", cliente)
                    insert_in_db(cliente)
                else:
                    print("\nEl cliente que esta intentando añadir ya existe")
                time.sleep(2)

            elif current_row_idx == 1:  # Listar propiedades

                listar_propiedades()

                goback = str(input("\n\nPresione una tecla para volver al menu..."))

            elif current_row_idx == 2:  # Agregar propiedad

                print("Ingrese el dni del dueño de la propiedad\n")
                cliente = get_cliente()
                if cliente_existe(cliente):
                    inmueble = agregar_propiedad(cliente.clienteId)
                    insert_in_db(inmueble)

                time.sleep(3)

            elif current_row_idx == 3:  # Registrar alquiler
                print("Ingrese DNI del inquilino")
                inquilino = get_cliente()

                if cliente_existe(inquilino):
                    listar_propiedades()
                    inmueble_id = int(input("Ingrese el numero de propiedad: "))
                    agregar_alquiler(inquilino.clienteId, inmueble_id)

                time.sleep(2)

            elif current_row_idx == 4:  # Listar alquileres
                choice = int(input("1. DNI dueño\n2. DNI inquilino\n3. Todos\n"))

                if choice == 1 or choice == 2:
                    cliente = get_cliente()
                    listar_alquileres(cliente, choice)

                else:
                    listar_alquileres(1, choice)

                goback = str(input("\n\nPresione una tecla para volver al menu..."))

            elif current_row_idx == 5:  # Ver cliente
                dni = int(input("Ingrese el DNI del cliente "))
                if cliente_existe(dni):
                    cliente = session.query(Cliente).filter(Cliente.dni == dni).one()
                    mostrar_cliente(cliente)
                    if session.query(Alquiler).filter(Alquiler.inquilino == cliente).count() > 0:
                        alquiler = session.query(Alquiler).filter(Alquiler.inquilino == cliente).one()
                        print("Alquilando: " + str(alquiler.inmueble))
                    else:
                        print("No esta alquilando ninguna propiedad")
                else:
                    print("\nCliente no encontrado")
                goback = str(input("\n\nPresione una tecla para volver al menu..."))

            elif current_row_idx == 6:  # Borrar alquiler
                dni_inquilino = int(input("Igrese el DNI del inquilino: "))
                try:
                    alquiler = session.query(Alquiler).join(Cliente).filter(Cliente.dni == dni_inquilino).one()
                    print(alquiler)
                    confirmacion = str(input("Seguro que desea borrar el alquiler? (s/n) "))
                    if confirmacion == 'S' or confirmacion == 's':
                        alquiler.inmueble.alquilado = 0
                        session.delete(alquiler)
                        session.commit()
                        print("Alquiler borrado con exito")
                except exc.SQLAlchemyError:
                    print("Este cliente no esta alquilando ninguna propiedad")
                time.sleep(2)

            elif current_row_idx == 7:  # Borras propiedad
                ownerdni = int(input("Ingrese el DNI del dueño "))
                if cliente_existe(ownerdni):
                    propiedades = session.query(Inmueble).join(Cliente).filter(Inmueble.alquilado == 0,
                                                                       Cliente.dni == ownerdni).order_by(
                        Inmueble.inmuebleId).all()

                    for casa in propiedades:
                        print(casa.inmuebleId, casa)

                    propiedad_id = int(input("\n\nSeleccione la propiedad a eliminar "))
                    try:
                        propiedad = session.query(Inmueble).filter(Inmueble.inmuebleId == propiedad_id).one()
                        print(propiedad)
                        confirmacion = str(input("\nSeguro que desea borrar esta propiedad? (s/n)"))
                        if confirmacion == 'S' or confirmacion == 's':
                            session.delete(propiedad)
                            session.commit()
                            print("Propiedad borrada con exito")
                            time.sleep(2)
                    except exc.SQLAlchemyError:
                        print("Seleccion incorrecta")
                else:
                    print("El cliente no existe")
                time.sleep(2)

            elif current_row_idx == 8:  # Registrar pago
                dni_inquilino = int(input("Ingrese el dni del inquilino: "))
                if session.query(Alquiler).join(Cliente).filter(Cliente.dni == dni_inquilino).count() == 1:
                    alquiler = session.query(Alquiler).join(Cliente).filter(Cliente.dni == dni_inquilino).one()
                    meses = registrar_pago(alquiler.inmueble)
                    if meses != 0:
                        alquiler.mesespagados = alquiler.mesespagados + meses
                        session.commit()
                        print("Pago registrado con exito")
                else:
                    print("Este cliente no existe o no esta alquilando ninguna propiedad")
                time.sleep(2)

            elif current_row_idx == 9:  # Imprimir
                casas_disponibles = session.query(Inmueble).filter(Inmueble.alquilado == 0).order_by(
                    Inmueble.precio).all()

                imprimir_casas(casas_disponibles)

            elif current_row_idx == len(opciones_menu) - 1:  # Salir
                print("Hasta luego!")
                for x in range(7):
                    time.sleep(0.2)
                    print(".")
                os.system('clear')
                break

        print_menu(stdscr, current_row_idx)

        stdscr.refresh()


curses.wrapper(main)
