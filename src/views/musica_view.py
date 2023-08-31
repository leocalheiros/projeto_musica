class MusicaView:
    def mostrar_mensagem(self, mensagem):
        print(mensagem)

    def mostrar_musicas(self, musicas):
        if not musicas:
            print("Nenhuma música encontrada.")
            return

        print("\nMúsicas encontradas:")
        for musica in musicas:
            print(f'Título: {musica.titulo}, Artista: {musica.artista}, Ano: {musica.ano}')
