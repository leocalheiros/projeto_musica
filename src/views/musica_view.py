class MusicaView:
    def mostrar_musicas(self, musicas):
        if not musicas:
            print("Nenhuma música encontrada.")
        else:
            print("\n--- Músicas Encontradas ---")
            for musica in musicas:
                print(f"Título: {musica.titulo}")
                print(f"Artista: {musica.artista}")
                print(f"Ano de Publicação: {musica.ano}")
                print("---------------------------")

class PlaylistView:
    def mostrar_playlist(self, playlist):
        print("\n--- Playlist Aleatória ---")
        print(playlist)
        print("--------------------------")

    def mostrar_mensagem(self, mensagem):
        print(mensagem)
