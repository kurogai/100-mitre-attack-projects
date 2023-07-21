import socket

def whois_query(domain):
    try:
        # We create a socket to connect to the WHOIS server
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect(("whois.iana.org", 43))
            s.send((domain + "\r\n").encode())

            # We receive the response from the WHOIS server
            response = b""
            while True:
                data = s.recv(1024)
                if not data:
                    break
                response += data

            # We get the name and port of the WHOIS server
            result = response.decode().splitlines()
            for line in result:
                if ":" in line:
                    server_info = line.split(": ")
                    if server_info[0].strip().lower() == "whois":
                        whois_server = server_info[1].strip()
                        break

        # We send a second request to the WHOIS server
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((whois_server, 43))
            s.send((domain + "\r\n").encode())

            # We get WHOIS result
            response = b""
            while True:
                data = s.recv(1024)
                if not data:
                    break
                response += data

        return response.decode()

    except Exception as e:
        return str(e)


if __name__ == "__main__":
    domain_name = input("Enter a domain name for the WHOIS query: ")
    whois_result = whois_query(domain_name)
    print(whois_result)
