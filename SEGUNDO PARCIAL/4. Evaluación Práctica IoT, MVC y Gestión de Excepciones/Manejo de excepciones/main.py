from controller import Controller
from view import View
import time

TELEGRAM_TOKEN = "8362344962:AAF18GdwswBhpNrZVkUqKqhRF1ZZLC6MxI4"
CHAT_ID = "8423666340"

view = View()
controller = Controller(view, TELEGRAM_TOKEN, CHAT_ID)

try:
    while True:
        controller.run()
        time.sleep(2)
except KeyboardInterrupt:
    print("Programa detenido")

finally:
    view.limpiar()
