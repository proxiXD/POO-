from systems.Inventario import Inventario

class Jugador:
    def __init__(self, nombre):
        self._nombre = nombre
        self._vida = 100
        self.defensa = 0
        self.inventario = Inventario()
        self._equipo = []

    @property
    def nombre(self):
        return self._nombre

    @property
    def vida(self):
        return self._vida

    def curar(self, cantidad):
        self._vida += cantidad
        if self._vida > 100:
            self._vida = 100

    def recibir_dano(self, dano):
        dano_real = max(0, dano - self.defensa)
        self._vida -= dano_real
        print(f"{self._nombre} recibe {dano_real} daño (vida: {self._vida})")

    def agregar_equipo(self, item):
        self._equipo.append(item)

    def mejor_arma(self, tipo=None):
        armas = self.inventario.obtener_armas()
        if tipo:
            armas = [a for a in armas if a.tipo == tipo]
        return max(armas, key=lambda x: x.dano, default=None)

    def atacar(self, enemigo):
        arma = self.mejor_arma(enemigo.debilidad)
        if not arma:
            arma = self.mejor_arma()
        if arma:
            print(f"Usando {arma.nombre}")
            arma.usar(enemigo)
        else:
            print("No tienes ningún arma en el inventario")

    def usar_pocion(self):
        pociones = self.inventario.obtener_pociones()
        if not pociones:
            print("No tienes pociones.")
            return False
        pocion = pociones[0]
        pocion.usar(self)
        self.inventario.eliminar_item(pocion)
        return True

    def esta_vivo(self):
        return self._vida > 0
