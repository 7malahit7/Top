from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout

#from kivy.uix.screenmanager import Screen
# from kivy.config import Config
#from kivy.uix.label import Label

#Config.set('graphics','resizeable','0')
# Config.set('graphics','height','1920')
# Config.set('graphics','width','1080')

# class MyScreen(Screen):
#     def __init__(self,**kwargs):
#         super().__init__(**kwargs)
class MyApp(App):
    def build(self):
        button1 = Button(text='Я волонтер',
                         font_size = 35,
                         color = 'black',
                         background_color = [0,.47,.24,1],
                         pos = (220,100),
                        size_hint = (.5,.25)
        )
        button2 = Button(text = "Я хочу сфоткать мусор",
                         font_size = 35,
                         color = "black",
                         background_color = [0,.47,.24,1],
                         pos = (220,450),
                         size_hint = (.5,.25))

        fl = FloatLayout(size = (300,300))
        fl.add_widget(button1)
        fl.add_widget(button2)
        # fl.add_widget(button2)
        button1.on_press()
        return fl
        
if __name__ == '__main__':
    print("Started")
    MyApp().run()
    
