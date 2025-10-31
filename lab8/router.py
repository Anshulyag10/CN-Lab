# router.py

from typing import List, Tuple
from ip_utils import ip_to_binary, get_network_prefix


class Router:
    def __init__(self, routes: List[Tuple[str, str]]):
       
        self._table = []
        self.build_forwarding_table(routes)

    def build_forwarding_table(self, routes: List[Tuple[str, str]]):
        
        table = []
        for cidr, link in routes:
            try:
                prefix_bits = get_network_prefix(cidr)
                prefix_length = len(prefix_bits)
                table.append((prefix_bits, prefix_length, link))
            except ValueError as e:
                # Skip invalid routes but notify (could also raise)
                raise ValueError(f"Invalid route '{cidr}' in routes: {e}")
        # Sort longest prefixes first
        table.sort(key=lambda item: item[1], reverse=True)
        self._table = table

    def route_packet(self, dest_ip: str) -> str:
        
        try:
            dest_bits = ip_to_binary(dest_ip)
        except ValueError:
            return "Default Gateway"

        for prefix_bits, prefix_length, link in self._table:
            if dest_bits.startswith(prefix_bits):
                return link
        return "Default Gateway"



if __name__ == "__main__":
    routes = [
        ("223.1.1.0/24", "Link 0"),
        ("223.1.2.0/24", "Link 1"),
        ("223.1.3.0/24", "Link 2"),
        ("223.1.0.0/16", "Link 4 (ISP)"),
    ]
    r = Router(routes)

    tests = {
        "223.1.1.100": "Link 0",
        "223.1.2.5": "Link 1",
        "223.1.250.1": "Link 4 (ISP)",
        "198.51.100.1": "Default Gateway",
    }

    print("Router LPM test results:")
    for ip, expected in tests.items():
        out = r.route_packet(ip)
        ok = "OK" if out == expected else "FAIL"
        print(f"{ip} -> {out} (expected: {expected}) [{ok}]")

