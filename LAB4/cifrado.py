from Crypto.Cipher import DES, DES3, AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

def clave(key, tam, algoritmo=None):
    key_bytes = key.encode('utf-8')
    
    # Ajuste de longitud
    if len(key_bytes) < tam:
        key_bytes += get_random_bytes(tam - len(key_bytes))
    else:
        key_bytes = key_bytes[:tam]
    
    # Ajuste de paridad si es 3DES
    if algoritmo == DES3:
        key_bytes = DES3.adjust_key_parity(key_bytes)

    return key_bytes

def cifrado_simetrico(algoritmo, key_len, vector_len):
    key_input = input("Ingrese la clave: ")
    vector_input = input("Ingrese el vector de inicialización (IV): ")
    texto = input("Ingrese el texto a cifrar: ")

    key = clave(key_input, key_len, algoritmo)
    iv = clave(vector_input, vector_len)

    print(f"\nClave utilizada (hex): {key.hex()}")
    print(f"IV utilizado (hex): {iv.hex()}")

    cipher = algoritmo.new(key, algoritmo.MODE_CBC, iv)
    texto_bytes = texto.encode('utf-8')
    cifrado = cipher.encrypt(pad(texto_bytes, algoritmo.block_size))

    print(f"Texto cifrado (hex): {cifrado.hex()}")

    decipher = algoritmo.new(key, algoritmo.MODE_CBC, iv)
    descifrado = unpad(decipher.decrypt(cifrado), algoritmo.block_size)

    print(f"Texto descifrado: {descifrado.decode()}\n")

def main():
    while True:
        print("Seleccione el algoritmo de cifrado:")
        print("1. DES")
        print("2. 3DES")
        print("3. AES-256")
        print("4. Salir")
        opcion = input("Opción: ")

        if opcion == '1':
            cifrado_simetrico(DES, 8, 8)
        elif opcion == '2':
            cifrado_simetrico(DES3, 24, 8)
        elif opcion == '3':
            cifrado_simetrico(AES, 32, 16)
        elif opcion == '4':
            break
        else:
            print("Opción no válida. Intente de nuevo.\n")

if __name__ == "__main__":
    main()
