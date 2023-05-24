from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from genera_tablas import Club, Jugador

from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

archivo = open('data/datos_jugadores.txt', 'r')

lista = archivo.readlines()

lista = [l.replace("\n", "").split(";") for l in lista]

for l in lista:
    equipo = l[0]
    posicion = l[1]
    numero = l[2]
    nombre = l[3]

    print(equipo, posicion, numero, nombre)

    var = session.query(Club).filter_by(nombre=equipo).one()

    jugador6 = Jugador(nombre=nombre, dorsal=numero, posicion=posicion, \
        club=var)

    session.add(jugador6)

session.commit()