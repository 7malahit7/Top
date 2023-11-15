from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.config import Config


Config.set('graphics','resizeable',False)   #блочит изменение размер (нет)
Config.set('graphics','height','1200')      #высота                         я хуй знает че сюда о размерам делать, + если их меняешь все слетает и криво, надо еще разобраться
Config.set('graphics','width','1000')       #ширина
Config.write()                  #хз нахуя

class EcoGorodApp(App):
    def build(self):
        button1 = Button(
                         background_normal = 'C:\\Users\\ilya\\Desktop\\project\\buttonImage2.png',         # <-- Кнопка Волонтер 
                         background_down = 'C:\\Users\\ilya\\Desktop\\project\\ButtonDown.png',             # <-- Кнопка Волонтер В нажатом состояние                                                                       
                         pos = (250,30),                                                                    # позиция
                        size_hint = (1,1)                                                                   # высота ширина  ( в % )
        )
        button2 = Button(
                         background_normal = 'C:\\Users\\ilya\\Desktop\\project\\buttonImage2.png',         # <-- Кнопка Юзера
                         background_down = 'C:\\Users\\ilya\\Desktop\\project\\ButtonDown.png',             # <-- Кнопка юзера в нажатом состояние                                                         
                         pos = (250, 220),                                                                  # позиция
                         size_hint = (1,1))                                                                 # высота ширина  ( в % )
        logo = Image(source='C:\\Users\\ilya\\Downloads\\logo_bez_fona_fona.png',                           # <-- лого
                    size_hint=(1, 1),                                                                       # высота ширина  ( в % )
                    pos = ((250,700)))                                                                      #позиция
        fl = FloatLayout(size = (570,180),size_hint = (None,None))                                          #лэйаут с кастомным выбором позиции, но от того и беды с расширение                             
                                                                                                            #надо почитать
        fl.add_widget(button1)                                                                              
        fl.add_widget(button2)                                                                              #добавление виджетов в флоатлейаут
        fl.add_widget(logo)

        
        Window.clearcolor = ('white')                                                                        #цвет окна
        return fl                                                                                            # возвращаем лейаут
        
if __name__ == '__main__':
    print("Started")
    EcoGorodApp().run()
    
