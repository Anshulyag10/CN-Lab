# part3_bgp.py
import networkx as nx

class BGP_Router:
    def __init__(self, as_num):
        self.as_num = as_num
        self.tbl = {}
        self.tbl[f"AS{as_num}_pfx"] = {'path': [self.as_num], 'next': 'self'}

    def rx_update(self, nbr_as, nbr_tbl):
        updated = False
        for pfx, info in nbr_tbl.items():
            
            if self.as_num in info['path']:
                continue
            
            new_path = [self.as_num] + info['path']
            
            if pfx not in self.tbl:
                self.tbl[pfx] = {'path': new_path, 'next': f"AS{nbr_as}"}
                updated = True
            else:
                curr_len = len(self.tbl[pfx]['path'])
                new_len = len(new_path)
                
                if new_len < curr_len:
                    self.tbl[pfx] = {'path': new_path, 'next': f"AS{nbr_as}"}
                    updated = True
        return updated

    def print_tbl(self):
        print(f"--- BGP Table for AS {self.as_num} ---")
        print("Prefix\t\tNext Hop\tAS Path")
        print("-------------------------------------------------")
        for pfx, info in self.tbl.items():
            path_str = " -> ".join(map(str, info['path']))
            print(f"{pfx}\t{info['next']}\t\t{path_str}")
        print("\n")

def sim_bgp(net):
    routers = {as_num: BGP_Router(as_num) for as_num in net.nodes()}

    converged = False
    i = 0
    print("--- Starting BGP ---")
    
    while not converged:
        i += 1
        print(f"\n--- Iteration {i} ---")
        
        curr_tbls = {as_num: r.tbl.copy() for as_num, r in routers.items()}
        updated = False
        
        for as_num, r in routers.items():
            for nbr_as in net.neighbors(as_num):
                nbr_r = routers[nbr_as]
                if nbr_r.rx_update(as_num, curr_tbls[as_num]):
                    updated = True
        
        if not updated:
            converged = True
            print(f"--- Converged after {i} iterations ---")
        
        if i > len(routers) * 2:
            print("Stopping: possible oscillation.")
            break

    print("\n--- Final BGP Tables ---")
    for r in routers.values():
        r.print_tbl()

if __name__ == "__main__":
    G = nx.Graph()
    G.add_edges_from([
        (100, 200), (100, 300), (200, 400),
        (300, 400), (300, 500), (400, 500)
    ])
    sim_bgp(G)