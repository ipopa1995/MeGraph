import networkx as nx
import matplotlib.pyplot as plt

# Importing graphs from a file
G = nx.read_graphml('D:\Wiederhol\Python\Programme\MemeGraph\Meme2\graph.graphml')

# Layout of the Graph
pos= nx.circular_layout(G)

# Node lables
node_labels = nx.get_node_attributes(G,'label')
print(node_labels)

# Node sizes based on the length of the lable
node_sizes = []

# Node color based on the lable
node_colors = []

for i in node_labels.values():
   node_sizes.append(len(i)*1000)
   if i == 'Person':
      node_colors.append('red')
   elif i == 'Store':
      node_colors.append('orange')
   else:
       node_colors.append('white')   
      
violet_edge = [('1', '2')]
black_edges = [edge for edge in G.edges() if edge not in violet_edge]

#nx.draw(G,pos,arrows=True, node_size=node_sizes, node_color=node_colors, edgecolors='black', edgelist=violet_edge, edge_color='violet', arrowsize=20)
#nx.draw(G,pos,arrows=True, node_size=node_sizes, node_color=node_colors, edgecolors='black', edgelist=black_edges, edge_color='black', arrowsize=10)
#nx.draw_networkx_labels(G, pos, labels = node_labels, font_family='Times New Roman', font_size=16)

nx.draw_networkx_nodes(G, pos, node_size = node_sizes, node_color = node_colors, edgecolors='black',)
nx.draw_networkx_edges(G, pos, edgelist = violet_edge, arrows = True, edge_color = '#a020f0', arrowsize=40, node_size = node_sizes, width=2)
nx.draw_networkx_edges(G, pos, edgelist = black_edges, arrows = True, edge_color = 'black', arrowsize=20, node_size = node_sizes)
nx.draw_networkx_labels(G, pos, labels = node_labels, font_family='Times New Roman', font_size = 16)

ax = plt.gca()
ax.margins(0.30)
plt.axis('off')
plt.autoscale() 
plt.show() 

