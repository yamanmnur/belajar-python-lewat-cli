#pycli master
import os
import datetime

from menu import menu
m = menu()
print("====================  SELAMAT DATANG DI PEMBELAJARAN PYTHON ====================")
print "                >> versi 1.0 | date : ",datetime.datetime.now()

while True:

	m.getMenu()
	pilih = True
	while pilih : 
		print(" ")
		print("  ===== pilih menu / part (1 - 14) =====")
		pilihMenu = raw_input("  >> ")
		
		if pilihMenu == '1':
			part1 = open("part1.txt","r")
			print part1.read()
			pilih = False
		else:
			print(" inputan anda salah")
			os.system("clear")
	else:
		kondisi = True
		while kondisi :
			
			keluar = raw_input("keluar (y/n) : ")
			if keluar == "y":
				exit()
			elif keluar == "n":
				kondisi = False
			else:
				print("inputan anda salah!")
		else:
			print("clear")
		os.system("clear")
		
