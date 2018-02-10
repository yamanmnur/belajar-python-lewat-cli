
import datetime

from menu import menu
m = menu()

print("====================  SELAMAT DATANG DI PEMBELAJARAN PYTHON ====================")
print "                >> versi 1.0 | date : ",datetime.datetime.now()

while True:

	m.getMenu()

	print(" ")
	print("  ===== pilih menu / part (1 - 14) =====")
	pilihMenu = input("  >> ")
	
	if pilihMenu == 1:
		part1 = open("part1.txt","r")
		print part1.read()
	else:
		print (" inputan anda salah")
	
	kondisia  = True
	kondisi = True
	while True :
		
		keluar = raw_input("keluar (y/n) : ")
		if keluar == "y":
			exit()
		elif keluar == "n":
			continue
			return False
		else:
			print("inputan anda salah!")

	