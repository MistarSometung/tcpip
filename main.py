from kivy.app import App
from controller import Controle

class Main(App):
    def build(self):

        wg = Controle()

        sm = wg.sm
        
        return sm

Main().run()