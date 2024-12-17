import sys
import logging
from scapy.all import *
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger(__name__)

# Function to read pcap file
def read_pcap(pcap_file):
    try:
        return rdpcap(pcap_file)
    except Exception as e:
        logger.error(f"Error reading PCAP: {e}")
        sys.exit(1)

# Function to extract basic packet data
def extract_packet_data(packets):
    data = []
    for packet in packets:
        if IP in packet:
            src_ip = packet[IP].src
            dst_ip = packet[IP].dst
            proto = packet[IP].proto
            size = len(packet)
            data.append({"src_ip": src_ip, "dst_ip": dst_ip, "protocol": proto, "size": size})
    return pd.DataFrame(data)

# Function to detect port scanning activity
def detect_port_scanning(df, threshold=100):
    scan_data = df.groupby(['src_ip', 'dst_port']).size().reset_index(name='count')
    unique_ports = scan_data.groupby('src_ip').size().reset_index(name='unique_ports')
    potential_scanners = unique_ports[unique_ports['unique_ports'] >= threshold]
    if not potential_scanners.empty:
        logger.warning(f"Potential port scanning detected from IPs: {', '.join(potential_scanners['src_ip'])}")

# Function to plot results
def plot_protocol_distribution(df):
    proto_counts = df['protocol'].value_counts().to_dict()
    proto_labels = {1: 'ICMP', 6: 'TCP', 17: 'UDP'}
    proto_counts = {proto_labels.get(k, k): v for k, v in proto_counts.items()}
    plt.bar(proto_counts.keys(), proto_counts.values())
    plt.xlabel('Protocol')
    plt.ylabel('Count')
    plt.title('Protocol Distribution')
    plt.show()

# Function to print results
def print_results(df, total_bandwidth):
    # Print bandwidth usage
    bandwidth_unit = "MB" if total_bandwidth < 10**6 else "GB"
    total_bandwidth = total_bandwidth / (10**6 if bandwidth_unit == "MB" else 10**9)
    logger.info(f"Total bandwidth used: {total_bandwidth:.2f} {bandwidth_unit}")

    # Print protocol distribution
    proto_counts = df['protocol'].value_counts(normalize=True) * 100
    proto_labels = {1: 'ICMP', 6: 'TCP', 17: 'UDP'}
    proto_counts = proto_counts.rename(index=proto_labels)
    logger.info(f"Protocol distribution:\n{proto_counts}")

    # Print top communication pairs (source-destination IP)
    comm_pairs = df.groupby(['src_ip', 'dst_ip']).size().sort_values(ascending=False).head(10)
    logger.info(f"Top communication pairs:\n{comm_pairs}")

# Main function
def main(pcap_file, port_scan_threshold=100):
    packets = read_pcap(pcap_file)
    df = extract_packet_data(packets)

    # Analyze bandwidth usage
    total_bandwidth = df['size'].sum()

    # Detect port scanning
    detect_port_scanning(df, port_scan_threshold)

    # Print results and plots
    print_results(df, total_bandwidth)
    plot_protocol_distribution(df)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        logger.error("Please provide the path to the PCAP file.")
        sys.exit(1)

    pcap_file = sys.argv[1]
    port_scan_threshold = int(sys.argv[2]) if len(sys.argv) > 2 else 100
    main(pcap_file, port_scan_threshold)
