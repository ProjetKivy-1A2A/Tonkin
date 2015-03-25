#!python
#!/usr/bin/env python

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.spinner import Spinner

Builder.load_string('''
<GridLayout>
    canvas.before:
        BorderImage:
            border: 10, 10, 10, 10
            source: 'plateau.jpg'
            pos: self.pos
            size: self.size

<RootWidget>
    GridLayout:
        size_hint: 1, 1
        pos_hint: {'center_x': .5, 'center_y': .5}
        rows:1

    Button:
    	id:btn41
		number:41
        size_hint: .05, .05
		pos_hint: {'x':.075, 'y':.075}
		id:btn41
		on_press: root.bouton_enfonce(btn41)	
	    background_normal: 'img/btns/b0.png'
		

    Button:
    	id:btn42
		number:42
        size_hint: .05, .05
		pos_hint: {'x':.325, 'y':.075}	
		on_press: root.bouton_enfonce(btn42)	
	    background_normal: 'img/btns/b0.png'
		
	Button:
    	id:btn43
		number:43
		size_hint: .05, .05
		pos_hint: {'x':.48, 'y':.075}	
		on_press: root.bouton_enfonce(btn43)	
	    background_normal: 'img/btns/b0.png'
				
	Button:
    	id:btn44
		number:44
		size_hint: .05, .05
		pos_hint: {'x':.635, 'y':.075}	
		on_press: root.bouton_enfonce(btn44)	
	    background_normal: 'img/btns/b0.png'	
	
	Button:
    	id:btn45
		number:45
		size_hint: .05, .05
		pos_hint: {'x':.88, 'y':.075}	
		on_press: root.bouton_enfonce(btn45)	
	    background_normal: 'img/btns/b0.png'

	Button:
    	id:btn26
		number:26
		size_hint: .05, .05
		pos_hint: {'x':.075, 'y':.325}	
		on_press: root.bouton_enfonce(btn26)	
	    background_normal: 'img/btns/b0.png'

	Button:
    	id:btn21
		number:21
		size_hint: .05, .05
		pos_hint: {'x':.075, 'y':.47}	
		on_press: root.bouton_enfonce(btn21)	
	    background_normal: 'img/btns/b0.png'

	Button:
    	id:btn10
		number:10
		size_hint: .05, .05
		pos_hint: {'x':.075, 'y':.62}	
		on_press: root.bouton_enfonce(btn10)	
	    background_normal: 'img/btns/b0.png'

	Button:
    	id:btn1
		number:1
		size_hint: .05, .05
		pos_hint: {'x':.075, 'y':.87}	
		on_press: root.bouton_enfonce(btn1)	
	    background_normal: 'img/btns/b0.png'

	Button:
    	id:btn31
		number:31
		size_hint: .05, .05
		pos_hint: {'x':.88, 'y':.325}	
		on_press: root.bouton_enfonce(btn31)	
	    background_normal: 'img/btns/b0.png'

	Button:
    	id:btn25
		number:25
		size_hint: .05, .05
		pos_hint: {'x':.88, 'y':.47}	
		on_press: root.bouton_enfonce(btn25)	
	    background_normal: 'img/btns/b0.png'

	Button:
    	id:btn16
		number:16
		size_hint: .05, .05
		pos_hint: {'x':.88, 'y':.62}	
		on_press: root.bouton_enfonce(btn16)	
	    background_normal: 'img/btns/b0.png'

	Button:
    	id:btn5
		number:5
		size_hint: .05, .05
		pos_hint: {'x':.88, 'y':.87}	
		on_press: root.bouton_enfonce(btn5)	
	    background_normal: 'img/btns/b0.png'

	Button:
    	id:btn2
		number:2
		size_hint: .05, .05
		pos_hint: {'x':.325, 'y':.87}	
		on_press: root.bouton_enfonce(btn2)	
	    background_normal: 'img/btns/b0.png'

	Button:
    	id:btn3
		number:3
		size_hint: .05, .05
		pos_hint: {'x':.48, 'y':.87}	
		on_press: root.bouton_enfonce(btn3)	
	    background_normal: 'img/btns/b0.png'

	Button:
    	id:btn4
		number:4
		size_hint: .05, .05
		pos_hint: {'x':.635, 'y':.87}	
		on_press: root.bouton_enfonce(btn4)	
	    background_normal: 'img/btns/b0.png'

	Button:
    	id:btn6
		number:6
		size_hint: .05, .05
		pos_hint: {'x':.2, 'y':.75}	
		on_press: root.bouton_enfonce(btn6)	
	    background_normal: 'img/btns/b0.png'

	Button:
    	id:btn17
		number:17
		size_hint: .05, .05
		pos_hint: {'x':.18, 'y':.58}	
		on_press: root.bouton_enfonce(btn17)	
	    background_normal: 'img/btns/b0.png'

	Button:
    	id:btn27
		number:27
		size_hint: .05, .05
		pos_hint: {'x':.18, 'y':.36}	
		on_press: root.bouton_enfonce(btn27)	
	    background_normal: 'img/btns/b0.png'

	Button:
    	id:btn37
		number:37
		size_hint: .05, .05
		pos_hint: {'x':.2, 'y':.20}	
		on_press: root.bouton_enfonce(btn37)	
	    background_normal: 'img/btns/b0.png'

	Button:
    	id:btn9
		number:9
		size_hint: .05, .05
		pos_hint: {'x':.76, 'y':.75}	
		on_press: root.bouton_enfonce(btn9)	
	    background_normal: 'img/btns/b0.png'

	Button:
    	id:btn20
		number:20
		size_hint: .05, .05
		pos_hint: {'x':.775, 'y':.58}	
		on_press: root.bouton_enfonce(btn20)	
	    background_normal: 'img/btns/b0.png'

	Button:
    	id:btn30
		number:30
		size_hint: .05, .05
		pos_hint: {'x':.775, 'y':.36}	
		on_press: root.bouton_enfonce(btn30)	
	    background_normal: 'img/btns/b0.png'

	Button:
    	id:btn40
		number:40
		size_hint: .05, .05
		pos_hint: {'x':.76, 'y':.20}	
		on_press: root.bouton_enfonce(btn40)	
	    background_normal: 'img/btns/b0.png'

	Button:
    	id:btn11
		number:11
		size_hint: .05, .05
		pos_hint: {'x':.278, 'y':.680}	
		on_press: root.bouton_enfonce(btn11)	
	    background_normal: 'img/btns/b0.png'

	Button:
    	id:btn18
		number:18
		size_hint: .05, .05
		pos_hint: {'x':.278, 'y':.55}	
		on_press: root.bouton_enfonce(btn18)	
	    background_normal: 'img/btns/b0.png'

	Button:
    	id:btn22
		number:22
		size_hint: .05, .05
		pos_hint: {'x':.278, 'y':.47}	
		on_press: root.bouton_enfonce(btn22)	
	    background_normal: 'img/btns/b0.png'

	Button:
    	id:btn28
		number:28
		size_hint: .05, .05
		pos_hint: {'x':.278, 'y':.4}	
		on_press: root.bouton_enfonce(btn28)	
	    background_normal: 'img/btns/b0.png'

	Button:
    	id:btn32
		number:32
		size_hint: .05, .05
		pos_hint: {'x':.278, 'y':.27}	
		on_press: root.bouton_enfonce(btn32)	
	    background_normal: 'img/btns/b0.png'

	Button:
    	id:btn15
		number:15
		size_hint: .05, .05
		pos_hint: {'x':.68, 'y':.671}	
		on_press: root.bouton_enfonce(btn15)	
	    background_normal: 'img/btns/b0.png'

	Button:
    	id:btn19
		number:19
		size_hint: .05, .05
		pos_hint: {'x':.68, 'y':.545}	
		on_press: root.bouton_enfonce(btn19)	
	    background_normal: 'img/btns/b0.png'

	Button:
    	id:btn24
		number:24
		size_hint: .05, .05
		pos_hint: {'x':.68, 'y':.465}	
		on_press: root.bouton_enfonce(btn24)	
	    background_normal: 'img/btns/b0.png'

	Button:
    	id:btn29
		number:29
		size_hint: .05, .05
		pos_hint: {'x':.68, 'y':.395}	
		on_press: root.bouton_enfonce(btn29)	
	    background_normal: 'img/btns/b0.png'

	Button:
    	id:btn36
		number:36
		size_hint: .05, .05
		pos_hint: {'x':.68, 'y':.268}	
		on_press: root.bouton_enfonce(btn36)	
	    background_normal: 'img/btns/b0.png'

	Button:
    	id:btn33
		number:33
		size_hint: .05, .05
		pos_hint: {'x':.4, 'y':.268}	
		on_press: root.bouton_enfonce(btn33)	
	    background_normal: 'img/btns/b0.png'

	Button:
    	id:btn34
		number:34
		size_hint: .05, .05
		pos_hint: {'x':.48, 'y':.268}	
		on_press: root.bouton_enfonce(btn34)	
	    background_normal: 'img/btns/b0.png'

	Button:
    	id:btn35
		number:35
		size_hint: .05, .05
		pos_hint: {'x':.55, 'y':.268}	
		on_press: root.bouton_enfonce(btn35)	
	    background_normal: 'img/btns/b0.png'

	Button:
    	id:btn12
		number:12
		size_hint: .05, .05
		pos_hint: {'x':.4, 'y':.671}	
		on_press: root.bouton_enfonce(btn12)	
	    background_normal: 'img/btns/b0.png'

	Button:
    	id:btn13
		number:13
		size_hint: .05, .05
		pos_hint: {'x':.48, 'y':.671}	
		on_press: root.bouton_enfonce(btn13)	
	    background_normal: 'img/btns/b0.png'

	Button:
    	id:btn14
		number:14
		size_hint: .05, .05
		pos_hint: {'x':.55, 'y':.671}	
		on_press: root.bouton_enfonce(btn14)	
	    background_normal: 'img/btns/b0.png'

	Button:
    	id:btn38
		number:38
		size_hint: .05, .05
		pos_hint: {'x':.37, 'y':.18}	
		on_press: root.bouton_enfonce(btn38)	
	    background_normal: 'img/btns/b0.png'

	Button:
    	id:btn39
		number:39
		size_hint: .05, .05
		pos_hint: {'x':.59, 'y':.18}	
		on_press: root.bouton_enfonce(btn39)	
	    background_normal: 'img/btns/b0.png'

	Button:
    	id:btn7
		number:7
		size_hint: .05, .05
		pos_hint: {'x':.37, 'y':.765}	
		on_press: root.bouton_enfonce(btn7)	
	    background_normal: 'img/btns/b0.png'

	Button:
    	id:btn8
		number:8
		size_hint: .05, .05
		pos_hint: {'x':.59, 'y':.765}	
		on_press: root.bouton_enfonce(btn8)	
	    background_normal: 'img/btns/b0.png'

	Button:
    	id:btn23
		number:23
		size_hint: .05, .05
		pos_hint: {'x':.477, 'y':.475}	
		on_press: root.bouton_enfonce(btn23)	
	    background_normal: 'img/btns/b0.png'
''')

class RootWidget(FloatLayout):
	joueur = 1 
	pion_a_placer = 20
	pion_selectionne = 0
	def bouton_enfonce(self, btn):

		if self.pion_a_placer > 0:
			if btn.state == 'down' and btn.background_normal == 'img/btns/b0.png':
				if self.joueur == 1:
					btn.background_normal = 'img/btns/btn1.png'
					self.changer_joueur()
				else:
					btn.background_normal = 'img/btns/btn2.png'
					self.changer_joueur()
				self.pion_a_placer = self.pion_a_placer - 1

		else:
			if self.pion_selectionne != 0:
				print("Le pion {} sera déplacé en {}".format(self.pion_selectionne,btn.number))
				self.pion_selectionne = 0

			else:
				self.pion_selectionne = btn.number

	def changer_joueur(self):
		if self.joueur == 1:
			self.joueur = 2
		else:
			self.joueur = 1

class MainApp(App):
    def build(self):
        return RootWidget()
    	


if __name__ == '__main__':
    MainApp().run()
