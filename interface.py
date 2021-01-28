from tkinter import *
import tkinter as tk
from programme_DE import *




class fenetre_affine(object):


	def chiffr(self):
			crypt = crypto_affine()
			crypt.a = int(self.Entry_A.get())
			crypt.b = int(self.Entry_B.get())
			crypt.modulo = int(self.Entry_modulo.get())
			res = crypt.chiffr(int(self.Entry_X.get()))
			self.Entry_result.delete(0, END)
			self.Entry_result.insert(0, res)

	def dechiffr(self):
			crypt = crypto_affine()
			crypt.a = int(self.Entry_A.get())
			crypt.b = int(self.Entry_B.get())
			crypt.modulo = int(self.Entry_modulo.get())
			res = crypt.dechiffr(int(self.Entry_X.get()))
			self.Entry_result.delete(0, END)
			self.Entry_result.insert(0, res)
	
	def __init__(self):
		self.fen = Tk()
		self.fen.geometry("500x300")
		self.fen.title("Cryptographie affine")

		self.title = Label(self.fen, text="Cryptographie affine")
		self.title.pack()

		self.frame_input = Frame(self.fen)
		self.frame_input.pack()

		self.Label_A = Label(self.fen, text="A:")
		self.Label_A.pack(in_=self.frame_input, side=LEFT)

		self.Entry_A = Entry(self.fen, width=10)
		self.Entry_A.pack(in_=self.frame_input, side=LEFT)

		self.Label_B = Label(self.fen, text="B:")
		self.Label_B.pack(in_=self.frame_input, side=LEFT)

		self.Entry_B = Entry(self.fen, width=10)
		self.Entry_B.pack(in_=self.frame_input, side=RIGHT)

		self.Label_X = Label(self.fen, text="X:")
		self.Label_X.pack()

		self.Entry_X = Entry(self.fen, width=10)
		self.Entry_X.pack()

		self.Label_modulo = Label(self.fen, text="Modulo:")
		self.Label_modulo.pack()

		self.Entry_modulo = Entry(self.fen, width=10)
		self.Entry_modulo.pack()

		self.frame_button = Frame(self.fen)
		self.frame_button.pack()

		self.button_chiffr = Button(self.fen, text="Chiffrer", command=self.chiffr)
		self.button_chiffr.pack(in_=self.frame_button, side=LEFT)

		self.button_dechiffr = Button(self.fen, text="Déchiffrer", command=self.dechiffr)
		self.button_dechiffr.pack(in_=self.frame_button, side=LEFT)

		self.frame_result = Frame(self.fen)
		self.frame_result.pack()

		self.Label_result = Label(self.fen, text="Result:")
		self.Label_result.pack(in_=self.frame_result, side=LEFT)

		self.Entry_result = Entry(self.fen, width=10)
		self.Entry_result.pack(in_=self.frame_result, side=LEFT)

		self.fen.mainloop()



