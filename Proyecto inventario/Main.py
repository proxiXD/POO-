from models.arma import Arma
from models.pocion import Pocion
from models.armadura import Armadura
from systems.inventario import Inventario

def main():
    inventario = Inventario()

    espada = Arma("Espada", 5, 20)
    pocion = Pocion("Poción de vida", 1, 50)
    armadura = Armadura("Armadura de hierro", 10, 15)

    inventario.agregar_item(espada)
    inventario.agregar_item(pocion)
    inventario.agregar_item(armadura)

    inventario.mostrar_items()

    print("\nUsando objetos:")
    inventario.usar_item(0)  # arma
    inventario.usar_item(1)  # pocion
    inventario.usar_item(2)  # armadura

    print("\nEquipando:")
    espada.equipar()
    armadura.equipar()

if _name_ == "_main_":
    main()