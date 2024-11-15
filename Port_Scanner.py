import socket #MrShawzen
import threading
import os, colorama, webbrowser, time; from colorama import *

os.system('color A')

os.system('cls')

print("""
   ____            _
  |  _ \ ___  _ __| |_
  | |_) / _ \| '__| __|
  |  __/ (_) | |  | |_          
  |_|   \___/|_|   \__|
 / ___|  ___ __ _ _ __  _ __   ___ _ __       
 \___ \ / __/ _` | '_ \| '_ \ / _ \ '__|      
  ___) | (_| (_| | | | | | | |  __/ |             
 |____/ \___\__,_|_| |_|_| |_|\___|_|                                                                                                              
""")

target = input("\n\nHedef IP veya URL'yi girin: ")
port_range = range(1, 1025)

def scan_port(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)

        result = s.connect_ex((target, port))

        if result == 0:
            print(f"Port {port}: AÇIK")
            try:
                banner = s.recv(1024)
                print(f"    Banner: {banner.decode().strip()}")
            except Exception as e:
                print(f"    Banner alınamadı: {e}")

        s.close()

    except KeyboardInterrupt:
        exit()
    except Exception as e:
        print(f"Hata: {e}")

for port in port_range:
    threading.Thread(target=scan_port, args=(port,)).start()