class fenetre_affine_dia(object):


	def chiffr(self):
			crypt = crypto_affine_dia()
			crypt.a = [ [int(self.Entry_A1.get()), int(self.Entry_A2.get())] , [int(self.Entry_A3.get()), int(self.Entry_A4.get())] ]
			crypt.b = [int(self.Entry_B1.get()), int(self.Entry_B2.get())]

			crypt.modulo = int(self.Entry_modulo.get())
			res = crypt.chiffr( [int(self.Entry_X1.get()) , int(self.Entry_X2.get())] )
			#res = multipli_matr(crypt.a, [int(self.Entry_X1.get()) , int(self.Entry_X2.get())])

			self.Entry_result1.delete(0, END)
			self.Entry_result1.insert(0, res[0])
			self.Entry_result2.delete(0, END)
			self.Entry_result2.insert(0, res[1])

	def dechiffr(self):
			crypt = crypto_affine_dia()
			crypt.a = [ [int(self.Entry_A1.get()), int(self.Entry_A2.get())] , [int(self.Entry_A3.get()), int(self.Entry_A4.get())] ]
			crypt.b = [int(self.Entry_B1.get()), int(self.Entry_B2.get())]

			crypt.modulo = int(self.Entry_modulo.get())
			res = crypt.dechiffr( [int(self.Entry_X1.get()) , int(self.Entry_X2.get())] )

			self.Entry_result1.delete(0, END)
			self.Entry_result1.insert(0, res[0])
			self.Entry_result2.delete(0, END)
			self.Entry_result2.insert(0, res[1])

	
	def __init__(self):
		self.fen = Tk()
		self.fen.geometry("500x300")
		self.fen.title("Cryptographie affine avec Diagramme")

		self.title = Label(self.fen, text="Cryptographie affine avec Diagramme")
		self.title.pack()

		####################################################################################################
		####################################################################################################
		####################################################################################################

		self.frame_A_top = Frame(self.fen)
		self.frame_A_top.pack()

		self.frame_A_bot = Frame(self.fen)
		self.frame_A_bot.pack()

		self.Label_A = Label(self.fen, text="A:")
		self.Label_A.pack(in_=self.frame_A_top, side=LEFT)

		self.Entry_A1 = Entry(self.fen, width=10)
		self.Entry_A1.pack(in_=self.frame_A_top, side=LEFT)

		self.Entry_A2 = Entry(self.fen, width=10)
		self.Entry_A2.pack(in_=self.frame_A_top, side=LEFT)

		self.Entry_A3 = Entry(self.fen, width=10)
		self.Entry_A3.pack(in_=self.frame_A_bot, side=LEFT)

		self.Entry_A4 = Entry(self.fen, width=10)
		self.Entry_A4.pack(in_=self.frame_A_bot, side=LEFT)
		####################################################################################################
		####################################################################################################
		####################################################################################################

		self.frame_B = Frame(self.fen)
		self.frame_B.pack(expand=0.5)

		self.Label_B = Label(self.fen, text="B:")
		self.Label_B.pack(in_=self.frame_B, side=LEFT)

		self.Entry_B1 = Entry(self.fen, width=10)
		self.Entry_B1.pack(in_=self.frame_B, side=TOP)

		self.Entry_B2 = Entry(self.fen, width=10)
		self.Entry_B2.pack(in_=self.frame_B, side=BOTTOM)

		####################################################################################################
		####################################################################################################
		####################################################################################################

		self.frame_X = Frame(self.fen)
		self.frame_X.pack(expand=0.2)

		self.Label_X = Label(self.fen, text="X:")
		self.Label_X.pack(in_=self.frame_X, side=LEFT)

		self.Entry_X1 = Entry(self.fen, width=10)
		self.Entry_X1.pack(in_=self.frame_X, side=TOP)

		self.Entry_X2 = Entry(self.fen, width=10)
		self.Entry_X2.pack(in_=self.frame_X, side=BOTTOM)

		####################################################################################################
		####################################################################################################
		####################################################################################################

		self.frame_modulo = Frame(self.fen)
		self.frame_modulo.pack(expand=1)

		self.Label_modulo = Label(self.fen, text="Modulo:")
		self.Label_modulo.pack(in_=self.frame_modulo, side=LEFT)

		self.Entry_modulo = Entry(self.fen, width=10)
		self.Entry_modulo.pack(in_=self.frame_modulo, side=LEFT)

		####################################################################################################
		####################################################################################################
		####################################################################################################

		self.frame_button = Frame(self.fen)
		self.frame_button.pack(expand=1)

		self.button_chiffr = Button(self.fen, text="Chiffrer", command=self.chiffr)
		self.button_chiffr.pack(in_=self.frame_button, side=LEFT)

		self.button_dechiffr = Button(self.fen, text="Déchiffrer", command=self.dechiffr)
		self.button_dechiffr.pack(in_=self.frame_button, side=LEFT)

		####################################################################################################
		####################################################################################################
		####################################################################################################


		self.frame_result = Frame(self.fen)
		self.frame_result.pack(expand=1)

		self.Label_result = Label(self.fen, text="Result:")
		self.Label_result.pack(in_=self.frame_result, side=LEFT)

		self.Entry_result1 = Entry(self.fen, width=10)
		self.Entry_result1.pack(in_=self.frame_result, side=TOP)
		self.Entry_result2 = Entry(self.fen, width=10)
		self.Entry_result2.pack(in_=self.frame_result, side=BOTTOM)

		self.fen.mainloop()




