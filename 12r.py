import pywhatkit as kit
import datetime
import schedule
import time

# Función para enviar el mensaje de WhatsApp
def enviar_mensaje_whatsapp():
    # Lista de números de WhatsApp a los que deseas enviar el mensaje
    numeros_whatsapp = ["+5492604012070", "+5492604386415", "+5492604632453", "+5492604338288"]

    # Crear el mensaje que deseas enviar
    mensaje_whatsapp = "Estimado cliente, su cuota está por vencer. Luego de recibir esta notificación, cuenta con 48 horas para abonar y no incurrir en mora. Annidada Tech."

    # Esperar 10 segundos antes de enviar el mensaje (ajusta este valor según tus necesidades)
    time.sleep(10)

    # Enviar el mensaje de WhatsApp a cada número
    for numero in numeros_whatsapp:
        kit.sendwhatmsg(numero, mensaje_whatsapp, 19, 55)  # Enviar a las 19:55

# Obtener la hora actual
hora_actual = datetime.datetime.now()

# Calcular la hora a la que deseas enviar el mensaje (por ejemplo, en 5 minutos)
# Ajusta la hora y el minuto según tus necesidades
hora_envio = hora_actual.replace(hour=19, minute=55)

# Programar el envío del mensaje en el tiempo especificado
schedule.every().day.at(f"{hora_envio.hour}:{hora_envio.minute}").do(enviar_mensaje_whatsapp)

# Bucle para ejecutar la programación
while True:
    schedule.run_pending()
    time.sleep(1)
