# Decompile by KangEhem:)
# with (uncompyle6) version : 3.7.4
# Time Succes decompile : 2021-11-08 02:38:42.553534
import os
import sys
import time
a = "\033[90m"
m = "\033[91m"
h = "\033[92m"
k = "\033[93m"
b = "\033[94m"
u = "\033[95m"
l = "\033[96m"
p = "\033[97m"
def load():
    load = ['\033[94m             ╼╣\033[91m█\033[90m▒▒▒▒▒▒▒▒▒▒▒▒▒\033[91m█\033[94m╠╾ ', '             \033[94m╼╣\033[91m██\033[90m▒▒▒▒▒▒▒▒▒▒▒\033[91m██\033[94m╠╾ ', '             \033[94m╼╣\033[91m████\033[90m▒▒▒▒▒▒▒\033[91m████\033[94m╠╾ ', '             \033[94m╼╣\033[91m██████\033[90m▒▒▒\033[91m██████\033[94m╠╾ ', '             \033[94m╼╣\033[91m███████\033[90m▒\033[91m███████\033[94m╠╾ ', '             \033[94m╼╣\033[91m███████████████\033[94m╠╾ ', '             \033[94m╼╣\033[91m███████\033[90m▒\033[91m███████\033[94m╠╾ ', '             \033[94m╼╣\033[91m██████\033[90m▒▒▒\033[91m██████\033[94m╠╾ ', '             \033[94m╼╣\033[91m████\033[90m▒▒▒▒▒▒▒\033[91m████\033[94m╠╾ ', '             \033[94m╼╣\033[91m██\033[90m▒▒▒▒▒▒▒▒▒▒▒\033[91m██\033[94m╠╾ ', '\033[94m             ╼╣\033[91m█\033[90m▒▒▒▒▒▒▒▒▒▒▒▒▒\033[91m█\033[94m╠╾ ', '             \033[94m╼╣\033[91m██\033[90m▒▒▒▒▒▒▒▒▒▒▒\033[91m██\033[94m╠╾ ', '             \033[94m╼╣\033[91m████\033[90m▒▒▒▒▒▒▒\033[91m████\033[94m╠╾ ', '             \033[94m╼╣\033[91m██████\033[90m▒▒▒\033[91m██████\033[94m╠╾ ', '             \033[94m╼╣\033[91m███████\033[90m▒\033[91m███████\033[94m╠╾ ', '             \033[94m╼╣\033[91m███████████████\033[94m╠╾ ', '             \033[94m╼╣\033[91m███████\033[90m▒\033[91m███████\033[94m╠╾ ', '             \033[94m╼╣\033[91m██████\033[90m▒▒▒\033[91m██████\033[94m╠╾ ', '             \033[94m╼╣\033[91m████\033[90m▒▒▒▒▒▒▒\033[91m████\033[94m╠╾ ', '             \033[94m╼╣\033[91m██\033[90m▒▒▒▒▒▒▒▒▒▒▒\033[91m██\033[94m╠╾ ', '\033[94m             ╼╣\033[91m█\033[90m▒▒▒▒▒▒▒▒▒▒▒▒▒\033[91m█\033[94m╠╾ ', '             \033[94m╼╣\033[91m██\033[90m▒▒▒▒▒▒▒▒▒▒▒\033[91m██\033[94m╠╾ ', '             \033[94m╼╣\033[91m████\033[90m▒▒▒▒▒▒▒\033[91m████\033[94m╠╾ ', '             \033[94m╼╣\033[91m██████\033[90m▒▒▒\033[91m██████\033[94m╠╾ ', '             \033[94m╼╣\033[91m███████\033[90m▒\033[91m███████\033[94m╠╾ ', '             \033[94m╼╣\033[91m███████████████\033[94m╠╾ ', '             \033[94m╼╣\033[91m███████\033[90m▒\033[91m███████\033[94m╠╾ ', '             \033[94m╼╣\033[91m██████\033[90m▒▒▒\033[91m██████\033[94m╠╾ ', '             \033[94m╼╣\033[91m████\033[90m▒▒▒▒▒▒▒\033[91m████\033[94m╠╾ ', '             \033[94m╼╣\033[91m██\033[90m▒▒▒▒▒▒▒▒▒▒▒\033[91m██\033[94m╠╾ ', '\033[94m             ╼╣\033[91m█\033[90m▒▒▒▒▒▒▒▒▒▒▒▒▒\033[91m█\033[94m╠╾ ', '             \033[94m╼╣\033[91m██\033[90m▒▒▒▒▒▒▒▒▒▒▒\033[91m██\033[94m╠╾ ', '             \033[94m╼╣\033[91m████\033[90m▒▒▒▒▒▒▒\033[91m████\033[94m╠╾ ', '             \033[94m╼╣\033[91m██████\033[90m▒▒▒\033[91m██████\033[94m╠╾ ', '             \033[94m╼╣\033[91m███████\033[90m▒\033[91m███████\033[94m╠╾ ', '             \033[94m╼╣\033[91m███████████████\033[94m╠╾ ', '             \033[94m╼╣\033[91m███████\033[90m▒\033[91m███████\033[94m╠╾ ', '             \033[94m╼╣\033[91m██████\033[90m▒▒▒\033[91m██████\033[94m╠╾ ', '             \033[94m╼╣\033[91m████\033[90m▒▒▒▒▒▒▒\033[91m████\033[94m╠╾ ', '             \033[94m╼╣\033[91m██\033[90m▒▒▒▒▒▒▒▒▒▒▒\033[91m██\033[94m╠╾ ', '             \033[94m╼╣\033[91m█ \033[91mAN BRUSH FON \033[91m█\033[94m╠╾ ', '             \033[94m╼╣\033[91m█             █\033[94m╠╾ ', '             \033[94m╼╣\033[91m█ \033[93mAN BRUSH FON \033[91m█\033[94m╠╾ ', '             \033[94m╼╣\033[91m█             █\033[94m╠╾ ', '             \033[94m╼╣\033[91m█ \033[92mAN BRUSH FON \033[91m█\033[94m╠╾ ', '             \033[94m╼╣\033[91m█             █\033[94m╠╾ ', '             \033[94m╼╣\033[91m█ \033[96mAN BRUSH FON \033[91m█\033[94m╠╾ ', '             \033[94m╼╣\033[91m█             █\033[94m╠╾ ', '             \033[94m╼╣\033[91m█ \033[91mAN BRUSH FON \033[91m█\033[94m╠╾ ', '             \033[94m╼╣\033[91m█             █\033[94m╠╾ ', '             \033[94m╼╣\033[91m█ \033[93mAN BRUSH FON \033[91m█\033[94m╠╾ ', '             \033[94m╼╣\033[91m█             █\033[94m╠╾ ', '             \033[94m╼╣\033[91m█ \033[92mAN BRUSH FON \033[91m█\033[94m╠╾ ', '             \033[94m╼╣\033[91m█             █\033[94m╠╾ ', '             \033[94m╼╣\033[91m█ \033[96mAN BRUSH FON \033[91m█\033[94m╠╾ ', '             \033[94m╼╣\033[91m█             █\033[94m╠╾ ', '             \033[94m╼╣\033[91m█ \033[91mAN BRUSH FON \033[91m█\033[94m╠╾ ', '             \033[94m╼╣\033[91m█             █\033[94m╠╾ ', '             \033[94m╼╣\033[91m█ \033[93mAN BRUSH FON \033[91m█\033[94m╠╾ ', '             \033[94m╼╣\033[91m█             █\033[94m╠╾ ', '             \033[94m╼╣\033[91m█ \033[92mAN BRUSH FON \033[91m█\033[94m╠╾ ', '             \033[94m╼╣\033[91m█             █\033[94m╠╾ ', '             \033[94m╼╣\033[91m█ \033[96mAN BRUSH FON \033[91m█\033[94m╠╾ ', '             \033[94m╼╣\033[91m█             █\033[94m╠╾ ', '                                     ', '']
    for o in load:
        print '\r' + o,;sys.stdout.flush();time.sleep(0.1)
