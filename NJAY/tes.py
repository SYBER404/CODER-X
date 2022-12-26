import os,re,sys,time,json,random,datetime,requests

m_fb = "m.facebook.com"
url_businness = "https://business.facebook.com"
ua_business = "Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36"
web_fb = "https://www.facebook.com/"
head_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"}
header = {"authority":"graph.facebook.com","cache-control":"max-age=0","sec-ch-ua-mobile":"?0","user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.66 Safari/537.36"}



def login():
	os.system('clear')
	cookie = str(input(f"(+) cookie : "))
	with requests.Session() as xyz:
		try:
			get_tok = xyz.get(url_businness+'/business_locations',headers = {"user-agent":ua_business,"referer": web_fb,"host": "business.facebook.com","origin": url_businness,"upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","content-type":"text/html; charset=utf-8"},cookies = {"cookie":cookie})
			token = re.search("(EAAG\w+)", get_tok.text).group(1)
			open('cookie.txt','w').write(cookie) 
			open('token.txt','w').write(token)
			menu()
		except requests.exceptions.ConnectionError:
			print ("(+) koneksi internet bermasalah !!!")
			exit()
		except (KeyError,IOError):
			print ("(+) cookie anda invalid !!!")
			os.system("rm -rf cookie.txt")
			os.system("rm -rf token.txt")
			
def menu():
	os.system('clear')
	token  = open('token.txt','r').read()
	cookie = {'cookie':open('cookie.txt','r').read()}
	os.system('clear')
	print ("")
	print ("(1) bot coment post facebook")
	print ("(2) bot spam coment post facebook")
	print ("(3) bot share posts facebook")
	print ("(0) log out ( keluar )")
	pahrul = input ("\n(+) choose : ")
	if pahrul =="1":
		os.system('clear')
		bot_komen()
	elif pahrul =="2":
		komen()
	elif pahrul =="3":
		share()
	elif pahrul =="0":
		print ("\n(+) terimakasih telah menggunakan script saya :)")
		os.system("rm cookie.txt")
		os.system("rm token.txt")
		login()
	else:
		print("(+) ngetik apaan lu bangsad !!!")
		exit()
		
		
def komen():
	ok,no=[],[]
	cookie = open('cookie.txt', 'r').read()
	token = open('token.txt', 'r').read()
	coki = {"cookie":cookie}
	os.system("clear")
	id = input(f"(+) id postingan : ")
	komen = input("(+) komentar : ")
	limit = int(input("(+) limit : "))
	print ("")
	for x in range(limit):
		_pahrul_ = requests.post(f'https://graph.facebook.com/{id}/comments/?message={komen}&access_token={token}',cookies={'cookie':cookie})
		cek_st = json.loads(_pahrul_.text)
		print(f'\r\033[1;97m[\033[1;92m✓\033[1;97m] SUCCES : {len(ok)} \033[1;97m[\033[1;91m!\033[1;97m] FAILED : {len(no)}', end=' ')
		if 'id' in cek_st:
			ok.append('succes')
		else:
			no.append('failed')
	
	
def share():
	ok,no=[],[]
	cookie = open('cookie.txt', 'r').read()
	token = open('token.txt', 'r').read()
	coki = {"cookie":cookie}
	os.system('clear')
	uiz = input(f"(+) masukan link post : ")
	limit = int(input(f"(+) masukan limit : "))
	print("")
	for x in range(limit):
		ress = requests.post(f"https://graph.facebook.com/me/feed?link={uiz}&published=0&access_token={token}",headers=header, cookies=coki).json()
		print(f'\r\033[1;97m[\033[1;92m✓\033[1;97m] SUCCES : {len(ok)} \033[1;97m[\033[1;91m!\033[1;97m] FAILED : {len(no)}', end=' ')
		if "id" in ress:
			ok.append('succes')
		else:
			no.append('failed')
			
			
