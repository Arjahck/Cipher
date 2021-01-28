from math import sqrt

'''
linear cryptography
'''



def diviseurs(n):
    D,racine=[1],int(sqrt(n))
    fin=racine+1
    for d in range(2,fin):
        if n%d==0 :
            D.extend([d,n//d])
    D=sorted(set(D))
    return D


def phi(n):
	D=diviseurs(n)

	Phi,somme=[1],"1"

	for i,div in enumerate(D):
	    if div!=1:
	        D_i,q=[d for d in D if div%d==0 and d<div],0
	        for d in D_i:
	            q+=Phi[D.index(d)]
	        p=div-q
	        Phi.append(p)
	        somme+="+"+str(p)
	return n-sum(Phi)

def bezout(n1, n2):
	if (n1 < n2):
		n1 = n1 + n2
		n2 = n1 - n2
		n1 = n1 - n2

	tableau = []
	tableau.append([n1, 1, 0])
	tableau.append([n2, 0, 1])
	quotient = int(tableau[0][0] / tableau[1][0])
	reste = tableau[0][0] % tableau[1][0]
	tableau.append([reste, tableau[0][1] - (quotient * tableau[1][1]) , tableau[0][2] - (quotient * tableau[1][2])])

	while (tableau[2][0] > 1):
		tableau[0] = tableau[1]
		tableau[1] = tableau[2]
		quotient = int(tableau[0][0] / tableau[1][0])
		reste = tableau[0][0] % tableau[1][0]
		tableau[2] = [reste, tableau[0][1] - (quotient * tableau[1][1]) , tableau[0][2] - (quotient * tableau[1][2])]

	if(tableau[2][0] == 1):
		dico = {"pgcd" : 1, str(n1) : tableau[2][1], str(n2) : tableau[2][2]}
	else:
		dico = {"pgcd" : tableau[1][0], str(n1) : tableau[1][1], str(n2) : tableau[1][2]}
	return dico

def affiche_tab(tab):
	for x in tab:
		'''for y in x:
			print(y)'''
		print(str(x))

def RestesChinois(nb, resultat, modulo):
	bez = bezout(nb, modulo)
	pgcd = bez["pgcd"]
	if (pgcd == 1):
		inverse = bez [str(nb)]
		x = (inverse*resultat)%modulo
		print(x)
	elif (resultat%nb == 0):
		i = 0
		while (i < 5):
			x = ((resultat + modulo*i)/nb)
			print(x)
			i = i +1
	else:
		print("Pas de solution")

def expo_modu(nmbr, pui, mod):
	return (nmbr**pui)%mod


def determinant(x):
	return (x[0][0] * x[1][1]) - (x[0][1] * x[1][0])


def multipli_matr(a, x):
	result = []
	result.append( (a[0][0] * x[0]) + (a[0][1] * x[1]) )
	result.append( (a[1][0] * x[0]) + (a[1][1] * x[1]) )
	return result


def decomposition_nbpremiers(n):
	nbPremiers=[]
	i=2
	while n>1:
		while n%i==0:
			nbPremiers.append(i)
			n=n/i
		i=i+1
	return nbPremiers
	
def theoremeRSA_verif(nbPremiers):
	prems = nbPremiers[0]
	i = 1
	for i in nbPremiers:
		if i == prems:
			boolean = 0
		else:
			prems = i
	boolean = 1
	if (boolean == 0):
		return False
	else:
		return True


class crypto_affine(object):
	"""docstring for crypto_affine"""
	def __init__(self):
		super(crypto_affine, self).__init__()
		self.a = 0
		self.b = 0
		self.modulo = 0

	def chiffr(self, x):
		return((self.a * x + self.b)%self.modulo)

	def dechiffr(self, y):
		inv_a = bezout(self.a, self.modulo)[str(self.a)]
		return ( ( (inv_a * y) - (inv_a * self.b) ) % self.modulo)


	def is_dechiffr(self):
		if (bezout(self.a, self.modulo)["pgcd"] == 1):
			return True
		else:
			return False



class crypto_affine_dia(object):
	"""docstring for crypto_affine"""
	def __init__(self):
		self.a = 0
		self.b = 0
		self.modulo = 0

	def is_bij(self):
		if (bezout(determinant(self.a)%self.modulo, self.modulo)["pgcd"] == 1):
			return True
		else:
			return False

	def chiffr(self, x):
		mult = multipli_matr(self.a, x)
		mult[0] = (mult[0] + self.b[0]) % self.modulo
		mult[1] = (mult[1] + self.b[1]) % self.modulo
		return mult

	def inv_a(self):
		det = determinant(self.a)%self.modulo
		inv_det = bezout(det, self.modulo)[str(det)]
		inverse_a = self.a
		temp = self.a[0][0]
		inverse_a[0][0] = (inv_det * self.a[1][1]) % self.modulo
		inverse_a[0][1] = (inv_det * (self.a[0][1]*-1)) % self.modulo
		inverse_a[1][0] = (inv_det * (self.a[1][0]*-1)) % self.modulo
		inverse_a[1][1] = (inv_det * temp) % self.modulo

		return inverse_a

	def dechiffr(self, y):
		inverse_a = self.inv_a()
		x = multipli_matr(inverse_a, y)
		y = multipli_matr(inverse_a, self.b) 
		x[0] = (x[0] - y[0])%self.modulo
		x[1] = (x[1] - y[1])%self.modulo
		return x


class crypto_rsa(object):
	"""docstring for crypto_rsa"""
	def __init__(self):
		self.nA = 0
		self.eA = 0
		self.dA = 0
		self.sA = 0

		self.nB = 0
		self.eB = 0
		self.dB = 0
		self.sB = 0


	def completeA(self):
		phin= phi(self.nA)
		x=bezout(self.dA,phin)
		if(x[str(self.dA)])<0:
			x[str(self.dA)]=x[str(self.dA)]+phi(self.nA)
		return x[str(self.dA)]

	def completdA(self):
		phin= phi(self.nA)
		x=bezout(self.eA,phin)
		if(x[str(self.eA)])<0:
			x[str(self.eA)]=x[str(self.eA)]+phi(self.nA)
		return x[str(self.eA)]

	def completeB(self):
		phin= phi(self.nB)
		x=bezout(self.dB,phin)
		if(x[str(self.dB)])<0:
			x[str(self.dB)]=x[str(self.dB)]+phi(self.nB)
		return x[str(self.dB)]

	def completdB(self):
		phin= phi(self.nB)
		x=bezout(self.eB,phin)
		if(x[str(self.eB)])<0:
			x[str(self.eB)]=x[str(self.eB)]+phi(self.nB)
		return x[str(self.eB)]


	"""def find_d(self,who):
		if (who == "A"):
			phin= phi(self.nA)
			x=bezout(self.eA,phin)
			if(x[str(self.eA)])<0:
				x[str(self.eA)]=x[str(self.eA)]+phi(self.nA)
			print(x[str(self.eA)])
		else:
			phin= phi(self.nB)
			x=bezout(self.eB,phin)
			if(x[str(self.eB)])<0:
				x[str(self.eB)]=x[str(self.eB)]+phi(self.nB)
			print(x[str(self.eB)])
        
	def find_e(self,who):
		if (who == "A"):
			phin= phi(self.nA)
			x=bezout(self.dA,phin)
			if(x[str(self.dA)])<0:
				x[str(self.dA)]=x[str(self.dA)]+phi(self.nA)
			print(x[str(self.dA)])
		else:
			phin= phi(self.nB)
			x=bezout(self.dB,phin)
			if(x[str(self.dB)])<0:
				x[str(self.dB)]=x[str(self.dB)]+phi(self.nB)
			print(x[str(self.dB)])"""


	def chiffr(self, x, who):
		if (who == "A"):
			return (x**self.eB)%self.nB
		elif (who == "B"):
			return (x**self.eA)%self.nA

	def dechiffr(self, y, who):
		if (who == "A"):
			return (y**self.dA)%self.nA
		elif (who == "B"):
			return (y**self.dB)%self.nB

	def signature(self, who):
		if (who == "A"):
			if (self.nA <= self.nB):
				sign = (((self.sA ** self.dA)%self.nA) ** self.eB)%self.nB
			else: 
				sign = (((self.sA ** self.eB)%self.nB) ** self.dA)%self.nA
		elif (who == "B"):
			if (self.nA <= self.nB):
				sign = (((self.sB ** self.eA)%self.nA) ** self.dB)%self.nB
			else: 
				sign = (((self.sB ** self.dB)%self.nB) ** self.eA)%self.nA
		return sign

	def signature_verif(self, sign, who):
		if (who == "A"):
			if (self.nA > self.nB):
				result = (((sign ** self.dA)%self.nA) ** self.eB)%self.nB
			else: 
				result = (((sign ** self.eB)%self.nB) ** self.dA)%self.nA
		elif (who == "B"):
			if (self.nA > self.nB):
				result = (((sign ** self.eA)%self.nA) ** self.dB)%self.nB
			else: 
				result = (((sign ** self.dB)%self.nB) ** self.eA)%self.nA
		return result

		
class crypto_elgamal(object):
	"""docstring for crypto_elgamal"""
	def __init__(self):
		self.g = 0
		self.modulo = 0

		self.eA = 0
		self.dA = 0

		self.eB = 0
		self.dB = 0

	def chiffr(self, x, k, who):
		r = (self.g ** k)%self.modulo
		if (who == "A"):
			y = (x * (self.eB**k))%self.modulo
		elif (who == "B"):
			y = (x * (self.eA**k))%self.modulo
		return {"r": r, "y" : y}
	
	def dechiffr(self, r, y, who):
		if (who == "A"):
			temp = r**self.dA
			x = y * bezout(temp, self.modulo)[str(temp)]
		elif (who == "B"):
			temp = r**self.dB
			x = y * bezout(temp, self.modulo)[str(temp)]
		return x%self.modulo

	def find_dA(self):
		x = 1
		while ( ((self.g**x)%self.modulo) != self.eA):
			x += 1

		return x
		

	def find_dB(self):
		x = 1
		while ( ((self.g**x)%self.modulo) != self.eB):
			x += 1

		return x

	def find_eA(self):
		return ( (self.g**self.dA)%self.modulo )

	def find_eB(self):
		return ( (self.g**self.dB)%self.modulo )
		pass
		

"""crypt = crypto_elgamal()

crypt.g = 2
crypt.modulo = 19

crypt.eA = 14
crypt.dA = 7

crypt.eB = 17
crypt.dB = 1

print(crypt.dechiffr(8, 10, "A"))"""


crypt = crypto_rsa()

crypt.nA = 77
crypt.eA = 29
crypt.dA = 29
crypt.sA = 8

crypt.nB = 65
crypt.eB = 35
crypt.dB = 11
crypt.sB = 12

print(crypt.signature("A"))
