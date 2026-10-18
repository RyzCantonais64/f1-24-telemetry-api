from Listener.listener import Listener
from fastapi import FastAPI
import hmac
import hashlib
import json


app = FastAPI()

SECRET_KEY = b"f1_paddock_secure_key_2026"

listener = Listener()

@app.get("/secure/telemetry/{index}")
def get_secure_telemetry(index: int):
    # Récupération des données brutes du jeu via le listener
    packet = listener.listen()
    car_data = packet.car_telemetry_data[index]
    
    # Construction du payload de télémétrie à sécuriser
    payload = {
        "speed": car_data.speed,
        "throttle": car_data.throttle,
        "brake": car_data.brake,
        "gear": car_data.gear,
        "engine_temperature": car_data.engine_temperature
    }
    
    # Génération de la signature HMAC-SHA256
    # On convertit le dictionnaire en chaîne JSON triée pour garantir l'uniformité
    payload_bytes = json.dumps(payload, sort_keys=True).encode('utf-8')
    signature = hmac.new(SECRET_KEY, payload_bytes, hashlib.sha256).hexdigest()
    
    # On retourne le paquet sécurisé contenant les données et le sceau cryptographique
    return {
        "status": "success",
        "payload": payload,
        "hmac_signature": signature
    }

@app.get("/speed/{index}")
def get_speed(index: int) -> int:
    packet = listener.listen()
    return packet.car_telemetry_data[index].speed


@app.get("/throttle/{index}")
def get_throttle(index: int) -> float:
    packet = listener.listen()
    return packet.car_telemetry_data[index].throttle


@app.get("/steer/{index}")
def get_steer(index: int) -> float:
    packet = listener.listen()
    return packet.car_telemetry_data[index].steer


@app.get("/brake/{index}")
def get_brake(index: int) -> float:
    packet = listener.listen()
    return packet.car_telemetry_data[index].brake


@app.get("/clutch/{index}")
def get_clutch(index: int) -> int:
    packet = listener.listen()
    return packet.car_telemetry_data[index].clutch


@app.get("/gear/{index}")
def get_gear(index: int) -> int:
    packet = listener.listen()
    return packet.car_telemetry_data[index].gear


@app.get("/engine_rpm/{index}")
def get_engine_rpm(index: int) -> int:
    packet = listener.listen()
    return packet.car_telemetry_data[index].engine_rpm


@app.get("/drs/{index}")
def get_drs(index: int) -> int:
    packet = listener.listen()
    return packet.car_telemetry_data[index].drs


@app.get("/rev_lights_percent/{index}")
def get_rev_lights_percent(index: int) -> int:
    packet = listener.listen()
    return packet.car_telemetry_data[index].rev_lights_percent


@app.get("/rev_lights_bit_value/{index}")
def get_rev_lights_bit_value(index: int) -> int:
    packet = listener.listen()
    return packet.car_telemetry_data[index].rev_lights_bit_value


@app.get("/brakes_temperature/{index}")
def get_brakes_temperature(index: int) -> list:
    packet = listener.listen()
    return packet.car_telemetry_data[index].brakes_temperature


@app.get("/tyres_surface_temperature/{index}")
def get_tyres_surface_temperature(index: int) -> list:
    packet = listener.listen()
    return packet.car_telemetry_data[index].tyres_surface_temperature


@app.get("/tyres_inner_temperature/{index}")
def get_tyres_inner_temperature(index: int) -> list:
    packet = listener.listen()
    return packet.car_telemetry_data[index].tyres_inner_temperature


@app.get("/engine_temperature/{index}")
def get_engine_temperature(index: int) -> int:
    packet = listener.listen()
    return packet.car_telemetry_data[index].engine_temperature


@app.get("/tyres_pressure/{index}")
def get_tyres_pressure(index: int) -> list:
    packet = listener.listen()
    return packet.car_telemetry_data[index].tyres_pressure


@app.get("/surface_type/{index}")
def get_surface_type(index: int) -> list:
    packet = listener.listen()
    return packet.car_telemetry_data[index].surface_type
