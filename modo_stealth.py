from scapy.all import IP, ICMP, send
import time
import binascii

mensaje = "larycxpajorj h bnpdarmjm nw anmnb"

def crear_payload_exacto(letra):
    """
    Crea payload de 40 bytes con la secuencia exacta:
    letra + puntos + !"#$%&'()*+,- ./01234567
    """
    # Secuencia exacta del padding
    padding_sequence = bytes([
        # !"#$%&'()*+,- 
        0x21, 0x22, 0x23, 0x24, 0x25, 0x26, 0x27, 0x28,  # !"#$%&'
        0x29, 0x2A, 0x2B, 0x2C, 0x2D,        # ()*+,-./
        
        # Espacio y ./
        0x20, 0x2E, 0x2F,                                #  ./
        
        # 01234567
        0x30, 0x31, 0x32, 0x33, 0x34, 0x35, 0x36, 0x37   # 01234567
    ])
    
    # Puntos de separación (calculamos cuántos necesitamos)
    puntos_necesarios = 40 - 1 - len(padding_sequence)  # 40 total - 1 letra - padding
    puntos = bytes([0x00] * puntos_necesarios)
    coma_invertida = bytes([0x60])
    
    # Combinar todo
    payload = bytes([ord(letra)]) + coma_invertida + puntos + padding_sequence
    return payload[:40]  # Asegurar 40 bytes

for i, letra in enumerate(mensaje):
    payload = crear_payload_exacto(letra)
    
    paquete = IP(dst="www.google.com")/ICMP()/payload
    send(paquete, verbose=False)
    
    # Mostrar el resultado con la letra y puntos juntos
    ascii_rep = ''.join(chr(b) if 32 <= b <= 126 else '.' for b in payload)
    print(f"Paquete {i+1}: '{letra}' -> {ascii_rep}")
    print(f"Longitud: {len(payload)} bytes")
    print("-" * 40)
    time.sleep(0.1)