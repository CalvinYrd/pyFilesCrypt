import os, string, random, time, sys
from getpass import getpass
from tkinter import filedialog

def clear():
	if os.name == 'nt': os.system('cls')
	else: os.system('clear')

chars = tuple(string.printable.replace('\r', ''))
clear()

while 1:
	key = getpass('Saisissez la clé (Tappez <Entrer> pour quitter) :\n> ')

	if not key.strip(' \t'):
		clear()
		sys.exit(0)

	if getpass('Confirmez la clé saisie :\n> ') == key:
		break

	else:
		clear()
		print('Erreur de saisie, les clés saisies ne sont pas correspondantes.\n')
		continue

random.seed(key)
afterChars = list(string.printable.replace('\r', ''))

random.shuffle(afterChars)
afterChars = tuple(afterChars)
clear()

while 1:
	ans = input('1 - Chiffrer un fichier.\n2 - Déchiffrer un fichier.\n3 - Quitter.\n\n> ')

	try:
		ans = int(ans)
		assert ans in range(1, 4)

	except (AssertionError, ValueError):
		clear()
		print('La valeur saisie est incorrecte.\n')
		continue

	clear()
	if ans == 3:
		clear()
		break

	while 1:
		if ans == 1:
			de = ''

		else:
			de = 'dé'

		userFile = input(f'1 - Parcourir \n2 - Retour\n\n> ')

		try:
			if userFile == '2':
				clear()
				break

			elif userFile == '1':
				userFile = filedialog.askopenfile()

				if not userFile:
					clear()
					break

				else:
					userFile = userFile.name

			else:
				clear()
				print('La valeur saisie est incorrecte.\n')
				continue

			timeA = time.time()

			with open(userFile, 'r', encoding = 'utf-8') as file:
				finalChars, fileContent = [], tuple(file.read())

			for i in fileContent:

				if i in chars:
					if ans == 1:
						finalChars.append(chars[afterChars.index(i)]) # Encryption

					else:
						finalChars.append(afterChars[chars.index(i)]) # Decryption

				else:
					finalChars.append(i)

			with open(userFile, 'w', encoding = 'utf-8') as file:

				for i in finalChars:
					file.write(i)

			timeB = time.time()
			clear()

			print(f'Le fichier <{userFile}> a bien été {de}chiffré. [{round(timeB - timeA, 3)}s]\n')
			break

		except FileNotFoundError:
			clear()
			print(f'Aucun fichier nommé <{userFile}>.\n')
			continue

		except UnicodeDecodeError:
			clear()
			print(f'Désolé, le fichier <{userFile}> n\'as pas plus être {de}chiffré.\n')
			continue