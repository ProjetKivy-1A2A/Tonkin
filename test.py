#!python
#!/usr/bin/env python

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.spinner import Spinner

from kivy.properties import ObjectProperty, StringProperty


Builder.load_string('''
#:kivy 1.0

<GridLayout>
    canvas.before:
        BorderImage:
            border: 10, 10, 10, 10
            source: 'plateau.jpg'
            pos: self.pos
            size: self.size

<TonkinTest>:

    GridLayout:
        size_hint: 1, 1
        pos_hint: {'center_x': .5, 'center_y': .5}
        rows:1

	    Button:
	    	size: .05,.05
	        id:btn: btn
	        on_press: root.changer_couleur(btn)
	        background_normal: 'img/btns/b0.png'

	    Button:
	        id:btn: btn2
	        on_press: root.changer_couleur(btn2)
	        background_normal: 'img/btns/b0.png'

	    Button:
	        id:btn: btn3
	        on_press: root.changer_couleur(btn3)
	        background_normal: 'img/btns/b0.png'

	    Button:
	        id:btn: btn4
	        on_press: root.changer_couleur(btn4)
	        background_normal: 'img/btns/b0.png'

	    Button:
	        id:btn: btn5
	        on_press: root.changer_couleur(btn5)
	        background_normal: 'img/btns/b0.png'

	    Button:
	        id:btn: btn6
	        on_press: root.changer_couleur(btn6)
	        background_normal: 'img/btns/b0.png'
''')


class TonkinTest(FloatLayout):
	joueur = 1 
	pion_a_placer = 5

	def changer_couleur(self, btn):
		if self.pion_a_placer > 0:
			if btn.state == 'down' and btn.background_normal == 'img/btns/b0.png':
				if self.joueur == 1:
					btn.background_normal = 'img/btns/btn1.png'
					self.changer_joueur()
				else:
					btn.background_normal = 'img/btns/btn2.png'
					self.changer_joueur()
				self.pion_a_placer = self.pion_a_placer - 1

	def changer_joueur(self):
		if self.joueur == 1:
			self.joueur = 2
		else:
			self.joueur = 1



class ControllerApp(App):

    def build(self):
        return TonkinTest()

if __name__ == '__main__':
    ControllerApp().run()