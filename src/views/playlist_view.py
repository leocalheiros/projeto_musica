class PlaylistView:
    def mostrar_mensagem(self, mensagem):
        print(mensagem)

    def mostrar_playlist(self, playlist):
        if not playlist:
            print("A playlist está vazia.")
            return

        print("Playlist Aleatória:")
        for index, musica in enumerate(playlist, start=1):
            print(f"{index}. {musica.titulo} - {musica.artista} ({musica.ano})")