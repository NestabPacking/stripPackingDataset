import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

def process_line(shared_dict,line):
    if line[0] =='#':
         return
    else:
        line = line.strip()
        s = line.split(' ')
        shared_dict['G'].add_edge(int(s[0]),int(s[1]))

def drawGraph(G,pos,Selnode,neighbors=False):
    
    # Get neighbors of node Selnode
    if neighbors:
        neighbors = list(G.neighbors(Selnode))
        node_colors = ['red' if node in neighbors else 'blue' if node == Selnode else 'lightblue' for node in G.nodes()]
    else:
        node_colors = ['blue' if node == Selnode else 'lightblue' for node in G.nodes()]
    plt.figure(figsize=(16, 12))
    plt.grid(True)
    plt.axhline(y=0, color='k', linestyle='-', alpha=0.3)
    plt.axvline(x=0, color='k', linestyle='-', alpha=0.3)
    

    nx.draw_networkx_nodes(G, pos,
                          node_color=node_colors,
                          node_size=20)

    plt.title('Nodes with Coordinate Axes')

def drawPolygons(polygons,label,linewidth,color='red'):
    
    for poly in polygons[:-1]:
        plt.gca().add_patch(Polygon(poly, fill=False, color=color,linewidth=linewidth, alpha=0.5))

    plt.gca().add_patch(Polygon(polygons[-1], fill=False, color=color,linewidth=linewidth, alpha=0.5,label=label))

