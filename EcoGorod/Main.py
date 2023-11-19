from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder




class Menu(Screen):
    pass

class Volonter1(Screen):
    pass
s
class WindowManager(ScreenManager):
    pass

# class MyMenu(BoxLayout):
#     Window.clearcolor = ('white') 
    
class ecogorodApp(App):
    Window.clearcolor = ('white') 
    Window.baackground = ""
    def build(self):                                      
        return Builder.load_file('ecogorod.kv')                                                                                           
        
if __name__ == '__main__':
    print("Started")
    ecogorodApp().run()
    
