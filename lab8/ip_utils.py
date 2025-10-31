# ip_utils.py

from typing import Tuple


def ip_to_binary(ip_address: str) -> str:
    
    parts = ip_address.strip().split(".")
    if len(parts) != 4:
        raise ValueError(f"Invalid IPv4 address: {ip_address}")
    bin_octets = []
    for p in parts:
        try:
            octet = int(p)
        except ValueError:
            raise ValueError(f"Invalid octet '{p}' in IP address {ip_address}")
        if octet < 0 or octet > 255:
            raise ValueError(f"Octet out of range in IP address: {ip_address}")
        bin_octets.append(f"{octet:08b}")
    return "".join(bin_octets)


def get_network_prefix(ip_cidr: str) -> str:
  
    try:
        ip_part, prefix_len_str = ip_cidr.strip().split("/")
        prefix_len = int(prefix_len_str)
    except Exception:
        raise ValueError(f"Invalid CIDR notation: {ip_cidr}")

    if prefix_len < 0 or prefix_len > 32:
        raise ValueError(f"Invalid prefix length: {prefix_len} in {ip_cidr}")

    bin_ip = ip_to_binary(ip_part)
    return bin_ip[:prefix_len]


# Quick tests if run directly
if __name__ == "__main__":
    tests = [
        "192.168.1.1",
        "0.0.0.0",
        "255.255.255.255",
        "223.1.1.100",
    ]
    for t in tests:
        print(f"{t} -> {ip_to_binary(t)}")

    cidr_tests = [
        "200.23.16.0/23",
        "223.1.1.0/24",
        "10.0.0.0/8",
    ]
    for c in cidr_tests:
        print(f"{c} prefix bits -> {get_network_prefix(c)} (len={len(get_network_prefix(c))})")

