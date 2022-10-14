from pytube import YouTube

# Digite o link do Video e o local que deseja salvar o video #
link = input("Digite o link do video que deseja baixar: ")
path = input("Digite o diretorio que deseja salva o video: ")
yt = YouTube(link)

#Mostras os detalhes do Video#
print("Titulo: ", yt.title)
print("Numero de Viws: ", yt.views)
print("Tamanho do video: ", yt.length)
print("Avaliação do video: ", yt.rating)

#usar a maior resolução#
ys = yt.streams.get_highest_resolution()

#começa o download#

print("baixando...")
ys.download(path)
print("Download completo!")