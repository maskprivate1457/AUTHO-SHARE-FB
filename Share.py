# coding:utf-8
#/usr/bin/python
import requests,json,os,sys,random,rich,datetime,time,re
from rich.progress import track as deddtrk
from time import sleep as deddturu
from rich.panel import Panel as deddnel
from rich.markdown import Markdown as deddmark
from rich.console import Console as deddsol
from rich.panel import Panel as deddnel
from rich.text import Text as deddtekz
from rich import print as deddpel
from datetime import datetime
os.system("clear")
def deddxyz(xyzdedd):
	for xyzdeddxyz in xyzdedd + "\n":sys.stdout.write(xyzdeddxyz);sys.stdout.flush();time.sleep(0.08)
	deddturu(1.2)
deddxyz('\t\t\t\t\x1b[1;92m SUBSCRIBE DULU CHANNEL GW🗿')
os.system("xdg-open https://youtube.com/@TutorialTermux")
time.sleep(3)
os.system("clear")
R = '\x1b[1;91m' #Merah
G = '\x1b[1;92m' #Hijau
X = '\33[m' #Netral
Y = '\033[93m' # KUNING +
P = '\033[95m' # UNGU
B = '\x1b[0;34m' # BIRU +
a = 'red'
#s = 'blue'
u = 'yellow'
l = 'green'
#o = 'purple'
M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
P2 = "[#FFFFFF]" # PUTIH
K2 = "[#FFFF00]" # KUNING
deddr = random.choice([a,u,l,])
deddr2 = random.choice([R,G,B,Y,P])
header = {"authority":"graph.facebook.com","cache-control":"max-age=0","sec-ch-ua-mobile":"?0","user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.66 Safari/537.36"}
ses=requests.Session()
def clear():
	os.system('clear')
def deddxy(xydedd):
	for xydeddxy in xydedd + "\n":sys.stdout.write(xydeddxy);sys.stdout.flush();time.sleep(0.08)
	deddturu(1.2)
def deddxz(xzdedd):
	for xzdeddxz in xzdedd + "\n":sys.stdout.write(xzdeddxz);sys.stdout.flush();time.sleep(0.04)
	deddturu(0.7)
os.system("clear")
deddxy('\t\t\x1b[1;92mSelamat Datang Di Tools Auto Share By Demias Syihab Aldino ')
clear()
def deddbann():
	martis='''
  ██████╗░░█████╗░████████╗░██████╗███████╗██████╗░
  ██╔══██╗██╔══██╗╚══██╔══╝██╔════╝██╔════╝██╔══██╗
  ██████╦╝██║░░██║░░░██║░░░╚█████╗░█████╗░░██████╔╝
  ██╔══██╗██║░░██║░░░██║░░░░╚═══██╗██╔══╝░░██╔══██╗
  ██████╦╝╚█████╔╝░░░██║░░░██████╔╝███████╗██║░░██║
  ╚═════╝░░╚════╝░░░░╚═╝░░░╚═════╝░╚══════╝╚═╝░░╚═╝                                                                                                                                                             
    Bot Share FB 4.2\n'''
    
	zilong = deddtekz(martis,justify='center',style=f'{deddr}')
	deddpel(deddnel(zilong))
	
	akai='''
• Author   : Demias Syihab     •
• Github   : maskprivate1457   •
• FB       : Demias Syihab     •
• IG       : mask_private1457  •
• WA       : +62 896-6783-8732 •\n'''
	yuzong = deddnel(deddtekz(akai,justify='center',style='green'))
	deddpel(deddnel(yuzong,title='[green] • Informasi Author • [/green]'))
def deddlog():
	try:
		clear()
		tokenz = open(".token","r").read()
		cokie = open(".coki","r").read()
		deddhome()
	except (KeyError,IOError):
		deddbann()
		layla = "\x1b[1;92mDi Sarankan Menggunakan Extension Cookiedough"
		deddpel(deddnel(deddtekz(layla, justify='center')))
		cookie = input(f" [{R}!{G}] Masukkan Cookie > \x1b[0;34m{deddr2}")
		try:
			get_tok = requests.get('https://business.facebook.com/business_locations',headers = {"user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","content-type":"text/html; charset=utf-8"},cookies = {"cookie":cookie})
			tokenz = re.search("(EAAG\w+)", get_tok.text).group(1)
			coki = {"cookie":cookie}
			open('.coki','w').write(cookie)
			open('.token','w').write(tokenz)
			deddxz(f" \n {X}[{G}+{X}] Berhasil Login, anda akan diarahkan kedalam menu.");deddhome()
		except requests.exceptions.ConnectionError:
			deddxz(f" {X}[{R}Ã—{X}] {R}Koneksi internet anda bermasalah!");exit()
		except (KeyError,IOError,AttributeError):
			deddxz(f" {X}[{R}Ã—{X}] {R}Cookie invalid/akun anda terkena spam!");exit()
