from Cliente import Cliente
from Alquiler import Alquiler
from Inmueble import Inmueble
from sqlalchemy import exc
import os
import utils.db_functions as db


def agregar_cliente():

    cliente = Cliente()

    cliente.dni = str(input("DNI: "))
    if not db.cliente_existe(cliente):
        cliente.nombre = str(input("Nombre: "))
        cliente.apellido = str(input("Apellido: "))
        cliente.telefono = int(input("Telefono: "))
        cliente.domicilio = str(input("Domicilio: "))
        cliente.email = str(input("Email: "))

        db.insert_in_db(cliente)
        print("\nCliente añadido con exito!")
    else:
        print("\nEl cliente que esta intentando añadir ya existe")


def agregar_propiedad(duenioid):
    propiedad = Inmueble()

    propiedad.ubicacion = str(input("Ubicacion: "))
    propiedad.habitaciones = int(input("Cantidad de habitaciones: "))
    propiedad.banios = int(input("Cantidad de baños: "))
    propiedad.zona = str(input("Zona: "))
    propiedad.tamanio = str(input("Tamaño: "))
    propiedad.descripcion = str(input("Descripcion: "))
    propiedad.propietarioId = duenioid

    db.insert_in_db(propiedad)
    print("\nPropiedad añadida con exito!")


def agregar_alquiler(inquilino_id, inmueble_id):
    alquiler = Alquiler()

    alquiler.inquilinoId = inquilino_id
    try:
        alquiler.inmuebleId = inmueble_id
        alquiler.mesesduracion = int(input("Meses de duracion: "))
        casa = db.get_inmueble(inmueble_id)
        casa.alquilado = 1
        db.insert_in_db(alquiler)

        print("Alquiler registrado con exito!")
    except exc.SQLAlchemyError:
        print("\nNo se pudo registrar alquiler. Seleccion de casa incorrecta")


def borrar_alquiler(cliente):
    if db.cliente_existe(cliente):
        cantidad_alquileres = db.contar_alquileres(cliente.dni)
        if cantidad_alquileres >= 1:
            alquileres = db.listar_alquileres(cliente, 2)
            for alquiler in alquileres:
                print("\n")
                print(str(alquiler.alquilerId) + ')')
                print(alquiler)
            eleccion = int(input("Seleccione el alquiler que desea borrar: "))
            os.system('clear')
            try:
                alquiler = db.get_alquiler(eleccion)
                print(alquiler)
                confirmar_borrado = True
            except exc.SQLAlchemyError:
                print("Ha ingresado un numero incorrecto. Reintente")
                confirmar_borrado = False
        else:
            confirmar_borrado = False
            print("Este cliente no esta alquilando ninguna propiedad")

        if confirmar_borrado is True:
            confirmacion = str(input("Seguro que desea borrar el alquiler? (s/n) "))
            if confirmacion == 'S' or confirmacion == 's':
                alquiler.inmueble.alquilado = 0
                db.delete_from_db(alquiler)
                print("Alquiler borrado con exito")


def borrar_propiedad(cliente):
    propiedades = db.listar_inmuebles(cliente)
    for casa in propiedades:
        casa.mostrar_datos()

    propiedad_id = int(input("\n\nSeleccione la propiedad a eliminar "))
    try:
        propiedad = db.get_inmueble(propiedad_id)
        os.system('clear')
        propiedad.mostrar_datos()
        confirmacion = str(input("\nSeguro que desea borrar esta propiedad? (s/n)"))
        if confirmacion == 'S' or confirmacion == 's':
            db.delete_from_db(propiedad)
            print("\nPropiedad borrada con exito!")
    except exc.SQLAlchemyError:
        print("\nSeleccion de propiedad incorrecta. Reintente")


'''
def registrar_pago(Inmueble):
    meses = int(input("Cantidad de meses a pagar: "))
    print("\nUsted pagara "+str(meses) + "meses por una suma de $" + str(Inmueble.precio * meses))
    confirmacion = str(input("Confirmar operacion? (S/N)\n"))
    if confirmacion != 's' and confirmacion != 'S':
        meses = 0
    return meses
'''


def imprimir_casas(casas_disponibles):
    with open("Casas_disponibles.txt", "w") as file:

        for casa in casas_disponibles:
            file.write('📍️ Ubicacion: ' + str(casa.ubicacion))
            file.write('\n🛏️ Habitaciones: ' + str(casa.habitaciones))
            file.write('\n🚽️ Baños: ' + str(casa.banios))
            file.write('\n🏘️ Zona: ' + str(casa.zona))
            file.write('\n📏️ Tamaño: ' + str(casa.tamanio))
            file.write('\n💰️ Precio: $' + str(casa.precio))
            file.write('\n--------------------------------------------------------\n')
