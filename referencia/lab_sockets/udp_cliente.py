import socket
from datetime import datetime

ENCODE = "UTF-8"
HOST = '127.0.0.1'   # Endereco IP do Servidor
PORT = 5000          # Porta que o Servidor esta
MAX_BYTES = 65535    # Quantidade de Bytes a serem ser recebidos

def client():
    """ Procedimento responsável por enviar dados para o servidor e receber alguma resposta por conta disso """

    text = input("Digite algum texto:\n")
    data = text.encode(ENCODE)
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    dest = (HOST, PORT)
    sock.sendto(data, dest)

    print(sock.getsockname())
    data, address = sock.recvfrom(MAX_BYTES)
    text = data.decode(ENCODE)
    print(address, text)

    sock.close()
    
client()