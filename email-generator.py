from bs4 import BeautifulSoup
import requests
import time
import os

def getEmail():
	URL_Email = "https://10minutemail.net/"
	email_page = requests.get(URL_Email)
	handle_email = BeautifulSoup(email_page.content, 'html.parser')
	email = handle_email.find(class_='div-m-0 text-c')
	email = str(email)[84:].replace("\"/></div>", '')
	return email

def clear(): 
	if os.name == 'nt':
		os.system('cls') 
	else:
		os.system('clear')

def banner():
	clear()
	print("""
 ▄▄▌ ▐ ▄▌ ▄▄▄· ▄▄▄  ▄▄▄ ..▄▄ ·      ▄▄ • ▄▄▄ . ▐ ▄ 
██· █▌▐█▐█ ▀█ ▀▄ █·▀▄.▀·▐█ ▀.     ▐█ ▀ ▪▀▄.▀·•█▌▐█
██▪▐█▐▐▌▄█▀▀█ ▐▀▀▄ ▐▀▀▪▄▄▀▀▀█▄    ▄█ ▀█▄▐▀▀▪▄▐█▐▐▌
▐█▌██▐█▌▐█ ▪▐▌▐█•█▌▐█▄▄▌▐█▄▪▐█    ▐█▄▪▐█▐█▄▄▌██▐█▌
 ▀▀▀▀ ▀▪ ▀  ▀ .▀  ▀ ▀▀▀  ▀▀▀▀     ·▀▀▀▀  ▀▀▀ ▀▀ █▪
		""")
	print("\t\t\tDeveloped by Sqwares\n\n")

def writeToFile(email):
	file = open("emails.txt", 'a')
	write = ''
	write += email + '\n'
	file.write(write)
	file.close()

def main():
	banner()
	try:
		numEmails = int(input("[+] Oluşturmak istediğiniz e-posta sayısını girin: "))
	except:
		print("[!] Geçersiz Değer Girildi. 2 saniye içinde yeniden başlatılıyor...")
		time.sleep(2)
		main()
	writeOrNot = str(input("[+] Bir dosyaya kaydetmek istiyor musunuz? (Y/N): "))
	write = False
	if 'y' == writeOrNot[0].lower():
		write = True
	if write == True:
		print("[*] Dosyaya yazma etkinleştirildi!")
	print("[*] Creating {} emails".format(numEmails))
	try:
		for x in range(numEmails):
			email = getEmail()
			if '@' not in email:
				print("""
					[!] IP'NİZ 10MINUTEMAIL.NET TARAFINDAN YASAKLANMIŞTIR.
						LÜTFEN BİR VPN KULLANARAK IP DEĞİŞTİRİN VEYA İNTERNETİ YENİDEN BAŞLATIN.
					""")
				break
			else:
				if write == True:
					writeToFile(email)
				print("Email number {} : {}".format(x+1, email))
	except:
		print("Çıkılıyor...")
		exit()
if __name__ == "__main__":
	main()
