from kivy.uix.screenmanager import Screen, ScreenManager, FadeTransition
from widgets import Widgets
from cliente_kivy import Cliente

class Controle(object):
    def __init__(self):

        wg = Widgets()
        self.sk = Cliente()

        self.sm = wg.sm

        # Telas
        self.screen_home = wg.screen_home # name = home
        self.screen_terminal = wg.screen_terminal # name = terminal
        self.screen_cadastro = wg.screen_cadastro # name = cadastro
        
        # Home
        self.label = wg.label
        
        self.entry_host = wg.entry_host
        self.entry_port = wg.entry_port
        
        # Terminal
        self.lbterminal = wg.lbterminal

        self.entry_comando = wg.entry_comando

        self.botao = wg.botao
        self.botao.bind(on_release = lambda x: self.conectar())

        self.botao_ins = wg.botao_ins
        self.botao_ins.bind(on_release = lambda x: self.insert())

        self.botao_ping = wg.botao_ping
        self.botao_ping.bind(on_release = lambda x: self.ping())

        self.botao_env = wg.botao_env
        self.botao_env.bind(on_release = lambda x: self.enviar())

        self.botao_desc = wg.botao_desc
        self.botao_desc.bind(on_release = lambda x: self.desconectar())

        # Cadastro

        self.lbcadastro = wg.lbcadastro
        self.entry_nome = wg.entry_nome
        self.entry_sexo = wg.entry_sexo
        self.entry_telefone = wg.entry_telefone
        self.entry_email = wg.entry_email

        self.btsend = wg.bt_send
        self.btsend.bind(on_release = lambda x: self.send())

    def conectar(self):
        if self.label.text != 'Conectado ao servidor' and self.label.text != 'O cliente já está conectado ao servidor.':
            try:
                host = self.entry_host.text
                port = int(self.entry_port.text)
                self.sk.conect(host, port)
                
                text = self.sk.data.decode()
                self.lbterminal.text= str(text)
                # Faz a mudança da tela
                self.sm.current='terminal'

            except:
                self.label.text='Não foi possível se conectar ao servidor'
        else:
            self.label.text='O cliente já está conectado ao servidor.'


    def ping(self):
        try:
            self.lbterminal.text=str(self.sk.ping().decode())
        except:
            self.lbterminal.text='Não foi possível enviar a solicitação de Ping\nao servidor. Certifique-se se está devidamente conectado.'

    
    def insert(self):
        
        try:
            #self.lbterminal.text=str(self.sk.inserir().decode())
            
            self.sm.current='cadastro'
            self.lbcadastro.text=str(self.sk.inserir().decode())
            
            """
            nome = self.entry_nome.text
            sexo = self.entry_sexo
            telefone = self.entry_telefone
            email = self.entry_email

            self.lbcadastro.text= str(self.sk.send(nome, sexo, telefone, email).decode())
            """
            
            pass
        except:
            self.lbterminal.text='Nenhum servidor conectado'

    def enviar(self):
        print('Abrir browser')
        
        self.lbterminal.text=str(self.sk.desligar().decode())
       
    
    def desconectar(self):
        
        self.sm.current='home'
        self.label.text=str(self.sk.desconectar().decode())
        
        pass


    def send(self):
        

        nome = self.entry_nome.text
        sexo = self.entry_sexo.text
        telefone = self.entry_telefone.text
        email = self.entry_email.text

        if len(nome) != 0 or len(sexo) != 0 or len(telefone) != 0 or len(email) != 0:
            self.label.text= str(self.sk.send(nome, sexo, telefone, email).decode())
            self.sm.current='home'
        else:
            self.lbcadastro.text='Favor preecher todos os campos'