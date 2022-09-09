import sys


def is_valid_ip_address(ip_address):
    ip_address_octets = ip_address.split('.')
    return len(ip_address_octets) == 4 \
           and 1 <= int(ip_address_octets[0]) <= 223 \
           and int(ip_address_octets[0]) != 127 \
           and 0 <= int(ip_address_octets[1]) <= 255 \
           and 0 <= int(ip_address_octets[2]) <= 255 \
           and 0 <= int(ip_address_octets[3]) <= 255


if __name__ == "__main__":
    try:
        while True:
            ip_address = input("\nEnter an IPv4 address: ")
            if is_valid_ip_address(ip_address):
                break
            else:
                print("\nThe IP address is INVALID, enter a valid IPv4 address!")
                continue
    except KeyboardInterrupt:
        print("/n Interrupted /n")
        sys.exit()
