import requests
#from datetime import datetime
#import smtplib
#import tkinter as tk

LATITUDE = -20.1394
LONGITUDE = -44.8872
 

def frase_zero(temp, umid, chuva, nuvem):
    if chuva > 0:
        return "Chove. Até o céu desistiu de aguentar sozinho."
    elif umid < 40:
        return "Seco. Ao menos que seus olhos chorem, nada mais vai molhar."
    elif temp > 33:
        return "Calor desnecessário. A realidade está derretendo como você às segundas-feiras."
    elif nuvem > 80:
        return "Nublado. Mas não confunda com paz de espírito."
    elif temp > 30 && umid < 40:
        return "Calor desnecessário. A realidade está derretendo como você às segundas-feiras."
    else:
        return "O clima está calmo. O caos, como sempre, é interno."
        
        
        
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
    topic = __import__("os").environ["NTFY_TOPIC"]

    ntfy_url = f"https://ntfy.sh/{topic}"

    notificacao = requests.post(
     ntfy_url,
     data=mensagem.encode("utf-8"),
     headers = {
        "Title": "MeteoCaos",
        "Priority": "default"
    }
)
    notificacao.raise_for_status()
    print("Notificação enviada com sucesso")

except Exception as e:
    print("⚠️ Erro geral:", e)

   
    
    
