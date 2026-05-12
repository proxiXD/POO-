class Enemigo:
    def __init__(self, nombre, vida, debilidad):
        self.nombre = nombre
        self.vida = vida
        self.debilidad = debilidad

    def recibir_dano(self, dano):
        self.vida -= dano
        print(f"{self.nombre} recibe {dano} daño (vida restante: {self.vida})")