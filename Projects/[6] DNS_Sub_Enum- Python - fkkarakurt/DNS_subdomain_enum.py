import socket

def is_valid_subdomain(subdomain, target_url):
    url = f"{subdomain}.{target_url}"
    try:
        host = socket.gethostbyname(url)
        if host != target_url:
            return True
    except socket.gaierror:
        pass
    return False

def main():
    target_url = input("Target URL: (exp: example.com): ").strip().lower()

    with open("common_subdomains.txt") as file:
        subdomains = [line.strip() for line in file]

    valid_subdomains = [subdomain for subdomain in subdomains if is_valid_subdomain(subdomain, target_url)]

    if valid_subdomains:
        print("\nValid subdomains:")
        for valid_subdomain in valid_subdomains:
            print(f"- {valid_subdomain}.{target_url}")
    else:
        print("\nNo valid subdomain found.")

if __name__ == "__main__":
    main()
