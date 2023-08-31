import random
from ..models.musica import Musica
from ..views.musica_view import MusicaView
from ..views.playlist_view import PlaylistView
from  musica_controller import MusicaController


class PlaylistController:
    def __init__(self):
        self.musica_view = MusicaView()
        self.playlist_view = PlaylistView()
        self.musica_controller = MusicaController()
        self.playlist = None

    def criar_playlist_aleatoria(self):
        musicas = self.musica_controller.obter_musicas()

        if not musicas:
            self.playlist_view.mostrar_mensagem('Nenhuma música cadastrada.')
            return

        random.shuffle(musicas)
        self.playlist = musicas
        self.playlist_view.mostrar_playlist(self.playlist)