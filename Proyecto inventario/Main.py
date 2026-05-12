from Models.Jugador import Jugador
from systems.game_system import generar_item, generar_enemigo

def menu_combate(jugador, enemigo):
    """Gestiona el combate turno a turno con menú de opciones."""
    print(f"\n  ¡Comienza el combate contra {enemigo.nombre}! (vida: {enemigo.vida})")

    while enemigo.vida > 0 and jugador.esta_vivo():
        print(f"\n{'─'*35}")
        print(f"  Tu vida: {jugador.vida} | {enemigo.nombre} vida: {enemigo.vida}")
        print(f"{'─'*35}")
        print("  ¿Qué quieres hacer?")
        print("  1. Atacar con arma específica")
        print("  2. Usar poción")
        print("  3. Ver inventario")
        print("  4. Huir")

        opcion = input("\n  Elige una opción (1-4): ").strip()

        if opcion == "1":
            armas = jugador.inventario.obtener_armas()
            if not armas:
                print("  No tienes armas en el inventario.")
                continue

            print(f"\n  Debilidad del enemigo: {enemigo.debilidad}")
            print("  Armas disponibles:")
            for i, arma in enumerate(armas, 1):
                efectiva = "✅" if arma.tipo == enemigo.debilidad else "  "
                print(f"  {i}. {efectiva} {arma.nombre} — daño: {arma.dano} (tipo: {arma.tipo})")

            try:
                eleccion = int(input("  Elige arma (número): ")) - 1
                if 0 <= eleccion < len(armas):
                    arma = armas[eleccion]
                    print(f"\n  Atacas con {arma.nombre}...")
                    arma.usar(enemigo)
                else:
                    print("  Número fuera de rango.")
                    continue
            except ValueError:
                print("  Entrada inválida.")
                continue

        elif opcion == "2":
            pociones = jugador.inventario.obtener_pociones()
            if not pociones:
                print("  No tienes pociones.")
                continue
            print(f"\n  Vida actual: {jugador.vida}/100")
            jugador.usar_pocion()

        elif opcion == "3":
            print("\n  Inventario:")
            jugador.inventario.mostrar()
            continue  # no gasta turno

        elif opcion == "4":
            print(f"\n  Huyes del combate contra {enemigo.nombre}...")
            return False  # huyó

        else:
            print("  Opción no válida, intenta de nuevo.")
            continue

        # turno del enemigo (ataque simple)
        if enemigo.vida > 0:
            dano_enemigo = 10
            print(f"\n  {enemigo.nombre} te ataca!")
            jugador.recibir_dano(dano_enemigo)

    if not jugador.esta_vivo():
        print("\n ¡Has sido derrotado!")
        return False

    print(f"\n🏆 ¡{enemigo.nombre} derrotado!")
    return True


def main():
    jugador = Jugador("Héroe")
    print("⚔️  ¡Bienvenido al juego!")

    for turno in range(1, 11):
        print(f"\n{'='*35}")
        print(f"  TURNO {turno}")
        print(f"{'='*35}")

        # recibir item
        item = generar_item()
        jugador.inventario.agregar_item(item)
        print(f"  Obtienes: {item.nombre}")

        # combate cada 3 turnos
        if turno % 3 == 0:
            enemigo = generar_enemigo()
            victoria = menu_combate(jugador, enemigo)

            if not jugador.esta_vivo():
                print("\n--- FIN DEL JUEGO ---")
                return

        if not jugador.esta_vivo():
            break

    print("\n🎉 ¡Completaste los 10 turnos!")


if __name__ == "__main__":
    main()
