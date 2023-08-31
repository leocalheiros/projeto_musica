from ..models.musica import Musica


class MusicaController:
    def __init__(self):
        self.lista_musicas = []

    def cadastrar_musica(self, titulo, artista, ano):
        musica = Musica(titulo, artista, ano)
        self.lista_musicas.append(musica)

    def buscar_por_titulo(self, titulo):
        return [musica for musica in self.lista_musicas if musica.titulo == titulo]

    def buscar_por_ano(self, ano):
        return [musica for musica in self.lista_musicas if musica.ano == ano]

    def obter_musicas(self):
        return self.lista_musicas