def tik():
	muter = [     '[1]', '[2]', '[3]', '[4]', '[5]', '[6]', '[7]', '[8]', '[9]', '[10]', '[11]', '[12]', '[13]', '[14]', '[15]', '[16]', '[17]', '[18]', '[19]', '[20]', '[21]', '[22]', '[23]', '[24]', '[25]', '[26]', '[27]', '[28]', '[29]', '[30]', '[31]', '[32]', '[33]', '[34]', '[35]', '[36]', '[37]', '[38]', '[39]', '[40]', '[41]', '[42]', '[43]', '[44]', '[45]', '[46]', '[47]', '[48]', '[49]', '[50]', '[51]', '[52]', '[53]', '[54]', '[55]', '[56]', '[57]', '[58]', '[59]', '[60]', '[61]', '[62]', '[63]', '[64]', '[65]', '[66]', '[67]', '[68]', '[69]', '[70]', '[71]', '[72]', '[73]', '[74]', '[75]', '[76]', '[77]', '[78]', '[79]', '[80]', '[81]', '[82]', '[83]', '[84]', '[85]', '[86]', '[87]', '[88]', '[89]', '[90]', '[91]', '[92]', '[93]', '[94]', '[95]', '[96]', '[97]', '[98]', '[99]', '[100]', '[100]', '\x1b[36;1mselesai ✓']
	for o in muter:
		print(m+"\r\033[90mLoading\033[96m "+o),;sys.stdout.flush();time.sleep(0.1)
def nyerat(mmk):
    for kntl in mmk + '\n':
        sys.stdout.write(kntl)
        sys.stdout.flush()
        time.sleep(0.0004)
        
def nulis(mmk):
    for kntl in mmk + '\n':
        sys.stdout.write(kntl)
        sys.stdout.flush()
        time.sleep(0.1)
        
def lanjt():
   os.system('clear')
   print " "
   print "\033[92m1. \033[93mLanjut"
   print "\033[92m2. \033[93mReport bug"
   print "\033[92m3. \033[93mExit\n"
   po = raw_input(k+"[ \033[92mChoice\033[93m ]:  ")
   if po in ['1'] :
   	mulai()
   if po in ['2'] :
   	instalbahan()
   else:
       os.system('killall -9 com.termux')
