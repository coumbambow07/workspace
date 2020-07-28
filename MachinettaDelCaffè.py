nome="cappuccino"             #nomi delle bevadne
nome1="caffè espresso"
nome2="caffè-macchiato"
nome3="latte-macchiato"
nome4="caffe-americano"

prezzo= {"prezzo ":0.50}        #prezzi delle bevande
prezzo1= {"prezzo ": 0.20}
prezzo2={"prezzo ":0.30}
prezzo3={"prezzo ":0.40}
prezzo4={"prezzo ":0.40}
prezzo5={"prezzo ":0.30}


prezzoarray=0.50               #gli array
prezzoarray1=0.20
prezzoarray2=0.30
prezzoarray3=0.40
prezzoarray4=0.40
prezzoarray5=0.30


drink_array= [nome,	prezzo]
drink_array1=[nome1, prezzo1]
drink_array2=[nome2, prezzo2]
drink_array3=[nome3, prezzo3]
drink_array4=[nome4, prezzo4]



import sys	
import time

									

def updt(total, progress):		#il progresso del bar
   
    barLength, status = 20, ""
    progress = float(progress) / float(total)
    if progress >= 1.:
        progress, status = 1, "\r\n"
    block = int(round(barLength * progress))
    text = "\r[{}] {:.0f}% {}".format(
        "#" * block + "-" * (barLength - block), round(progress * 100, 0),
        status)
    sys.stdout.write(text)
    sys.stdout.flush()


runs = 50


chiavetta=input
ricarica=0

chiavetta=0.00
diecicent=0.10
venticent=0.20
cinquantacent=0.50
a=float
maximport=2
maximport=int(input("Dimmi l'importo"))		
print("maximport",maximport)					#il massimo importo inserito
while maximport<2 or maximport>25:
		maximport=int(input("reinserisci il massimo importo"))
		print("max 25 , min 2")
		print("maximport",maximport)	



while chiavetta<maximport:
		ricarica=round(float(input("inserisci moneta ")),2)
		while ricarica<0:
			ricarica=round(float(input("inserisci moneta ")),2)
			if ricarica<0:
				print("ricarica deve essere >0")
		while ricarica>2:
			print("max moneta da 2 euro, 5cent non accettati, dammi un'altra moneta")
			ricarica=round(float(input("inserisci moneta ")),2)
	
		if (ricarica==0.10 or ricarica==0.20 or ricarica%0.5==0 or ricarica%1==0):
			chiavetta=chiavetta+ricarica
	
	
			print("importo tot chiavetta" ,round(chiavetta,2))
	
		elif (ricarica==0.30):
			print("non esiste moneta da 30cent")
		
		elif (ricarica==0.40):
	
		
			print("non esiste moneta da 40cent")
	
	
		elif (ricarica==0.60):
			print("non esiste moneta da 60cent")
	
		elif (ricarica==0.70):
			print("non esiste moneta da 70cent")
	
		elif (ricarica==0.80):
			print("non esiste moneta da 80cent")
	
		elif (ricarica==0.90):
			print("non esiste moneta da 90cent")
	
	
	
	
	
		else:
			print("deve essere diecicent, venticent ,50cent, 1 euro o 2 euro")
		
	
	
	
		if chiavetta >maximport:
			print("ritirare seguente importo")
			print(maximport-chiavetta)
	
		if chiavetta>maximport:
			chiavetta=maximport
			
		print("saldochiavetta ", chiavetta)	
		
ginsen=15
caffe=8
acqua=4									
latte=6		
bicchieri=99
grappa=7		

def prodbevanda1():
	chiavetta=8
	ginsen=15
	caffe=8
	acqua=4									
	latte=6		
	bicchieri=99
	grappa=7
	
	
	print(drink_array)
	if((chiavetta-prezzoarray)>0):									
		
		if((bicchieri)>0 and caffe>0 and latte>0 and acqua>0 and grappa>0 and ginsen>0):		
	
				caffe=caffe-1
				bicchieri=bicchieri-1
				latte=latte-1
				
				
					
				print("bicchieri rimanenti",bicchieri)	
				if bicchieri<5 and bicchieri>=1:
					print("i bicchieri sono quasi esauriti")

				chiavetta=chiavetta-prezzoarray
				print("hai selezionato bevanda1")
			
					
				print("prezzo ", prezzoarray)
				print("importo rimanente chiavetta", chiavetta)
				print("attendi un attimo...")
				for run_num in range(runs):
					time.sleep(.1)
					updt(runs, run_num + 1)
				print("La bevanda è pronta!!")
				

				if bicchieri==0:
					print("bicchieri esauriti, ","bicchieri=",bicchieri)
					bicchieri=25
					
				
				if (chiavetta<0.60):
					print("ricarica chiavetta")
					chiavetta=3
	



