#Questo programma permette alle persone registrate di entrare mettendo dei credenziali
#per prima cosa ti chiede come ti chiami 
#Inserendo il nome ti dice se sei iscritto o meno 
#Poi chiede la password
#Se si vuole entrare o no
#e infine chiede il numero del badge
#se è giusto il badge entri sennò no


import random
import datetime
date_format = "%d/%m/%Y %H:%M:%S"

Name = []
Surname = []
Tax_code = []
badge_number = []
Presence = []

a = 3
b = 5
persona1="Coumba"	

persona2="Fama"

persona3="Sokhna"	
                 #questo programma consente l accesso solo ad una persona alla volta
	
password1="123"

password2="456"

password3="789"

badge_number1="89"

badge_number2="83"

badge_number3="85"

			## le password sono unic
listapersonaentrate=[]
i = 0
cont = 0


def badge_number():	
	
			
	name = input("Nome: ")
	Name.append(name)
	surname = input("Cognome: ")
	Surname.append(surname)
	tax_code = input("C.F: ")
	Tax_code.append(tax_code)
	Presence.append(False)
	date = datetime.datetime.now().strftime(date_format)
	Badge_number.append(random.randint(1, 100))
	print(f'Sono i dati\n Nome:{Name[-1]}\n Cognome:{Surname[-1]}\n Tax Code:{Tax_code[-1]}\n Badge_number:{Badge_number[-1]}')


chiedi=input("Come ti chiami? ")

if (chiedi==persona1 or chiedi==persona2 or chiedi==persona3):
	print(chiedi," Bene! ti sei iscritto!")
	dimmipassword=(input("Dimmi la tua password! "))

	if (dimmipassword==password1 or dimmipassword==password2 or dimmipassword== password3):
		print("password corretta!!")
		chiedi=input("vuoi entrare? ")
		if chiedi=="yes":
			badge_number = int(input("Inserisci il numero del tuo badge: "))
						#chiedi=random.randint((550,553)  )
						#if badge_number==chiedi:
						
			if badge_number==badge_number1 or badge_number2 or badge_number3:
					print("Benvenuto!!!")	
	
		
	else:
		chiedi=input("vuoi uscire? ")
		if	chiedi=="Yes":
			print("Arrivederci!!!")
		
						
	#quando la lista è completa chiede se si vuole uscire 



	#for v in admitted:
	#chiedi=input("vuoi uscire? ")
	#if	chiedi=="Yes":
	#badge_number = (input("Inserisci il numero del tuo badge: "))
	#print(v, "Arrivederci!")
			                                               #listapersonaentrate.append(v)		#.pop elimina elemento dalla list

else: 
	print(chiedi," Non sei iscritto")
