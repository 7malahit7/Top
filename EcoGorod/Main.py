from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.config import Config
from kivy.core.window import Window

Config.set('graphics','resizeable',False)
Config.write()

class Menu(Screen):
    pass
class UserScreen1(Screen):
    pass
class UserScreen2(Screen):
    pass
class WindowManager(ScreenManager):
    pass
class VolonterScreen1(Screen):
    pass
    
class ecogorodApp(App):    
    Window.clearcolor = ('white') 
    Window.size = (1080,1920)
    def build(self):                                      
        return Builder.load_file('ecogorod.kv')   
                                                                                                    
if __name__ == '__main__':
    ecogorodApp().run()
    
