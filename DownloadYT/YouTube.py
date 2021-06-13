try:    
    from pytube import YouTube
    from pytube import Playlist
    import moviepy.editor as mp
    import re
    import os
except Exception as e:
    print("Algo deu errado {}".format(e))

#Digite o link do video e o local que deseja salvar o mp3
link = input("Digite o link do video: ")
path = input("Digite o diretorio que deseja salvar: ")
yt= YouTube(link)

#Começa a baixar
print("Baixando...")
ys= yt.streams.filter(only_audio=True).first().download()
print("Completo!!!")

#converte mp4 para mp3
print("Convertendo...")
for file in os.listdir(path):
    if re.search('mp4', file):
        mp4_path = os.path.join(path, file)
        mp3_path = os.path.join(path, os.path.splitext(file)[0]+'.mp3')
        new_file = mp.AudioFileClip(mp4_path)
        new_file.write_audiofile(mp3_path)
        os.remove(mp4_path)
print("Sucesso!!!")         
