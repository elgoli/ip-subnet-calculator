import sys


def is_valid_ip_address(ip_address):
    ip_address_octets = ip_address.split('.')
    return len(ip_address_octets) == 4 \
           and 1 <= int(ip_address_octets[0]) <= 223 \
           and int(ip_address_octets[0]) != 127 \
           and 0 <= int(ip_address_octets[1]) <= 255 \
           and 0 <= int(ip_address_octets[2]) <= 255 \
           and 0 <= int(ip_address_octets[3]) <= 255


def is_valid_subnet_mask(subnet_mask):
    subnet_mask_octets = subnet_mask.split('.')
    valid_subnet_masks = [255, 254, 252, 248, 240, 224, 192, 128, 0]
    return (len(subnet_mask_octets) == 4) \
           and (int(subnet_mask_octets[0]) in valid_subnet_masks) \
           and (int(subnet_mask_octets[1]) in valid_subnet_masks) \
           and (int(subnet_mask_octets[2]) in valid_subnet_masks) \
           and (int(subnet_mask_octets[3]) in valid_subnet_masks) \
           and (int(subnet_mask_octets[0]) >= int(subnet_mask_octets[1]) >= int(subnet_mask_octets[2]) >= int(
        subnet_mask_octets[3]))


if __name__ == "__main__":
    try:
        while True:
            ip_address = input("\nEnter an IPv4 address: ")
            if is_valid_ip_address(ip_address):
                break
            else:
                print("\nThe IP address is INVALID, enter a valid IPv4 address!")
                continue
        while True:
            subnet_mask = input("\nEnter a subnetmask: ")
            if is_valid_subnet_mask(subnet_mask):
                break
            else:
                print("\nThe subnetmask is INVALID, enter a valid subnetmask!")
                continue

    except KeyboardInterrupt:
        print("/n Interrupted /n")
        sys.exit()