def prodbevanda2():
	chiavetta=8
	
	ginsen=15
	caffe=8
	acqua=4									
	latte=6		
	bicchieri=99
	grappa=7
	
		
	print(drink_array1)
	if((chiavetta-prezzoarray)>0):									
		
		if((bicchieri)>0 and caffe>0 and latte>0 and acqua>0 and grappa>0 and ginsen>0):		
		
					caffe=caffe-1
					
					bicchieri=bicchieri-1
					
					print("bicchieri rimanenti",bicchieri)
					if bicchieri<5 and bicchieri>=1:
						print("i bicchieri sono quasi esauriti, la preghiamo di rivolgersi al personale")
					
					
					
					chiavetta=chiavetta-prezzoarray1
					print("hai selezionato bevanda2")
				
					
					print("prezzo ", prezzoarray1)
					print("importo rimanente chiavetta", (chiavetta))
					print("attendi un attimo... ")
					for run_num in range(runs):
						time.sleep(.1)
						updt(runs, run_num + 1)
					print("La tua bevanda è pronta!!")
					
					
					
						
					if bicchieri==0:
						print("bicchieri esauriti, ","bicchieri=",bicchieri)
						bicchieri=25
						
					
					if (chiavetta<0.60):
						print("ricarica chiavetta")
						#funzionechiavetta()
						chiavetta=3
					
					
					if grappa<0:
						grappa=17
					if ginsen<0:
						ginsen=20
					
					if latte==0:
						latte=10
					if caffe==0:
						caffe=10
					if acqua==0:
						acqua=10
			




def prodbevanda3():
	chiavetta=8
	
	print(drink_array2)
	
	
	
	
	ginsen=15
	caffe=8
	acqua=4									
	latte=6		
	bicchieri=99
	grappa=7

	if((chiavetta-prezzoarray)>0):									
		
		if((bicchieri)>0 and caffe>0 and latte>0 and acqua>0 and grappa>0 and ginsen>0):	
			
					latte=latte-1
					caffe=caffe-1
					bicchieri=bicchieri-1
					
					chiavetta=chiavetta-prezzoarray2
					print("hai selezionato bevanda3")
				
					print("prezzo ", prezzoarray2)
					print("importo rimanente chiavetta", chiavetta)
					print("bicchieri rimanenti",bicchieri)
					if bicchieri<5 and bicchieri>=1:
						print("i bicchieri sono quasi esauriti, la preghiamo di rivolgersi al personale")
				
					
					
					
					print("attendi un attimo...")
					
					for run_num in range(runs):
						time.sleep(.1)
						updt(runs, run_num + 1)
					print("La tua bevanda è pronta")
					
					if bicchieri==0:
						print("bicchieri esauriti, ","bicchieri=",bicchieri)
						bicchieri=25
						
					
					if (chiavetta<0.60):
						print("ricarica chiavetta")
						#funzionechiavetta()
						chiavetta=3
					
					
					if grappa<0:
						grappa=17
					if ginsen<0:
						ginsen=20
					
					if latte==0:
						latte=10
					if caffe==0:
						caffe=10
					if acqua==0:
						acqua=10
						
					return(chiavetta)
					return(acqua)
					return(latte)
					return(caffe)
					return(ginsen)
					return(grappa)
						
					
					
					

			
def prodbevanda4():
	chiavetta=8
	
	ginsen=15
	caffe=8
	acqua=4									
	latte=6		
	bicchieri=99
	grappa=7
						
	print(drink_array3)
	if((chiavetta-prezzoarray)>0):									
		
		if((bicchieri)>0 and caffe>0 and latte>0 and acqua>0 and grappa>0 and ginsen>0):		
															
				
				
		
					latte=latte-1
					caffe=caffe-1
					bicchieri=bicchieri-1
					
					
					chiavetta=chiavetta-prezzoarray3
					print("hai selezionato bevanda4")
					
					print("prezzo ", prezzoarray3)
					print("bicchieri rimanenti",bicchieri)
					
				
					
					
					
					print("importo rimanente chiavetta", (chiavetta))
					print("attendi un attimo...")
					for run_num in range(runs):
						time.sleep(.1)
						updt(runs, run_num + 1)
					print("La tua bevanda è pronta!!")
					
					if bicchieri==0:
						print("bicchieri esauriti, ","bicchieri=",bicchieri)
						bicchieri=25
						
					
					if (chiavetta<0.60):
						print("ricarica chiavetta")
						#funzionechiavetta()
						chiavetta=3
					
					
					if grappa<0:
						grappa=17
					if ginsen<0:
						ginsen=20
					
					if latte==0:
						latte=10
					if caffe==0:
						caffe=10
					if acqua==0:
						acqua=10
						
					return(chiavetta)
					return(acqua)
					return(latte)
					return(caffe)
					return(ginsen)
					return(grappa)


