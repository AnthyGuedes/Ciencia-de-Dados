import requests

def enviar_arquivo():
    caminho = 'C:/Users/guede/Downloads/MeuHorario (2).pdf'

    requisicao = requests.post('https://gofile.io/uploadfile', files={'file': open(caminho, 'rb')}) # b = formato binário
    saida_requisicao = requisicao.json()

    print(saida_requisicao)
    url = saida_requisicao['link']
    print("Arquivo enviado | Link para acesso: ", url)

def enviar_arquivo_chave():

    caminho = caminho = 'C:/Users/guede/Downloads/MeuHorario (2).pdf'
    chave_acess = 'XdywuvKATFkZ4ZzJOu6a8dd2gXd03FCN' # API KEY

    requisicao = requests.post(
        'https://gofile.io/uploadfile',
        files={'file': open(caminho, 'rb')},
        headers={'Authorization': + chave_acess}
    )

    saida_requisicao = requisicao.json()

    print(saida_requisicao)
    url = saida_requisicao['link']
    print("Arquivo enviado com chave de acesso | Link para acesso: ", url)

def receber_arquivo(file_url):

    requisao = requests.get(file_url)

    if requisao.ok:
        with open('arquivo_baixado.pdf', 'wb') as file:
            file.write(requisao.content)
        print("Arquivo baixado com sucesso")
    else:
        print("Erro ao baixar arquivo: ", requisao.json())

enviar_arquivo()
