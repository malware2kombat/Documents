from scapy.all import sniff

def packet_callback(packet):
    print(packet.show())

def main():
    snif(prn=packet_callback, count=1)

if __name__ == '__main__':
    main()