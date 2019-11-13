from jsonrpclib.SimpleJSONRPCServer import SimpleJSONRPCServer


def printName(nome, sobrenome):
    return nome + " " + sobrenome

def server():
    serverRPC = SimpleJSONRPCServer(('localhost', 7002))
    serverRPC.register_function(printName)
    print("Iniciando servidor")
    serverRPC.serve_forever()
