class Playlist:
    def __init__(self):
        self.musicas = []

    def adicionar_musica(self, musica):
        self.musicas.append(musica)

    def mostrar_playlist(self):
        if not self.musicas:
            return "Playlist vazia."

        playlist_str = "\n--- Playlist ---\n"
        for idx, musica in enumerate(self.musicas, start=1):
            playlist_str += f"{idx}. {musica.titulo} - {musica.artista} ({musica.ano})\n"

        return playlist_str

    def limpar_playlist(self):
        self.musicas = []