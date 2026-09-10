import requests
import time
#from datetime import datetime
#import smtplib
#import tkinter as tk

LATITUDE = -20.1394
LONGITUDE = -44.8872
INTERVALO = 600 

def frase_zero(temp, umid, chuva, nuvem):
    if chuva > 0:
        return "Chove. Até o céu desistiu de aguentar sozinho."
    elif umid < 40:
        return "Seco. Ao menos que seus olhos chorem, nada mais vai molhar."
    elif temp > 33:
        return "Calor desnecessário. A realidade está derretendo como você às segundas-feiras."
    elif nuvem > 80:
        return "Nublado. Mas não confunda com paz de espírito."
    else:
        return "O clima está calmo. O caos, como sempre, é interno."
        
        
        
while True:
    try:
        url = "https://api.open-meteo.com/v1/forecast"
        params = {
            "latitude": LATITUDE,
            "longitude": LONGITUDE,
            "current": "temperature_2m,relative_humidity_2m,precipitation,cloudcover"
        }

        resposta = requests.get(url, params=params)
        dados = resposta.json()["current"]

        temp = dados["temperature_2m"]
        umid = dados["relative_humidity_2m"]
        chuva = dados["precipitation"]
        nuvem = dados["cloudcover"]

        mensagem = f"Clima: {temp}°C, Umidade: {umid}%, Chuva: {chuva}mm, Nuvens: {nuvem}%\n"
        mensagem += frase_zero(temp, umid, chuva, nuvem)

        print(mensagem)
       # registrar_txt(mensagem)

    except Exception as e:
        print("⚠️ Erro geral:", e)

    time.sleep(INTERVALO)
    
    