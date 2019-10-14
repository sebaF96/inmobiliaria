import curses
from funciones import *
from modelos import Cliente, Inmueble, Alquiler
from database import Session, Base
from sqlalchemy import or_
import time
import os
from datetime import datetime

session = Session()
opciones = ["Registrar cliente", "Listar propiedades", "Añadir propiedad", "Registrar alquiler", "Ver alquileres",
            "Ver clientes", "Salir"]


def print_menu(stdscr, selected_row_idx):
    stdscr.clear()
    h, w = stdscr.getmaxyx()

    for idx, row in enumerate(opciones):
        x = w // 2 - len(row) // 2
        y = h // 2 - len(opciones) // 2 + idx
        if idx == selected_row_idx:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y, x, row)
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(y, x, row)

    stdscr.refresh()


def main(stdscr):
    global alquileres
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

    current_row_idx = 0

    print_menu(stdscr, current_row_idx)

    while 1:

        key = stdscr.getch()

        stdscr.clear()

        if key == curses.KEY_UP and current_row_idx > 0:
            current_row_idx = current_row_idx - 1
        elif key == curses.KEY_DOWN and current_row_idx < len(opciones) - 1:
            current_row_idx = current_row_idx + 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            stdscr.refresh()
            curses.endwin()
            os.system('clear')

            if current_row_idx == 0:
                cliente = AgregarCliente()
                print("\nCliente añadido con exito!\n")
                print(cliente)
                session.add(cliente)
                session.commit()

            elif current_row_idx == 1:

                casas_disponibles = session.query(Inmueble).filter(Inmueble.alquilado == 0).order_by(
                    Inmueble.inmuebleId).all()

                for casa in casas_disponibles:
                    print(casa.inmuebleId, casa)

                goback = str(input("\n\nPresione una tecla para volver al menu..."))

            elif current_row_idx == 2:

                ownerdni = str(input("Ingrese el dni del dueño de la propiedad: "))
                cliente = session.query(Cliente).filter(Cliente.dni == ownerdni).one()
                inmueble = AgregarPropiedad(cliente.clienteId)
                print("Propiedad añadida con exito!\n")
                print(inmueble)
                session.add(inmueble)
                session.commit()
                time.sleep(3)

            elif current_row_idx == 3:
                dni_inquilino = str(input("Ingrese DNI del inquilino: "))
                inquilino = session.query(Cliente).filter(Cliente.dni == dni_inquilino).one()

                print("Ingrese el numero de propiedad: ")

                casas_disponibles = session.query(Inmueble).filter(Inmueble.alquilado == 0).order_by(
                    Inmueble.inmuebleId).all()

                for casa in casas_disponibles:
                    print(casa.inmuebleId, casa)

                inmueble_id = int(input())

                alquiler = AgregarAlquiler(inquilino.clienteId, inmueble_id)

                session.add(alquiler)

                print("\nAlquiler registrado con exito!")

                casa = session.query(Inmueble).filter(Inmueble.inmuebleId == inmueble_id).one()
                casa.alquilado = 1

                session.commit()

            elif current_row_idx == 4:
                print("1. DNI dueño\n2. DNI inquilino\n3. Todos")
                choice = int(input())
                if choice == 1:
                    dni = int(input("Ingrese DNI de cliente "))
                    alquileres = session.query(Alquiler).join(Inmueble).join(Cliente).filter(Cliente.dni == dni).all()

                elif choice == 2:
                    dni = int(input("Ingrese DNI del cliente "))
                    alquileres = session.query(Alquiler).join(Cliente).filter(Cliente.dni == dni).all()

                elif choice == 3:
                    alquileres = session.query(Alquiler).order_by(Alquiler.fechainicio).all()

                for alquiler in alquileres:
                    print("\n")
                    print(alquiler)

                goback = str(input("\n\nPresione una tecla para volver al menu..."))

            elif current_row_idx == 5:
                dni = int(input("Ingrese el DNI del cliente "))
                cliente = session.query(Cliente).filter(Cliente.dni == dni).one()
                mostrar_cliente(cliente)
                alquiler = session.query(Alquiler).filter(Alquiler.inquilino == cliente).one()
                print("Alquilando: " + str(alquiler.inmueble))
                goback = str(input("\n\nPresione una tecla para volver al menu..."))

            elif current_row_idx == len(opciones) - 1:
                print("Hasta luego!")
                for x in range(7):
                    time.sleep(0.2)
                    print(".")
                os.system('clear')
                break

        print_menu(stdscr, current_row_idx)

        stdscr.refresh()


curses.wrapper(main)
