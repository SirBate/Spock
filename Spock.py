import random

print("\n¡Bienvenido a \" Piedra, Papel, Tijeras, Lagarto o Spock\" ")
nameJ = input("\n Digíta tu Nickname\n")
nameJ = nameJ.upper()
print("\n \n Te recordamos las reglas básicas :) \n \n" )
print("1. Papel le gana a Piedra y a Spock")
print("2. Piedra le gana a Lagarto y a Tijeras")
print("3. Lagarto le gana a Spock y a Papel")
print("4. Spock le gana a Tijeras y a Piedra")
print("5. Tijeras le gana a Papel y a Lagarto\n")
Game = 'si'  #Interruptor
cont = 0
PuntuaPC = 0 
PuntuaUS = 0
while Game == "si":
	print("----------------------------------------------------------------------------------")
	print("\nJuego   #{}\n".format(cont+1))
	cont = cont	+ 1 
	empate = 1
	while empate == 1:

		#Entrada User
		User = input("¡Tu turno! \n Digíta \"Piedra, papel, tijeras, lagarto o spock\" \n ")#'TijErAs'
		User = User.lower()

			
		#Verificación valor User
		if User == 'piedra' or User == 'tijeras' or User == 'papel'or User == 'spock' or User == 'lagarto':
			print("")
		else:
			print("EEEERRROOOOOORR")


		#Metodo numero Random 
		Acum_PC = random.randint(0, 4) #Num random en 5 posibles
		if Acum_PC == 0:
		    PC = 'piedra'
		elif Acum_PC == 1:
		    PC = 'papel'
		elif Acum_PC == 2:
		    PC = 'tijeras'
		elif Acum_PC == 3:
		    PC = 'spock'
		else:
		    PC = 'lagarto'


		#Enfrentamiento User vs PC con While
		print('\n{}   {} vs PC {} \n'.format(nameJ,User.upper(), PC.upper()) ) 
		empate = 2
		if User == 'piedra' and PC == 'tijeras' or User == 'papel' and PC == 'piedra' or User == 'tijeras' and PC == 'papel' or User =="spock" and PC =="tijeras" or User =="spock" and PC =="piedra" or User== "lagarto" and PC =="spock" or User =="lagarto" and PC =="papel" or User== "piedra" and PC == "lagarto" or User == "papel" and PC == "spock" or User == "tijeras" and PC == "lagarto":#Fana User
			print ("{} ¡WINN!".format(nameJ))
			PuntuaUS += 1
			#User mas 1 punto
		elif  User == "tijeras" and PC =="piedra" or User== "piedra" and PC== "papel"  or User =="papel" and PC =="tijeras" or User =="tijeras" and PC =="spock" or User =="piedra" and PC =="spock" or User =="spock" and PC =="lagarto" or User =="papel" and PC =="lagarto" or User == "lagarto" and PC == "piedra" or User == "spock" and PC == "papel" or User == "lagarto" and PC == "tijeras": #PC FANA
			print ("PC ¡WINN!")
			PuntuaPC += 1
			#PC mas 1 punto
		else:
				empate =1
				print ("\n¡Vamos a DESEMPATAR!")

	Game = input("\n¿Deseas Continuar en el Juego? \n Escribe \"Si o No\"\n")
	Game = Game.lower()


print("\n\nTotal de Juegos #{}\n".format(cont))
print("*****  PUNTAJE  *****\n PC       {}\n {}     {}".format(PuntuaPC,nameJ,PuntuaUS))
print("\n*****  Gracias por jugar  *****")