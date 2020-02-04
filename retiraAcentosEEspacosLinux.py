 #!/usr/bin/env python
 # -*- encoding: utf-8 -*-
  
from os import rename
from os import listdir
import os
 
for root, dirs, files in os.walk('path'):
 for dir in dirs:
  arquivos = listdir(root +'/'+ dir)
  for arquivo in arquivos:
   rename(root +'/'+ dir + '/'+ arquivo, root +'/'+ dir + '/'+ arquivo.replace("á","a").replace("é","e").replace("í","i").replace("ó","o").replace("ú","u").replace("ã","a").replace("ç","c").replace(" ","_").replace(",","").replace("õ","o"))
   print root +'/'+ dir + '/'+ arquivo.replace("á","a").replace("é","e").replace("í","i").replace("ó","o").replace("ú","u").replace("ã","a").replace("ç","c").replace(" ","_").replace(",","").replace("õ","o");