import random
from Models.Arma import Arma
from Models.Armadura import Armadura
from Models.Pocion import Pocion
from Models.Enemigo import Enemigo

def generar_item():
    opciones = [
        Arma("Espada corta", 5, 10, "corte"),
        Arma("Espada larga", 7, 20, "corte"),
        Arma("Arco", 3, 15, "distancia"),
        Armadura("Armadura básica", 10, 5),
        Pocion("Poción", 1, 20)
    ]
    return random.choice(opciones)


def generar_enemigo():
    return random.choice([
        Enemigo("Orco", 50, "corte"),
        Enemigo("Dragón", 80, "distancia"),
        Enemigo("Esqueleto", 40, "golpe")
    ])