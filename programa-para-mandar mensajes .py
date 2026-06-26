import os
import requests
import time

# ==============================================================================
# CONFIGURACIÓN DE LA API DE WHATSAPP BUSINESS (CLOUD API)
# ==============================================================================
# Para mayor seguridad, las credenciales y números se leen de variables de entorno 
# o se solicitan durante la ejecución del script. Esto evita guardar PII o tokens
# sensibles directamente en el código fuente.

ACCESS_TOKEN = os.getenv("WA_ACCESS_TOKEN") or input("Introduce tu ACCESS_TOKEN de Meta: ").strip()
PHONE_NUMBER_ID = os.getenv("WA_PHONE_NUMBER_ID") or input("Introduce tu PHONE_NUMBER_ID: ").strip()

# El número debe incluir el código de país (ej. 56) sin signos '+' ni espacios (ej: 56912345678)
RECIPIENT_PHONE = os.getenv("WA_RECIPIENT_PHONE") or input("Introduce el número de destino (ej. 569XXXXXXXX): ").strip()
MENSAJE_TEXTO = "seva manda las fotos"

# URL del endpoint oficial de la API de WhatsApp Cloud
URL = f"https://graph.facebook.com/v17.0/{PHONE_NUMBER_ID}/messages"

headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Content-Type": "application/json"
}

def enviar_mensaje_texto(mensaje):
    """
    Envía un mensaje de texto libre a un número específico.
    """
    payload = {
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": RECIPIENT_PHONE,
        "type": "text",
        "text": {
            "preview_url": False,
            "body": mensaje
        }
    }
    
    try:
        response = requests.post(URL, headers=headers, json=payload)
        return response.json()
    except Exception as e:
        return {"error": str(e)}

def ejecutar_pruebas_de_carga(cantidad_mensajes, intervalo_segundos):
    """
    Realiza el envío controlado de una cantidad específica de mensajes de prueba.
    """
    print(f"\nIniciando envío de {cantidad_mensajes} mensajes de prueba al número destinatario...")
    for i in range(1, cantidad_mensajes + 1):
        print(f"Enviando mensaje {i}/{cantidad_mensajes}...")
        
        resultado = enviar_mensaje_texto(MENSAJE_TEXTO)
        print(f"Respuesta del servidor: {resultado}")
        
        if i < cantidad_mensajes:
            # Intervalo de tiempo seguro
            time.sleep(intervalo_segundos)

if __name__ == "__main__":
    CANTIDAD_ENVIOS = 5
    INTERVALO_ENTRE_ENVIOS = 2.0  # en segundos
    
    # Validación básica de datos de entrada
    if not ACCESS_TOKEN or not PHONE_NUMBER_ID or not RECIPIENT_PHONE:
        print("[!] ERROR: Todos los campos son obligatorios.")
    else:
        ejecutar_pruebas_de_carga(CANTIDAD_ENVIOS, INTERVALO_ENTRE_ENVIOS)


