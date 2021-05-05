#!/usr/bin/env python3 

import ipaddress
import unittest

import iptool

class TestIP(unittest.TestCase):
    #ip = ipaddress.ip_interface('192.168.3.45/24')

    ips = {'192.168.3.45/24': {'address' : ipaddress.ip_interface('192.168.3.45/24'),
                               'broadcast_address' : '192.168.3.255',
                               'network_address' : '192.168.3.0',
                               'subnet_mask' : '255.255.255.0',
                               'first_ip' : '192.168.3.1' ,
                               'last_ip' : '192.168.3.254',
                              },
           '10.16.128.217/23': {'address' : ipaddress.ip_interface('10.16.218.217/23'),
                               'broadcast_address' : '10.16.219.255',
                               'network_address' : '10.16.218.0',
                               'subnet_mask' : '255.255.254.0',
                               'first_ip' : '10.16.218.1' ,
                               'last_ip' : '10.16.219.254',
                              }
          }

    def test_broadcast(self):
        for ip in self.ips:
            self.assertEqual(iptool.broadcast_address(self.ips[ip]['address']), self.ips[ip]['broadcast_address'])

    def test_network_address(self):
        for ip in self.ips:
            self.assertEqual(iptool.network_address(self.ips[ip]['address']), self.ips[ip]['network_address'])

    def test_subnet_mask(self):
        for ip in self.ips:
            self.assertEqual(iptool.subnet_mask(self.ips[ip]['address']), self.ips[ip]['subnet_mask'])

    def test_first_address(self):
        for ip in self.ips:
            self.assertEqual(iptool.first_ip(self.ips[ip]['address']), self.ips[ip]['first_ip'])

    def test_last_address(self):
        for ip in self.ips:
            self.assertEqual(iptool.last_ip(self.ips[ip]['address']), self.ips[ip]['last_ip'])

if __name__ == "__main__":
    unittest.main()