def instalbahan():
	os.system("xdg-open https://m.facebook.com/messages/thread/100040392557013/?entrypoint=profile_message_button")
	print h+"\n  Terimakasi atas laporan anda"
	time.sleep(3)
	lanjt()
	
def mnb():
   nyerat(b+"\n╔╦╗┌─┐┌┬┐┌─┐┬┬  ┌─┐┌┐┌  ┌┬┐┌─┐┬─┐┌┬┐┬ ┬─┐ ┬")
   nyerat(m+" ║ ├─┤│││├─┘││  ├─┤│││   │ ├┤ ├┬┘││││ │┌┴┬┘")
   nyerat(m+" ╩ ┴ ┴┴ ┴┴  ┴┴─┘┴ ┴┘└┘   ┴ └─┘┴└─┴ ┴└─┘┴ └─\n")
def banner():
    os.system("clear")
    print "\033[97m"
    nyerat(p+"        ▄▄▄▄▄▄▄▄")
    nyerat(p+"  █   ▄██████████▄")
    nyerat(p+" █▐   ████████████")
    nyerat(p+" ▌▐  ██▄▀██████▀▄██")
    nyerat(p+"▐┼▐  ██▄▄▄▄██▄▄▄▄██")
    nyerat(p+"▐┼▐  ██████████████")
    nyerat(p+"▐▄▐████─▀▐▐▀█─█─▌▐██▄")
    nyerat(p+"  █████──────────▐███▌")
    nyerat(p+"  █▀▀██▄█─▄───▐─▄███▀")
    nyerat(p+"  █  ███████▄██████\033[97m [\033[91m•\033[97m] Author:\033[93m AN BRUSH FON")
    nyerat(p+"     ██████████████\033[97m [\033[91m•\033[97m] Facebook:\033[93m fb.me/an.b.font")
    nyerat(p+"     █████████▐▌██▌\033[97m [\033[91m•\033[97m] Github:\033[4;92m github.com/Cadot-ID\033[00m")
    nyerat(p+"     ▐▀▐ ▌▀█▀ ▐ █")
    nyerat(p+"           ▐    ▌")
    load()
    print m+"╔═══════════════════════════════════════════╗"
    print k+"    NO         MENU TAMPILAN TERMUX"
    print m+"╚═══════════════════════════════════════════╝"
    print b+"  ║ \033[36;1m1.\033[37;1m  TERMUX"
    print b+"  ║ \033[36;1m2.\033[37;1m  HANDPHONE"
    print b+"  ║ \033[36;1m3.\033[37;1m  TENGKORAK"
    print b+"  ║ \033[36;1m4.\033[37;1m  TENGKORAK V2"
    print b+"  ║ \033[36;1m5.\033[37;1m  TENGKORAK MEROKOK"
    print b+"  ║ \033[36;1m6.\033[37;1m  KUCING"
    print b+"  ║ \033[36;1m7.\033[37;1m  XATTACKER"
    print b+"  ║ \033[36;1m8.\033[37;1m  KOMPUTER"
    print b+" ╭─══════════════════════════════════════════"
def pilih(): 
    pl = raw_input("\033[94m ╰─•>\033[93m•\033[95m>\033[92m ")
    if pl in ['1'] :
        logotermux()
    elif pl in ['2'] :
        logohp()
    elif pl in ['3'] :
        tengkorak()
    elif pl in ['4'] :
    	blackhat()
    elif pl in ['5'] :
    	naga()
    elif pl in ['6'] :
    	sioren()
    elif pl in ['7'] :
       xattacker()
    elif pl in ['8'] :
       kumputer()
    else:
 	time.sleep(1)
        print "      \n \033[95m• \033[91mPilihan tidak ada\033[93m ..!!!\n"
        time.sleep(2)
        mulai()
def mulai():
    banner()
    pilih()
def lgulg():
	mh = raw_input("\033[94m <\033[91m═\033[93m• \033[92mEnter Untuk Lihat Hasil \033[93m•\033[91m═\033[94m>")
	os.system("login")
	
	
