import curses

opciones_menu = ["Registrar cliente", "Listar propiedades", "Añadir propiedad", "Registrar alquiler", "Ver alquileres",
                 "Ver clientes", "Borrar alquiler", "Borrar propiedad", "Registrar pago", "Imprimir propiedades",
                 "Salir"]


def print_menu(stdscr, selected_row_idx):
    stdscr.clear()
    h, w = stdscr.getmaxyx()

    for idx, row in enumerate(opciones_menu):
        x = w // 2 - len(row) // 2
        y = h // 2 - len(opciones_menu) // 2 + idx
        if idx == selected_row_idx:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y, x, row)
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(y, x, row)

    stdscr.refresh()

