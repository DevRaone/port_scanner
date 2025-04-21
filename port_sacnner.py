import socket
import concurrent.futures
import time

def scan_port(host, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            result = s.connect_ex((host, port))
            if result == 0:
                print(f"Porta {port} está aberta")
                return port
    except:
        pass
    return None

def port_scanner(host, start_port, end_port, max_threads=100):
    open_ports = []
    print(f"Escaneando {host} de porta {start_port} até {porta_final}...")
    start_time = time.time()
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_threads) as executor:
        futures = [executor.submit(scan_port, host, port) 
                  for port in range(start_port, end_port + 1)]
        
        for future in concurrent.futures.as_completed(futures):
            result = future.result()
            if result:
                open_ports.append(result)
    
    end_time = time.time()
    print(f"\nEscaneamento concluído em {end_time - start_time:.2f} segundos")
    print(f"Portas abertas encontradas: {sorted(open_ports)}")

if __name__ == "__main__":
    target = input("Digite o host ou IP para scanear: ")
    start_port = int(input("Porta inicial: "))
    end_port = int(input("Porta final: "))
    
    port_scanner(target, start_port, end_port)
