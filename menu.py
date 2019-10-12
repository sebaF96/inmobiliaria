import curses
from funciones import AgregarCliente, AgregarPropiedad, AgregarAlquiler
from modelos import Cliente, Inmueble, Alquiler
from database import Session

session = Session()

opciones = ["Registrar cliente", "Añadir propiedad", "Registrar alquiler", "Ver alquileres"]


def print_menu(stdscr, selected_row_idx):
    stdscr.clear()
    h, w = stdscr.getmaxyx()

    for idx, row in enumerate(opciones):
        x = w//2 - len(row)//2
        y = h//2 - len(opciones)//2 + idx
        if idx == selected_row_idx:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y, x, row)
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(y, x, row)

    stdscr.refresh()


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
        elif key == curses.KEY_DOWN and current_row_idx < len(opciones) - 1:
            current_row_idx = current_row_idx + 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            stdscr.addstr(0, 0, "You presed {}".format(opciones[current_row_idx]))
            stdscr.refresh()
            stdscr.getch()

            if current_row_idx == len(opciones) - 1:
                break
            elif current_row_idx == 0:
                cliente = AgregarCliente()
                session.add(cliente)
                session.commit()
                print("Cliente añadido con exito!")
                print(cliente)

        print_menu(stdscr, current_row_idx)

        stdscr.refresh()


curses.wrapper(main)