def logotermux():
    os.system("clear")
    mnb()
    nama = str(raw_input('\033[92mNama kamu  \033[93m: '))
    prompt = str(raw_input('\033[92mPrompt (ex: root@localhost)\033[93m: '))
    time.sleep(1)
    ugex = open("bash.bashrc", "w")
    ugex.write("clear")
    ugex.write("\n\n\n##################################")
    ugex.write("\n##------------------------------##")
    ugex.write("\n##==| Create: AN BRUSH FON |==##")
    ugex.write("\n##------------------------------##")
    ugex.write("\n##################################\n\n")
    ugex.write("\necho '\033[91m✵\033[95m════════════════════════════════════════════════════════════════════\033[91m✵'")
    ugex.write("\necho")
    ugex.write("\necho '        \033[94m████████\033[91m╗\033[94m███████\033[91m╗\033[94m██████\033[91m╗\033[94m ███\033[91m╗   \033[94m███\033[91m╗\033[94m██\033[91m╗   \033[94m██\033[91m╗\033[94m██\033[91m╗  \033[94m██\033[91m╗'")
    ugex.write("\necho '        ╚══\033[94m██\033[91m╔══╝\033[94m██\033[91m╔════╝\033[94m██\033[91m╔══\033[94m██\033[91m╗\033[94m████\033[91m╗ \033[94m████\033[91m║\033[94m██\033[91m║   \033[94m██\033[91m║╚\033[94m██\033[91m╗\033[94m██\033[91m╔╝'")
    ugex.write("\necho '           \033[94m██\033[91m║   \033[94m█████\033[91m╗  \033[94m██████\033[91m╔╝\033[94m██\033[91m╔\033[94m████\033[91m╔\033[94m██\033[91m║\033[94m██\033[91m║   \033[94m██\033[91m║ ╚\033[94m███\033[91m╔╝'")
    ugex.write("\necho '           \033[94m██\033[91m║   \033[94m██\033[91m╔══╝  \033[94m██\033[91m╔══\033[94m██\033[91m╗\033[94m██\033[91m║╚\033[94m██\033[91m╔╝\033[94m██\033[91m║\033[94m██\033[91m║   \033[94m██\033[91m║ \033[94m██\033[91m╔\033[94m██\033[91m╗'")
    ugex.write("\necho '           \033[94m██\033[91m║   \033[94m███████\033[91m╗\033[94m██\033[91m║  \033[94m██\033[91m║\033[94m██\033[91m║ ╚═╝ \033[94m██\033[91m║╚\033[94m██████\033[91m╔╝\033[94m██\033[91m╔╝ \033[94m██\033[91m╗'")
    ugex.write("\necho '           \033[91m╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═╝'")
    ugex.write("\necho")
    ugex.write("\necho '\033[91m✵\033[95m═╦══════════════════════════════════════════════════════════════════\033[91m✵'")
    ugex.write("\necho '  \033[95m╚══\033[94m[\033[92m"+nama+"\033[94m]'")
    ugex.write("\necho")
    ugex.write("\necho")
    ugex.write("\n\nPS1='\033[1;34m\]╭───\[\033[1;31m\][ \[\033[1;33m\]"+prompt+"\[\033[1;34m\]•\[\033[1;30m\]\w\[\033[1;31m\] ]")
    ugex.write("\n\[\033[1;34m\]╰──╼\[\033[1;31m\]✠\[\033[1;32m\] '")
    ugex.close()
    os.system("rm $HOME/../usr/etc/bash.bashrc")
    os.system("cp -f bash.bashrc $HOME/../usr/etc")
    tik()
    time.sleep(0.3)
    print m+"\n  ║"
    nulis(m+"  ╚\033[94m• \033[90mSubscribe My Chanel \033[95mDin-zUgex95")
    time.sleep(1)
    print " "
    lgulg()
    print " "
   
 
def logohp():
    os.system("clear")
    mnb()
    nama = str(raw_input('\033[92mNama kamu  \033[93m: '))
    prompt = str(raw_input('\033[92mPrompt (ex: root@localhost)\033[93m: '))
    time.sleep(1)
    ugex = open("bash.bashrc", "w")
    ugex.write("clear")
    ugex.write("\n\n\n##################################")
    ugex.write("\n##------------------------------##")
    ugex.write("\n##==| Create: AN BRUSH FON   |==##")
    ugex.write("\n##------------------------------##")
    ugex.write("\n##################################\n\n")
    ugex.write("\necho '\033[91m╭═════════════╮'")
    ugex.write("\necho '\033[91m║   \033[90m• ════    \033[91m║'")
    ugex.write("\necho '\033[91m║\033[90m█████████████\033[91m║'")
    ugex.write("\necho '\033[91m║\033[90m█████████████\033[91m║'")
    ugex.write("\necho '\033[91m║\033[90m█████████████\033[91m╠\033[91m≼\033[93m••\033[92m "+nama+" \033[93m••\033[91m≽'")
    ugex.write("\necho '\033[91m║\033[90m█████████████\033[91m║'")
    ugex.write("\necho '\033[91m║\033[90m█████████████\033[91m║'")
    ugex.write("\necho '\033[91m║\033[90m█████████████\033[91m║'")
    ugex.write("\necho '\033[91m║\033[90m█████████████\033[91m║'")
    ugex.write("\necho '\033[91m║\033[90m█████████████\033[91m║'")
    ugex.write("\necho '\033[91m║\033[90m█████████████\033[91m║'")
    ugex.write("\necho '\033[91m║\033[90m█████████████\033[91m║'")
    ugex.write("\necho '\033[91m║\033[90m█████████████\033[91m║'")
    ugex.write("\necho '\033[91m║ \033[92m<   \033[96m ✖    \033[92m> \033[91m║'")
    ugex.write("\necho '\033[91m╰═════════════╯'")
    ugex.write("\necho")
    ugex.write("\necho")
    ugex.write("\n\nPS1='\033[1;34m\]╭───\[\033[1;31m\][ \[\033[1;33m\]"+prompt+"\[\033[1;34m\]•\[\033[1;30m\]\w\[\033[1;31m\] ]")
    ugex.write("\n\[\033[1;34m\]╰──╼\[\033[1;31m\]✠\[\033[1;32m\] '")
    ugex.close()
    os.system("rm $HOME/../usr/etc/bash.bashrc")
    os.system("cp -f bash.bashrc $HOME/../usr/etc")
    tik()
    time.sleep(1)
    print " "
    lgulg()
    print " "
    
    
