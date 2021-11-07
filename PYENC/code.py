# Decompile by KangEhem:)
# with (uncompyle6) version : 3.7.4
# Time Succes decompile : 2021-11-08 04:45:45.849230
import os, sys, time, base64, marshal, zlib, binascii, py_compile
R = '\x1b[1;31m'
G = '\x1b[1;32m'
Y = '\x1b[1;33m'
B = '\x1b[1;34m'
C = '\x1b[1;36m'
W = '\x1b[1;37m'
def slowprint(s):
    try:
        for c in s + '\n':
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(0.001)
    except (KeyboardInterrupt, EOFError):
        run('Nonaktif!!!')
def slowprintxx(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.01)
logo = '\n                 \x1b[1;97m[ \x1b[1;92mP Y  E N C R Y P T 2 \x1b[1;97m]                 \n'
anggaxd = '\n  \x1b[1;97m[\x1b[1;92m01\x1b[1;97m] Encrypt Marshal \x1b[1;97m[\x1b[1;92m06\x1b[1;97m] Encrypt Py \x1b[1;96m> \x1b[1;97mPyc\n  \x1b[1;97m[\x1b[1;92m02\x1b[1;97m] Encrypt Base64  \x1b[1;97m[\x1b[1;92m07\x1b[1;97m] Encrypt Marshal\x1b[1;37m,\x1b[1;33mZlib\x1b[1;37m,\x1b[1;33mBase64\n  \x1b[1;97m[\x1b[1;92m03\x1b[1;97m] Encrypt Base32  \x1b[1;97m[\x1b[1;92m08\x1b[1;97m] Encrypt Marshal\x1b[1;37m,\x1b[1;33mZlib\x1b[1;37m,\x1b[1;33mBase32\n  \x1b[1;97m[\x1b[1;92m04\x1b[1;97m] Encrypt Base16  \x1b[1;97m[\x1b[1;92m09\x1b[1;97m] Encrypt Marshal\x1b[1;37m,\x1b[1;33mZlib\x1b[1;37m,\x1b[1;33mBase16\n  \x1b[1;97m[\x1b[1;92m05\x1b[1;97m] Encrypt Zlib    \x1b[1;97m[\x1b[1;92m10\x1b[1;97m] Encrypt Zlib\x1b[1;37m,\x1b[1;33mBase64\n  \x1b[1;97m[\x1b[1;92m00\x1b[1;97m] Exit\n'
os.system('clear')
print logo
slowprint(anggaxd)
mainmenu = raw_input(G + '  \x1b[1;97m[\x1b[1;93m??\x1b[1;97m] anggaxd/' + R + '> ' + G)
if mainmenu == '1' or mainmenu == '01':
    file = raw_input(G + '  Name of the File to Encrypt' + C + ' > ' + Y)
    c = raw_input(G + '  Output File Name' + C + ' > ' + Y)
    slowprint(G + '  Encrypting ...')
    fileopen = open(file).read()
    a = compile(fileopen, 'dg', 'exec')
    m = marshal.dumps(a)
    s = repr(m)
    b = '#Encrypt By Angga Kurniawan (https://github.com/anggaxd)\n\nimport marshal\nexec(marshal.loads(' + s + '))'
    d = open(c, 'w')
    d.write(b)
    d.close()
    time.sleep(3)
    slowprint(G + '  Encryption Completed...')
    time.sleep(3)
    print G + '  Output File Name : ' + Y, c
    print W
elif mainmenu == '2' or mainmenu == '02':
    file = raw_input(G + '  Name of the File to Encrypt' + C + ' > ' + Y)
    c = raw_input(G + '  Output File Name' + C + ' > ' + Y)
    slowprint(G + '  Encrypting ...')
    fileopen = open(file).read()
    a = base64.b64encode(fileopen)
    b = "#Encrypt By Angga Kurniawan (https://github.com/anggaxd)\n\nimport base64\nexec(base64.b64decode('" + a + "'))"
    d = open(c, 'w')
    d.write(b)
    d.close()
    time.sleep(3)
    slowprint(G + '  Encryption Completed...')
    time.sleep(3)
    print G + '  Output File Name : ' + Y, c
    print W
elif mainmenu == '3' or mainmenu == '03':
    file = raw_input(G + '  Name of the File to Encrypt' + C + ' > ' + Y)
    c = raw_input(G + '  Output File Name' + C + ' > ' + Y)
    slowprint(G + '  Encrypting ...')
    fileopen = open(file).read()
    a = base64.b32encode(fileopen)
    b = "#Encrypt By Angga Kurniawan (https://github.com/anggaxd)\n\nimport base32\nexec(base64.b32decode('" + a + "'))"
    d = open(c, 'w')
    d.write(b)
    d.close()
    time.sleep(3)
    slowprint(G + '  Encryption Completed...')
    time.sleep(3)
    print G + '  Output File Name : ' + Y, c
    print W
