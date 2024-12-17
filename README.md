# network-traffic-analyzer
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


Steps to Capture Network Traffic Using Wireshark
1. Install Wireshark:
Download and install Wireshark from the Wireshark Download Page.
2. Start Capturing Traffic:
Open Wireshark.
Select the network interface to capture traffic (e.g., Ethernet or Wi-Fi).
Click the Start capturing packets button (the shark fin icon).
3. Capture Network Traffic:
Let Wireshark run for a period of time to capture traffic.
Once you have sufficient data, click the Stop capturing packets button (the red square icon).
4. Save the Capture File:
Go to File > Save As.
Save the captured file in .pcap format (e.g., capture.pcap).
Note: Ensure that the .pcap file is saved in the project directory or an appropriate subfolder (e.g., captures/).

Steps to Run the Network Analyzer Script
1. Clone the Repository:
Clone this repository to your local machine using the following command:

bash
Copy code
git clone https://github.com/your-username/network-analyzer.git
2. Place the PCAP File:
Copy the .pcap file (the file you captured with Wireshark) into the captures/ directory. You can create this directory if it does not already exist.
3. Modify the Script (If Necessary):
Open the src/network_analyzer.py file.
Ensure that the path to your .pcap file is correct in the script (e.g., captures/capture.pcap).
4. Run the Script:
After placing the capture file and ensuring the script is correctly configured, run the Python script:

bash
Copy code
python src/network_analyzer.py captures/capture.pcap
5. View the Results:
The script will output the analysis results in the terminal or command prompt, including:

Total bandwidth used.
Protocol distribution (ICMP, TCP, UDP).
Source and destination IP communication details.
Potential port scanning activity, if detected.
Additionally, tables and graphs may be generated to visualize the results.

Additional Notes
You can modify the threshold for port scanning detection by changing the port_scan_threshold parameter in the script.
If you want to analyze another .pcap file, simply replace the file path in the command with the new file path:
bash
Copy code
python src/network_analyzer.py captures/new_capture.pcap
Dependencies
Ensure that you have the following dependencies installed to run the script:

Scapy: For reading and analyzing packets.
Pandas: For data analysis.
Matplotlib: For generating visual plots.
