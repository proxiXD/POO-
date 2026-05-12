class Inventario:
    def __init__(self):
        self._items = []

    def agregar_item(self, item):
        self._items.append(item)

    def eliminar_item(self, item):
        if item in self._items:
            self._items.remove(item)

    def obtener_armas(self):
        return [i for i in self._items if hasattr(i, "dano")]

    def obtener_pociones(self):
        return [i for i in self._items if hasattr(i, "_curacion")]

    def mostrar(self):
        if not self._items:
            print("  (inventario vacío)")
        for i, item in enumerate(self._items, 1):
            tipo = type(item).__name__
            print(f"  {i}. [{tipo}] {item.nombre}")
