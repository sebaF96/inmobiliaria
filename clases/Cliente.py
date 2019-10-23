from config.db_config import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.hybrid import hybrid_property


class Cliente(Base):
    __tablename__ = 'cliente'

    __clienteId = Column('clienteId', Integer, primary_key=True)

    __nombre = Column('nombre', String(70), nullable=False)

    __apellido = Column('apellido', String(70), nullable=False)

    __domicilio = Column('domicilio', String(100), nullable=False)

    __telefono = Column('telefono', String(15), nullable=False)

    __email = Column('email', String(70))

    __dni = Column('dni', String(10), nullable=False)

    propiedades = relationship('Inmueble', back_populates="propietario")

    alquilando = relationship('Alquiler', back_populates="inquilino")

    def mostrar_datos(self):
        print(self)
        print("Telefono: " + str(self.telefono))
        print("Domicilio: " + str(self.domicilio))
        print("Email: " + str(self.email))
        print("Dueño de:")
        for propiedad in self.propiedades:
            print(propiedad)
        print("Alquilando:")
        for alquiler in self.alquilando:
            print(alquiler.inmueble)

    @hybrid_property
    def clienteId(self):
        return self.__clienteId

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, value):
        self.__nombre = value

    @hybrid_property
    def apellido(self):
        return self.__apellido

    @apellido.setter
    def apellido(self, value):
        self.__apellido = value

    @property
    def domicilio(self):
        return self.__domicilio

    @domicilio.setter
    def domicilio(self, value):
        self.__domicilio = value

    @property
    def telefono(self):
        return self.__telefono

    @telefono.setter
    def telefono(self, value):
        self.__telefono = value

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        self.__email = value

    @hybrid_property
    def dni(self):
        return self.__dni

    @dni.setter
    def dni(self, value):
        self.__dni = value

    def __repr__(self):
        return str(self.nombre) + ' ' + str(self.apellido) + ' ' + str(self.dni)
