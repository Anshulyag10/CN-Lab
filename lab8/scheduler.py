# scheduler.py
# FIFO and Priority schedulers for packets.

from dataclasses import dataclass
from typing import List
import heapq


@dataclass
class Packet:
    source_ip: str
    dest_ip: str
    payload: str
    priority: int  # 0=High, 1=Medium, 2=Low


def fifo_scheduler(packet_list: List[Packet]) -> List[Packet]:
    
    return list(packet_list)


def priority_scheduler(packet_list: List[Packet]) -> List[Packet]:
    
    # attach arrival index to preserve original order for ties
    enumerated = [(pkt.priority, idx, pkt) for idx, pkt in enumerate(packet_list)]
    enumerated.sort(key=lambda x: (x[0], x[1]))
    return [t[2] for t in enumerated]


if __name__ == "__main__":
    packets = [
        Packet("10.0.0.1", "10.0.0.2", payload="Data Packet 1", priority=2),
        Packet("10.0.0.3", "10.0.0.4", payload="Data Packet 2", priority=2),
        Packet("10.0.0.5", "10.0.0.6", payload="VOIP Packet 1", priority=0),
        Packet("10.0.0.7", "10.0.0.8", payload="Video Packet 1", priority=1),
        Packet("10.0.0.9", "10.0.0.10", payload="VOIP Packet 2", priority=0),
    ]

    fifo_out = fifo_scheduler(packets)
    print("FIFO output payload order:")
    print([p.payload for p in fifo_out])
    
    prio_out = priority_scheduler(packets)
    print("Priority scheduler output payload order:")
    print([p.payload for p in prio_out])
    

