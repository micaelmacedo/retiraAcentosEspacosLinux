 #!/usr/bin/env python
 # -*- encoding: utf-8 -*-
  
from os import rename
from os import listdir
import os
 
for root, dirs, files in os.walk('path'):
 for dir in dirs:
  arquivos = listdir(root +'/'+ dir)
  for arquivo in arquivos:
   rename(root +'/'+ dir + '/'+ arquivo, root +'/'+ dir + '/'+ arquivo.replace("�","a").replace("�","e").replace("�","i").replace("�","o").replace("�","u").replace("�","a").replace("�","c").replace(" ","_").replace(",","").replace("�","o"))
   print root +'/'+ dir + '/'+ arquivo.replace("�","a").replace("�","e").replace("�","i").replace("�","o").replace("�","u").replace("�","a").replace("�","c").replace(" ","_").replace(",","").replace("�","o");