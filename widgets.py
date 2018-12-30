from kivy.uix.screenmanager import Screen, ScreenManager, FadeTransition
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

class Widgets(object):
    def __init__(self):
        self.sm = ScreenManager(transition = FadeTransition())
        
        # WIDGETS HOME
        self.label = Label()
        self.entry_host = TextInput()
        self.entry_host.text='192.168.0.4'

        self.entry_port = TextInput()
        self.entry_port.text = '5000'

        self.botao = Button()
        self.botao.text='Conectar'
        #=============================================

        # WIDGETS TERMINAL
        self.lbterminal = Label()
        self.entry_comando = TextInput()

        self.botao_ping = Button()
        self.botao_ping.text='Ping'
        
        self.botao_ins = Button()
        self.botao_ins.text='Cadastro'

        self.botao_env = Button()
        self.botao_env.text='Chrome'

        self.botao_desc = Button()
        self.botao_desc.text='Desconectar'
        #============================================

        # WIDGETS CADASTRO

        self.lbcadastro = Label()
        
        self.entry_nome = TextInput(hint_text = 'Nome')
        self.entry_sexo = TextInput(hint_text = 'Sexo')
        self.entry_telefone = TextInput(hint_text = 'Telefone')
        self.entry_email = TextInput(hint_text = 'E-mail')

        self.bt_send = Button()
        self.bt_send.text='Enviar'
        #============================================


        """Configuração da janela principal (Home) """
        
        # Tela inicial
        self.screen_home = Screen()
        self.screen_home.name='home'
        
        # BoxLayout da Tela principal
        box_label = BoxLayout()
        box_entry = BoxLayout(orientation = 'vertical')
        box_botao = BoxLayout()
        box_pai = BoxLayout(orientation = 'vertical')

        # BoxLayout da Label
        box_label.add_widget(self.label)

        # BoxLayout das entry
        box_entry.add_widget(self.entry_host)
        box_entry.add_widget(self.entry_port)

        # BoxLayout dos botões
        box_botao.add_widget(self.botao)
        
        # BoxLayout -pai que unificar todos os outros Box Layout
        box_pai.add_widget(box_label)
        box_pai.add_widget(box_entry)
        box_pai.add_widget(box_botao)

        # Inserir Box_pai na Janela principal
        self.screen_home.add_widget(box_pai)
        

        """Configuração da janela pós-conexão (Terminal) """
        
        # Tela a ser exibida
        self.screen_terminal = Screen()
        self.screen_terminal.name='terminal'

        # BoxLayout do terminal
        box_lbscreen = BoxLayout()
        box_interminal = BoxLayout()
        box_btterminal = BoxLayout()
        box_paiterminal = BoxLayout(orientation = 'vertical')

        # BoxLayout da label terminal
        box_lbscreen.add_widget(self.lbterminal)

        # BoxLayout da entry terminal
        box_interminal.add_widget(self.entry_comando)

        # BoxLayout dos botões terminal
        box_btterminal.add_widget(self.botao_ins)
        box_btterminal.add_widget(self.botao_env)
        box_btterminal.add_widget(self.botao_ping)
        box_btterminal.add_widget(self.botao_desc)

        # BoxLayout -pai que unificar todos os outros Box Layout
        box_paiterminal.add_widget(box_lbscreen)
        box_paiterminal.add_widget(box_interminal)
        box_paiterminal.add_widget(box_btterminal)

        # Inserir box_pai terminal na janela
        self.screen_terminal.add_widget(box_paiterminal)


        """ Tela de cadastro """
        
        # Tela a ser exibida
        self.screen_cadastro = Screen()
        self.screen_cadastro.name='cadastro'

        # BoxLayout do cadastro
        box_lbcadastro = BoxLayout()
        box_incadastro = BoxLayout(orientation = 'vertical')
        box_btcadastro = BoxLayout()
        box_paicadastro = BoxLayout(orientation = 'vertical')

        # BoxLayout label cadastro
        box_lbcadastro.add_widget(self.lbcadastro)

        # BoxLayout entry cadastro
        box_incadastro.add_widget(self.entry_nome)
        box_incadastro.add_widget(self.entry_sexo)
        box_incadastro.add_widget(self.entry_telefone)
        box_incadastro.add_widget(self.entry_email)

        # BoxLayout botão cadastro
        box_btcadastro.add_widget(self.bt_send)

        # Box_pai cadastro
        box_paicadastro.add_widget(box_lbcadastro)
        box_paicadastro.add_widget(box_incadastro)
        box_paicadastro.add_widget(box_btcadastro)
        
        # Inserir box_pai na janela
        self.screen_cadastro.add_widget(box_paicadastro)
        

        #-------------------------------------------------------

        self.sm.add_widget(self.screen_home)
        self.sm.add_widget(self.screen_terminal)
        self.sm.add_widget(self.screen_cadastro)

        




        






        