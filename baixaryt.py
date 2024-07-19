from pytube import YouTube

def download_video(url, resolution="1080p"):
    try:
        # Cria o objeto YouTube
        yt = YouTube(url)
        
        # Obtém o stream com a resolução especificada
        stream = yt.streams.filter(res=resolution, file_extension='mp4').first()
        
        if not stream:
            print(f"Resolução {resolution} não encontrada. Baixando na maior resolução disponível.")
            stream = yt.streams.get_highest_resolution()

        # Baixa o vídeo
        stream.download()

        print(f'Vídeo baixado com sucesso: {yt.title}')
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# URL do vídeo do YouTube
video_url = "https://www.youtube.com/watch?v=szj_9-Fpba8"

# Baixa o vídeo
download_video(video_url)