class fenetre_rsa(object):
	"""docstring for fenetre_rsa"""

	def chiffr(self):
		crypt = crypto_rsa()
		crypt.nA = int(self.Entry_nA.get()) 
		crypt.eA = int(self.Entry_eA.get())
		crypt.dA = int(self.Entry_dA.get())
		crypt.nB = int(self.Entry_nB.get())
		crypt.eB = int(self.Entry_eB.get())
		crypt.dB = int(self.Entry_dB.get())
		qui = self.Entry_Qui.get()

		res = crypt.chiffr(int(self.Entry_X.get()), qui)
		self.Entry_result.delete(0, END)
		self.Entry_result.insert(0, res)

	def dechiffr(self):
		crypt = crypto_rsa()
		crypt.nA = int(self.Entry_nA.get()) 
		crypt.eA = int(self.Entry_eA.get())
		crypt.dA = int(self.Entry_dA.get())
		crypt.nB = int(self.Entry_nB.get())
		crypt.eB = int(self.Entry_eB.get())
		crypt.dB = int(self.Entry_dB.get())
		qui = self.Entry_Qui.get()

		res = crypt.dechiffr(int(self.Entry_X.get()), qui)
		self.Entry_result.delete(0, END)
		self.Entry_result.insert(0, res)

	def __init__(self):
		self.fen = Tk()
		self.fen.geometry("500x300")
		self.fen.title("Cryptographie RSA")

		self.title = Label(self.fen, text="Cryptographie RSA")
		self.title.pack()

		self.frame_info = Frame(self.fen)
		self.frame_info.pack()

		self.frame_Alice = Frame(self.fen)
		self.frame_Alice.pack(in_=self.frame_info, side=LEFT)
		self.frame_input_Alice = Frame(self.fen)
		self.frame_input_Alice.pack(in_=self.frame_info, side=LEFT)

		self.frame_Bob = Frame(self.fen)
		self.frame_Bob.pack(in_=self.frame_info, side=LEFT)
		self.frame_input_Bob = Frame(self.fen)
		self.frame_input_Bob.pack(in_=self.frame_info, side=LEFT)


		####################################################################################################
		####################################################################################################
		####################################################################################################

		self.Label_Alice = Label(self.fen, text="Alice", borderwidth=2, relief="groove")
		self.Label_Alice.pack(in_=self.frame_Alice)
		self.Label_Alic = Label(self.fen, text="")
		self.Label_Alic.pack(in_=self.frame_input_Alice)

		self.Label_nA = Label(self.fen, text="nA")
		self.Label_nA.pack(in_=self.frame_Alice)
		self.Entry_nA = Entry(self.fen, width=10)
		self.Entry_nA.pack(in_=self.frame_input_Alice)

		self.Label_eA = Label(self.fen, text="eA")
		self.Label_eA.pack(in_=self.frame_Alice)
		self.Entry_eA = Entry(self.fen, width=10)
		self.Entry_eA.pack(in_=self.frame_input_Alice)

		self.Label_dA = Label(self.fen, text="dA")
		self.Label_dA.pack(in_=self.frame_Alice)
		self.Entry_dA = Entry(self.fen, width=10)
		self.Entry_dA.pack(in_=self.frame_input_Alice)

		####################################################################################################
		####################################################################################################
		####################################################################################################

		self.Label_Bob = Label(self.fen, text="Bob", borderwidth=2, relief="groove")
		self.Label_Bob.pack(in_=self.frame_Bob)
		self.Label_Bo = Label(self.fen, text="")
		self.Label_Bo.pack(in_=self.frame_input_Bob)

		self.Label_nB = Label(self.fen, text="nB")
		self.Label_nB.pack(in_=self.frame_Bob)
		self.Entry_nB = Entry(self.fen, width=10)
		self.Entry_nB.pack(in_=self.frame_input_Bob)

		self.Label_eB = Label(self.fen, text="eB")
		self.Label_eB.pack(in_=self.frame_Bob)
		self.Entry_eB = Entry(self.fen, width=10)
		self.Entry_eB.pack(in_=self.frame_input_Bob)

		self.Label_dB = Label(self.fen, text="dB")
		self.Label_dB.pack(in_=self.frame_Bob)
		self.Entry_dB = Entry(self.fen, width=10)
		self.Entry_dB.pack(in_=self.frame_input_Bob)

		####################################################################################################
		####################################################################################################
		####################################################################################################

		self.Label_X = Label(self.fen, text="X:")
		self.Label_X.pack()

		self.Entry_X = Entry(self.fen, width=10)
		self.Entry_X.pack()

		self.Label_Qui = Label(self.fen, text="Qui ('A' ou 'B'):")
		self.Label_Qui.pack()

		self.Entry_Qui = Entry(self.fen, width=10)
		self.Entry_Qui.pack()

		####################################################################################################
		####################################################################################################
		####################################################################################################

		self.frame_button = Frame(self.fen)
		self.frame_button.pack(expand=1)

		self.button_chiffr = Button(self.fen, text="Chiffrer", command=self.chiffr)
		self.button_chiffr.pack(in_=self.frame_button, side=LEFT)

		self.button_dechiffr = Button(self.fen, text="Déchiffrer", command=self.dechiffr)
		self.button_dechiffr.pack(in_=self.frame_button, side=LEFT)

		####################################################################################################
		####################################################################################################
		####################################################################################################

		self.frame_result = Frame(self.fen)
		self.frame_result.pack()

		self.Label_result = Label(self.fen, text="Result:")
		self.Label_result.pack(in_=self.frame_result, side=LEFT)

		self.Entry_result = Entry(self.fen, width=10)
		self.Entry_result.pack(in_=self.frame_result, side=LEFT)



