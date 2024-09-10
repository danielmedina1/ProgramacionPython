import ftplib

FTP_HOST = 'localhost'
FTP_USER = 'Usuario_1'
FTP_PASS = 'usu1'

def ver_ftp():
    ftp = ftplib.FTP(FTP_HOST, FTP_USER, FTP_PASS)
    ftp.encoding = 'utf8'
    print(ftp.getwelcome(),'\n')
    respuesta = ftp.retrlines('LIST')
    print(respuesta)
    print('\n')
    respuesta = ftp.retrlines('NLST')
    print(respuesta)
    ftp.close()

def subir_ftp(fichero_local, fichero_remoto):
    ftp = ftplib.FTP(FTP_HOST, FTP_USER, FTP_PASS)
    ftp.encoding = 'utf8'
    print(ftp.getwelcome(),'\n')
    fichero = open(fichero_local,'rb')
    ftp.storbinary(f'STOR {fichero_remoto}',fichero)
    ftp.close()

def descargar_ftp(fichero_local, fichero_remoto):
    ftp = ftplib.FTP(FTP_HOST, FTP_USER, FTP_PASS)
    ftp.encoding = 'utf8'
    print(ftp.getwelcome(),'\n')
    fichero = open(fichero_local,'wb')
    ftp.retrbinary(f'RETR {fichero_remoto}',fichero.write)
    print("Fichero desgargado")
    ftp.close()


if __name__ == '__main__':
    ver_ftp()
    fichero_local = 'UT4/ejemplo.txt'
    fichero_remoto = 'ejemplo.txt'
    #subir_ftp(fichero_local, fichero_remoto)
    fichero_local = 'UT4/nuevo.txt'
    fichero_remoto = 'daniel/texto.txt'
    #descargar_ftp(fichero_local,fichero_remoto)