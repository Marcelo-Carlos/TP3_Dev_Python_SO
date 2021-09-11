#Associado à questão anterior, crie um programa servidor que:
#Espere conexões UDP de processos na porta 9991.
#Aguarde indefinidamente conexão de clientes.
#Sirva cada cliente com a informação da quantidade total e disponível de armazenamento do disco principal (diretório corrente que o processo servidor está executando).
from CONSTANTS import MSG_HD
import socket
from CONSTANTS import PORTA

HOST = socket.gethostname()
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dest = (HOST, PORTA)
msg = MSG_HD

udp.sendto(msg.encode('ascii'), dest)


(msg, server) = udp.recvfrom(1024)
msg = msg.decode('ascii')
print(msg)


udp.close()
    
    
    