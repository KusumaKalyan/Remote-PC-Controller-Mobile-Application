import kivy
kivy.require('1.1.1') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout

import PCcontrollerscript as pcs
from kivy.graphics.instructions import Canvas
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Rectangle
from kivy.uix.image import Image
from kivy.uix.label import Label

class InnerWidget(AnchorLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas: 
            Color(204/255, 246/255, 200/255, mode='rgb')  # set the colour  
            # Seting the size and position of canvas 
            self.rect = Rectangle(pos = self.center, 
                                  size =(self.width, 
                                        self.height)) 
            # Update the canvas as the screen size change 
            self.bind(pos = self.update_rect, 
                  size = self.update_rect)
        self.build()
        # try:
        if pcs.getPCStatus() == "1":
            self.on_btn.background_color = (184/255,59/255,93/255,0.7)
            self.off_btn.background_color = (112/255,173/255,181/255,0.7)
        elif pcs.getPCStatus() == "0":
            self.on_btn.background_color = (112/255,173/255,181/255,0.7)
            self.off_btn.background_color = (184/255,59/255,93/255,0.7)
        # except expression as identifier:
import kivy
kivy.require('1.1.1') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout

import PCcontrollerscript as pcs
from kivy.graphics.instructions import Canvas
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Rectangle
from kivy.uix.image import Image
from kivy.uix.label import Label
import cProfile

class InnerWidget(AnchorLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas: 
            Color(204/255, 246/255, 200/255, mode='rgb')  # set the colour  
            # Seting the size and position of canvas 
            self.rect = Rectangle(pos = self.center, 
                                  size =(self.width, 
                                        self.height)) 
            # Update the canvas as the screen size change 
            self.bind(pos = self.update_rect, 
                  size = self.update_rect)
        self.build()
        try:
            if pcs.getPCStatus() == "1":
                self.on_btn.background_color = (184/255,59/255,93/255,0.7)
                self.off_btn.background_color = (112/255,173/255,181/255,0.7)
            elif pcs.getPCStatus() == "0":
                self.on_btn.background_color = (112/255,173/255,181/255,0.7)
                self.off_btn.background_color = (184/255,59/255,93/255,0.7)
        except expression as identifier:
            pass
  
    # update function which makes the canvas adjustable. 
    def update_rect(self, *args): 
        self.rect.pos = self.pos 
        self.rect.size = self.size 
    
    def onMachine(self, value):
        if pcs.onMachine() == 'successfull':
            value.background_color = (184/255,59/255,93/255,0.7)
            self.off_btn.background_color = (112/255,173/255,181/255,0.7)
    
    def offMachine(self, value):
        if pcs.offMachine() == 'successfull':
            value.background_color= (184/255,59/255,93/255,0.7)
            self.on_btn.background_color = (112/255,173/255,181/255,0.7)
    
    def on_start(self):
        pass

    def on_stop(self):
    	Window.close()
    
    def on_pause(self):
      # Here you can save data if needed
        Window.close()
        App.get_running_app().stop()
        return False

    def on_resume(self):
      # Here you can check if any data needs replacing (usually nothing)
        pass
    
    def build(self):
        self.show_img = Image(source='images/remote-desktop.png',
        			 allow_stretch= True,)
        self.on_btn = Button(id='on_btn', text='ON', background_color=(112/255,173/255,181/255,0.7), size_hint=(1,0.25),
                                background_normal= '',)
        self.on_btn.bind(on_press = self.onMachine)
        self.off_btn = Button(id='off_btn', text='OFF', background_color=(112/255,173/255,181/255,0.7), size_hint=(1,0.25),
                                background_normal= '',)
        self.off_btn.bind(on_press = self.offMachine)
        self.box_layout = BoxLayout(orientation='vertical', size_hint=(0.5,0.5), spacing=3)
        self.box_layout.add_widget(self.show_img)
        self.box_layout.add_widget(self.on_btn)
        self.box_layout.add_widget(self.off_btn)
        self.add_widget(self.box_layout)
        
class PCApp(App):
    
    def build(self):
        return InnerWidget()

def reset():
    import kivy.core.window as window
    from kivy.base import EventLoop
    if not EventLoop.event_listeners:
        from kivy.cache import Cache
        window.Window = window.core_select_lib('window', window.window_impl, True)
        Cache.print_usage()
        for cat in Cache._categories:
            Cache._objects[cat] = {}

if __name__ == '__main__':
    reset()
    PCApp().run()
