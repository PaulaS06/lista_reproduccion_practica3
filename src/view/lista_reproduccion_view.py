import sys
sys.path.append("src")
from logic.lista_reproduccion_logic import AudioPlayer, Song

def pedir_datos():
    print("Introduce los datos de la canción")
    title = input("Título: ")
    artist = input("Artista: ")
    duration = float(input("Duración (en segundos): "))
    return title, artist, duration

def mostrar_menu():
    print("\n--- Reproductor de música ---")
    print("1. Añadir canción a la playlist")
    print("2. Reproducir canción")
    print("3. Avanzar a la siguiente canción")
    print("4. Devolverse a la canción anterior")
    print("5. Eliminar canción por su nombre")
    print("6. Mostrar canción actual")
    print("7. Mostrar playlist")
    print("8. Activar modo aleatorio") # PENDIENTE
    print("9. Adelantar canción") # PENDIENTE
    print("10. Generar una subplaylist") # PENDIENTE
    print("_______________________________\n")
    print("11. Salir")


player = AudioPlayer()

while True:
    mostrar_menu()
    opcion = input("\nElige una opción: ")

    if opcion == "1":
        title, artist, duration = pedir_datos()
        song = Song(title, artist, duration)
        player.playlist.add_song(song)
        print(f"Se ha añadido la canción: {song} de {song.artist} a la playlist exitosamente")
    elif opcion == "2": ## REVISAR
        print(player.play())
        messages = player.simulate_playback()
        for msg in messages:
            print(msg)

    elif opcion == "3":
        print(player.next_song())
    elif opcion == "4":
        print(player.previous_song())
    elif opcion == "5":
        title = input("Introduce el título de la canción a eliminar: ")
        player.playlist.remove_song(title)
        print(f"Se ha eliminado la canción: {title} de la playlist exitosamente")
    elif opcion == "6":
        print(player.show_current_song())
    elif opcion == "7":
        print(player.show_playlist())
    elif opcion == "8":
        print("Activando modo aleatorio...")
        print(player.shuffle())
        print("Modo aleatorio activado")

    elif opcion == "9":
        ...
    elif opcion == "10":
        ...

    elif opcion == "11":
        print("Saliendo del sistema...")
        break
    else:
        print("Opción no válida. Por favor, elige una opción del menú.")

