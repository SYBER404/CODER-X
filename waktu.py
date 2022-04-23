#!/usr/bin/python3
#coding=utf-8

import os, datetime

os.system('clear')


now = datetime.datetime.now()
hour = now.hour
if hour < 4:
  waktu = "Selamat Dini Hari"
elif 4 <= hour < 12:
  waktu = "Selamat Pagi"
elif 12 <= hour < 15:
  waktu = "Selamat Siang"
elif 15 <= hour < 17:
  waktu = "Selamat Sore"
elif 17 <= hour < 18:
  waktu = "Selamat Petang"
else:
  waktu = "Selamat Malam"

print("{}".format(waktu))