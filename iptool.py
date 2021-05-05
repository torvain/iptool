#!/usr/bin/env python3

import argparse
import ipaddress
import sys

def network_address(ip):
    return str(ip.network).split('/')[0]

def broadcast_address(ip):
    return str(ip.network.broadcast_address).split('/')[0]

def subnet_mask(ip):
    return ip.with_netmask.split('/')[1]

def subnet_len(ip):
    return ip.with_prefixlen.split('/')[1]

def first_ip(ip):
    return str(list(ip.network.hosts())[0])

def last_ip(ip):
    return str(list(ip.network.hosts())[-1])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("ip/mask", help="IP address in x.x.x.x/netmask form")
    arg_group = parser.add_mutually_exclusive_group(required=True)

    arg_group.add_argument("--network-address", help="Show network address", action="store_true")
    arg_group.add_argument("--broadcast-address", help="Show broadcast address", action="store_true")
    arg_group.add_argument("--subnet-mask", help="Show subnet mask as x.x.x.x", action="store_true")
    arg_group.add_argument("--subnet-len", help="Show subnet length as a digit (/24)", action="store_true")
    arg_group.add_argument("--first-ip", help="Show first IP address in the subnet", action="store_true")
    arg_group.add_argument("--last-ip", help="Show last IP address in the subnet", action="store_true")
    args = parser.parse_args()

    functions = {'network_address' : network_address,
                 'broadcast_address' : broadcast_address,
                 'subnet_mask' : subnet_mask,
                 'subnet_len' : subnet_len,
                 'first_ip' : first_ip,
                 'last_ip' : last_ip
                 }

    # put the args into a dict
    opts = vars(args)
    # first entry is the IP address
    ip = ipaddress.ip_interface(opts.pop('ip/mask'))

    for o in opts:
        if(opts[o]):
            print(functions[o](ip))


if __name__ == "__main__":
    main()
