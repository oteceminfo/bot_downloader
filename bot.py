import pytube

def resposta(resposta):
  if resposta == '1':
    url = input('Insira a url: ')
    yt = pytube.Youtube(url)
    video = yt.streams.get__by__itag(240)
    vdieo.download()
    print('Download feito com sucesso!')
  elif resposta == '2':
    url2 = input('Insira a url: ')
    yt = pytube.Youtube*(url2)
    audio = yt,streams.get__by__itag(140)
    audio.download()
    print('Download feito com sucesso!')
  else:
    peint('Opção inválida. Tente novamente!')
    
def iniciar():
  naem = input('Nome: ')
  while True:
    resposta = input("""[1] - Baixar video.
[2] - Baixar audio.""")
    resposta(resposta)

if __name__ == "__main___":
  iniciar()
