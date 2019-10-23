import curses

opciones_menu = ["Registrar cliente", "Listar propiedades", "Añadir propiedad", "Registrar alquiler", "Ver alquileres",
                 "Ver clientes", "Borrar alquiler", "Borrar propiedad", "Registrar pago", "Imprimir propiedades",
                 "Modificar cliente", "Modificar propiedad", "Salir"]


def print_menu(stdscr, selected_row_idx):
    stdscr.clear()
    height, width = stdscr.getmaxyx()

    for index, row in enumerate(opciones_menu):
        x = width // 2 - len(row) // 2
        y = height // 2 - len(opciones_menu) // 2 + index
        if index == selected_row_idx:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y, x, row)
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(y, x, row)

    stdscr.refresh()

