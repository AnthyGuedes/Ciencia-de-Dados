import requests


def enviar_arquivo():
    caminho = r'C:/Users/guede/Downloads/MeuHorario (2).pdf'

    # -------------------------------------------------------------
    # MUDANÇA 1: Definimos o servidor manualmente (store1 é o principal)
    # MUDANÇA 2: O caminho da URL mudou. Adicionamos '/contents/'
    # -------------------------------------------------------------
    servidor = "store1"
    url_upload = f'https://{servidor}.gofile.io/contents/uploadfile'

    print(f'Tentando upload direto para: {url_upload}')

    try:
        with open(caminho, 'rb') as arquivo:
            files = {'file': arquivo}

            # Adicionamos um timeout para não travar se o site demorar
            response_upload = requests.post(url_upload, files=files, timeout=60)

            # Verifica se a API respondeu algo válido
            try:
                saida_upload = response_upload.json()

                if saida_upload['status'] == 'ok':
                    link = saida_upload['data']['downloadPage']
                    print(f"✅ SUCESSO! Link: {link}")
                else:
                    print("❌ Falha no upload. Resposta da API:", saida_upload)

            except requests.exceptions.JSONDecodeError:
                print("Erro: A API não retornou JSON. O servidor pode estar cheio ou o endereço mudou novamente.")
                print("Resposta bruta:", response_upload.text[:200])  # Mostra só o começo do erro

    except FileNotFoundError:
        print(f"Erro: Arquivo não encontrado: {caminho}")
    except Exception as e:
        print(f"Erro genérico: {e}")


enviar_arquivo()