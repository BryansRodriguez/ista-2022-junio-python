import requests

SERVIDOR="http://127.0.0.1:5000"

respuesta = requests.get(SERVIDOR)
print(respuesta.text)

respuesta = requests.get(f"{SERVIDOR}/datos")
respuesta_objeto = respuesta.json()
print(f"Mi nombre es {respuesta_objeto['nombre']}")