def deddhome():
	try:
		clear()
		deddbann()
		niba ='''\x1b[1;92m
[1]  Masuk Ke Menu [✓]
[2]  Exit/Hapus Cookie\n'''
		niba2 = deddtekz(niba,justify='center')
		deddpel(deddnel(niba2,title='[green] • Pilih Menu • [/green]'))
		angela = input(f' [{R}#{X}] {G}Pilih > \x1b[1;91m')
		if angela in ['1']:
			time.sleep(0.5)
			deddmenu()
		if angela in ['2']:
			os.system('rm -f .coki')
			deddxz(f' [{G}✕“{X}] {G}Berhasil menghapus cookie');exit()
		else:
			deddxz(f' [{R}—{X}] {R}Input yang anda masukan salah.{X}');deddhome()
			time.sleep(0.8)
	except (KeyError, IOError):
		deddxz(f' [{R}—{X}] {R}Input yang anda masukan salah.{X}');deddhome()
		time.sleep(1)
def deddmenu():
	try:  
		clear()
		token = open('.token', 'r').read()
		cok = open(".coki","r").read()
		deddnem = requests.get("https://graph.facebook.com/me/?access_token=%s"%(token), cookies={"cookie":cok}).json()["name"]
	except (KeyError, IOError):
		os.system('rm -f .token')
		deddlog()
	except requests.exceptions.ConnectionError: 
		exit(f" {X}[{R}Ã—{X}] Koneksi internet anda bermasalah!")
	deddbann()
	benet = f"{deddnem}"
	benet2 = deddtekz(benet,justify='center',style=f'{l}')
	deddpel(deddnel(benet2,title=f'[b] x Selamat Datang x [/b]'))
	martis ="Masukan Link Postingan"
	deddpel(deddnel(deddtekz(martis,justify='center',style=f'{a}')))
	idt = input(f" {X}[{R}#{X}] {G}Link  > \x1b[0;34m")
	try:
		amon ="\x1b[1;92mMasukan Jumlah Limit"
		deddpel(deddnel(deddtekz(amon,justify='center',style=f'{a}')))
		limit = int(input(f" {X}[{R}#{X}] {G}Limit > \x1b[1;91m"))
	except:
		deddturu(1)
		deddxz(f' {X}[{R}#{X}]{R} Input yang anda masukan salah.');exit()
	print(f" {X}[{G}#{X}] Tekan {G}Ctrl+Z {X}untuk berhenti\n")
	cok = open('.coki', 'r').read()
	token = open('.token', 'r').read()
	cookie = {"cookie":cok}
	try:
		for x in range(limit):
			x+=1
			response = ses.post(f"https://graph.facebook.com/v13.0/me/feed?link={idt}&published=0&access_token={token}",headers=header, cookies=cookie).json()
			if "id" in response:
				sys.stdout.write(f"\r {X}[{G}#{X}] Berhasil Membagikan {Y}{x}{X}/{R}{limit}{X} | {G}{response['id']}");sys.stdout.flush()
			else:
				deddxz(f"\n {X}[{R}Ã—{X}]{R} Gagal, mungkin akun anda terkena spam");deddnext()
	except requests.exceptions.ConnectionError:
		deddxz(f"\n {X}[{R}Ã—{X}]{R} Koneksi internet anda bermasalah !");exit()
	print("")
	deddnext()
def deddnext():
	deddxz(f" {X}[{R}#{X}] Ingin menjalankan ulang?");estes=input(f" {X}[{R}#{X}] ({G}Y{X}/{R}N{X}) : ")
	if estes in ['Y','y']:
		deddturu(4)
		deddhome()
	else:
		deddxz(f" {X}[{Y}#{X}]{Y} Sampai jumpa lain waktu ! ");exit()
if __name__=='__main__':
	try:os.system('git pull')
	except:pass
	deddlog()
