from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from genera_tablas import Club, Jugador

from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

archivo = open('data/datos_clubs.txt', 'r')

lista = archivo.readlines()

lista = [l.replace("\n", "").split(";") for l in lista]

for l in lista: 
    nombre = l[0]
    deporte = l[1]
    anio = l[2]
    print(nombre, deporte, anio)

    club1 = Club(nombre=nombre, deporte=deporte, \
        fundacion=anio)
    
    session.add(club1)

session.commit()

    
