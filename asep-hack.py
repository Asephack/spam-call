# KALO MAU MAKE PAKE AJA
# SCRIPT JANGAN DI UBAH
# HARGAI CREATHOR
# CAPE MEMBUAT SCRIPT MALAH DI RUSAK
# JADI JANGAN DI APA² YA SCRIPT INI
import requests
import time

#logo
print ('----------------------------')
print ('[•] AUTHOR : ASEP HACK      ')
print ('[•] TEAM   : MAFIA TEHNOLOGI')
print ('----------------------------')
print ('\n[+] Nomor di awali dengan 8xx ')

# run nomor
nomor = input('[+] Nomor target : ')
req=requests.get('https://ainxbot-sms.herokuapp.com/api/spamsms',params={'phone':nomor}).text
if 'terkirim' in req:
     print ('[√] succes terkirim')
else:
     print ('[!] spam gagal')