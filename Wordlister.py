#!/usr/bin/env python3

#Coded by გიო რგი
#Contributed by S4RR4

import os
os.system('clear')

import time

import signal

def keyboardInterruptHandler(signal, frame):
    print("\nპროგრამა გაითიშა.".format(signal))
    exit(0)

signal.signal(signal.SIGINT, keyboardInterruptHandler)

print('\n     __...--~~~~~-._   _.-~~~~~--...__')
print('   //               `V`               \\')
print('  //                 |                 \\') 
print(' //__...--~~~~~~-._  |  _.-~~~~~~--...__\\') 
print('//__.....----~~~~._\ | /_.~~~~----.....__\\')
print('====================\|/===================')
print(' Wordlister.py v1.0 - Coded by გიო რგი\n')
print('https://github.com/AnonymousFromGeorgia/Wordlister')
print("\nგამოიყენეთ კლავიში Enter, რათა გამოტოვოთ შეკითხვა.")
print("\nგამოიყენეთ კლავიშების კომბინაცია CTRL+C, რათა გათიშოთ პროგრამა.")
print("\nსასურველია კითხვებს უპასუხოდ ლათინური დამწერლობით.")
print("\nამჟამად ხელმისაწვდომია 12 შეკითხვა.\n")
name = input("1). შეიყვანეთ მსხვერპლის სახელი: ")
lname = input("\n2). შეიყვანეთ მსხვერპლის გვარი: ")
bgfriendN = input("\n3). შეიყვანეთ მსხვერპლის შეყვარებულის სახელი: ")
bgfriendL = input("\n4). შეიყვანეთ მსხვერპლის შეყვარებულის გვარი: ")
byear = input("\n5). შეიყვანეთ მსხვერპლის დაბადების წელი: ")
bmonth = input("\n6). შეიყვანეთ მსხვერპლის დაბადების თვე რიცხვით (მაგ. 05 ან 11): ")
bday = input("\n7). შეიყვანეთ მსხვერპლის დაბადების რიცხვი: ")
bday2 = input("\n8). შეიყვანეთ მსხვერპლის ახლობლის დაბადების რიცხვი (10-ზე ნაკლებს დაუწერეთ წინ 0): ")
color = input("\n9). შეიყვანეთ მსხვერპლის საყვარელი ფერი: ")
pet = input("\n10). შეიყვანეთ მსხვერპლის შინაური ცხოველის (Pet) სახელი: ")
country = input("\n11). შეიყვანეთ ქვეყანა სადაც მსხვერპლი იმოგზაურებდა: ")
city = input("\n12). შეიყვანეთ ქალაქი სადაც მსხვერპლი იცხოვრებდა: ")

