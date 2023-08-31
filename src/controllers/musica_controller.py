from ..models.musica import Musica
from ..views.musica_view import MusicaView

class MusicaController:
    def __init__(self):
        self.lista_musicas = []
        self.musica_view = MusicaView()

    def cadastrar_musica(self, titulo, artista, ano):
        musica = Musica(titulo, artista, ano)
        self.lista_musicas.append(musica)  # Adiciona a música diretamente à lista
        self.musica_view.mostrar_mensagem(f'{titulo} cadastrada com sucesso!')

    def buscar_por_titulo(self, titulo):
        musicas_encontradas = [musica for musica in self.lista_musicas if musica.titulo == titulo]
        self.musica_view.mostrar_musicas(musicas_encontradas)

    def buscar_por_ano(self, ano):
        musicas_encontradas = [musica for musica in self.lista_musicas if musica.ano == ano]
        self.musica_view.mostrar_musicas(musicas_encontradas)
