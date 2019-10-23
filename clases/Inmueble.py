from config.db_config import Base
from sqlalchemy import Column, Integer, ForeignKey, String, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.ext.hybrid import hybrid_property


class Inmueble(Base):
    __tablename__ = 'inmueble'

    __inmuebleId = Column('inmuebleId', Integer, primary_key=True)

    __ubicacion = Column('ubicacion', String(100), nullable=False)

    __tamanio = Column('tamanio', String(8), nullable=False)

    __zona = Column('zona', String(80))

    __habitaciones = Column('habitaciones', Integer)

    __banios = Column('banios', Integer)

    __descripcion = Column('descripcion', String(450), nullable=False)

    __alquilado = Column('alquilado', Boolean, default=0)

    __precio = Column('precio', Integer, nullable=False, default=6000)

    propietarioId = Column(Integer, ForeignKey('cliente.clienteId'), nullable=False)

    alquiler = relationship('Alquiler', back_populates='inmueble')

    propietario = relationship('Cliente', back_populates="propiedades")

    def mostrar_datos(self):
        print("\n")
        print(self.inmuebleId, self)
        print(str(self.banios) + " baños")
        print("Precio: $" + str(self.precio))
        print("Dueño:", self.propietario)

    @hybrid_property
    def inmuebleId(self):
        return self.__inmuebleId

    @inmuebleId.setter
    def inmuebleId(self, value):
        self.__inmuebleId = value

    @property
    def ubicacion(self):
        return self.__ubicacion

    @ubicacion.setter
    def ubicacion(self, value):
        self.__ubicacion = value

    @property
    def tamanio(self):
        return self.__tamanio

    @tamanio.setter
    def tamanio(self, value):
        self.__tamanio = value

    @property
    def zona(self):
        return self.__zona

    @zona.setter
    def zona(self, value):
        self.__zona = value

    @property
    def habitaciones(self):
        return self.__habitaciones

    @habitaciones.setter
    def habitaciones(self, value):
        self.__habitaciones = value

    @property
    def banios(self):
        return self.__banios

    @banios.setter
    def banios(self, value):
        self.__banios = value

    @property
    def descripcion(self):
        return self.__descripcion

    @descripcion.setter
    def descripcion(self, value):
        self.__descripcion = value

    @hybrid_property
    def alquilado(self):
        return self.__alquilado

    @alquilado.setter
    def alquilado(self, value):
        self.__alquilado = value

    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def precio(self, value):
        self.__precio = value

    def __repr__(self):
        return str(self.ubicacion) + ', ' + str(self.habitaciones) + ' habitaciones, ' + str(
            self.descripcion)
