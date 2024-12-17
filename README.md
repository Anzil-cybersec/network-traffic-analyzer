# Network Traffic Analyzer
Python project to analyze network traffic captured with Wireshark
## Prerequisites

Before you can run the script, you need to set up the following:

- **Wireshark**: For capturing network traffic.
- **Python 3.x**: To run the Python analysis script.

### Dependencies

You need to install the following Python libraries:

- `scapy`: For reading and analyzing network packets.
- `pandas`: For processing and organizing the data.
- `matplotlib`: For plotting graphs (if required).
- `tabulate`: For formatting tables in the output.



## **Steps to Capture Network Traffic Using Wireshark**

### **1. Install Wireshark:**
- Download and install Wireshark from the [Wireshark Download Page](https://www.wireshark.org/download.html).

### **2. Start Capturing Traffic:**
- Open **Wireshark**.
- Select the network interface to capture traffic (e.g., Ethernet or Wi-Fi).
- Click the **Start capturing packets** button (the shark fin icon).

### **3. Capture Network Traffic:**
- Let Wireshark run for a period of time to capture traffic.
- Once you have sufficient data, click the **Stop capturing packets** button (the red square icon).

### **4. Save the Capture File:**
- Go to **File > Save As**.
- Save the captured file in **.pcap** format (e.g., `capture.pcap`).
  
> **Note**: Ensure that the `.pcap` file is saved in the **project directory** or an appropriate **subfolder** (e.g., `captures/`).

---

## **Steps to Run the Network Analyzer Script**

### **1. Clone the Repos