class fenetre_elgamal(object):
	"""docstring for fenetre_rsa"""

	def chiffr(self):
		crypt = crypto_elgamal()

		crypt.eA = int(self.Entry_eA.get())
		crypt.dA = int(self.Entry_dA.get())
		crypt.eB = int(self.Entry_eB.get())
		crypt.dB = int(self.Entry_dB.get())
		crypt.g =  int(self.Entry_g.get())
		crypt.modulo = int(self.Entry_modulo.get())
		k = int(self.Entry_kr.get())
		qui = self.Entry_Qui.get()
		x = int(self.Entry_X.get())

		res = crypt.chiffr(x, k, qui)
		self.Entry_result.delete(0, END)
		self.Entry_result.insert(0, res["y"])
		self.Entry_r.delete(0, END)
		self.Entry_r.insert(0, res["r"])

	def dechiffr(self):
		crypt = crypto_elgamal()

		crypt.eA = int(self.Entry_eA.get())
		crypt.dA = int(self.Entry_dA.get())
		crypt.eB = int(self.Entry_eB.get())
		crypt.dB = int(self.Entry_dB.get())
		crypt.g =  int(self.Entry_g.get())
		crypt.modulo = int(self.Entry_modulo.get())
		r = int(self.Entry_kr.get())
		qui = self.Entry_Qui.get()
		y = int(self.Entry_X.get())

		res = crypt.dechiffr(r, y, qui)
		self.Entry_result.delete(0, END)
		self.Entry_result.insert(0, res)

	def __init__(self):
		self.fen = Tk()
		self.fen.geometry("500x300")
		self.fen.title("Cryptographie Elgamal")

		self.title = Label(self.fen, text="Cryptographie Elgamal")
		self.title.pack()

		self.frame_info = Frame(self.fen)
		self.frame_info.pack()

		self.frame_Alice = Frame(self.fen)
		self.frame_Alice.pack(in_=self.frame_info, side=LEFT)
		self.frame_input_Alice = Frame(self.fen)
		self.frame_input_Alice.pack(in_=self.frame_info, side=LEFT)

		self.frame_Bob = Frame(self.fen)
		self.frame_Bob.pack(in_=self.frame_info, side=LEFT)
		self.frame_input_Bob = Frame(self.fen)
		self.frame_input_Bob.pack(in_=self.frame_info, side=LEFT)


		####################################################################################################
		####################################################################################################
		####################################################################################################

		self.Label_Alice = Label(self.fen, text="Alice", borderwidth=2, relief="groove")
		self.Label_Alice.pack(in_=self.frame_Alice)
		self.Label_Alic = Label(self.fen, text="")
		self.Label_Alic.pack(in_=self.frame_input_Alice)

		self.Label_modulo = Label(self.fen, text="modulo")
		self.Label_modulo.pack(in_=self.frame_Alice)
		self.Entry_modulo = Entry(self.fen, width=10)
		self.Entry_modulo.pack(in_=self.frame_input_Alice)

		self.Label_eA = Label(self.fen, text="eA")
		self.Label_eA.pack(in_=self.frame_Alice)
		self.Entry_eA = Entry(self.fen, width=10)
		self.Entry_eA.pack(in_=self.frame_input_Alice)

		self.Label_dA = Label(self.fen, text="dA")
		self.Label_dA.pack(in_=self.frame_Alice)
		self.Entry_dA = Entry(self.fen, width=10)
		self.Entry_dA.pack(in_=self.frame_input_Alice)

		####################################################################################################
		####################################################################################################
		####################################################################################################

		self.Label_Bob = Label(self.fen, text="Bob", borderwidth=2, relief="groove")
		self.Label_Bob.pack(in_=self.frame_Bob)
		self.Label_Bo = Label(self.fen, text="")
		self.Label_Bo.pack(in_=self.frame_input_Bob)

		self.Label_g = Label(self.fen, text="g")
		self.Label_g.pack(in_=self.frame_Bob)
		self.Entry_g = Entry(self.fen, width=10)
		self.Entry_g.pack(in_=self.frame_input_Bob)

		self.Label_eB = Label(self.fen, text="eB")
		self.Label_eB.pack(in_=self.frame_Bob)
		self.Entry_eB = Entry(self.fen, width=10)
		self.Entry_eB.pack(in_=self.frame_input_Bob)

		self.Label_dB = Label(self.fen, text="dB")
		self.Label_dB.pack(in_=self.frame_Bob)
		self.Entry_dB = Entry(self.fen, width=10)
		self.Entry_dB.pack(in_=self.frame_input_Bob)

		####################################################################################################
		####################################################################################################
		####################################################################################################

		self.Label_X = Label(self.fen, text="X:")
		self.Label_X.pack()

		self.Entry_X = Entry(self.fen, width=10)
		self.Entry_X.pack()

		self.Label_Qui = Label(self.fen, text="Qui ('A' ou 'B'):")
		self.Label_Qui.pack()

		self.Entry_Qui = Entry(self.fen, width=10)
		self.Entry_Qui.pack()

		self.Label_kr = Label(self.fen, text="k ou r")
		self.Label_kr.pack(side=LEFT)

		self.Entry_kr = Entry(self.fen, width=10)
		self.Entry_kr.pack(side=LEFT)


		####################################################################################################
		####################################################################################################
		####################################################################################################

		self.frame_button = Frame(self.fen)
		self.frame_button.pack(expand=1)

		self.button_chiffr = Button(self.fen, text="Chiffrer", command=self.chiffr)
		self.button_chiffr.pack(in_=self.frame_button, side=LEFT)

		self.button_dechiffr = Button(self.fen, text="Déchiffrer", command=self.dechiffr)
		self.button_dechiffr.pack(in_=self.frame_button, side=LEFT)

		####################################################################################################
		####################################################################################################
		####################################################################################################

		self.frame_result = Frame(self.fen)
		self.frame_result.pack()

		self.Label_result = Label(self.fen, text="Result:")
		self.Label_result.pack(in_=self.frame_result, side=LEFT)

		self.Entry_result = Entry(self.fen, width=10)
		self.Entry_result.pack(in_=self.frame_result, side=LEFT)


		self.Label_r = Label(self.fen, text="r:")
		self.Label_r.pack(in_=self.frame_result, side=LEFT)

		self.Entry_r = Entry(self.fen, width=10)
		self.Entry_r.pack(in_=self.frame_result, side=LEFT)


