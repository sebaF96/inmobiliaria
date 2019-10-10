from funciones import AgregarCliente, AgregarPropiedad, AgregarAlquiler
from modelos import Cliente, Inmueble, Alquiler
from database import Session

session = Session()

salir = False

while salir is False:
    print("\nIngrese que desea hacer:\n1. Registrar cliente\n2. Añadir propiedad\n3. Registrar alquiler\n4. Ver "
          "alquileres\n5. Terminar alquiler")

    opcion = int(input())

    if opcion == 1:         # Registrar cliente

        cliente = AgregarCliente()
        session.add(cliente)
        session.commit()
        print("Cliente añadido con exito!")
        print(cliente)

    elif opcion == 2:       # Añadir propiedad
        ownerdni = str(input("Ingrese el dni del dueño de la propiedad: "))
        cliente = session.query(Cliente).filter(Cliente.dni == ownerdni).one()

        inmueble = AgregarPropiedad(cliente.clienteId)

        session.add(inmueble)
        session.commit()

        print("Propiedad añadida con exito!\n")
        print(inmueble)

    elif opcion == 3:       # Registrar alquiler.

        dni_inquilino = str(input("Ingrese DNI del inquilino: "))
        inquilino = session.query(Cliente).filter(Cliente.dni == dni_inquilino).one()

        print("Ingrese el numero de propiedad: ")

        casas_disponibles = session.query(Inmueble).filter(Inmueble.alquilado == 0).order_by(Inmueble.inmuebleId).all()

        for casa in casas_disponibles:
            print(casa.inmuebleId, casa)

        inmueble_id = int(input())

        alquiler = AgregarAlquiler(inquilino.clienteId, inmueble_id)

        session.add(alquiler)

        casa = session.query(Inmueble).filter(Inmueble.inmuebleId == inmueble_id).one()
        casa.alquilado = 1

        session.commit()

    elif opcion == 4:       # Ver alquileres
        alquileres = session.query(Alquiler).order_by(Alquiler.fechainicio).all()

        for alquiler in alquileres:
            print("\n")
            print(alquiler)

    elif opcion == 9:
        print("Hasta luego!")
        salir = True



