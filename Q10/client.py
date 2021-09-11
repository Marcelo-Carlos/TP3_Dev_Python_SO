import socket, sys, os

# Cria o socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
nome_arq = input('Entre com o nome do arquivo: ')
"/Users/marca/Downloads/imagem.png"
try:
    # Tenta se conectar ao servidor
    s.connect((socket.gethostname(), 8881))
    # Envia o nome do arquivo:
    s.send(nome_arq.encode('ascii'))
    # Recebe o tamanho do arquivo:
    msg = s.recv(1024)
    tamanho = int(msg.decode('ascii'))
    # Checa se o arquivo existe no servidor:
    if tamanho >= 0:
        print('tamanho do arquivo', tamanho)
        # Gera o arquivo local na pasta download
        nome_arq = nome_arq.split('/')[-1]
        with open(nome_arq, "wb+") as arq:
            soma = 0
            txt_bytes = s.recv(4096)
            # Escreve o arquivo
            while txt_bytes:
                arq.write(txt_bytes)
                soma = soma + len(txt_bytes)
                # os.system('clear')
                print("Baixando..." ,soma, "KB", tamanho, "KB")
                txt_bytes = s.recv(4096)
    else:
        print('Arquivo não encontrado no servidor!')
except Exception as erro:
    raise
s.close()
input("Pressione qualquer tecla para sair...")