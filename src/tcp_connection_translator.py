from tabulate import tabulate

def open_tcp_file(): # This method gets the lines from /proc/net/tcp and splits them into listss
    tcp_file_lines = []
    with open('/proc/net/tcp', 'r') as file:
        for line in file:
            temp_list = []
            parts = line.split(" ")
            for part in parts:
                if part != '' and part != '\n':
                    temp_list.append(part)
            tcp_file_lines.append(temp_list)
    return tcp_file_lines

def parse_ip_port(field): # This method converts the hex ip:port format to decimal dotted ip:port format
    ip_hex, port_hex = field.split(':')
    ip_octets = [str(int(ip_hex[i:i+2], 16)) for i in range(0, 8, 2)]
    ip = '.'.join(reversed(ip_octets))
    port = str(int(port_hex, 16))
    return ip, port
    

def parse_tcp_info(info): # This method parses each line of /proc/net/tcp and converts the fields to human-readable format
    state_dict = {
        '01': 'ESTABLISHED',
        '02': 'SYN_SENT',
        '03': 'SYN_RECV',
        '04': 'FIN_WAIT1',
        '05': 'FIN_WAIT2',
        '06': 'TIME_WAIT',
        '07': 'CLOSE',
        '08': 'CLOSE_WAIT',
        '09': 'LAST_ACK',
        '0A': 'LISTEN',
        '0B': 'CLOSING'
    }

    info[0] = int(info[0].rstrip(':'))
    local_ip, local_port = parse_ip_port(info[1])
    remote_ip, remote_port = parse_ip_port(info[2])
    info[1] = f"{local_ip}:{local_port}"
    info[2] = f"{remote_ip}:{remote_port}"
    info[3] = state_dict.get(info[3], 'UNKNOWN')
    tx_queue = info[4].split(':')[0]
    rx_queue = info[4].split(':')[1]
    info[4] = f"{int(tx_queue, 16)}:{int(rx_queue, 16)}"  # TX_QUEUE and RX_QUEUE combined
    timer_active = info[5].split(':')[0]
    numer_of_jiffies = info[5].split(':')[1]
    info[5] = f"{int(timer_active, 16)}:{int(numer_of_jiffies, 16)}"  # TIMER_ACTIVE and NUMBER_OF_JIFFIES combined
    info[6] = int(info[6], 16)  # Number of unrecovered RTO timeouts

    return info


def main(): # This is the main method that calls the other methods and prints the final table
    tcp_data = open_tcp_file()
    header = tcp_data[0]
    rows = []
    for line in tcp_data[1:]:  # Skip header line
        rows.append(parse_tcp_info(line))

    tcp_table = tabulate(rows, headers=header, tablefmt='grid')
    print(tcp_table)

if __name__ == "__main__":
    main()