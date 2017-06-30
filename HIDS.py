# -*- coding: utf-8 -*-
import os
import glob
import time
import getpass
import string
import shutil
import subprocess


def backupFirmas(): #Guardar firmas de los archivos binarios del sistema
    file = open('/home/hids/files.txt', 'r') #Abrir archivo con nombre de los binarios
    sign = open('/home/hids/sign.txt', 'a') 

    for line in file:
    #path = file.readline()
    	path  = line
    	firmaPath = os.popen("md5sum "+path).read()
    	firmaPath = firmaPath.replace("\n", "")
	sign.write(firmaPath+"\n")
    	#print firmaPath
    file.close()
    sign.close()



def compararBinarios():#comparar con firmas de binarios
    sign = open('/home/hids/sign.txt', 'r') 
    for line in sign:
        signANTERIOR = line[0:33] #Separa la firma del archivo
        pathARCHIVO = line[34:].replace("\n", "") #Separa el camino del archivo
        md5Result = os.popen("md5sum "+pathARCHIVO).read() #md5sum del archivo
        md5Result = md5Result[0:33]
        if md5Result == signANTERIOR:
            print("Firmas coinciden! Ninguna modficacion en el archivo "+ pathARCHIVO)
        else:
            print("ALERTA! Archivo "+pathARCHIVO+ " ha sido modificado!")
    sign.close()

compararBinarios()
#backupFirmas()
