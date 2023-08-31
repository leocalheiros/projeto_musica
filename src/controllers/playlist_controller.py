import random
from ..models.playlist import Playlist

class PlaylistController:
    def __init__(self):
        self.playlist = Playlist()

    def criar_playlist_aleatoria(self, musicas):
        self.playlist.limpar_playlist()  # Limpar a playlist atual
        random.shuffle(musicas)
        for musica in musicas:
            self.playlist.adicionar_musica(musica)

    def obter_playlist(self):
        return self.playlist.mostrar_playlist()
