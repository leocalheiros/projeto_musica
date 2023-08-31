from src.controllers.musica_controller import MusicaController
from src.controllers.playlist_controller import PlaylistController
from src.views.menu_view import MenuView
from src.views.musica_view import MusicaView
from src.views.playlist_view import PlaylistView

def main():
    musica_controller = MusicaController()
    playlist_controller = PlaylistController()
    menu_view = MenuView()

    while True:
        menu_view.mostrar_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            titulo = input("Digite o título da música: ")
            artista = input("Digite o nome do artista: ")
            ano = input("Digite o ano de publicação: ")
            musica_controller.cadastrar_musica(titulo, artista, ano)

        elif opcao == '2':
            titulo = input("Digite o título da música que deseja buscar: ")
            musicas_encontradas = musica_controller.buscar_por_titulo(titulo)
            MusicaView().mostrar_musicas(musicas_encontradas)

        elif opcao == '3':
            ano = input("Digite o ano de publicação das músicas que deseja buscar: ")
            musicas_encontradas = musica_controller.buscar_por_ano(ano)
            MusicaView().mostrar_musicas(musicas_encontradas)

        elif opcao == '4':
            musicas = musica_controller.obter_musicas()
            if not musicas:
                print("Nenhuma música cadastrada.")
            else:
                playlist_controller.criar_playlist_aleatoria(musicas)
                playlist = playlist_controller.obter_playlist()
                PlaylistView().mostrar_playlist(playlist)

        elif opcao == '5':
            print("Saindo do programa.")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
