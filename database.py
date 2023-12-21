from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base
from config import DevelopmentConfig

#Carga de datos hardcodeada
#from z_load_data import cargar_autos, cargar_usuarios, cargar_grupos

engine = create_engine(DevelopmentConfig.SQLALCHEMY_ENGINE)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    import models
    Base.metadata.drop_all(bind=engine) # elimina todas la tablas de la base de datos
    Base.metadata.create_all(bind=engine)
    #cargar_autos(models.Auto, models.Reserva, db_session)
    #cargar_grupos(models.Grupo, db_session)
    #cargar_usuarios(models.Usuario, db_session)
