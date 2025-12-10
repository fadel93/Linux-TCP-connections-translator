# Linux TCP Connections Translator

## Overview
The Linux TCP Connections Translator is a Python project designed to read and parse TCP connection information from the `/proc/net/tcp` file in Linux. It formats this information into a human-readable table using the `tabulate` library, making it easier for users to understand the current TCP connections on their system.

## Features
- Reads TCP connection data from the Linux kernel's `/proc/net/tcp` file.
- Parses IP addresses and ports from hexadecimal format to a human-readable format.
- Displays TCP connection details in a structured table format.
- Provides a simple command-line interface for users.

## Installation
To install the required dependencies, you can use the following command:

```
pip install -r requirements.txt
```

## Usage
To run the TCP connections translator, execute the following command in your terminal:

```
python src/tcp_connection_translator.py
```

This will display the current TCP connections in a formatted table.

## Contributing
Contributions are welcome! If you would like to contribute to this project, please fork the repository and submit a pull request with your changes.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

## Acknowledgments
- The `tabulate` library for formatting tables in Python.
- The Linux kernel for providing the `/proc/net/tcp` interface.