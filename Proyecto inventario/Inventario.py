class Inventario:
    def _init_(self):
        self._items = []

    def agregar_item(self, item):
        self._items.append(item)

    def mostrar_items(self):
        print("\nInventario:")
        for i, item in enumerate(self._items):
            print(f"{i + 1}. {item.get_nombre()}")

    def usar_item(self, indice):
        if 0 <= indice < len(self._items):
            self._items[indice].usar()
        else:
            print("Índice inválido")
