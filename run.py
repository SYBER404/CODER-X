import requests, re, time,os
from bs4 import BeautifulSoup

url = (lambda x: "https://mbasic.facebook.com/removefriend.php?friend_id={}&unref=profile_gear".format(x))
names = (lambda x: "\033[1;97m[✓] menghapus : \033[1;96m{}\033[1;97m".format(x))
cookies = {"cookie":None}

def convert(cookie):
	cookies["cookie"] = cookie
	res = requests.Session().get('https://business.facebook.com/business_locations', headers = {
   	     'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36',
    	    'referer': 'https://www.facebook.com/',
   	     'host' : 'business.facebook.com',
    	    'origin' : 'https://business.facebook.com',
   	     'upgrade-insecure-requests' : '1',
    	    'accept-language' : 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
        	'cache-control' : 'max-age=0',
    	    'accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    	    'content-type' : 'text/html; charset=utf-8'
	    }, cookies = cookies)
	try:
		token = re.search('(EAAG\w+)',res.text).group(1)
	except:
		token = "cookies invalid"
	finally:
		return token

class Main:
	
	def __init__(self,id,name,cookie):
		self.id, self.name, self.cookie = id, name, {"cookie":cookie}
	
	def remove(self,**kwargs):
		with requests.Session() as session:
			return session.post("https://mbasic.facebook.com"+str(kwargs["url"]), cookies=self.cookie, data=kwargs["data"]).status_code

class Get(Main):

	@property
	def get(self):
		count = 0
		with requests.Session() as session:
			for i,j in zip(list(map(url,self.id)), list(map(names,self.name))):
				count += 1
				res = BeautifulSoup(session.get(i, cookies=self.cookie).text, "html.parser")
				form = res.find("form",{"method":"post"})
				data = {x.get("name"):x.get("value") for x in form.findAll("input",{"type":["hidden","submit"]})}
				if str(self.remove(url=form.get("action"),data=data))!="200":
					exit("\n\033[1;97m(+) gagal menghapus !!!")
				else:
					if count % 50 == 0:
						print("\n\033[1;97m(+) akun anda terkunci !!!")
						time.sleep(5)
					else:
						print(j,f"\t")
		return {"program":"finished"}

if __name__=="__main__":
	os.system("clear")
	coki = input("\n\033[1;97m(+) cookie : \033[1;92m")
	token = convert(coki)
	if token=="cookies invalid":
		print("\n\033[1;97m(+) cookie anda invalid !!!")
		exit()
	__info = requests.get("https://graph.facebook.com/me?fields=name,id&access_token={}".format(token), cookies={"cookie":coki}).json()
	_data = requests.get(f"https://graph.facebook.com/{__info['id']}?fields=friends.fields(id,name)&access_token={token}", cookies={"cookie":coki}).json()
	id, name = [],[]
	for x in _data["friends"]["data"]:
		id.append(x['id'])
		name.append(x['name'])
	print("\033[1;97m\n(+) name : {}\n(+) Id : {}\n(+) jumlah teman : {}\n".format(__info["name"], __info["id"], len(id)))
	count = int(input(f"\n\033[1;97m(+) berapa jumlah teman yang ingin anda hapus : "))
	print("\033[1;97m\n(+) please wait...\n")
	if count > len(id):
		exit()
	else:
		id = id[0:count]
		try:
			Debug = Get(id,name,coki)
			Debug.get
		except KeyboardInterrupt:
			exit()
	print("\n\033[1;97m(+) finished...")
		