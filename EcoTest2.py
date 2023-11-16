from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.config import Config
from kivy.uix.screenmanager import ScreenManager, Screen



Config.set('graphics','resizeable',False)   #блочит изменение размер (нет)
#Config.set('graphics','height','1200')      #высота                         я хуй знает че сюда о размерам делать, + если их меняешь все слетает и криво, надо еще разобраться
#Config.set('graphics','width','1000')       #ширина
Config.write()                  #хз нахуя



class FirstScreen(Screen):
    button1 = Button(
     background_normal = 'VolonterButton.png',         # <-- Кнопка Волонтер 
     background_down = 'VolonterButtonDown.png',             # <-- Кнопка Волонтер В нажатом состояние                                                                       
     pos = (250,30),                                                                    # позиция
     size_hint = (1,1)                                                                   # высота ширина  ( в % )
    )
    button2 = Button(
                     background_normal = 'Button.png',         # <-- Кнопка Юзера
                     background_down = 'ButtonDown.png',             # <-- Кнопка юзера в нажатом состояние                                                         
                     pos = (250, 220),                                                                  # позиция
                     size_hint = (1,1))                                                                 # высота ширина  ( в % )
    logo = Image(source='logo.png',                           # <-- лого
                size_hint=(2, 2),                                                                       # высота ширина  ( в % )
                pos = (-20,701))                                                                      #позиция
    fl = FloatLayout(size = (570,180),size_hint = (None,None))                                          #лэйаут с кастомным выбором позиции, но от того и беды с расширение                             
                                                                                                        #надо почитать
    fl.add_widget(button1)                                                                              
    fl.add_widget(button2)                                                                              #добавление виджетов в флоатлейаут
    fl.add_widget(logo)
    Window.clearcolor = ('white')   
          

class EcoGorodApp(App):
    def build(self):

        sm = ScreenManager()
        sm.add_widget(FirstScreen())                                                                  #цвет окна
        return sm                                                                           
        
if __name__ == '__main__':
    print("Started")
    EcoGorodApp().run()