ask = input("\nდაიწყოს Wordlist-ის გენერირება? (კი/არა): ")
if ask == 'კი':

	report = open('wordlist.txt', 'w')


	for target in (name,lname,bgfriendN,bgfriendL,byear,bmonth,bday,bday2,color,pet,country,city):
		report.write(name + '\n')
		report.write(lname + '\n')
		report.write(name+lname + '\n')
		report.write(byear + '\n')
		report.write(bmonth + '\n')
		report.write(bday + '\n')
		report.write(color + '\n')
		report.write(pet + '\n')
		report.write(country + '\n')
		report.write(city + '\n')

		report.write(name + byear + '\n')
		report.write(name + bmonth + '\n')
		report.write(name + bday + '\n')
		report.write(name + bday2 + '\n')
		report.write(name + byear + bmonth + '\n')
		report.write(name + bmonth + byear + '\n')
		report.write(name + bday + byear + bmonth + '\n')
		report.write(name + bday2 + byear + bmonth + '\n')
		report.write(name + bday + bmonth + byear + '\n')
		report.write(name + byear + bday + '\n')
		report.write(name + byear + bday2 + '\n')
		report.write(name + bday + bmonth + '\n')
		report.write(name + bday2 + bmonth + '\n')
		report.write(name + color + bday + byear + '\n')
		report.write(name + color + bday2 + byear + '\n')
		report.write(name + color + byear + '\n')
		report.write(name + pet + byear + '\n')
		report.write(pet + name + '\n')
		report.write(name + pet + '\n')
		report.write(pet + name + byear + '\n')
		report.write(name + pet + bday + '\n')
		report.write(name + pet + bday2 + '\n')
		report.write(name + pet + bmonth + '\n')
		report.write(pet + name + byear + '\n')
		report.write(name + country + byear + '\n')
		report.write(name + country + bday + '\n')
		report.write(name + country + bday2 + '\n')
		report.write(name + country + bmonth + '\n')
		report.write(name + country + city + '\n')
		report.write(name + byear + country + '\n')
		report.write(name + byear + city + '\n')
		report.write(name + city + byear + '\n')	
		report.write(name + country + city + '\n')
		report.write(name + bday + country + '\n')
		report.write(name + bday2 + country + '\n')
		report.write(name + bday + city + '\n')
		report.write(name + bday2 + city + '\n')
		report.write(name + city + bday + '\n')
		report.write(name + city + bday2 + '\n')
		report.write(name + "_" + byear + '\n')
		report.write(name + "_" + bday + '\n')
		report.write(name + "_" + bday2 + '\n')	
		report.write(name + "-" + byear + '\n')
		report.write(name + "-" + bday + '\n')
		report.write(name + "-" + bday2 + '\n')

		report.write(lname + byear + '\n')
		report.write(lname + bmonth + '\n')
		report.write(lname + bday + '\n')
		report.write(lname + bday2 + '\n')
		report.write(lname + byear + bmonth + '\n')
		report.write(lname + bmonth + byear + '\n')
		report.write(lname + bday + byear + bmonth + '\n')
		report.write(lname + bday2 + byear + bmonth + '\n')
		report.write(lname + bday + bmonth + byear + '\n')
		report.write(lname + byear + bday2 + '\n')
		report.write(lname + bday + bmonth + '\n')
		report.write(lname + bday2 + bmonth + '\n')
		report.write(lname + color + bday + byear + '\n')
		report.write(lname + color + bday2 + byear + '\n')
		report.write(lname + color + byear+ '\n')
		report.write(lname + pet + byear + '\n')
		report.write(pet + lname + '\n')
		report.write(lname + pet + '\n')
		report.write(pet + lname + byear + '\n')
		report.write(lname + pet + bday + '\n')
		report.write(lname + pet + bday2 + '\n')
		report.write(lname + pet + bmonth + '\n')
		report.write(pet + lname + byear + '\n')
		report.write(lname + country + byear + '\n')
		report.write(lname + country + bday + '\n')
		report.write(lname + country + bday2 + '\n')
		report.write(lname + country + bmonth + '\n')
		report.write(lname + country + city + '\n')
		report.write(lname + byear + country + '\n')
		report.write(lname + byear + city + '\n')
		report.write(lname + city + byear + '\n')	
		report.write(lname + country + city + '\n')
		report.write(lname + bday + country + '\n')
		report.write(lname + bday2 + country + '\n')
		report.write(lname + bday + city + '\n')
		report.write(lname + bday2 + city + '\n')
		report.write(lname + city + bday + '\n')
		report.write(lname + city + bday2 + '\n')
		report.write(lname + "_" + byear + '\n')
		report.write(lname + "_" + bday + '\n')
		report.write(lname + "_" + bday2 + '\n')	
		report.write(lname + "-" + byear + '\n')
		report.write(lname + "-" + bday + '\n')
		report.write(lname + "-" + bday2 + '\n')

		report.write(byear + lname + '\n')
		report.write(byear + bmonth + '\n')
		report.write(byear + bday + '\n')
		report.write(byear + bday2 + '\n')
		report.write(byear + lname + bmonth + '\n')
		report.write(byear + bmonth + lname + '\n')
		report.write(byear + bday + lname + bmonth + '\n')
		report.write(byear + bday2 + lname + bmonth + '\n')
		report.write(byear + bday + bmonth + lname + '\n')
		report.write(byear + name + bday + '\n')
		report.write(byear + name + bday2 + '\n')
		report.write(byear + bday + bmonth + '\n')
		report.write(byear + bday2 + bmonth + '\n')
		report.write(byear + color + bday + lname + '\n')
		report.write(byear + color + bday2 + lname + '\n')
		report.write(byear + color + lname + '\n')
		report.write(byear + pet + lname + '\n')
		report.write(byear + pet + '\n')
		report.write(byear + pet + '\n')
		report.write(byear + lname + pet + '\n')
		report.write(byear + pet + bday + '\n')
		report.write(byear + pet + bday2 + '\n')
		report.write(byear + pet + bmonth + '\n')
		report.write(byear + lname + pet + '\n')
		report.write(byear + country + byear + '\n')
		report.write(byear + country + bday + '\n')
		report.write(byear + country + bday2 + '\n')
		report.write(byear + country + bmonth + '\n')
		report.write(byear + country + city + '\n')
		report.write(byear + byear + country + '\n')
		report.write(byear + byear + city + '\n')
		report.write(byear + city + byear + '\n')	
		report.write(byear + country + city + '\n')
		report.write(byear + bday + country + '\n')
		report.write(byear + bday2 + country + '\n')
		report.write(byear + bday + city + '\n')
		report.write(byear + bday2 + city + '\n')
		report.write(byear + city + bday + '\n')
		report.write(byear + city + bday2 + '\n')
		report.write(byear + "_" + byear + '\n')
		report.write(byear + "_" + bday + '\n')
		report.write(byear + "_" + bday2 + '\n')	
		report.write(byear + "-" + byear + '\n')
		report.write(byear + "-" + bday + '\n')
		report.write(byear + "-" + bday2 + '\n')

		report.write(country + lname + '\n')
		report.write(country + bmonth + '\n')
		report.write(country + bday + '\n')
		report.write(country + bday2 + '\n')
		report.write(country + lname + bmonth + '\n')
		report.write(country + bmonth + lname + '\n')
		report.write(country + bday + lname + bmonth + '\n') 
		report.write(country + bday2 + lname + bmonth + '\n')
		report.write(country + bday + bmonth + lname + '\n')
		report.write(country + byear + bday + '\n')
		report.write(country + byear + bday2 + '\n')
		report.write(country + bday + bmonth + '\n')
		report.write(country + bday2 + bmonth + '\n')
		report.write(country + color + bday + lname + '\n')
		report.write(country + color + bday2 + lname + '\n')
		report.write(country + color + lname + '\n')
		report.write(country + pet + lname + '\n')
		report.write(country + pet + '\n')
		report.write(country + pet + '\n')
		report.write(country + lname + pet + '\n')
		report.write(country + pet + bday + '\n')
		report.write(country + pet + bday2 + '\n')
		report.write(country + pet + bmonth + '\n')
		report.write(country + lname + pet + '\n')
		report.write(country + byear + byear + '\n')
		report.write(country + byear + bday + '\n')
		report.write(country + byear + bday2 + '\n')
		report.write(country + byear + bmonth + '\n')
		report.write(country + byear + city + '\n')
		report.write(country + byear + byear + '\n')
		report.write(country + byear + city + '\n')
		report.write(country + city + byear + '\n')	
		report.write(country + byear + city + '\n')
		report.write(country + bday + byear + '\n')
		report.write(country + bday2 + byear + '\n')
		report.write(country + bday + city + '\n')
		report.write(country + bday2 + city + '\n')
		report.write(country + city + bday + '\n')
		report.write(country + city + bday2 + '\n')
		report.write(country + "_" + byear + '\n')
		report.write(country + "_" + bday + '\n')
		report.write(country + "_" + bday2 + '\n')	
		report.write(country + "-" + byear + '\n')
		report.write(country + "-" + bday + '\n')
		report.write(country + "-" + bday2 + '\n')

		report.write(city + byear + '\n')
		report.write(city + bmonth + '\n')
		report.write(city + bday + '\n')
		report.write(city + bday2 + '\n')
		report.write(city + byear + bmonth + '\n')
		report.write(city + bmonth + byear + '\n')
		report.write(city + bday + byear + bmonth + '\n')
		report.write(city + bday2 + byear + bmonth + '\n')
		report.write(city + bday + bmonth + byear + '\n')
		report.write(city + byear + bday + '\n')
		report.write(city + byear + bday2 + '\n')
		report.write(city + bday + bmonth + '\n')
		report.write(city + bday2 + bmonth + '\n')
		report.write(city + color + bday + byear + '\n')
		report.write(city + color + bday2 + byear + '\n')
		report.write(city + color + byear + '\n')
		report.write(city + pet + byear + '\n')
		report.write(city + name + '\n')
		report.write(city + pet + '\n')
		report.write(city + name + byear + '\n')
		report.write(city + pet + bday + '\n')
		report.write(city + pet + bday2 + '\n')
		report.write(city + pet + bmonth + '\n')
		report.write(city + name + byear + '\n')
		report.write(city + country + byear + '\n')
		report.write(city + country + bday + '\n')
		report.write(city + country + bday2 + '\n')
		report.write(city + country + bmonth + '\n')
		report.write(city + country + name + '\n')
		report.write(city + byear + country + '\n')
		report.write(city + byear + name + '\n')
		report.write(city + name + byear + '\n')	
		report.write(city + country + name + '\n')
		report.write(city + bday + country + '\n')
		report.write(city + bday2 + country + '\n')
		report.write(city + bday + name + '\n')
		report.write(city + bday2 + name + '\n')
		report.write(city + name + bday + '\n')
		report.write(city + name + bday2 + '\n')
		report.write(city + "_" + byear + '\n')
		report.write(city + "_" + bday + '\n')
		report.write(city + "_" + bday2 + '\n')	
		report.write(city + "-" + byear + '\n')
		report.write(city + "-" + bday + '\n')
		report.write(city + "-" + bday2 + '\n')

		report.write(bgfriendN + byear + '\n')
		report.write(bgfriendN + bmonth + '\n')
		report.write(bgfriendN + bday + '\n')
		report.write(bgfriendN + bday2 + '\n')
		report.write(bgfriendN + byear + bmonth + '\n')
		report.write(bgfriendN + bmonth + byear + '\n')
		report.write(bgfriendN + bday + byear + bmonth + '\n')
		report.write(bgfriendN + bday2 + byear + bmonth + '\n')
		report.write(bgfriendN + bday + bmonth + byear + '\n')
		report.write(bgfriendN + byear + bday + '\n')
		report.write(bgfriendN + byear + bday2 + '\n')
		report.write(bgfriendN + bday + bmonth + '\n')
		report.write(bgfriendN + bday2 + bmonth + '\n')
		report.write(bgfriendN + color + bday + byear + '\n')
		report.write(bgfriendN + color + bday2 + byear + '\n')
		report.write(bgfriendN + color + byear + '\n')
		report.write(name + bgfriendN + byear + '\n')
		report.write(bgfriendN + name + '\n')
		report.write(name + bgfriendN + '\n')
		report.write(bgfriendN + name + byear + '\n')
		report.write(bgfriendN + pet + bday + '\n')
		report.write(bgfriendN + pet + bday2 + '\n')
		report.write(bgfriendN + pet + bmonth + '\n')
		report.write(bgfriendN + name + byear + '\n')
		report.write(bgfriendN + country + byear + '\n')
		report.write(bgfriendN + country + bday + '\n')
		report.write(bgfriendN + country + bday2 + '\n')
		report.write(bgfriendN + country + bmonth + '\n')
		report.write(bgfriendN + country + city + '\n')
		report.write(bgfriendN + byear + country + '\n')
		report.write(bgfriendN + byear + city + '\n')
		report.write(bgfriendN + city + byear + '\n')	
		report.write(bgfriendN + country + city + '\n')
		report.write(bgfriendN + bday + country + '\n')
		report.write(bgfriendN + bday2 + country + '\n')
		report.write(bgfriendN + bday + city + '\n')
		report.write(bgfriendN + bday2 + city + '\n')
		report.write(bgfriendN + city + bday + '\n')
		report.write(bgfriendN + city + bday2 + '\n')
		report.write(bgfriendN + "_" + byear + '\n')
		report.write(bgfriendN + "_" + bday + '\n')
		report.write(bgfriendN + "_" + bday2 + '\n')	
		report.write(bgfriendN + "-" + byear + '\n')
		report.write(bgfriendN + "-" + bday + '\n')
		report.write(bgfriendN + "-" + bday2 + '\n')

		report.write(bgfriendL + byear + '\n')
		report.write(bgfriendL + bmonth + '\n')
		report.write(bgfriendL + bday + '\n')
		report.write(bgfriendL + bday2 + '\n')
		report.write(bgfriendL + byear + bmonth + '\n')
		report.write(bgfriendL + bmonth + byear + '\n')
		report.write(bgfriendL + bday + byear + bmonth + '\n')
		report.write(bgfriendL + bday2 + byear + bmonth + '\n')
		report.write(bgfriendL + bday + bmonth + byear + '\n')
		report.write(bgfriendL + byear + bday+ '\n')
		report.write(bgfriendL + byear + bday2 + '\n')
		report.write(bgfriendL + bday + bmonth + '\n')
		report.write(bgfriendL + bday2 + bmonth + '\n')
		report.write(bgfriendL + color + bday + byear + '\n')
		report.write(bgfriendL + color + bday2 + byear + '\n')
		report.write(bgfriendL + color + byear + '\n')
		report.write(name + bgfriendL + byear + '\n')
		report.write(bgfriendL + name + '\n')
		report.write(name + bgfriendL + '\n')
		report.write(bgfriendL + name + byear + '\n')
		report.write(bgfriendL + pet + bday + '\n')
		report.write(bgfriendL + pet + bday2 + '\n')
		report.write(bgfriendL + pet + bmonth + '\n')
		report.write(bgfriendL + name + byear + '\n')
		report.write(bgfriendL + country + byear + '\n')
		report.write(bgfriendL + country + bday + '\n')
		report.write(bgfriendL + country + bday2 + '\n')
		report.write(bgfriendL + country + bmonth + '\n')
		report.write(bgfriendL + country + city + '\n')
		report.write(bgfriendL + byear + country + '\n')
		report.write(bgfriendL + byear + city + '\n')
		report.write(bgfriendL + city + byear + '\n')	
		report.write(bgfriendL + country + city + '\n')
		report.write(bgfriendL + bday + country + '\n')
		report.write(bgfriendL + bday2 + country + '\n')
		report.write(bgfriendL + bday + city + '\n')
		report.write(bgfriendL + bday2 + city + '\n')
		report.write(bgfriendL + city + bday + '\n')
		report.write(bgfriendL + city + bday2 + '\n')
		report.write(bgfriendL + "_" + byear + '\n')
		report.write(bgfriendL + "_" + bday + '\n')
		report.write(bgfriendL + "_" + bday2 + '\n')	
		report.write(bgfriendL + "-" + byear + '\n')
		report.write(bgfriendL + "-" + bday + '\n')
		report.write(bgfriendL + "-" + bday2 + '\n')

	report.close()
	print("\nWordlist-ის გენერირება წარმატებით დასრულდა.")
else:
	pass
