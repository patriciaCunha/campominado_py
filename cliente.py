from ast import literal_eval
from socket import socket, AF_INET, SOCK_DGRAM
from datetime import datetime
from campo_minado_view import iniciar_novo_jogo, continuar_jogo, efetuar_nova_jogada,menu_inicial, sair
from consts_mensagem import CODIGO_COMANDO, CODIGO_RESPOSTA, COMANDO_EFETUAR_JOGADA, JOGADA_LINHA, JOGADA_COLUNA ,COMANDO_SHOW, IMPRIMIR, QTD

ENCODE = "UTF-8"
HOST = '127.0.0.1'
PORT = 5000
MAX_BYTES = 65535

def enviar(mensagem):

    dest = (HOST, PORT)
    sock = socket(AF_INET, SOCK_DGRAM)

    data = mensagem.encode(ENCODE)
    sock.sendto(data, dest)

    data, address = sock.recvfrom(MAX_BYTES)
    respota = data.decode(ENCODE)

    sock.close()

    return respota
"""Função para receber as jogadas e enviar para o servidor"""

def qtd_jogadas():
    contexto = {CODIGO_COMANDO: QTD}
    mensagem = str(contexto)
    resposta = literal_eval(enviar(mensagem))
    return (str(resposta))

def tabuleiro_show():
    contexto = {CODIGO_COMANDO: IMPRIMIR}
    mensagem = str(contexto)
    resposta = literal_eval(enviar(mensagem))
    for posicao in resposta:
        print (str(posicao))

def tratar_jogadas():
    while True:
        contexto = {CODIGO_COMANDO: COMANDO_EFETUAR_JOGADA}
        contexto[JOGADA_LINHA] = input("[Jogada] Informe a linha: ")
        contexto[JOGADA_COLUNA] = input("[Jogada] Informe a coluna: ")
        mensagem = str(contexto)
        resposta = literal_eval(enviar(mensagem))  #resposta
        qtd = qtd_jogadas()
        print('QUANTIDADE DE JOGADAS RESTANTES',qtd)
        if qtd == '0':
            print("GAMEOVER")



        tabuleiro_show()






"""Fim tratar_jogadas"""


def cliente():

    switcher = {
        1: iniciar_novo_jogo,
        9: sair,
    }

    while True:
        menu_inicial()
        opcao = int(input("Opção escolhida: "))

        contexto = {CODIGO_COMANDO: opcao}

        func = switcher.get(opcao)

        mensagem = func(contexto)
        print(contexto)

        resposta = literal_eval(enviar(mensagem))
        for posicao in resposta:
             print (str(posicao))

        tratar_jogadas()

if __name__ == "__main__":
    cliente()
