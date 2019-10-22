from db_config import Base, engine
import Cliente
import Inmueble
import Alquiler


Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)