def prodbevanda5():
	chiavetta=8
	print(drink_array4)
	ginsen=15
	caffe=8
	acqua=4									
	latte=6		
	bicchieri=99
	grappa=7

	
	
	
	
	if((chiavetta-prezzoarray)>0):									
		
		if((bicchieri)>0 and caffe>0 and latte>0 and acqua>0 and grappa>0 and ginsen>0):	
					ginsen=ginsen-3
					latte=latte-1
					caffe=caffe-1
					bicchieri=bicchieri-1
					
				
					chiavetta=chiavetta-prezzoarray4
					print("hai selezionato bevanda5")
				
					print("prezzo ", prezzoarray4)
					print("bicchieri rimanenti",bicchieri)
					if bicchieri<5 and bicchieri>=1:
						print("i bicchieri sono quasi esauriti, la preghiamo di rivolgersi al personale")
					
					print("importo rimanente chiavetta", chiavetta )
					print("attendi un attimo...")
					for run_num in range(runs):
						time.sleep(.1)
						updt(runs, run_num + 1)
					print(" La tua bevanda è pronta")
					
					if bicchieri==0:
						print("bicchieri esauriti, ","bicchieri=",bicchieri)
						bicchieri=25
						
					
					if (chiavetta<0.60):
						print("ricarica chiavetta")
						#funzionechiavetta()
						chiavetta=3
					
					
					if grappa<0:
						grappa=17
					if ginsen<0:
						ginsen=20
					
					if latte==0:
						latte=10
					if caffe==0:
						caffe=10
					if acqua==0:
						acqua=10
			
				
			

	
def funzionechiavetta():
	chiavetta=0
	
	while chiavetta<maximport:
	
		
		ricarica=round(float(input("inserisci moneta ")),2)
		while ricarica>2:
			print("max moneta da 2 euro, 5cent non accettati, dammi un'altra moneta")
			ricarica=round(float(input("inserisci moneta ")),2)
	
		if (ricarica==0.10 or ricarica==0.20 or ricarica%0.5==0 or ricarica%1==0):
			chiavetta=chiavetta+ricarica
	
	
			print("importo tot chiavetta" ,round(chiavetta,2))
	
		elif (ricarica==0.30):
			print("non esiste moneta da 30cent")
		
		elif (ricarica==0.40):
	
		
			print("non esiste moneta da 40cent")
	
	
		elif (ricarica==0.60):
			print("non esiste moneta da 60cent")
	
		elif (ricarica==0.70):
			print("non esiste moneta da 70cent")
	
		elif (ricarica==0.80):
			print("non esiste moneta da 80cent")
	
		elif (ricarica==0.90):
			print("non esiste moneta da 90cent")
	
	
	
	
	
		else:
			print("deve essere diecicent, venticent ,50cent, 1 euro o 2 euro")
		
	
	
	
		if chiavetta >maximport:
			print("ritirare seguente importo")
			print(maximport-chiavetta)
	
		if chiavetta>maximport:
			chiavetta=maximport
			
		print("saldochiavetta ", chiavetta)	
		
		return chiavetta+ricarica
		
	

def switch_demo(argument):
	switcher = {
			1: 
				prodbevanda1(),											
																		
			2:  prodbevanda2(),
			
			3: prodbevanda3(),
 
			4: prodbevanda4(),
            
			5:prodbevanda5(),
			         
				
	}
	print (switcher.get(argument, "invalid drink: buttons that can be pressed are 1,2,3,4,5"))


def pulsanti():	
	import tkinter as tk
    
    
	root = tk.Tk()
	frame = tk.Frame(root)
	frame.pack()


	def press1():
		prodbevanda1()
	
	
	
	def press2():
		prodbevanda2()

	def press3():
		prodbevanda3()

	def press4():
		prodbevanda4()
	
	def press5():
		prodbevanda5()
	
	
		

	def funzbicchieri():
		a=3
		bicchieri=0
		if a<4:
			bicchieri=bicchieri+5					
		print("bicchieri",bicchieri)			
		print("good")
	
	


	button = tk.Button(frame, 
						   text="Cappuccino + Zucc", 
						   fg="red",
						   command=press1)
	button.pack(side=tk.LEFT)
	button1 = tk.Button(frame, 
						   text="Caffè-Espresso", 
						   fg="green",
						   command=press2)
	button1.pack(side=tk.LEFT)

	button2 = tk.Button(frame, 
					   text="Caffè-Macchiato + Zucc", 
						   fg="red",
						   command=press3)
	button2.pack(side=tk.LEFT)


	button3 = tk.Button(frame, 
						   text="Latte-Macchiato + Zucc", 
						   fg="green",
						   command=press4)
	button3.pack(side=tk.LEFT)


	button4 = tk.Button(frame, 
						   text="Caffè-Americano + Zucc", 
						   fg="red",
						   command=press5)
	button4.pack(side=tk.LEFT)


	

	root.mainloop()

pulsanti()





