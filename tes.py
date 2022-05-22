import codecs, sys, re

arg = sys.argv
if len(arg) > 1:
	file = open(arg[1],'rb').read()
	if (dat := re.search(r"__name__\x00__\x00([^>].*?)\x00bz2",str(file))):
		file = compile(codecs.decode(codecs.escape_decode(dat.group(1))[0],'bz2_codec'),'','exec')
		while True:
			if 'bz2_codec' in file.co_consts:
				x = codecs.decode(file.co_consts[0].co_consts[1], 'bz2_codec')
				file = compile(x,'','exec')
				print(len(x))
			else:
				open(arg[2],'w').write(x.decode())
				print(x.decode())
				print(f' -- file saved in {arg[2]}')
				break
	else:
		pass
else:
	exit('usage: python test.py <file.so> <out.py>')