class fenetre_utilitaire(object):
	"""docstring for fenetre_utilitaire"""
	def __init__(self):
		self.fen= Tk()
		self.fen.geometry("500x300")
		self.fen.title("Utilitaires")
		
		self.fen.title = Label(self.fen, text="MENU UTILITAIRES")
		self.fen.title.grid(row=1, sticky=W, ipadx=24, padx=160,pady=2)
		
		
		self.fen.boutonMatrices = Button(self.fen, text="Multiplication matrices", command=fenetre)
		self.fen.boutonMatrices.grid(row=2, sticky=W, ipadx=24, padx=160,pady=2)
		
		self.fen.boutonPhi = Button(self.fen, text="Calcul de Phi", command=fenetre)
		self.fen.boutonPhi.grid(row=3, sticky=W, ipadx=50, padx=160,pady=2)
		
		self.fen.boutonOrdre = Button(self.fen, text="Calcul d'ordre", command=fenetre)
		self.fen.boutonOrdre.grid(row=4, sticky=W, ipadx=47, padx=160,pady=2)
		
		self.fen.pack()
		

		


"""fenetre = Tk()
fenetre.geometry("500x100")

cha_lab = Label(fenetre, text="Plop")
cha_lab.pack()

tes = test(fenetre)

#aff = fenetre_affine()

but = Button(fenetre, text="quit", command=fenetre_affine)
but.pack()

fenetre.mainloop()"""

