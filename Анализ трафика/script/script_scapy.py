from scapy.all import *

def send_message():
    target_ip = "127.0.0.1"
    target_port = 12345
    message = "Dear Steel Cat! This is no attack, it's my hamster Pinkie you should track"

    packet = IP(dst=target_ip) / TCP(dport=target_port) / message
    send(packet, verbose=False)

if __name__ == "__main__":
    send_message()