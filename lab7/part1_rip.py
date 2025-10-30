# part1_rip.py
import networkx as nx

class Router:
    def __init__(self, name):
        self.name = name
        self.tbl = {name: {'next': name, 'cost': 0}}

    def init_tbl(self, all_nodes):
        for n in all_nodes:
            if n != self.name:
                self.tbl[n] = {'next': None, 'cost': float('inf')}

    def update(self, nbr, nbr_tbl):
        updated = False
        for dest, info in nbr_tbl.items():
            cost_to_nbr = self.tbl[nbr.name]['cost']
            cost_from_nbr = info['cost']
            
            new_cost = cost_to_nbr + cost_from_nbr
            
            if new_cost < self.tbl[dest]['cost']:
                self.tbl[dest] = {'next': nbr.name, 'cost': new_cost}
                updated = True
        return updated

    def print_tbl(self):
        print(f"--- Table for {self.name} ---")
        print("Dest\tNext\tCost")
        print("--------------------")
        for dest, info in self.tbl.items():
            print(f"{dest}\t{info['next']}\t{info['cost']}")
        print("\n")

def sim_rip(net):
    routers = {name: Router(name) for name in net.nodes()}
    all_names = list(routers.keys())
    
    for r_name, r in routers.items():
        r.init_tbl(all_names)
        for nbr in net.neighbors(r_name):
            r.tbl[nbr] = {'next': nbr, 'cost': 1}

    converged = False
    i = 0
    print("--- Starting RIP ---")
    while not converged:
        i += 1
        print(f"\n--- Iteration {i} ---")
        
        curr_tbls = {r_name: r.tbl.copy() for r_name, r in routers.items()}
        updated = False
        
        for r_name, r in routers.items():
            for nbr_name in net.neighbors(r_name):
                nbr = routers[nbr_name]
                if r.update(nbr, curr_tbls[nbr_name]):
                    updated = True

        if not updated:
            converged = True
            print(f"--- Converged after {i} iterations ---")
        
        if i > len(routers):
            print("Stopping: possible loop.")
            break

    print("\n--- Final Tables ---")
    for r in routers.values():
        r.print_tbl()

if __name__ == "__main__":
    G = nx.Graph()
    G.add_edges_from([
        ('A', 'B'), ('A', 'C'), ('B', 'D'), ('B', 'C'),
        ('C', 'E'), ('D', 'E'), ('D', 'F'), ('E', 'F')
    ])
    sim_rip(G)