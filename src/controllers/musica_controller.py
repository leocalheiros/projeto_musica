from ..models.musica import Musica
from ..models.repositorio_musicas import RepositorioMusicas
from ..views.musica_view import MusicaView

class MusicaController:
    def __init__(self):
        self.repositorio_musicas = RepositorioMusicas()
        self.musica_view = MusicaView()

    def cadastrar_musica(self, titulo, artista, ano):
        musica = Musica(titulo, artista, ano)
        self.repositorio_musicas.cadastrar_musica(musica)
        self.musica_view.mostrar_mensagem(f'{titulo} cadastrada com sucesso!')

    def buscar_por_titulo(self, titulo):
        musicas_encontradas = self.repositorio_musicas.buscar_por_titulo(titulo)
        self.musica_view.mostrar_musicas(musicas_encontradas)

    def buscar_por_ano(self, ano):
        musicas_encontradas = self.repositorio_musicas.buscar_por_ano(ano)
        self.musica_view.mostrar_musicas(musicas_encontradas)