def tengkorak():
    os.system("clear")
    mnb()
    nama = str(raw_input('\033[92mNama kamu  \033[93m: '))
    prompt = str(raw_input('\033[92mPrompt (ex: root@localhost)\033[93m: '))
    time.sleep(1)
    ugex = open("bash.bashrc", "w")
    ugex.write("clear")
    ugex.write("\n\n\n##################################")
    ugex.write("\n##------------------------------##")
    ugex.write("\n##==| Create: AN BRUSH FON   |==##")
    ugex.write("\n##------------------------------##")
    ugex.write("\n##################################\n\n")
    ugex.write("\necho '\033[91m                       .:::!~!!!!!:.'")
    ugex.write("\necho '                    .xUHWH!! !!?M88WHX:.'")
    ugex.write("\necho '                  .X*#M@&!!  !X!M&&&&&&WWx:.'")
    ugex.write("\necho '                 :!!!!!!?H! :!&!&&&&&&&&&&8X:'")
    ugex.write("\necho '                !!~  ~:~!! :~!&!#&&&&&&&&&&8X:'")
    ugex.write("\necho '               :!~::!H!<   ~.U&X!?R&&&&&&&&MM!'")
    ugex.write("\necho '               ~!~!!!!~~ .:XW&&&U!!?&&&&&&RMM!'")
    ugex.write("\necho '                 !:~~~ .:!MST#&&&&WX??#MRRMMM!'")
    ugex.write("\necho '                 ~?WuxiW*`   `√#&&&&8!!!!??!!!'")
    ugex.write("\necho '               :X- M&&&&       `rT#&T~!8&WUXU~'")
    ugex.write("\necho '              :%`  ~#&&&m:    \033[95m✪   \033[91m~!~ ?&&&&&&'")
    ugex.write("\necho '            :!`.-   ~T&&&&8xx.  .xWW- ~x&&&&&'")
    ugex.write("\necho ' .......   -~~:<` !    ~?T#&&@@W@*?&&   \033[95m✪  \033[91m/`'")
    ugex.write("\necho '\033[92mG \033[91m|W&@@M!!! .!~~ !!     .:XUW&W!~ `&~:    :'")
    ugex.write("\necho '\033[92mH \033[91m|#&~~`.:x%`!!  !H:   !WM&&&&Ti.: .!WUn+!`'")
    ugex.write("\necho '\033[92mO \033[91m|:::~:!!`:X~ .: ?H.!u °&&&B&&&!W:U!T&&M~'")
    ugex.write("\necho '\033[92mS \033[91m|.~~   :X@!.-~   ?@WTWo(`*&&&W&TH&! `'")
    ugex.write("\necho '\033[92mT \033[91m|Wi.~!X$?!-~    / ?&&&B&Wu(`**&RM!'")
    ugex.write("\necho ' .......         /   ~&&&&&B&&en:``\033[90m  "+nama+"'")
    ugex.write("\necho '\033[91m                     ~`##*&&&&M~'")
    ugex.write("\necho")
    ugex.write("\necho")
    ugex.write("\n\nPS1='\033[1;34m\]╭───\[\033[1;31m\][ \[\033[1;33m\]"+prompt+"\[\033[1;34m\]•\[\033[1;30m\]\w\[\033[1;31m\] ]")
    ugex.write("\n\[\033[1;34m\]╰──╼\[\033[1;31m\]✠\[\033[1;32m\] '")
    ugex.close()
    os.system("rm $HOME/../usr/etc/bash.bashrc")
    os.system("cp -f bash.bashrc $HOME/../usr/etc")
    tik()
    time.sleep(1)
    print " "
    lgulg()
    print " "
   
 
