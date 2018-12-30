from socket import *

class Cliente(object):
    def __init__(self):
        pass
    # Recebe o host e port, depois solicita a conexão ao servidor
    def conect(self, host, port):
        serverhost = host
        serverport = port

        self.sockobj = socket(AF_INET, SOCK_STREAM)
        
        self.sockobj.connect((serverhost, serverport))
        self.data = self.sockobj.recv(1024)
            
        

        

    def ping(self):

        msg = b'ok'

        self.sockobj.send(msg)

        data = self.sockobj.recv(1024)

        return data

    def inserir(self):
        self.sockobj.send(b'1')
        data = self.sockobj.recv(1024)
        return data

    # Envia dados de cadastro ao banco de dados do servidor
    def send(self, nome, sexo, telefone, email):
        
        msg = [bytes(nome, 'utf-8'), bytes(sexo, 'utf-8'), bytes(telefone, 'utf-8'), bytes(email, 'utf-8')]

        print(msg)
        print(type(msg))

        data = []
        for dados in msg:
            self.sockobj.send(dados)
            data.append(self.sockobj.recv(1024))
            print(dados)
        
  
        print(data)
        return data[3]

        

    def enviar(self, nome):
        self.sockobj.send(bytes(nome, 'utf-8'))
        data = self.sockobj.recv(1024)
        print(data)
        return data

    def desconectar(self):
        self.sockobj.send(b's')
        data = self.sockobj.recv(1024)
        return data

    def desligar(self):
        self.sockobj.send(b'2')
        return self.sockobj.recv(1024)



        

