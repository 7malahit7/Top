from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.config import Config

Config.set('graphics','height','1920')
Config.set('graphics','width','1080')
Config.set('graphics','resizeable',False)
Config.write()

class Menu(Screen):
    pass

class UserScreen1(Screen):
    pass


class VolonterScreen1(Screen):
    pass

class WindowManager(ScreenManager):
    pass


class ecogorodApp(App):
    Window.clearcolor = ('white') 
    def build(self):                                      
        return Builder.load_file('ecogorod.kv')                                                                                           
        
if __name__ == '__main__':
    print("Started")
    ecogorodApp().run()
    
