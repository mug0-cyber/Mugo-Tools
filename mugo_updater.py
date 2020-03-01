from urllib import request
from os import chdir
import zipfile

chdir("C:\\HACK")

con = request.urlopen("https://github.com/mug0-cyber/Mugo-Tools/raw/master/Update.zip?raw=true")
dosya = open("Update.zip", "wb")
dosya.write(con.read())
dosya.close()
con.close()

with zipfile.ZipFile("Update.zip", 'r') as zip_ref:
    zip_ref.extractall()

input("ENTER Basarak Uygulamadan Çıkış Yapa Bilirsiniz \n")