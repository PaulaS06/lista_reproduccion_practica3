import time
import random
import sys

sys.path.append("src")
from exceptions.exceptions import AlreadyExistsError, EmptyPlaylistError, InvalidSongError

class Song():
    def __init__(self, title: str, artist: str, duration: float):
        self.title: str = title
        self.artist: str = artist
        self.duration: float = duration

    def __str__(self):
        return f"{self.title} - {self.artist} - {self.duration}s"


class DoubleNode:
    def __init__(self, song: Song, next = None, prev = None):
        self.song = song
        self.next = next
        self.prev = prev

    def __repr__(self) -> str:
        return f"{self.song}"


class Playlist(): # Va a ser la lista enlazada circular
    def __init__(self, head: DoubleNode = None, tail: DoubleNode = None):
        self.__head : DoubleNode = head
        self.__tail: DoubleNode = tail
        self.__size: int = 0

    # Métodos para acceder a los atributos privados
    def get_head(self):
        return self.__head

    def get_tail(self):
        return self.__tail

    def get_size(self):
        return self.__size


    def add_song(self, new_song: Song):
        new_song_node = DoubleNode(new_song)

        if (self.__size > 0):
            current_song = self.__head
            for _ in range(self.__size):
                if (current_song.song.title == new_song.title):
                    raise AlreadyExistsError("La canción ya existe")
                current_song = current_song.next

        if (self.__size == 0):
            self.__head = new_song_node
            self.__tail = new_song_node # como está vacía, el inicio y el final es el mismo
            self.__head.prev = new_song_node
            self.__tail.next = self.__head
        else:
            new_song_node.prev = self.__tail
            self.__tail.next = new_song_node
            self.__tail = new_song_node
            self.__head.prev = new_song_node # Se asigna al prev de la cabeza la cola, para que sea circular
            self.__tail.next = self.__head # Se asigna a la cola que su next es el head, para que sea circular
        self.__size += 1
        return


    def remove_song(self, song_title: str):

        if (self.__size == 0):
            raise EmptyPlaylistError("La playlist está vacía")

        current_song = self.__head

        for _ in range(self.__size):
            if (current_song.song.title == song_title):
                if self.__size == 1:  # Si solo hay un elemento
                    self.__head = None
                    self.__tail = None

                else:
                    if current_song == self.__head:  # Si es el primer elemento, la cabeza pasa a ser el siguiente
                        self.__head = current_song.next
                    elif current_song == self.__tail:  # Si es el último elemento, la cola pasa a ser el anterior
                        self.__tail = current_song.prev

                    current_song.prev.next = current_song.next
                    current_song.next.prev = current_song.prev

                self.__size -= 1
                return

            current_song = current_song.next

        raise InvalidSongError("La canción que quiere eliminar no existe en esta playlist")


    def __repr__(self) -> str:
        songs = []
        current = self.__head
        for _ in range(self.__size):
            songs.append(str(current.song.title))
            current = current.next
        return " <-> ".join(songs)
    

class AudioPlayer():
    def __init__(self):
        self.playlist = Playlist()
        self.current = None

    def play(self):
        if (self.playlist.get_size() == 0):
            raise EmptyPlaylistError("La playlist está vacía")

        if self.current is None:
            self.current = self.playlist.get_head()
        return f"Reproduciendo: {self.current.song} de {self.current.song.artist}"

    def simulate_playback(self):
        if self.current:
            message_start = f"🎧 Sonando: {self.current.song.title} de {self.current.song.artist}"
            time.sleep(self.current.song.duration)  
            message_end = "🎶 Canción finalizada."
            return (message_start, message_end)
        else:
            return ("⛔ No hay canción seleccionada para reproducir.",)

    def next_song(self):
        if (self.playlist.get_size() == 0):
            raise EmptyPlaylistError("La playlist está vacía")

        if self.current:
            self.current = self.current.next
            return f"Reproduciendo la siguiente canción de la playlist: {self.current.song}"
        else:
            return f"No se está reproduciendo actualmente ninguna canción"

    def previous_song(self):
        if (self.playlist.get_size() == 0):
            raise EmptyPlaylistError("La playlist está vacía")

        if self.current:
            self.current = self.current.prev
            return f"Reproduciendo anterior canción de la playlist: {self.current.song}"
        else:
            return f"No se está reproduciendo actualmente ninguna canción"

    def show_current_song(self):
        if self.current:
            return f"Actualmente suena '{self.current.song.title}', de {self.current.song.artist} y dura {self.current.song.duration}s."
        else:
            return "No hay ninguna canción seleccionada."

    def show_playlist(self):
        if (self.playlist.get_size() == 0):
            return f"La playlist está vacía"
        return str(self.playlist)

    def shuffle(self):
        if self.playlist.get_size() == 0:
            raise EmptyPlaylistError("La playlist está vacía")

        songs = []
        current = self.playlist.get_head()
        for _ in range(self.playlist.get_size()):
            songs.append(current.song.title)
            current = current.next

        print(songs)
        random_title = random.choice(songs)

        current = self.playlist.get_head()

        for _ in range(self.playlist.get_size()):
            if current.song.title == random_title:
                self.current = current
                break
            current = current.next

        return f"🔀 Reproduciendo aleatoriamente: {random_title}"
    
    def generate_subplaylist(self):
        pass

    def advance_song(self):
        pass

