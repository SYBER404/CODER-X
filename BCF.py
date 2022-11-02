import os,re,sys,bs4,time,json,random,datetime,requests
from rich.panel import Panel as panel
from rich import print as vprint
from time import sleep as turu
ses=requests.Session()

FR = {'1':'Januari','2':'Februari','3':'Maret','4':'April','5':'Mei','6':'Juni','7':'Juli','8':'Agustus','9':'September','10':'Oktober','11':'November','12':'Desember'}
tgl = datetime.datetime.now().day
bln = FR[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year

m_fb = "m.facebook.com"
url_businness = "https://business.facebook.com"
ua_business = "Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36"
web_fb = "https://www.facebook.com/"
head_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"}
sekarang = str(tgl)+" "+str(bln)+" "+str(thn)


def jalan(xnxx):
	for hengker in xnxx + '\n':
		sys.stdout.write(hengker);sys.stdout.flush();turu(0.05)

now = datetime.datetime.now()
hour = now.hour
if hour < 4:
  hhl = "Selamat Dini Hari !"
elif 4 <= hour < 12:
  hhl = "Selamat Pagi !"
elif 12 <= hour < 15:
  hhl = "Selamat Siang !"
elif 15 <= hour < 17:
  hhl = "Selamat Sore !"
elif 17 <= hour < 18:
  hhl = "Selamat Petang !"
else:
  hhl = "Selamat Malam !"

expired_script = ['01', '11', '2022']

try:ua_crack=open("useragent.txt","r").read().splitlines()
except:ua_crack=["nokiac3-00/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/5.0 applewebkit/420+ (khtml, like gecko) safari/420+","Mozilla/5.0 (Linux; Android 8.0.0; RNE-L21 Build/HUAWEIRNE-L21; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.58 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/360.0.0.30.113;]"]


logo = ('''\033[1;91m
   ____                  _____                    __ 
  / __/__  ___ ___ _    / ___/__  __ _  ___ ___  / /_
 _\ \/ _ \/ _ `/  ' \  / /__/ _ \/  ' \/ -_) _ \/ __/
\033[1;97m/___/ .__/\_,_/_/_/_/  \___/\___/_/_/_/\__/_//_/\__/ 
   /_/                                               

\033[1;97m(+) facebook : Pahrul Aguspriana XD.
\033[1;97m(+) whatsapp : -
\033[1;97m(+) version  : 0.2
''')

def login_cookie():
	os.system('clear')
	print (logo)
	cookie = str(input(f"\033[1;97m(+) cookie : \033[1;92m"))
	with requests.Session() as xyz:
		try:
			get_tok = xyz.get(url_businness+'/business_locations',headers = {"user-agent":ua_business,"referer": web_fb,"host": "business.facebook.com","origin": url_businness,"upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","content-type":"text/html; charset=utf-8"},cookies = {"cookie":cookie})
			token = re.search("(EAAG\w+)", get_tok.text).group(1)
			open('cookie.txt','w').write(cookie) 
			open('token.txt','w').write(token)
			jalan ("\n\033[1;97m(+) sedang masuk tunggu sebentar...")
			comen(cookie)
		except requests.exceptions.ConnectionError:
			print ("\033[1;97m(+) koneksi internet bermasalah !!!")
			exit()
		except (KeyError,IOError):
			print ("\033[1;97m(+) cookie anda invalid !!!")
			os.system("rm -rf cookie.txt")
			os.system("rm -rf token.txt")
			login_cookie() 
		
def comen(cookie):
	waktu = str(datetime.datetime.now().strftime('%H:%M:%S'))
	_hari_   = {'Sunday':'Minggu','Monday':'Senin','Tuesday':'Selasa','Wednesday':'Rabu','Thursday':'Kamis','Friday':'Jumat','Saturday':'Sabtu'}[str(datetime.datetime.now().strftime("%A"))]
	kuki = cookie
	toket = open("token.txt","r").read()
	os.system('clear')
	print (logo)
	id = input ("\033[1;97m(+) masukan id : ")
	kom = input ("\033[1;97m(+) komentar : ")
	limit = int(input ('\033[1;97m(+) limit     : \033[1;92m'))
	for i in range(limit):
		requests.post("https://graph.facebook.com/"+ id + "/comments?message=" + kom + "\n\n- Bot Active"+ "\n- ( "+ _hari_ + ", "+ sekarang + " ) -" + "&access_token="+toket,headers = {"cookie":kuki})
		
	
	comen(cookie)



        
login_cookie()