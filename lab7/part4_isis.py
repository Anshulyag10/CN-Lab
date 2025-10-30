# part4_isis.py
import networkx as nx

def sim_isis(net):
    print("--- Starting IS-IS ---")
    all_nodes = list(net.nodes())
    
    for r_name in all_nodes:
        print(f"\n--- Calculations for {r_name} ---")
        
        lengths = nx.single_source_dijkstra_path_length(net, r_name, weight='weight')
        paths = nx.single_source_dijkstra_path(net, r_name, weight='weight')
        
        print(f"Table for {r_name}:")
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
    G.add_edge('R1', 'R2', weight=10)
    G.add_edge('R1', 'R3', weight=5)
    G.add_edge('R2', 'R4', weight=20)
    G.add_edge('R3', 'R4', weight=10)
    G.add_edge('R3', 'R5', weight=15)
    G.add_edge('R4', 'R5', weight=5)
    
    sim_isis(G)