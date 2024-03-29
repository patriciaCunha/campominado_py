import socket
from datetime import datetime
from ast import literal_eval
from campo_minado_negocio import CampoMinado
from jsonrpclib.SimpleJSONRPCServer import SimpleJSONRPCServer
from consts_mensagem import QUANTIDADE_COLUNAS, QUANTIDADE_LINHAS, CODIGO_RESPOSTA, RESPOSTA_FALHA, RESPOSTA_SUCESSO ,JOGADA_LINHA , CODIGO_COMANDO, COMANDO_EFETUAR_JOGADA, COMANDO_SHOW, IMPRIMIR, QTD

ENCODE = "UTF-8"
MAX_BYTES = 65535
PORT = 5000
HOST = '127.0.0.1'

def server():
    serverRPC = SimpleJSONRPCServer(('localhost', 7002))
    serverRPC.register_function(printName)
    print("Iniciando servidor")
    serverRPC.serve_forever()

    jogo = CampoMinado()

    while True:
        data, address = sock.recvfrom(MAX_BYTES)
        mensagem = data.decode(ENCODE)
        contexto = literal_eval(mensagem)

        resposta = tratar_mensagem(jogo, contexto)
        print(address, mensagem)

        data = resposta.encode(ENCODE)
        sock.sendto(data, address)
        
def printName(nome, sobrenome):
    return nome + " " + sobrenome

def tratar_mensagem(jogo, contexto):

    codigo = contexto["codigo_comando"]
    print("CODIGO =  ",codigo)
    switch = {
       "1": criar_novo_jogo,
       "efetuar_jogada":jogada,
       "jogadas":quatidade,
       "tabuleiro":tabuleiro_show
    }
    func = switch.get(str(codigo))
    print("IMPRIMIR CONTEXTO ",contexto)
    return func(jogo, contexto)


def tabuleiro_show(jogo,contexto):
    tabuleiro = jogo.tabuleiro_show()
    return str(tabuleiro)

def quatidade(jogo,contexto):
    jogadas = jogo.qtd_jogadas()
    return str(jogadas)


def jogada(jogo,contexto):
    print("JOGADA() CONTEXTO  ", contexto)
    linha = int(contexto.get(JOGADA_LINHA))
    coluna = int(contexto.get(JOGADA_LINHA))
    print("LINHA ",linha," COLUNA ",coluna)
    jogo.jogada(linha,coluna)
    jogadas = jogo.qtd_jogadas()
    resposta = [tabuleiro]
     #resposta[1] = jogadas
    tabuleiro = jogo.tabuleiro_show()
    return str(tabuleiro)
    return (str(tabuleiro),str(jogadas))
    return str({CODIGO_RESPOSTA:RESPOSTA_SUCESSO})


def criar_novo_jogo(jogo,contexto):

    linha = int(contexto.get(QUANTIDADE_LINHAS))
    coluna = int(contexto.get(QUANTIDADE_COLUNAS))

    print(linha,coluna)
    jogo.criar_novo_jogo(linha,coluna)
    jogo.tabuleiro_show()
    tabu = jogo.tabuleiro_show()
    print (tabu)

    return str(tabu)
    return str({CODIGO_RESPOSTA:RESPOSTA_SUCESSO})

if __name__ == "__main__":
    servidor()
