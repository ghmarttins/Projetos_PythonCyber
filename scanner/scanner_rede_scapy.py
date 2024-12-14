import scapy.all as scapy

def escanear_rede(endereco):
    scapy.arping(endereco)


escanear_rede("192.168.19.84/24")