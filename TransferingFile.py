from ftplib import FTP
import fileinput
import os
import glob
import shutil

ftp = FTP('ftp.dlptest.com' , 'dlpuser@dlptest.com', 'SzMf7rTE4pCrf9dV286GuNe4N')

src = (r'C:\Users\Lenovo\Desktop\FIEK\viti3\internetSecurity\detyra4_Python\FilesToBeTransfered')

for file in glob.glob(src +'/*'):
    splittedfile = file.split('.')
    if splittedfile[1] in ["doc","docx","xls","xlsx"]:
        print("Uploading-"+ os.path.basename(file))
        fp = open(file, 'rb')
        ftp.cwd("/done/") 
        ftp.storbinary('STOR %s' % os.path.basename(file), fp, 1024)
        fp.close()

