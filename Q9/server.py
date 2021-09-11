from CONSTANTS import MSG_HD
import socket
from CONSTANTS import PORTA
import psutil, os


def mostra_uso_disco():
      disco = psutil.disk_usage('.')
      total = round(disco.total/(1024*1024*1024), 2)      
      totalDisp = round(disco.free/(1024*1024*1024),1)
      uso_total = "Uso de Disco: (Total: " + str(total) + "GB)  "
      uso_disp = "Uso de Disco: (Disponivel: " + str(totalDisp) + "GB)  "
      result = uso_total + uso_disp
      return result

def exibir_nome_dir():
      diretorio_caminho = os.getcwd()
      diretorio_nome = os.path.basename(diretorio_caminho)
      return "Diretorio: " + diretorio_nome
    
    

udp = socket.socket (socket.AF_INET, socket.SOCK_DGRAM)
host = socket.gethostname()
udp.bind((host, PORTA))
print('Esperando receber na porta', PORTA, '...')
(msg, cliente) = udp.recvfrom(1024)
msg = msg.decode('ascii')

while True: 
      if msg == MSG_HD:
            resposta = mostra_uso_disco() + exibir_nome_dir()
        
      udp.sendto(resposta.encode('ascii'), cliente)     
   
      udp.close()