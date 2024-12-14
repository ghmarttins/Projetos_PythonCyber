from socket import * 

#           localhost
endereco = "127.0.0.1"

porta = 43210


while True:
    # IPv4 e o IPv6

    #TCP ou UDP
    #TCP - Mais Segura
    # UDP - Menos Seguro e Mais Rapido
    obj_socket = socket(AF_INET, SOCK_STREAM)

    obj_socket.connect((endereco, porta))
    msg = bytes(input("Mensagem: "), 'utf-8')


    obj_socket.send(msg)

    resposta = obj_socket.recv(1024)
    print("Resposta: ", str(resposta)[2:-1])
    if str(msg)[2:-1] == "fim":
        break
obj_socket.close()

