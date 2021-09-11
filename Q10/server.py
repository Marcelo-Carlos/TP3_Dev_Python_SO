import socket, os
PORTA = 8881
socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
socket_servidor.bind((host, PORTA))

socket_servidor.listen()
print("Servidor de nome", host, "esperando conexão na porta", PORTA)
while True:
    # Aceita alguma conexão
    (socket_cliente,addr) = socket_servidor.accept()
    print("Conectado a:", str(addr))
    # Recebe pedido do cliente:
    msg = socket_cliente.recv(2048)
    nome_arq = msg.decode('ascii')
    print(nome_arq)
    if os.path.isfile(nome_arq):
        # Envia primeiro o tamanho
        tamanho = os.stat(nome_arq).st_size
        print(tamanho)
        socket_cliente.send(str(tamanho).encode('ascii'))
        # Abre o arquivo no modo leitura de bytes
        arq = open(nome_arq, 'rb')
        # Envia os dados
        info_bytes = arq.read(4096)
        while info_bytes:
            socket_cliente.send(info_bytes)
            info_bytes = arq.read(4096)
        # Fecha o arquivo
        arq.close()
    else:
        print("Não encontrou o arquivo")
        # tamanho é -1 para indicar que não achou arquivo
        socket_cliente.send(b'-1')
    # Fecha o socket cliente
    socket_cliente.close()
    # Fecha o socket servidor
socket_servidor.close()