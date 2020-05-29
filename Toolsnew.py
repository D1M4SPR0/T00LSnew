import os
import sys
import time

os.system ('clear')
time.sleep(1)
os.system('figlet TOOLS')
time.sleep(2)
print "======================================="
print " Author  : Dimas"
print " FaceBok : Dimas Pro"
print " GitHub  : https://github.com/D1M4SPR0"
print "======================================="
print
time.sleep(2)
print "SELAMAT DATANG DI TOOLS INI JANGAN LUPA ADD FACEBOK ADMIN YG TERTERA DI ATAS DAN GUNAKAN TOOLS INI DENGAN BIJAK JIKA DI SALAH GUNAKAN ADMIN TIDAK AKAN BERTANGGUNG JAWAB:)"
print
time.sleep(5)
print "[+]Pilih:"
print "===================================================="
print
print "[1] Dark-Fb"
print
print "===================================================="
print
print "[2] MBF"
print
print "===================================================="
print
print "[3] SpamSms"
print
print "===================================================="
print
print "[4] install bahan"
print
print "===================================================="
print
print "[5] Keluar"
print
print "===================================================="
print
print "PILIH SALAH SATU TOOLS DI ATAS INI"
print
print "===================================================="
print
time.sleep(2)
pilih = raw_input('[?] pilih : ')
if pilih == "1":
      os.system('git clone https://github.com/B4N954N2-ID/DarkPremium')
      print "[+]Selanjutnya ketik $cd DarkPremium"
      time.sleep(3)
      print "[+]Selanjutnya ketik $python2 darkpremium.py"
elif pilih == "2":
        os.system('git clone https://github.com/pirmansx/mbf')
        time.sleep(4)
        print "[+]Selanjutnya ketik $cd mbf"
        time.sleep(3)
        print "[+]Selanjutnya ketik $python2 MBF.py"
elif pilih == "3":
        os.system('git clone https://github.com/AdeMara01/PrankSms')
        time.sleep(4)
        print "[+]Selanjutnya ketik $cd PrankSms"
        time.sleep(3)
        print "[+]Selanjutnya ketik $python2 PrankSms"
elif pilih == "4": 
        os.system('apt update && apt upgrade')
        os.system('pkg install nano')
        os.system('pkg install python2')                                      
        os.system('pkg install git')
        os.system('pip2 install requests mechanize')
        os.system('pip install requests mechanize')
        os.system('pkg install php')
        time.sleep(4)
        print "[+] Penginstallan Selesai [+]"
elif pilih == "5":
        time.sleep(7)
        print "[+]KELUAR"
