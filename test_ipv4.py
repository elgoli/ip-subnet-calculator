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
        subnet_mask = "255.255.255.0"
        mask_bits = ipv4.ip_calculator(subnet_mask)
        self.assertEqual(mask_bits, 24)
