class GrilleTonkin(GridLayout):
plateau_jeu = [ #definition de plateau de jeu
	1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 
	0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
	0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
	0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
	0, 0, 0, 0, 0, 0

	]



def verifierGagnant(self):
			
		# si tous les pions noir font une ligne 
		if self.plateau_jeu[0] == 1 and self.plateau_jeu[1] == 1 and self.plateau_jeu[2] == 1 and self.plateau_jeu[3] == 1 and self.plateau_jeu[4] == 1:
			popup = ModalView(size_hint=(0.6, 0.2))		
			victory_label = Label(text='Le joueur Noir a gagné !',font_size=30)		
			Window.clearcolor = (1, 1, 0, 1)
			popup.add_widget(victory_label)
			popup.open() # on ouvre la pop-up de victoire
			popup.bind(on_dismiss=self.reset) # lorsque le pop-up est fermée, on reset le plateau
			
			
		# si tous les pions noir font une ligne 
		if self.plateau_jeu[10] == 1 and self.plateau_jeu[11] == 1 and self.plateau_jeu[12] == 1 and self.plateau_jeu[13] == 1 and self.plateau_jeu[14] == 1:
			popup = ModalView(size_hint=(0.6, 0.2))		
			victory_label = Label(text='Le joueur Noir a gagné !',font_size=30)		
			Window.clearcolor = (1, 1, 0, 1)
			popup.add_widget(victory_label)
			popup.open() # on ouvre la pop-up de victoire
 			popup.bind(on_dismiss=self.reset) # lorsque le pop-up est fermée, on reset le plateau 
			
			
		# si tous les pions noir font une ligne 
		if self.plateau_jeu[20] == 1 and self.plateau_jeu[21] == 1 and self.plateau_jeu[22] == 1 and self.plateau_jeu[23] == 1 and self.plateau_jeu[24] == 1:
			popup = ModalView(size_hint=(0.6, 0.2))		
			victory_label = Label(text='Le joueur Noir a gagné !',font_size=30)		
			Window.clearcolor = (1, 1, 0, 1)
			popup.add_widget(victory_label)
			popup.open() # on ouvre la pop-up de victoire
 			popup.bind(on_dismiss=self.reset) # lorsque le pop-up est fermée, on reset le plateau 
			
			
			
		# si tous les pions noir font une ligne 
		if self.plateau_jeu[31] == 1 and self.plateau_jeu[32] == 1 and self.plateau_jeu[33] == 1 and self.plateau_jeu[34] == 1 and self.plateau_jeu[35] == 1:
			popup = ModalView(size_hint=(0.6, 0.2))		
			victory_label = Label(text='Le joueur Noir a gagné !',font_size=30)		
			Window.clearcolor = (1, 1, 0, 1)
			popup.add_widget(victory_label)
			popup.open() # on ouvre la pop-up de  victoire
 			popup.bind(on_dismiss=self.reset) # lorsque le pop-up est fermée, on reset le plateau 
		
		
		
		# si tous les pions noir font une ligne 
		if self.plateau_jeu[40] == 1 and self.plateau_jeu[41] == 1 and self.plateau_jeu[42] == 1 and self.plateau_jeu[43] == 1 and self.plateau_jeu[44] == 1:
			popup = ModalView(size_hint=(0.6, 0.2))		
			victory_label = Label(text='Le joueur Noir a gagné !',font_size=30)		
			Window.clearcolor = (1, 1, 0, 1)
			popup.add_widget(victory_label)
			popup.open() # on ouvre la pop-up de victoire
 			popup.bind(on_dismiss=self.reset) # lorsque le pop-up est fermée, on reset le plateau 
			
			
			
		# si tous les pions noir font une ligne 
		if self.plateau_jeu[0] == 1 and self.plateau_jeu[9] == 1 and self.plateau_jeu[20] == 1 and self.plateau_jeu[25] == 1 and self.plateau_jeu[40] == 1:
			popup = ModalView(size_hint=(0.6, 0.2))		
			victory_label = Label(text='Le joueur Noir a gagné !',font_size=30)		
			Window.clearcolor = (1, 1, 0, 1)
			popup.add_widget(victory_label)
			popup.open() # on ouvre la pop-up de victoire
 			popup.bind(on_dismiss=self.reset) # lorsque le pop-up est fermée, on reset le plateau 
			
			
		# si tous les pions noir font une ligne 
		if self.plateau_jeu[10] == 1 and self.plateau_jeu[17] == 1 and self.plateau_jeu[21] == 1 and self.plateau_jeu[27] == 1 and self.plateau_jeu[31] == 1:
			popup = ModalView(size_hint=(0.6, 0.2))		
			victory_label = Label(text='Le joueur Noir a gagné !',font_size=30)		
			Window.clearcolor = (1, 1, 0, 1)
			popup.add_widget(victory_label)
			popup.open() # on ouvre la pop-up de victoire
 			popup.bind(on_dismiss=self.reset) # lorsque le pop-up est fermée, on reset le plateau 
		
		
		
		# si tous les pions noir font une ligne 
		if self.plateau_jeu[2] == 1 and self.plateau_jeu[12] == 1 and self.plateau_jeu[22] == 1 and self.plateau_jeu[33] == 1 and self.plateau_jeu[42] == 1:
			popup = ModalView(size_hint=(0.6, 0.2))		
			victory_label = Label(text='Le joueur Noir a gagné !',font_size=30)		
			Window.clearcolor = (1, 1, 0, 1)
			popup.add_widget(victory_label)
			popup.open() # on ouvre la pop-up de victoire
 			popup.bind(on_dismiss=self.reset) # lorsque le pop-up est fermée, on reset le plateau 
			
		
		# si tous les pions noir font une ligne 
		if self.plateau_jeu[14] == 1 and self.plateau_jeu[18] == 1 and self.plateau_jeu[23] == 1 and self.plateau_jeu[28] == 1 and self.plateau_jeu[35] == 1:
			popup = ModalView(size_hint=(0.6, 0.2))		
			victory_label = Label(text='Le joueur Noir a gagné !',font_size=30)		
			Window.clearcolor = (1, 1, 0, 1)
			popup.add_widget(victory_label)
			popup.open() # on ouvre la pop-up de victoire
 			popup.bind(on_dismiss=self.reset) # lorsque le pop-up est fermée, on reset le plateau  
			
			
			
		# si tous les pions noir font une ligne 
		if self.plateau_jeu[4] == 1 and self.plateau_jeu[15] == 1 and self.plateau_jeu[24] == 1 and self.plateau_jeu[30] == 1 and self.plateau_jeu[44] == 1:
			popup = ModalView(size_hint=(0.6, 0.2))		
			victory_label = Label(text='Le joueur Noir a gagné !',font_size=30)		
			Window.clearcolor = (1, 1, 0, 1)
			popup.add_widget(victory_label)
			popup.open() # on ouvre la pop-up de victoire
 			popup.bind(on_dismiss=self.reset) # lorsque le pop-up est fermée, on reset le plateau  
			
			
			
		# si tous les pions noir font une ligne 
		if self.plateau_jeu[9] == 1 and self.plateau_jeu[5] == 1 and self.plateau_jeu[1] == 1 :
			popup = ModalView(size_hint=(0.6, 0.2))		
			victory_label = Label(text='Le joueur Noir a gagné !',font_size=30)		
			Window.clearcolor = (1, 1, 0, 1)
			popup.add_widget(victory_label)
			popup.open() # on ouvre la pop-up de victoire
 			popup.bind(on_dismiss=self.reset) # lorsque le pop-up est fermée, on reset le plateau 
			
			
		# si tous les pions noir font une ligne 
		if self.plateau_jeu[20] == 1 and self.plateau_jeu[16] == 1 and self.plateau_jeu[10] == 1 and self.plateau_jeu[6] == 1 and self.plateau_jeu[2] == 1:
			popup = ModalView(size_hint=(0.6, 0.2))		
			victory_label = Label(text='Le joueur Noir a gagné !',font_size=30)		
			Window.clearcolor = (1, 1, 0, 1)
			popup.add_widget(victory_label)
			popup.open() # on ouvre la pop-up de victoire
 			popup.bind(on_dismiss=self.reset) # lorsque le pop-up est fermée, on reset le plateau 
			
			
		# si tous les pions noir font une ligne 
		if self.plateau_jeu[42] == 1 and self.plateau_jeu[38] == 1 and self.plateau_jeu[35] == 1 and self.plateau_jeu[29] == 1 and self.plateau_jeu[24] == 1:
			popup = ModalView(size_hint=(0.6, 0.2))		
			victory_label = Label(text='Le joueur Noir a gagné !',font_size=30)		
			Window.clearcolor = (1, 1, 0, 1)
			popup.add_widget(victory_label)
			popup.open() # on ouvre la pop-up de victoire
 			popup.bind(on_dismiss=self.reset) # lorsque le pop-up est fermée, on reset le plateau 
			
			
		# si tous les pions noir font une ligne 
		if self.plateau_jeu[43] == 1 and self.plateau_jeu[39] == 1 and self.plateau_jeu[30] == 1:
			popup = ModalView(size_hint=(0.6, 0.2))		
			victory_label = Label(text='Le joueur Noir a gagné !',font_size=30)		
			Window.clearcolor = (1, 1, 0, 1)
			popup.add_widget(victory_label)
			popup.open() # on ouvre la pop-up de victoire
 			popup.bind(on_dismiss=self.reset) # lorsque le pop-up est fermée, on reset le plateau 
			
			
			
		# si tous les pions noir font une ligne 
		if self.plateau_jeu[25] == 1 and self.plateau_jeu[36] == 1 and self.plateau_jeu[41] == 1:
			popup = ModalView(size_hint=(0.6, 0.2))		
			victory_label = Label(text='Le joueur Noir a gagné !',font_size=30)		
			Window.clearcolor = (1, 1, 0, 1)
			popup.add_widget(victory_label)
			popup.open() # on ouvre la pop-up de victoire
 			popup.bind(on_dismiss=self.reset) # lorsque le pop-up est fermée, on reset le plateau 
			
			
		# si tous les pions noir font une ligne 
		if self.plateau_jeu[20] == 1 and self.plateau_jeu[26] == 1 and self.plateau_jeu[31] == 1 and self.plateau_jeu[37] == 1 and self.plateau_jeu[42] == 1:
			popup = ModalView(size_hint=(0.6, 0.2))		
			victory_label = Label(text='Le joueur Noir a gagné !',font_size=30)		
			Window.clearcolor = (1, 1, 0, 1)
			popup.add_widget(victory_label)
			popup.open() # on ouvre la pop-up de victoire
 			popup.bind(on_dismiss=self.reset) # lorsque le pop-up est fermée, on reset le plateau 
			
			
			
			
		# si tous les pions noir font une ligne 
		if self.plateau_jeu[2] == 1 and self.plateau_jeu[7] == 1 and self.plateau_jeu[14] == 1 and self.plateau_jeu[19] == 1 and self.plateau_jeu[24] == 1:
			popup = ModalView(size_hint=(0.6, 0.2))		
			victory_label = Label(text='Le joueur Noir a gagné !',font_size=30)		
			Window.clearcolor = (1, 1, 0, 1)
			popup.add_widget(victory_label)
			popup.open() # on ouvre la pop-up de victoire
 			popup.bind(on_dismiss=self.reset) # lorsque le pop-up est fermée, on reset le plateau  
			
			
		# si tous les pions noir font une ligne 
		if self.plateau_jeu[3] == 1 and self.plateau_jeu[8] == 1 and self.plateau_jeu[15] == 1:
			popup = ModalView(size_hint=(0.6, 0.2))		
			victory_label = Label(text='Le joueur Noir a gagné !',font_size=30)		
			Window.clearcolor = (1, 1, 0, 1)
			popup.add_widget(victory_label)
			popup.open() # on ouvre la pop-up de victoire
 			popup.bind(on_dismiss=self.reset) # lorsque le pop-up est fermée, on reset le plateau 
		
		
		# si tous les pions noir font une ligne 
		if self.plateau_jeu[0] == 1 and self.plateau_jeu[5] == 1 and self.plateau_jeu[10] == 1 and self.plateau_jeu[22] == 1 and self.plateau_jeu[35] == 1  and self.plateau_jeu[39] == 1 and self.plateau_jeu[44] == 1:
			popup = ModalView(size_hint=(0.6, 0.2))		
			victory_label = Label(text='Le joueur Noir a gagné !',font_size=30)		
			Window.clearcolor = (1, 1, 0, 1)
			popup.add_widget(victory_label)
			popup.open() # on ouvre la pop-up de victoire
 			popup.bind(on_dismiss=self.reset) # lorsque le pop-up est fermée, on reset le plateau 
		
		
		# si tous les pions noir font une ligne 
		if self.plateau_jeu[1] == 1 and self.plateau_jeu[6] == 1 and self.plateau_jeu[11] == 1 and self.plateau_jeu[22] == 1 and self.plateau_jeu[34] == 1  and self.plateau_jeu[38] == 1 and self.plateau_jeu[42] == 1:
			popup = ModalView(size_hint=(0.6, 0.2))		
			victory_label = Label(text='Le joueur Noir a gagné !',font_size=30)		
			Window.clearcolor = (1, 1, 0, 1)
			popup.add_widget(victory_label)
			popup.open() # on ouvre la pop-up de victoire
 			popup.bind(on_dismiss=self.reset) # lorsque le pop-up est fermée, on reset le plateau 
			
		# si tous les pions noir font une ligne 
		if self.plateau_jeu[3] == 1 and self.plateau_jeu[7] == 1 and self.plateau_jeu[13] == 1 and self.plateau_jeu[22] == 1 and self.plateau_jeu[32] == 1  and self.plateau_jeu[37] == 1 and self.plateau_jeu[41] == 1:
			popup = ModalView(size_hint=(0.6, 0.2))		
			victory_label = Label(text='Le joueur Noir a gagné !',font_size=30)		
			Window.clearcolor = (1, 1, 0, 1)
			popup.add_widget(victory_label)
			popup.open() # on ouvre la pop-up de victoire
 			popup.bind(on_dismiss=self.reset) # lorsque le pop-up est fermée, on reset le plateau 
			
			
			
			
			
			
		# si tous les pions noir font une ligne 
		if self.plateau_jeu[15] == 1 and self.plateau_jeu[19] == 1 and self.plateau_jeu[18] == 1 and self.plateau_jeu[22] == 1 and self.plateau_jeu[27] == 1  and self.plateau_jeu[26] == 1 and self.plateau_jeu[25] == 1:
			popup = ModalView(size_hint=(0.6, 0.2))		
			victory_label = Label(text='Le joueur Noir a gagné !',font_size=30)		
			Window.clearcolor = (1, 1, 0, 1)
			popup.add_widget(victory_label)
			popup.open() # on ouvre la pop-up de victoire
 			popup.bind(on_dismiss=self.reset) # lorsque le pop-up est fermée, on reset le plateau 
			
			
		# si tous les pions noir font une ligne 
		if self.plateau_jeu[30] == 1 and self.plateau_jeu[29] == 1 and self.plateau_jeu[28] == 1 and self.plateau_jeu[22] == 1 and self.plateau_jeu[17] == 1  and self.plateau_jeu[16] == 1 and self.plateau_jeu[9] == 1:
			popup = ModalView(size_hint=(0.6, 0.2))		
			victory_label = Label(text='Le joueur Noir a gagné !',font_size=30)		
			Window.clearcolor = (1, 1, 0, 1)
			popup.add_widget(victory_label)
			popup.open() # on ouvre la pop-up de victoire
 			popup.bind(on_dismiss=self.reset) # lorsque le pop-up est fermée, on reset le plateau 
			
			
			
				# si tous les pions blanc font une ligne 
		if self.plateau_jeu[0] == 2 and self.plateau_jeu[1] == 2 and self.plateau_jeu[2] == 2 and self.plateau_jeu[3] == 2 and self.plateau_jeu[4] == 2:
			popup = ModalView(size_hint=(0.6, 0.2))		
			victory_label = Label(text='Le joueur Blanc a gagné !',font_size=30)		
			Window.clearcolor = (1, 1, 0, 1)
			popup.add_widget(victory_label)
			popup.open() # on ouvre la pop-up de victoire
 			popup.bind(on_dismiss=self.reset) # lorsque le pop-up est fermée, on reset le plateau 
			
		# si tous les pions blanc font une ligne 
		if self.plateau_jeu[10] == 2 and self.plateau_jeu[11] == 2 and self.plateau_jeu[12] == 2 and self.plateau_jeu[13] == 2 and self.plateau_jeu[14] == 2:
			popup = ModalView(size_hint=(0.6, 0.2))		
			victory_label = Label(text='Le joueur Blanc a gagné !',font_size=30)		
			Window.clearcolor = (1, 1, 0, 1)
			popup.add_widget(victory_label)
			popup.open() # on ouvre la pop-up de victoire
 			popup.bind(on_dismiss=self.reset) # lorsque le pop-up est fermée, on reset le plateau 
			
			
		# si tous les pions blanc font une ligne 
		if self.plateau_jeu[20] == 2 and self.plateau_jeu[21] == 2 and self.plateau_jeu[22] == 2 and self.plateau_jeu[23] == 2 and self.plateau_jeu[24] == 2:
			popup = ModalView(size_hint=(0.6, 0.2))		
			victory_label = Label(text='Le joueur Blanc a gagné !',font_size=30)		
			Window.clearcolor = (1, 1, 0, 1)
			popup.add_widget(victory_label)
			popup.open() # on ouvre la pop-up de victoire
 			popup.bind(on_dismiss=self.reset) # lorsque le pop-up est fermée, on reset le plateau 
			
			
			
		# si tous les pions blanc font une ligne 
		if self.plateau_jeu[31] == 2 and self.plateau_jeu[32] == 2 and self.plateau_jeu[33] == 2 and self.plateau_jeu[34] == 2 and self.plateau_jeu[35] == 2:
			popup = ModalView(size_hint=(0.6, 0.2))		
			victory_label = Label(text='Le joueur Blanc a gagné !',font_size=30)		
			Window.clearcolor = (1, 1, 0, 1)
			popup.add_widget(victory_label)
			popup.open() # on ouvre la pop-up de victoire
 			popup.bind(on_dismiss=self.reset) # lorsque le pop-up est fermée, on reset le plateau 
		
		
		
		# si tous les pions blanc font une ligne 
		if self.plateau_jeu[40] == 2 and self.plateau_jeu[41] == 2 and self.plateau_jeu[42] == 2 and self.plateau_jeu[43] == 2 and self.plateau_jeu[44] == 2:
			popup = ModalView(size_hint=(0.6, 0.2))		
			victory_label = Label(text='Le joueur Blanc a gagné !',font_size=30)		
			Window.clearcolor = (1, 1, 0, 1)
			popup.add_widget(victory_label)
			popup.open() # on ouvre la pop-up de victoire
 			popup.bind(on_dismiss=self.reset) # lorsque le pop-up est fermée, on reset le plateau 
			
			
		# si tous les pions blanc font une ligne 
		if self.plateau_jeu[0] == 2 and self.plateau_jeu[9] == 2 and self.plateau_jeu[20] == 2 and self.plateau_jeu[25] == 2 and self.plateau_jeu[40] == 2:
			popup = ModalView(size_hint=(0.6, 0.2))		
			victory_label = Label(text='Le joueur Blanc a gagné !',font_size=30)		
			Window.clearcolor = (1, 1, 0, 1)
			popup.add_widget(victory_label)
			popup.open() # on ouvre la pop-up de  victoire
 			popup.bind(on_dismiss=self.reset) # lorsque le pop-up est fermée, on reset le plateau  
			
			
		# si tous les pions blanc font une ligne 
		if self.plateau_jeu[10] == 2 and self.plateau_jeu[17] == 2 and self.plateau_jeu[21] == 2 and self.plateau_jeu[27] == 2 and self.plateau_jeu[31] == 2:
			popup = ModalView(size_hint=(0.6, 0.2))		
			victory_label = Label(text='Le joueur Blanc a gagné !',font_size=30)		
			Window.clearcolor = (1, 1, 0, 1)
			popup.add_widget(victory_label)
			popup.open() # on ouvre la pop-up de victoire
 			popup.bind(on_dismiss=self.reset) # lorsque le pop-up est fermée, on reset le plateau 
		
		
		# si tous les pions blanc font une ligne 
		if self.plateau_jeu[2] == 2 and self.plateau_jeu[12] == 2 and self.plateau_jeu[22] == 2 and self.plateau_jeu[33] == 2 and self.plateau_jeu[42] == 2:
			popup = ModalView(size_hint=(0.6, 0.2))		
			victory_label = Label(text='Le joueur Blanc a gagné !',font_size=30)		
			Window.clearcolor = (1, 1, 0, 1)
			popup.add_widget(victory_label)
			popup.open() # on ouvre la pop-up de victoire
 			popup.bind(on_dismiss=self.reset) # lorsque le pop-up est fermée, on reset le plateau 
			
		
		# si tous les pions blanc font une ligne 
		if self.plateau_jeu[14] == 2 and self.plateau_jeu[18] == 2 and self.plateau_jeu[23] == 2 and self.plateau_jeu[28] == 2 and self.plateau_jeu[35] == 2:
			popup = ModalView(size_hint=(0.6, 0.2))		
			victory_label = Label(text='Le joueur Blanc a gagné !',font_size=30)		
			Window.clearcolor = (1, 1, 0, 1)
			popup.add_widget(victory_label)
			popup.open() # on ouvre la pop-up de victoire
 			popup.bind(on_dismiss=self.reset) # lorsque le pop-up est fermée, on reset le plateau 
			
			
			
		# si tous les pions blanc font une ligne 
		if self.plateau_jeu[4] == 2 and self.plateau_jeu[15] == 2 and self.plateau_jeu[24] == 2 and self.plateau_jeu[30] == 2 and self.plateau_jeu[44] == 2:
			popup = ModalView(size_hint=(0.6, 0.2))		
			victory_label = Label(text='Le joueur Blanc a gagné !',font_size=30)		
			Window.clearcolor = (1, 1, 0, 1)
			popup.add_widget(victory_label)
			popup.open() # on ouvre la pop-up de victoire
 			popup.bind(on_dismiss=self.reset) # lorsque le pop-up est fermée, on reset le plateau 
			
			
			
		# si tous les pions blanc font une ligne 
		if self.plateau_jeu[9] == 2 and self.plateau_jeu[5] == 2 and self.plateau_jeu[1] == 2 :
			popup = ModalView(size_hint=(0.6, 0.2))		
			victory_label = Label(text='Le joueur Blanc a gagné !',font_size=30)		
			Window.clearcolor = (1, 1, 0, 1)
			popup.add_widget(victory_label)
			popup.open() # on ouvre la pop-up de victoire
 			popup.bind(on_dismiss=self.reset) # lorsque le pop-up est fermée, on reset le plateau 
			
			
		# si tous les pions blanc font une ligne 
		if self.plateau_jeu[20] == 2 and self.plateau_jeu[16] == 2 and self.plateau_jeu[10] == 2 and self.plateau_jeu[6] == 2 and self.plateau_jeu[2] == 2:
			popup = ModalView(size_hint=(0.6, 0.2))		
			victory_label = Label(text='Le joueur Blanc a gagné !',font_size=30)		
			Window.clearcolor = (1, 1, 0, 1)
			popup.add_widget(victory_label)
			popup.open() # on ouvre la pop-up de victoire
 			popup.bind(on_dismiss=self.reset) # lorsque le pop-up est fermée, on reset le plateau 
			
			
		# si tous les pions blanc font une ligne 
		if self.plateau_jeu[42] == 2 and self.plateau_jeu[38] == 2 and self.plateau_jeu[35] == 2 and self.plateau_jeu[29] == 2 and self.plateau_jeu[24] == 2:
			popup = ModalView(size_hint=(0.6, 0.2))		
			victory_label = Label(text='Le joueur Blanc a gagné !',font_size=30)		
			Window.clearcolor = (1, 1, 0, 1)
			popup.add_widget(victory_label)
			popup.open() # on ouvre la pop-up de victoire
 			popup.bind(on_dismiss=self.reset) # lorsque le pop-up est fermée, on reset le plateau  
			
			
			
		# si tous les pions blanc font une ligne 
		if self.plateau_jeu[43] == 2 and self.plateau_jeu[39] == 2 and self.plateau_jeu[30] == 2:
			popup = ModalView(size_hint=(0.6, 0.2))		
			victory_label = Label(text='Le joueur Blanc a gagné !',font_size=30)		
			Window.clearcolor = (1, 1, 0, 1)
			popup.add_widget(victory_label)
			popup.open() # on ouvre la pop-up de victoire
 			popup.bind(on_dismiss=self.reset) # lorsque le pop-up est fermée, on reset le plateau 
			
			
			
			
		# si tous les pions blanc font une ligne 
		if self.plateau_jeu[25] == 2 and self.plateau_jeu[36] == 2 and self.plateau_jeu[41] == 2:
			popup = ModalView(size_hint=(0.6, 0.2))		
			victory_label = Label(text='Le joueur Blanc a gagné !',font_size=30)		
			Window.clearcolor = (1, 1, 0, 1)
			popup.add_widget(victory_label)
			popup.open() # on ouvre la pop-up de victoire
 			popup.bind(on_dismiss=self.reset) # lorsque le pop-up est fermée, on reset le plateau 
			
			
		# si tous les pions blanc font une ligne 
		if self.plateau_jeu[20] == 2 and self.plateau_jeu[26] == 2 and self.plateau_jeu[31] == 2 and self.plateau_jeu[37] == 2 and self.plateau_jeu[42] == 2:
			popup = ModalView(size_hint=(0.6, 0.2))		
			victory_label = Label(text='Le joueur Blanc a gagné !',font_size=30)		
			Window.clearcolor = (1, 1, 0, 1)
			popup.add_widget(victory_label)
			popup.open() # on ouvre la pop-up de victoire
 			popup.bind(on_dismiss=self.reset) # lorsque le pop-up est fermée, on reset le plateau 
			
			
			
			
		# si tous les pions blanc font une ligne 
		if self.plateau_jeu[2] == 2 and self.plateau_jeu[7] == 2 and self.plateau_jeu[14] == 2 and self.plateau_jeu[19] == 2 and self.plateau_jeu[24] == 2:
			popup = ModalView(size_hint=(0.6, 0.2))		
			victory_label = Label(text='Le joueur Blanc a gagné !',font_size=30)		
			Window.clearcolor = (1, 1, 0, 1)
			popup.add_widget(victory_label)
			popup.open() # on ouvre la pop-up de victoire
 			popup.bind(on_dismiss=self.reset) # lorsque le pop-up est fermée, on reset le plateau 
			
			
		# si tous les pions blanc font une ligne 
		if self.plateau_jeu[3] == 2 and self.plateau_jeu[8] == 2 and self.plateau_jeu[15] == 2:
			popup = ModalView(size_hint=(0.6, 0.2))		
			victory_label = Label(text='Le joueur Blanc a gagné !',font_size=30)		
			Window.clearcolor = (1, 1, 0, 1)
			popup.add_widget(victory_label)
			popup.open() # on ouvre la pop-up de victoire
 			popup.bind(on_dismiss=self.reset) # lorsque le pop-up est fermée, on reset le plateau 
		
		
		
		# si tous les pions blanc font une ligne 
		if self.plateau_jeu[0] == 2 and self.plateau_jeu[5] == 2 and self.plateau_jeu[10] == 2 and self.plateau_jeu[22] == 2 and self.plateau_jeu[35] == 2  and self.plateau_jeu[39] == 2 and self.plateau_jeu[44] == 2:
			popup = ModalView(size_hint=(0.6, 0.2))		
			victory_label = Label(text='Le joueur Blanc a gagné !',font_size=30)		
			Window.clearcolor = (1, 1, 0, 1)
			popup.add_widget(victory_label)
			popup.open() # on ouvre la pop-up de victoire
 			popup.bind(on_dismiss=self.reset) # lorsque le pop-up est fermée, on reset le plateau 
		
		
		# si tous les pions blanc font une ligne 
		if self.plateau_jeu[1] == 2 and self.plateau_jeu[6] == 2 and self.plateau_jeu[11] == 2 and self.plateau_jeu[22] == 2 and self.plateau_jeu[34] == 2  and self.plateau_jeu[38] == 2 and self.plateau_jeu[42] == 2:
			popup = ModalView(size_hint=(0.6, 0.2))		
			victory_label = Label(text='Le joueur Blanc a gagné !',font_size=30)		
			Window.clearcolor = (1, 1, 0, 1)
			popup.add_widget(victory_label)
			popup.open() # on ouvre la pop-up de victoire
 			popup.bind(on_dismiss=self.reset) # lorsque le pop-up est fermée, on reset le plateau 
			
			
		# si tous les pions blanc font une ligne 
		if self.plateau_jeu[3] == 2 and self.plateau_jeu[7] == 2 and self.plateau_jeu[13] == 2 and self.plateau_jeu[22] == 2 and self.plateau_jeu[32] == 2  and self.plateau_jeu[37] == 2 and self.plateau_jeu[41] == 2:
			popup = ModalView(size_hint=(0.6, 0.2))		
			victory_label = Label(text='Le joueur Blanc a gagné !',font_size=30)		
			Window.clearcolor = (1, 1, 0, 1)
			popup.add_widget(victory_label)
			popup.open() # on ouvre la pop-up de victoire
 			popup.bind(on_dismiss=self.reset) # lorsque le pop-up est fermée, on reset le plateau  
			
			
			
	###########################################################################################################################		
			
			
		# si tous les pions blanc font une ligne 
		if self.plateau_jeu[15] == 2 and self.plateau_jeu[19] == 2 and self.plateau_jeu[18] == 2 and self.plateau_jeu[22] == 2 and self.plateau_jeu[27] == 2  and self.plateau_jeu[26] == 2 and self.plateau_jeu[25] == 2:
			popup = ModalView(size_hint=(0.6, 0.2))		
			victory_label = Label(text='Le joueur Blanc a gagné !',font_size=30)		
			Window.clearcolor = (1, 1, 0, 1)
			popup.add_widget(victory_label)
			popup.open() # on ouvre la pop-up de victoire
 			popup.bind(on_dismiss=self.reset) # lorsque le pop-up est fermée, on reset le plateau 
			
	
		# si tous les pions blanc font une ligne 
		if self.plateau_jeu[30] == 2 and self.plateau_jeu[29] == 2 and self.plateau_jeu[28] == 2 and self.plateau_jeu[22] == 2 and self.plateau_jeu[17] == 2  and self.plateau_jeu[16] == 2 and self.plateau_jeu[9] == 2:
			popup = ModalView(size_hint=(0.6, 0.2))		
			victory_label = Label(text='Le joueur Blanc a gagné !',font_size=30)		
			Window.clearcolor = (1, 1, 0, 1)
			popup.add_widget(victory_label)
			popup.open() # on ouvre la pop-up de victoire
 			popup.bind(on_dismiss=self.reset) # lorsque le pop-up est fermée, on reset le plateau 