def bot_komen():
	ok,no=[],[]
	cookie = open('cookie.txt', 'r').read()
	token = open('token.txt', 'r').read()
	coki = {"cookie":cookie}
	os.system("clear")
	idx = input(f"\033[1;97m(+) id target : ")
	cek = requests.get("https://graph.facebook.com/"+idx+"?access_token="+token,cookies=coki).json()
	lim = input(f"\033[1;97m(+) limit : ")
	print("")
	post = requests.get("https://graph.facebook.com/"+cek['id']+"?fields=feed.limit("+lim+")&access_token="+token,cookies=coki).json()
	for i in post['feed']['data']:
		tag = ("@["+ idx +":]")
		texs = random.choice(['"Kamu laiknya karya seni. Tidak semua orang akan mengerti dirimu, tetapi orang-orang yang mengerti, tidak akan pernah melupakanmu."','"Orang yang tak pernah membuat kesalahan adalah orang yang tidak pernah berbuat apa-apa." - Norman Edwin','"Belajarlah dari kesalahan orang lain. Anda tak dapat hidup cukup lama untuk melakukan semua kesalahan itu sendiri." - Martin Vanbee','"Belajar memang melelahkan, namun akan lebih melelahkan lagi bila saat ini kamu tidak belajar."','"Diam adalah lebih baik daripada mengucapkan kata-kata yang tanpa makna." - Pythagoraz','"Jika Anda takut gagal, Anda tidak pantas untuk sukses!" - Charles Barkley','"Ingin menjadi orang lain adalah tindakan untuk menyia-nyiakan dirimu sendiri." - Kurt Cobain','"Jika kamu mencari satu orang yang akan mengubah hidupmu, lihatlah di cermin."','"Terkadang kita diuji bukan untuk menunjukkan kelemahan kita, tetapi untuk menemukan kekuatan kita."','Jangan pernah menyerah ketika kamu masih mampu berusaha lagi. Tidak ada kata berakhir sampai kamu berhenti mencoba','"Belajar bukan hanya mengetahui apa yang harus dilakukan, tapi melakukan apa yang sudah kita ketahui."','"Sukses adalah sebuah perjalanan, bukan sebuah tujuan. Usaha sering lebih penting daripada hasilnya."','"Kegagalan adalah kunci kesuksesan. Setiap kesalahan mengajarkan kita sesuatu."','"Kamu tidak bisa menyenangkan semua orang, dan kamu tidak bisa membuat semua orang menyukaimu," Katie Couric.','"Lakukan satu hal setiap hari yang membuatmu takut," Eleanor Roosevelt.','"Ingat, tidak ada yang bisa membuat Anda merasa rendah diri tanpa persetujuan Anda," Eleanor Roosevelt.','"Jika Anda menginginkan pelangi, Anda harus tahan dengan hujan," Dolly Parton.','"Hidup bukanlah tentang menemukan diri Anda sendiri. Hidup adalah tentang menciptakan diri Anda sendiri," George Bernard Shaw.','"Semua impian kita bisa menjadi kenyataan jika kita memiliki keberanian untuk mengejarnya," Walt Disney.','"Seseorang yang luar biasa itu sederhana dalam ucapannya, tetapi hebat dalam tindakannya."','" Jangan menjelaskan tentang dirimu kepada siapa pun, karena yang menyukaimu tidak butuh itu. Dan yang membencimu tidak percaya itu."','" Untuk mendapatkan apa yang diinginkan, kau harus bersabar dengan apa yang kau benci."','Balas dendam terbaik adalah menjadikan dirimu lebih baik."','"Jangan takut akan perubahan. Kita mungkin kehilangan sesuatu yang baik, namun kita akan peroleh sesuatu yang lebih baik lagi."','" Jika diammu bijak, maka diamlah. Apabila diammu diinjak, maka bicaralah supaya tak ada lagi orang yang menginjak dan meremehkan dirimu."','"Kegagalan dibuat hanya oleh mereka yang gagal untuk berani, bukan oleh mereka yang berani gagal."','"Janganlah pernah menyerah ketika kamu masih mampu berusaha lagi. Tidak ada kata berakhir sampai kamu berhenti mencoba." - Brian Dyson','"Lakukan apa yang harus kamu lakukan sampai kamu dapat melakukan apa yang ingin kamu lakukan." - Oprah Winfrey'])
		kom = ("Komentar Ini Ditulis Oleh Bot ")
		waktu = str(datetime.datetime.now().strftime('%H:%M:%S'))
		_hari_   = {'Sunday':'Minggu','Monday':'Senin','Tuesday':'Selasa','Wednesday':'Rabu','Thursday':'Kamis','Friday':'Jumat','Saturday':'Sabtu'}[str(datetime.datetime.now().strftime("%A"))]
		submit = requests.post("https://graph.facebook.com/"+i['id']+"/comments?message=" + hhl + "\n"+ tag + "\n\n" + texs + "\n\n" + kom + "\n[ Pukul "+ waktu + " WIB ] "+ "\n- "+ _hari_ + ", "+ sekarang + " -" + "&access_token="+token,cookies=coki).json()
		print(f'\r\033[1;97m[\033[1;92m✓\033[1;97m] SUCCES : {len(ok)} \033[1;97m[\033[1;91m!\033[1;97m] FAILED : {len(no)}', end=' ')
		if "id" in submit:
			ok.append('succes')
		else:
			no.append('failed')

login() 
		
