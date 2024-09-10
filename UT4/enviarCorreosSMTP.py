import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def enviarCorreo(destino):
    body = '''Buenos Dias'''
    #destino, cuenta y pass
    enviadoPor = 'danielmedinaalcolea@outlook.es'
    contra = '1234aaaa'
    to = destino
    
    mensaje = MIMEMultipart()
    mensaje['From'] = enviadoPor
    mensaje['To'] = destino
    mensaje['Subject'] = 'Saludo'
    
    mensaje.attach(MIMEText(body, 'plain')) #MIMEText, MIMEImage, etc...
    
    
    #Ajuntar Archivo
    filename = 'UT4/nuevo.txt'
    attachment = open (filename, 'rb')#rb = lectura binaria
    part = MIMEBase('application','octet-stream')
    part.set_payload(attachment.read()) #leer el archivo
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename=%s" %filename)
    
    mensaje.attach(part)


    sesion = smtplib.SMTP('smtp-mail.outlook.com', 587)
    sesion.starttls()
    sesion.login(enviadoPor, contra)
    text = mensaje.as_string()
    sesion.sendmail(enviadoPor, to, text)
    sesion.quit()
    print("Mensaje Enviado")



if __name__ == "__main__":
    enviarCorreo('dam_danielmedina@riberadeltajo.es')