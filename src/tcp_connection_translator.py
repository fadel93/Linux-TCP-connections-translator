
# This method gets the lines from /proc/net/tcp and splits them into lists
def open_tcp_file():
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

if __name__ == "__main__":
    data = open_tcp_file()
    print(data)