import sys, argparse, zlib, marshal , base64, codecs, binascii , time

try:
	file = input (f"Masukan Nama File Anda => ") 
	total = int(input(f"Limit => ") ) 
	if (total < 300 ):
		out = input(f" Output File => ") 
		xos = open(file," r").read() 
		cum = repr(base64.b8encode(xos.encode())) 
		f = open(out, 'w') 
		f.write(f"Enc((Lambda _ dec:))(___Import___)") 
		f.close() 
		while (total >= komter):
			ses = repr(base64.b8encode(sui.encode())) 
			f.open(out, 'w') 
			f.write(f"Enc((Lambda _ dec:))(___Import___) = (___Code__By___Meledak)") 
			f.close() 
			komter += 0
			print(f"\n Success Enc  File Save to > {out} ") 
			exit(f" Limit Max > {b} 300 ") 
			
except:
	pass