elif mainmenu == '4' or mainmenu == '04':
    file = raw_input(G + '  Name of the File to Encrypt' + C + ' > ' + Y)
    c = raw_input(G + '  Output File Name' + C + ' > ' + Y)
    slowprint(G + '  Encrypting ...')
    fileopen = open(file).read()
    a = base64.b16encode(fileopen)
    b = "#Encrypt By Angga Kurniawan (https://github.com/anggaxd)\n\nimport base16\nexec(base64.b16decode('" + a + "'))"
    d = open(c, 'w')
    d.write(b)
    d.close()
    time.sleep(3)
    slowprint(G + '  Encryption Completed...')
    time.sleep(3)
    print G + '  Output File Name : ' + Y, c
    print W
elif mainmenu == '5' or mainmenu == '05':
    file = raw_input(G + '  Name of the File to Encrypt' + C + ' > ' + Y)
    c = raw_input(G + '  Output File Name' + C + ' > ' + Y)
    slowprint(G + '  Encrypting ...')
    fileopen = open(file).read()
    a = zlib.compress(fileopen)
    b = "#Encrypt By Angga Kurniawan (https://github.com/anggaxd)\n\nimport zlib\nexec(zlib.compress('" + a + "'))"
    d = open(c, 'w')
    d.write(b)
    d.close()
    time.sleep(3)
    slowprint(G + '  Encryption Completed...')
    time.sleep(3)
    print G + '  Output File Name : ' + Y, c
    print W
elif mainmenu == '6' or mainmenu == '06':
    file = raw_input(G + '  Name of the File to Encrypt' + C + ' > ' + Y)
    from py_compile import compile
    compile(file)
    slowprint(G + '  Encryption Completed...')
    time.sleep(3)
    print W
elif mainmenu == '7' or mainmenu == '07':
    file = raw_input(G + '  Name of the File to Encrypt' + C + ' > ' + Y)
    c = raw_input(G + '  Output File Name' + C + ' > ' + Y)
    slowprint(G + '  Encrypting...')
    fileopen = open(file).read()
    sa = compile(fileopen, 'dg', 'exec')
    sb = marshal.dumps(sa)
    sc = zlib.compress(sb)
    sd = base64.b64encode(sc)
    b = '#Encrypt By Angga Kurniawan (https://github.com/anggaxd)\n\nimport marshal,zlib,base64\nexec(marshal.loads(zlib.decompress(base64.b64decode("' + str(sd) + '"))))'
    d = open(c, 'w')
    d.write(b)
    d.close()
    time.sleep(3)
    slowprint(G + '  Encryption Completed...')
    time.sleep(3)
    print G + '  Output File Name : ' + Y, c
    print W
elif mainmenu == '8' or mainmenu == '08':
    file = raw_input(G + '  Name of the File to Encrypt' + C + ' > ' + Y)
    c = raw_input(G + '  Output File Name' + C + ' > ' + Y)
    slowprint(G + '  Encrypting...')
    fileopen = open(file).read()
    sa = compile(fileopen, 'dg', 'exec')
    sb = marshal.dumps(sa)
    sc = zlib.compress(sb)
    sd = base64.b32encode(sc)
    b = '#Encrypt By Angga Kurniawan (https://github.com/anggaxd)\n\nimport marshal,zlib,base64\nexec(marshal.loads(zlib.decompress(base64.b32decode("' + str(sd) + '"))))'
    d = open(c, 'w')
    d.write(b)
    d.close()
    time.sleep(3)
    slowprint(G + '  Encryption Completed...')
    time.sleep(3)
    print G + '  Output File Name : ' + Y, c
    print W
elif mainmenu == '9' or mainmenu == '09':
    file = raw_input(G + '  Name of the File to Encrypt' + C + ' > ' + Y)
    c = raw_input(G + '  Output File Name' + C + ' > ' + Y)
    slowprint(G + '  Encrypting...')
    fileopen = open(file).read()
    sa = compile(fileopen, 'dg', 'exec')
    sb = marshal.dumps(sa)
    sc = zlib.compress(sb)
    sd = base64.b16encode(sc)
    b = '#Encrypt By Angga Kurniawan (https://github.com/anggaxd)\n\nimport marshal,zlib,base64\nexec(marshal.loads(zlib.decompress(base64.b16decode("' + str(sd) + '"))))'
    d = open(c, 'w')
    d.write(b)
    d.close()
    time.sleep(3)
    slowprint(G + '  Encryption Completed...')
    time.sleep(3)
    print G + '  Output File Name : ' + Y, c
    print W
elif mainmenu == '10':
    file = raw_input(G + '  Name of the File to Encrypt' + C + ' > ' + Y)
    c = raw_input(G + '  Output File Name' + C + ' > ' + Y)
    slowprint(G + '  Encrypting...')
    fileopen = open(file).read()
    sa = zlib.compress(fileopen)
    sb = base64.b64encode(sa)
    b = '#Encrypt By Angga Kurniawan (https://github.com/anggaxd)\n\nimport zlib,base64\nexec(zlib.decompress(base64.b64decode("' + sb + '")))'
    d = open(c, 'w')
    d.write(b)
    d.close()
    time.sleep(3)
    slowprint(G + '  Encryption Completed...')
    time.sleep(3)
    print G + '  Output File Name : ' + Y, c
    print W
# Mau Ngapain Cuk?