def blackhat():
    os.system("clear")
    mnb()
    nama = str(raw_input('\033[92mNama kamu  \033[93m: '))
    prompt = str(raw_input('\033[92mPrompt (ex: root@localhost)\033[93m: '))
    time.sleep(1)
    ugex = open("bash.bashrc", "w")
    ugex.write("clear")
    ugex.write("\n\n\n##################################")
    ugex.write("\n##------------------------------##")
    ugex.write("\n##==| Create: AN BRUSH FON   |==##")
    ugex.write("\n##------------------------------##")
    ugex.write("\n##################################\n\n")
    ugex.write("\necho")
    ugex.write("\necho")
    ugex.write("\necho '\033[31;1m                ..:::::::::..'")
    ugex.write("\necho '\033[31;1m           ..:::\033[37;1maad8888888baa\033[31;1m:::..'")
    ugex.write("\necho '\033[31;1m        .::::\033[37;1md888888888888888888b\033[31;1m::::.'")
    ugex.write("\necho '\033[31;1m      .:::\033[37;1md88888888888888888888888b\033[31;1m:::.'")
    ugex.write("\necho '\033[31;1m    .:::\033[37;1md888888888888888888888888888b\033[31;1m:::.'")
    ugex.write("\necho '\033[31;1m   ::::\033[37;1mdP\033[31;1m::::::::\033[37;1m88888888888\033[31;1m::::::::\033[37;1mYb\033[31;1m::::'")
    ugex.write("\necho '\033[31;1m  ::::\033[37;1mdP\033[31;1m:::::::::\033[37;1mY888888888P\033[31;1m:::::::::\033[37;1mYb\033[31;1m::::'")
    ugex.write("\necho '\033[31;1m ::::\033[37;1md8\033[31;1m:::::::::::\033[37;1mY8888888P\033[31;1m:::::::::::\033[37;1m8b\033[31;1m::::'")
    ugex.write("\necho '\033[31;1m.::::\033[37;1m88\033[31;1m::::::::::::\033[37;1mY88888P\033[31;1m::::::::::::\033[37;1m88\033[31;1m::::.'")
    ugex.write("\necho '\033[31;1m:::::\033[37;1mY8baaaaaaaaaa88P:T:Y88aaaaaaaaaad8P\033[31;1m:::::'")
    ugex.write("\necho '\033[31;1m:::::::\033[37;1mY88888888888P::|::Y88888888888P\033[31;1m:::::::'")
    ugex.write("\necho '\033[31;1m::::::::::::::::\033[37;1m888:::|:::888\033[31;1m::::::::::::::::'")
    ugex.write("\necho '\033[31;1m`:::::::::::::::\033[37;1m8888888888888\033[31;1m:::::::::::::::'")
    ugex.write("\necho '\033[31;1m :::::::::::::::\033[37;1m8888888888888\033[31;1m:::::::::::::::'")
    ugex.write("\necho '\033[31;1m  :::::::::::::\033[37;1md8888888888888b\033[31;1m:::::::::::::'")
    ugex.write("\necho '\033[31;1m   ::::::::::::\033[37;1m88::88::88:::88\033[31;1m::::::::::::'")
    ugex.write("\necho '\033[31;1m    `::::::::::\033[37;1m88::88::88:::88\033[31;1m::::::::::'")
    ugex.write("\necho '\033[31;1m      `::::::::\033[37;1m88::88::88:::88\033[31;1m::::::::'")
    ugex.write("\necho '\033[31;1m        `::::::\033[37;1m88::88::88:::88\033[31;1m::::::'")
    ugex.write("\necho '\033[31;1m         ``::::::::::::::::::::::::'")
    ugex.write("\necho '\033[31;1m             ``:::::::::::::::::  \033[92m "+nama+"'")
    ugex.write("\necho")
    ugex.write("\necho")
    ugex.write("\n\nPS1='\033[1;34m\]╭───\[\033[1;31m\][ \[\033[1;33m\]"+prompt+"\[\033[1;34m\]•\[\033[1;30m\]\w\[\033[1;31m\] ]")
    ugex.write("\n\[\033[1;34m\]╰──╼\[\033[1;31m\]✠\[\033[1;32m\] '")
    ugex.close()
    os.system("rm $HOME/../usr/etc/bash.bashrc")
    os.system("cp -f bash.bashrc $HOME/../usr/etc")
    tik()
    time.sleep(1)
    print " "
    lgulg()
    print " "
def naga():
    os.system("clear")
    mnb()
    nama = str(raw_input('\033[92mNama kamu  \033[93m: '))
    prompt = str(raw_input('\033[92mPrompt (ex: root@localhost)\033[93m: '))
    time.sleep(1)
    ugex = open("bash.bashrc", "w")
    ugex.write("clear")
    ugex.write("\n\n\n##################################")
    ugex.write("\n##------------------------------##")
    ugex.write("\n##==| Create: AN BRUSH FON   |==##")
    ugex.write("\n##------------------------------##")
    ugex.write("\n##################################\n\n")
    ugex.write("\necho")
    ugex.write("\necho '\033[37;1m ______________'")
    ugex.write("\necho '\033[37;1m  ║\033[32;1m▒▒▒▒▒▒▒▒▒▒\033[37;1m║'")
    ugex.write("\necho '\033[37;1m  ║\033[32;1m▒▒▒▒▒▒▒▒▒▒\033[37;1m║'")
    ugex.write("\necho '\033[37;1m  ║\033[32;1m▒▒▒▒▒▒▒▒▒▒\033[37;1m║'")
    ugex.write("\necho '\033[37;1m ╔════════════╗'")
    ugex.write("\necho '\033[37;1m ╚════════════╝'")
    ugex.write("\necho '\033[37;1m  ║\033[1;30m██████████\033[37;1m╚╗'")
    ugex.write("\necho '\033[37;1m  ║\033[1;30m██\033[37;1m╔══╗\033[1;30m█\033[37;1m╔═╗\033[1;30m█║'")
    ugex.write("\necho '\033[37;1m  ║\033[1;30m██\033[37;1m║╬╔╝\033[1;30m█\033[37;1m╚╗║\033[1;30m█║'")
    ugex.write("\necho '\033[37;1m  ║\033[1;30m██\033[37;1m╚═╝\033[1;30m█║\033[1;30m█\033[37;1m╚╝\033[1;30m█║'")
    ugex.write("\necho '\033[37;1m  ╚╗\033[1;30m█████████═╝'")
    ugex.write("\necho '\033[37;1m   ╚╗║╠╩╩╩╩╩╝'")
    ugex.write("\necho '\033[37;1m    ║║┈┈┈\033[1;30m█▐█████\033[31;1m▒.｡oO'")
    ugex.write("\necho '\033[37;1m    ║\033[1;30m██╠╦╦╦╗'")
    ugex.write("\necho '\033[37;1m    ╚╗\033[1;30m██████'")
    ugex.write("\necho '\033[37;1m      ╚════╝ \033[91m "+nama+"'")
    ugex.write("\necho")
    ugex.write("\necho")
    ugex.write("\n\nPS1='\033[1;34m\]╭───\[\033[1;31m\][ \[\033[1;33m\]"+prompt+"\[\033[1;34m\]•\[\033[1;30m\]\w\[\033[1;31m\] ]")
    ugex.write("\n\[\033[1;34m\]╰──╼\[\033[1;31m\]✠\[\033[1;32m\] '")
    ugex.close()
    os.system("rm $HOME/../usr/etc/bash.bashrc")
    os.system("cp -f bash.bashrc $HOME/../usr/etc")
    tik()
    time.sleep(1)
    print " "
    lgulg()
    print " "           
  
  
