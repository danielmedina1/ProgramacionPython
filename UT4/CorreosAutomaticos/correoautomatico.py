import json
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders



def enviar_correoSMTP(destino,tag,body):
    #direccion, contraseña y destinatario
    enviadoPor = 'danielmedinaalcolea@outlook.es'
    contra = '1234aaaa'
    
    

    #Establecimiento MIME
    mensaje = MIMEMultipart()
    mensaje['From'] = enviadoPor
    mensaje['To'] = destino
    mensaje['Subject'] = 'Fichero Solicitado'
    
    mensaje.attach(MIMEText(body, 'plain'))

  #Cuerpo y adjuntos para el correo
    nombreFichero='UT4/CorreosAutomaticos/tags/'+tag+'.txt'
    attachment = open (nombreFichero, 'rb')
    part = MIMEBase('application','octet-stream')
    part.set_payload(attachment.read()) #leer el archivo
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename=%s" %nombreFichero)
    
    mensaje.attach(part)
    
  #Sesión SMTP para el envío del correo
    sesion = smtplib.SMTP('smtp-mail.outlook.com', 587)
    sesion.starttls()
    sesion.login(enviadoPor, contra)
    text = mensaje.as_string()
    sesion.sendmail(enviadoPor, destino, text)
    sesion.quit()
    print("Mensaje Enviado")
    


def enviar_correo(correo, intereses):
    for tag in intereses:
        print(f"{tag}")
        nombreFichero='UT4/CorreosAutomaticos/tags/'+tag+'.txt'
        
        #si el fichero existe leer el contenido y llamar al método
        body = ""
        try:
            file = open (nombreFichero, 'rw')
            body = file.read()
        except:
            print(f"El fichero {tag} no existe")
            
        
        if file is not None:
             enviar_correoSMTP(correo, tag, body)
    


   



# Función para cargar los datos del archivo JSON en una lista de diccionarios
def cargar_datos_desde_json(archivo):
    with open(archivo, 'r') as f:
        datos = json.load(f)
    return datos

if __name__ == "__main__":
    # Nombre del archivo JSON
    archivo_json = 'UT4/CorreosAutomaticos/datos.json'
    # Cargar los datos del archivo JSON en una lista de diccionarios
    datos = cargar_datos_desde_json(archivo_json)

    # Imprimir los datos cargados
    print("Datos cargados desde el archivo JSON:")
    for persona in datos:
        print("Nombre:", persona["nombre"])
        print("Correo electrónico:", persona["correo_electronico"])
        print("Tags de intereses:", persona["tags_de_intereses"])
        destino=persona["correo_electronico"]
        intereses=persona["tags_de_intereses"]
        enviar_correo(destino,intereses)
    

