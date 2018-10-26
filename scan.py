#Jangan ganti author , hargai creator cape loh buat nya

import LIST
from LIST.id import *
from LIST.it import *
from LIST.jp import *
from LIST.us import *
import requests,re,os

b="\033[0;34m"
g="\033[1;32m"
w="\033[1;37m"
r="\033[1;31m"
y="\033[1;33m"


url = 'https://www.insecam.org/en/bycountry/ID/?page=1'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}



def main():
    os.system('clear')
    print (g+"|=|============================|=|")
    print (y+"         IPCam Scanner v1")
    print (y+"       Kancot Team - HVmbl3")
    print (y+"   https://github.com/kancotdiq")
    print (g+"|=|============================|=|")
    print ""
    print (r+"    [1] "+g+"Italy")
    print (r+"    [2] "+g+"Indonesia")
    print (r+"    [3] "+g+"Japan")
    print (r+"    [4] "+g+"United States")
    print (r+"    [5] "+g+"Keluar")
    print ""
    pilih = input(b+"Pilih "+r+": "+y)
    if pilih == 1:
        italy()
    elif pilih == 2:
        indonesia()
    elif pilih == 3:
        japan()
    elif pilih == 4:
        unitedstates()
    elif pilih == 5:
        print (r+"Keluar ..."+w)
        os.sys.exit()
    else:
        print (r+"Keluar ..."+w)
        os.sys.exit()
    
    
if __name__ == '__main__':
    main()
