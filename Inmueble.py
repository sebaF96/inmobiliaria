from db_config import Base
from sqlalchemy import Column, Integer, ForeignKey, String, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.ext.hybrid import hybrid_property


class Inmueble(Base):
    __tablename__ = 'inmueble'

    inmuebleId = Column('inmuebleId', Integer, primary_key=True)

    __ubicacion = Column('ubicacion', String(100), nullable=False)

    tamanio = Column('tamanio', String(8), nullable=False)

    zona = Column('zona', String(80))

    habitaciones = Column('habitaciones', Integer)

    banios = Column('banios', Integer)

    propietarioId = Column(Integer, ForeignKey('cliente.clienteId'), nullable=False)

    propietario = relationship('Cliente', back_populates="propiedades")

    descripcion = Column('descripcion', String(450), nullable=False)

    __alquilado = Column('alquilado', Boolean, default=0)

    alquiler = relationship('Alquiler', back_populates='inmueble')

    precio = Column('precio', Integer, nullable=False, default=6000)

    @property
    def ubicacion(self):
        return self.__ubicacion

    @ubicacion.setter
    def ubicacion(self, value):
        self.__ubicacion = value

    @hybrid_property
    def alquilado(self):
        return self.__alquilado

    @alquilado.setter
    def alquilado(self, value):
        self.__alquilado = value

    def __repr__(self):
        return str(self.ubicacion) + ', ' + str(self.habitaciones) + ' habitaciones, ' + str(
            self.descripcion)

    def mostrar_datos(self):
        print("\n")
        print(self.inmuebleId, self)
        print(str(self.banios) + " baños")
        print("Precio: $" + str(self.precio))
        print("Dueño:", self.propietario)
