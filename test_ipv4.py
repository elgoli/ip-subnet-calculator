import unittest

import ipv4


class IpCalculator(unittest.TestCase):

    def test_is_valid_ip_address(self):
        self.assertFalse(ipv4.is_valid_ip_address("0.0.0.1"))
        self.assertTrue(ipv4.is_valid_ip_address("172.16.0.1"))
