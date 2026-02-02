# telegram_bot.py

import telepot
from telepot.loop import MessageLoop
from controlador.controlador import ControladorLED
import time

TOKEN = "8362344962:AAF18GdwswBhpNrZVkUqKqhRF1ZZLC6MxI4"

controlador = ControladorLED()

def manejar_mensaje(msg):
    contenido = msg.get("text", "")
    chat_id = msg["chat"]["id"]

    #Mostrar en consola lo que llega desde Telegram
    print(f"[TELEGRAM] Mensaje recibido: {contenido}")

    respuesta = controlador.procesar_comando(contenido)
    bot.sendMessage(chat_id, respuesta)

bot = telepot.Bot(TOKEN)

def iniciar_bot():
    MessageLoop(bot, manejar_mensaje).run_as_thread()
    print("Bot iniciado...")

    while True:
        time.sleep(10)
