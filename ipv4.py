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


def ip_calculator(subnet_mask):
    subnet_mask_binaries, subnet_mask_decimal_octets = get_subnet_mask_octets(subnet_mask)
    zeros_in_subnet_mask = subnet_mask_binaries.count("0")
    mask_bits = 32 - zeros_in_subnet_mask
    hosts = (2 ** zeros_in_subnet_mask) - 2
    return mask_bits, hosts


def get_subnet_mask_octets(subnet_mask):
    subnet_mask_decimal_octets = subnet_mask.split(".")
    subnet_mask_binary_octets = []
    for octet in range(0, len(subnet_mask_decimal_octets)):
        subnet_mask_binary = bin(int(subnet_mask_decimal_octets[octet])).split("b")[1]
        if len(subnet_mask_binary) == 8:
            subnet_mask_binary_octets.append(subnet_mask_binary)
        elif len(subnet_mask_binary) < 8:
            subnet_mask_binary_completed_octet = subnet_mask_binary.zfill(8)
            subnet_mask_binary_octets.append(subnet_mask_binary_completed_octet)
    return "".join(subnet_mask_binary_octets), subnet_mask_decimal_octets


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

        mask_bits, hosts = ip_calculator(subnet_mask)

        print("\nThe number of mask bits is: %s" % mask_bits)
        print("\nThe number of valid hosts per subnet is: %s" % hosts)

    except KeyboardInterrupt:
        print("/n Interrupted /n")
        sys.exit()