fenetre = Tk()
fenetre.geometry("500x500")
Txt = Label(fenetre, text="Menu")
Txt.grid(row=0, sticky=W)

boutonAffine = Button(fenetre, text="Affine", command=fenetre_affine)
boutonAffine.grid(row=1, sticky=W, ipadx=46, padx=180,pady=2)
boutonAffine.grid_location(200, 200)

boutonAffineDiag = Button(fenetre, text="Affine avec Diagramme", command=fenetre_affine_dia)
boutonAffineDiag.grid(row=2, sticky=W, padx=180,pady=2)

boutonRSA = Button(fenetre, text="RSA", command=fenetre_rsa)
boutonRSA.grid(row=3, sticky=W, ipadx=52, padx=180,pady=2)

boutonElgamal = Button(fenetre, text="Elgamal", command=fenetre_elgamal)
boutonElgamal.grid(row=4, sticky=W, ipadx=41, padx=180,pady=2)

boutonUtilitaire = Button(fenetre, text="Utilitaire", command=fenetre_utilitaire)
boutonUtilitaire.grid(row=5, sticky=W, ipadx=41, padx=180,pady=2)

but = Button(fenetre, text="Quit", command=fenetre.quit)
but.grid(row=5, sticky=W, ipadx=30, pady=15)

fenetre.mainloop()