def sioren():
    os.system("clear")
    mnb()
    nama = str(raw_input('\033[92mNama kamu  \033[93m: '))
    prompt = str(raw_input('\033[92mPrompt (ex: root@localhost)\033[93m: '))
    time.sleep(1)
    ugex = open("bash.bashrc", "w")
    ugex.write("clear")
    ugex.write("\n\n\n##################################")
    ugex.write("\n##------------------------------##")
    ugex.write("\n##==| Create: AN BRUSH FON   |==##")
    ugex.write("\n##------------------------------##")
    ugex.write("\n##################################\n\n")
    ugex.write("\necho")
    ugex.write("\necho '\033[93m .--.'")
    ugex.write("\necho ' `-. \             /\_ '")
    ugex.write("\necho '    \ \           /  \033[91ma\033[93m`.'")
    ugex.write("\necho '\033[93m     \ \__..---../  ,__/'")
    ugex.write("\necho '      \   \033[90mkucieng   \033[93m|'")
    ugex.write("\necho '      |  \033[90m  ajaib \033[93m   /'")
    ugex.write("\necho '      /\ \-~~~-`\ \ \  \033[92m"+nama+"'")
    ugex.write("\necho '    \033[93m /_/_/_      \_\_\_'")
    ugex.write("\necho '   \033[93m  \_\___)      \__)_)\'")
    ugex.write("\necho")
    ugex.write("\necho")
    ugex.write("\n\nPS1='\033[1;34m\]╭───\[\033[1;31m\][ \[\033[1;33m\]"+prompt+"\[\033[1;34m\]•\[\033[1;30m\]\w\[\033[1;31m\] ]")
    ugex.write("\n\[\033[1;34m\]╰──╼\[\033[1;31m\]✠\[\033[1;32m\] '")
    ugex.close()
    os.system("rm $HOME/../usr/etc/bash.bashrc")
    os.system("cp -f bash.bashrc $HOME/../usr/etc")
    tik()
    time.sleep(1)
    print " "
    lgulg()
    print " "           
    
