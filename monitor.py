import time
import socket
import json
import os

# Dirección y puerto del servidor de Minecraft
HOST = 'localhost'
PORT = 25565
# Tiempo de espera en minutos antes de cerrar el servidor
WAIT_TIME_MINUTES = 1

def get_online_players():
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            s.sendall(b'\xFE\x01')
            data = s.recv(1024)
            if data:
                decoded_data = data.decode('utf-16be').split('\x00\x00\x01player_\x00\x00')[1]
                player_count = int(decoded_data.split('\x00')[0])
                return player_count
    except:
        return 0
    return 0

def main():
    no_players_start_time = None

    while True:
        player_count = get_online_players()
        
        if player_count == 0:
            if no_players_start_time is None:
                no_players_start_time = time.time()
            elapsed_time = time.time() - no_players_start_time
            if elapsed_time >= WAIT_TIME_MINUTES * 60:
                os.system("taskkill /IM java.exe /F")
                break
        else:
            no_players_start_time = None  # Reset timer if players are connected
        
        time.sleep(1)  # Esperar un minuto antes de verificar de nuevo

if __name__ == '__main__':
    main()
