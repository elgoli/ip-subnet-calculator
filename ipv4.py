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


def ip_calculator(ip_address, subnet_mask):
    subnet_mask_binaries, subnet_mask_decimal_octets = get_subnet_mask_octets(subnet_mask)
    zeros_in_subnet_mask = subnet_mask_binaries.count("0")
    mask_bits = 32 - zeros_in_subnet_mask
    hosts = (2 ** zeros_in_subnet_mask) - 2
    wildcard_mask = get_wildcard_mask(subnet_mask_decimal_octets)
    ip_binary = get_ip_binary(ip_address)
    network_address = get_network_address(ip_binary, mask_bits, zeros_in_subnet_mask)
    broadcast_ip_address = get_broadcast_address(ip_binary, mask_bits, zeros_in_subnet_mask)
    return mask_bits, hosts, wildcard_mask, network_address, broadcast_ip_address


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


def get_wildcard_mask(subnet_mask_decimal_octets):
    wildcard_mask_octets = []
    for octets in subnet_mask_decimal_octets:
        wildcard_mask_octet = 255 - int(octets)
        wildcard_mask_octets.append(str(wildcard_mask_octet))
    wildcard_mask = ".".join(wildcard_mask_octets)
    return wildcard_mask


def get_ip_binary(ip_address):
    ip_decimal_octets = ip_address.split(".")
    ip_binary_octets = []
    for octets in range(0, len(ip_decimal_octets)):
        ip_binary_octet = bin(int(ip_decimal_octets[octets])).split("b")[1]
        if len(ip_binary_octet) == 8:
            ip_binary_octets.append(ip_binary_octet)
        elif len(ip_binary_octet) < 8:
            ip_binary_completed_octet = ip_binary_octet.zfill(8)
            ip_binary_octets.append(ip_binary_completed_octet)
    return "".join(ip_binary_octets)


def get_network_address(ip_binary, mask_bits, zeros_in_subnet_mask):
    network_address_binary = ip_binary[:mask_bits] + "0" * zeros_in_subnet_mask
    network_address_octets = []
    for octet in range(0, len(network_address_binary), 8):
        network_address_octet = network_address_binary[octet:octet + 8]
        network_address_octets.append(network_address_octet)
    network_address = []
    for octet in network_address_octets:
        network_address.append(str(int(octet, 2)))
    return ".".join(network_address)


def get_broadcast_address(ip_binary, no_ones_in_subnet_mask, no_zeros_in_subnet_mask):
    broadcast_address_binary = ip_binary[:no_ones_in_subnet_mask] + ("1" * no_zeros_in_subnet_mask)
    broadcast_address_octets = []
    for octet in range(0, len(broadcast_address_binary), 8):
        broadcast_octet = broadcast_address_binary[octet:octet + 8]
        broadcast_address_octets.append(broadcast_octet)
    broadcast_address = []
    for octet in broadcast_address_octets:
        broadcast_address.append(str(int(octet, 2)))
    return ".".join(broadcast_address)


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

        mask_bits, hosts, wildcard_mask, network_address, broadcast_ip_address = ip_calculator(ip_address, subnet_mask)

        print("\nThe number of mask bits: %s" % mask_bits)
        print("\nThe number of valid hosts per subnet: %s" % hosts)
        print("\nThe wildcard mask: %s" % wildcard_mask)
        print("\nThe network address: %s" % network_address)
        print("\nThe broadcast address: %s" % broadcast_ip_address)

    except KeyboardInterrupt:
        print("/n Interrupted /n")
        sys.exit()