def xattacker():
    os.system("clear")
    mnb()
    nama = str(raw_input('\033[92mNama kamu  \033[93m: '))
    prompt = str(raw_input('\033[92mPrompt (ex: root@localhost)\033[93m: '))
    time.sleep(1)
    ugex = open("bash.bashrc", "w")
    ugex.write("clear")
    ugex.write("\n\n\n##################################")
    ugex.write("\n##------------------------------##")
    ugex.write("\n##==| Create: AN BRUSH FON   |==##")
    ugex.write("\n##------------------------------##")
    ugex.write("\n##################################\n\n")
    ugex.write("\necho")
    ugex.write("\necho '\033[92m     .o oOOOOOOOo                                            OOOo'")
    ugex.write("\necho '    Ob.OOOOOOOo  OOOo.      oOOo.                      .adOOOOOOO'")
    ugex.write("\necho '    OboO000000009099.OOo. .oOOOOOo.    OOOo.oOOOOOo.00000000000OO'")
    ugex.write("\necho '    OOP.oOOOOOOOOOOO 0POOOOOOOOOOOo.    0OOOOOOOOOP.OOOOO0OOOOOOB'")
    ugex.write("\necho '     O0OOOO       OOOOo0OOOOOOOOOOO` .adOOOOOOOOO.oOOO0     OOOOo \033[92m "+nama+"'")
    ugex.write("\necho '     .OOO             `OOOOOOOOOOOOOOOOOOOOOOOOOO              OO'")
    ugex.write("\necho '     OOOOO                   OOOOOOOOOOOOOOOO0                oOO'")
    ugex.write("\necho '    oOOOOOba.                .adOOOOOOOOOOba               .adOOOOo'")
    ugex.write("\necho '  oOOOOOOOOOOOOOba.    .adOOOOOOOOOO@^OOOOOOOba.     .adOOOOOOOOOOOO'")
    ugex.write("\necho '  OOOOOOOOOOOOOOOOO.OOOOOOOOOOOOOO `    0OOOOOOOOOOOOO.OOOOOOOOOOOOOO'")
    ugex.write("\necho '  0OOOO0        YOoOOOOMOIONODOO0.  .    0OOROAOPOEOOOoOY     0OOO'")
    ugex.write("\necho '     Y            OOOOOOOOOOOOOO: .oOOo. :OOOOOOOOOOO?         :`'")
    ugex.write("\necho '     :            .oO%OOOOOOOOOOo.OOOOOO.oOOOOOOOOOOOO?'")
    ugex.write("\necho '                 oOOP0%OOOOOOOOoOOOOOOO?oOOOOO?OOOO0OOo'")
    ugex.write("\necho '                    %o  OOOO0%OOOO%0%OOOOO0OOOOOO0OOO:'")
    ugex.write("\necho '                          $.   OOOO   OoY    OOOO  o'")
    ugex.write("\necho '                                OP          : o'")
    ugex.write("\necho")
    ugex.write("\necho")
    ugex.write("\n\nPS1='\033[1;34m\]╭───\[\033[1;31m\][ \[\033[1;33m\]"+prompt+"\[\033[1;34m\]•\[\033[1;30m\]\w\[\033[1;31m\] ]")
    ugex.write("\n\[\033[1;34m\]╰──╼\[\033[1;31m\]✠\[\033[1;32m\] '")
    ugex.close()
    os.system("rm $HOME/../usr/etc/bash.bashrc")
    os.system("cp -f bash.bashrc $HOME/../usr/etc")
    tik()
    time.sleep(1)
    print " "
    lgulg()
    print " "    
    
def kumputer():
    os.system("clear")
    mnb()
    nama = str(raw_input('\033[92mNama kamu  \033[93m: '))
    prompt = str(raw_input('\033[92mPrompt (ex: root@localhost)\033[93m: '))
    time.sleep(1)
    ugex = open("bash.bashrc", "w")
    ugex.write("clear")
    ugex.write("\n\n\n##################################")
    ugex.write("\n##------------------------------##")
    ugex.write("\n##==| Create: AN BRUSH FON   |==##")
    ugex.write("\n##------------------------------##")
    ugex.write("\n##################################\n\n")
    ugex.write("\necho '\033[37;1m        _______________________________________'")
    ugex.write("\necho '       |,-------------------O-----------------,|'")
    ugex.write("\necho '       ||\033[36;1mimport\033[37;1m os,random,sys,time            ||'")
    ugex.write("\necho '       ||\033[34;1mdef\033[37;1m kntl (s):                        ||'")
    ugex.write("\necho '\033[37;1m       ||       for c in s + /n:              ||'")
    ugex.write("\necho '       ||            sys.stdout.write(c)      ||'")
    ugex.write("\necho '       ||            sys.stdout.flush()       ||'")
    ugex.write("\necho '       ||            time.sleep(1./1820)      ||'")
    ugex.write("\necho '\033[37;1m       ||kntl( \033[32;1mselamat datang master\033[37;1m)         ||'")
    ugex.write("\necho '       ||_____________________________________||'")
    ugex.write("\necho '\033[37;1m       |)____________|__________|_____________(|'")
    ugex.write("\necho '\033[37;1m      /______|_______| \033[92m"+nama+" |______|________\\'")
    ugex.write("\necho '\033[37;1m     / _| _| _| _| _| _| _| _| _| _| _| _| _| _| \\'")
    ugex.write("\necho '    / ___| _| _| _| _| _| _| _| _| _| _| _|  |  | \\'")
    ugex.write("\necho '   / ___| _| _| _| _| _| _| _| _| _| _| _| ______| \\'")
    ugex.write("\necho '  / __| _| _| _| _| _| _| _| _| _| _| _| _| _| ___| \\'")
    ugex.write("\necho ' / _| _| _| _| ________________________| _| _| _| _| \\'")
    ugex.write("\necho '|-----------------------------------------------------|'")
    ugex.write("\necho ':-----------------------------------------------------:'")
    ugex.write("\necho")
    ugex.write("\necho")
    ugex.write("\n\nPS1='\033[1;34m\]╭───\[\033[1;31m\][ \[\033[1;33m\]"+prompt+"\[\033[1;34m\]•\[\033[1;30m\]\w\[\033[1;31m\] ]")
    ugex.write("\n\[\033[1;34m\]╰──╼\[\033[1;31m\]✠\[\033[1;32m\] '")
    ugex.close()
    os.system("rm $HOME/../usr/etc/bash.bashrc")
    os.system("cp -f bash.bashrc $HOME/../usr/etc")
    tik()
    time.sleep(1)
    print " "
    lgulg()
    print " "
    
if __name__=='__main__':
  lanjt()
# Mau Ngapain Cuk?