from ftplib import FTP
import fileinput
import os
import glob
# shutil metoda na vyn per bartjen lokale te files psh prej nji directory te nji tjeter lokalisht n'pc psh me shutil.move(prej kujt, ku) -> qekjo i move krejt, edhe psh shutil.copy(prej kujt, ku)-> kjo i bon copy po nuk i zhvendos.
import shutil

# Inicializon klasen FTP ( me parametrat si hosts (host i joni osht FTP serveri online) mandej username edhe passwordi)
ftp = FTP('ftp.dlptest.com' , 'dlpuser@dlptest.com', 'SzMf7rTE4pCrf9dV286GuNe4N')

# osht directory location n'pc me qato files
src = (r'C:\Users\Lenovo\Desktop\FIEK\viti3\internetSecurity\detyra4_Python\FilesToBeTransfered')

# loopa for ka me iteru ne qat follder ne path-in te instanca src mandej glob.glob metoda mundson qe me i mar krejt files qaj ylli tregon qe i mer krejt se na kemi mujt edhe qitu me bo (src +'/* docx') po i kish gjet krejt files me docx e mbasi ky ka thon edhe 3 lloje tjera te extentions fillimisht i mer krejt files ne follderin e qati pathi
for file in glob.glob(src +'/*'):
    # tash qato krejt files qe i ka mar, nepermjet metodes split n'kete rast file.split ('.') ka me i nda te pika domethon nji file qe i kom lon n'qat follder une e ka emrin (file transfer protocol.docx) e qet string e ndan te pika edhe e run te qekjo array splittedfile
    splittedfile = file.split('.')
    # tash e bon nji kushtezim nese ANETARI I DYTE i array splittedfile (pra anetari i pare osht file transfer protocol) i dyti (eshte extensioni) mbas pikes me qene njeri nga anetaret ne listen se extentions ["doc","docx","xls","xlsx"]
    if splittedfile[1] in ["doc","docx","xls","xlsx"]:
        # atehere printoje emrin e file: kur te i'a boni python TransferingFile.py ju del Uploading - file tranfer protocol.docx (psh).  Metoden os.path.basename(file) e di qe e merr emrin e file-it amo qe doni kqyrni edhe ma shume per to
        print("Uploading-"+ os.path.basename(file))
        # tash e qel qat file ne formatin binary 'rb'edhe i run qaty te fp instanca
        fp = open(file, 'rb')
        # kur na e kemi inacializu klasen FTP e inicializum te nji ftp, qato parametra osht serveri jon' jo-lokal ne te cilen na kemi me upload file ton prej follderit lokal. ftp.cwd (change in "/done/" directory) merr per parameter path-in e directoriumit ne te cilin ne po dojm me upload files. U kon edhe directoriumi ("/") mundemi edhe qaty me i lon ku te doni 
        ftp.cwd("/done/") 
        # qekjo tash e bon upload file-in edhe kto kqyrne pak per me i kuptu nashta ma mire
        ftp.storbinary('STOR %s' % os.path.basename(file), fp, 1024)
        # mbasi qe kryhet krejt seksioni mbyllet
        fp.close()

