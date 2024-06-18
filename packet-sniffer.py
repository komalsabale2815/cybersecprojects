from scapy.all import *

def packet_callback(packet):
    # Extract relevant information from the packet
    src_ip = packet[IP].src
    dst_ip = packet[IP].dst
    protocol = packet[IP].proto
    payload = packet[TCP].payload if TCP in packet else packet[UDP].payload if UDP in packet else ""

    # Print or process the extracted information
    print(f"Source IP: {src_ip} | Destination IP: {dst_ip} | Protocol: {protocol} | Payload: {payload}")

def main():
    print("Simple Packet Sniffer - Press Ctrl+C to stop sniffing")

    try:
        # Start sniffing packets
        sniff(filter="ip", prn=packet_callback, store=0)
    except KeyboardInterrupt:
        print("Sniffing stopped.")

if __name__ == "__main__":
    main()
