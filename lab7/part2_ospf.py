# part2_ospf.py
import networkx as nx

def sim_ospf(net):
    print("--- Starting OSPF ---")
    all_nodes = list(net.nodes())
    
    for r_name in all_nodes:
        print(f"\n--- Calculations for {r_name} ---")
        
        lengths = nx.single_source_dijkstra_path_length(net, r_name, weight='weight')
        paths = nx.single_source_dijkstra_path(net, r_name, weight='weight')
        
        print(f"Paths from {r_name}:")
        for dest, p in paths.items():
            print(f"  To {dest}: {' -> '.join(p)} (Cost: {lengths[dest]})")
            
        print(f"\nTable for {r_name}:")
        print("Dest\tNext\tCost")
        print("--------------------")
        for dest in all_nodes:
            if dest == r_name:
                print(f"{dest}\t-\t0")
            else:
                next_hop = paths[dest][1] if len(paths[dest]) > 1 else '-'
                cost = lengths[dest]
                print(f"{dest}\t{next_hop}\t{cost}")

if __name__ == "__main__":
    G = nx.Graph()
    G.add_edge('A', 'B', weight=4)
    G.add_edge('A', 'C', weight=2)
    G.add_edge('B', 'D', weight=3)
    G.add_edge('B', 'C', weight=5)
    G.add_edge('C', 'E', weight=1)
    G.add_edge('D', 'E', weight=6)
    G.add_edge('D', 'F', weight=8)
    G.add_edge('E', 'F', weight=7)
    
    sim_ospf(G)