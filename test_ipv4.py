import unittest

import ipv4


class IpCalculator(unittest.TestCase):

    def test_is_valid_ip_address(self):
        self.assertFalse(ipv4.is_valid_ip_address("0.0.0.1"))
        self.assertTrue(ipv4.is_valid_ip_address("172.16.0.1"))

    def test_is_valid_subnet_mask(self):
        self.assertFalse(ipv4.is_valid_subnet_mask("1.0.0.0"))
        self.assertTrue(ipv4.is_valid_subnet_mask("255.0.0.0"))

    def test_ip_calculator(self):
        mask_bits, hosts, wildcard_mask, network_address, broadcast_ip_address = \
            ipv4.ip_calculator("192.168.1.1", "255.255.255.0")

        self.assertEqual(mask_bits, 24)
        self.assertEqual(hosts, 254)
        self.assertEqual(wildcard_mask, "0.0.0.255")
        self.assertEqual(network_address, "192.168.1.0")
        self.assertEqual(broadcast_ip_address, "192.168.1.255")
