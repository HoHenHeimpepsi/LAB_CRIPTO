from scapy.all import rdpcap, ICMP
import string

# Colores ANSI
VERDE = "\033[92m"
RESET = "\033[0m"

def extraer_mensaje(pcap_file):
    
    paquetes = rdpcap(pcap_file)
    letras = []

    for pkt in paquetes:
        if pkt.haslayer(ICMP):
            raw = bytes(pkt[ICMP].payload)
            if len(raw) > 0:
                letra = chr(raw[0])
                letras.append(letra)

    return "".join(letras)

def cesar_descifrar(texto, desplazamiento):
    resultado = ""
    for c in texto:
        if c.isalpha():
            base = ord('A') if c.isupper() else ord('a')
            resultado += chr((ord(c) - base - desplazamiento) % 26 + base)
        else:
            resultado += c
    return resultado

if __name__ == "__main__":
    archivo_pcap = "captura con padding correcto.pcapng"  
    mensaje_cifrado = extraer_mensaje(archivo_pcap)

    print("Mensaje capturado (cifrado):", mensaje_cifrado)
    print("\nPosibles descifrados con corrimiento César:\n")

    palabra_correcta = "criptografia y seguridad en redes"

    for shift in range(1, 27):
        descifrado = cesar_descifrar(mensaje_cifrado, shift)

        if palabra_correcta in descifrado.lower():
            print(f"Shift {shift:2d}: {VERDE}{descifrado}{RESET}")
        else:
            print(f"Shift {shift:2d}: {descifrado}")
