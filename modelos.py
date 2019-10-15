from database import Base, engine
from sqlalchemy import Column, Integer, ForeignKey, String, DateTime, func, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime, date, timedelta


class Cliente(Base):
    __tablename__ = 'cliente'

    clienteId = Column('clienteId', Integer, primary_key=True)

    nombre = Column('nombre', String(70), nullable=False)

    apellido = Column('apellido', String(70), nullable=False)

    domicilio = Column('domicilio', String(100), nullable=False)

    telefono = Column('telefono', String(15), nullable=False)

    email = Column('email', String(70))

    dni = Column('dni', String(10), nullable=False)

    propiedades = relationship('Inmueble', back_populates="propietario")

    alquilando = relationship('Alquiler', back_populates="inquilino")

    def __repr__(self):
        return str(self.nombre) + ' ' + str(self.apellido) + ' ' + str(self.dni)


class Inmueble(Base):
    __tablename__ = 'inmueble'

    inmuebleId = Column('inmuebleId', Integer, primary_key=True)

    ubicacion = Column('ubicacion', String(100), nullable=False)

    tamanio = Column('tamanio', String(8), nullable=False)

    zona = Column('zona', String(80))

    habitaciones = Column('habitaciones', Integer)

    banios = Column('banios', Integer)

    propietarioId = Column(Integer, ForeignKey('cliente.clienteId'), nullable=False)

    propietario = relationship('Cliente', back_populates="propiedades")

    descripcion = Column('descripcion', String(450), nullable=False)

    alquilado = Column('alquilado', Boolean, default=0)

    alquiler = relationship('Alquiler', back_populates='inmueble')

    def __repr__(self):
        return str(self.ubicacion) + ', ' + str(self.habitaciones) + ' habitaciones, ' + str(self.descripcion)


class Alquiler(Base):
    __tablename__ = 'alquiler'

    alquilerId = Column('alquilerId', Integer, primary_key=True)

    inmuebleId = Column('inmuebleId', ForeignKey('inmueble.inmuebleId'), nullable=False)

    inmueble = relationship('Inmueble', back_populates="alquiler", uselist=False)

    inquilinoId = Column('inquilinoId', ForeignKey('cliente.clienteId'), nullable=False)

    inquilino = relationship('Cliente', back_populates="alquilando")

    fechainicio = Column('fechainicio', DateTime, default=func.now())

    mesesduracion = Column('mesesduracion', Integer, nullable=False)

    def __repr__(self):
        return 'Casa: ' + str(self.inmueble) + '\nInquilino:  ' + str(self.inquilino) + '\nDueño:  ' + str(
            self.inmueble.propietario) + "\nInicio de alquiler: " + str(
            self.fechainicio.strftime("%d %B, %Y")) + "\nMeses de duracion: " + str(
            self.mesesduracion)


# Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)
