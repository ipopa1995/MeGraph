import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_nodes_from([('1', {'label': 'FrankfurtTrainStation', 'station': 'Frankfurt Hbf'}),
                  ('9', {'label': 'FrankfurtTrainStation', 'station': 'Frankfurt Südbahnhof'}),
                  ('15', {'label': 'FrankfurtTrainStation', 'station': 'Frankfurt Westbahnhof'}),
                  ('18', {'label': 'FrankfurtTrainStation', 'station': 'Frankfurt Ostbahnhof'}),
                  ('20', {'label': 'FrankfurtTrainStation', 'station': 'Lokalbahnhof'})])


G.add_nodes_from([('5', {'label': 'FairStation', 'station': 'Festhalle/Messe'}),
                  ('14', {'label': 'FariStation', 'station': 'Messe'})])


G.add_nodes_from([('2', {'label': 'CenterCity', 'station': 'Tanusanlage'}),
                  ('3', {'label': 'CenterCity', 'station': 'Willy-Brand-Platz'}),
                  ('4', {'label': 'CenterCity', 'station': 'Hauptwache'}),
                  ('12', {'label': 'CenterCity', 'station': 'Dom/Römer'}),
                  ('11', {'label': 'CenterCity', 'station': 'Konstablerwache'})])

G.add_nodes_from([('6', {'label': 'UniverityCampus', 'station': 'Bockenheimer Warte'}),
                  ('7', {'label': 'UniverityCampus', 'station': 'Niederrrad'})])

G.add_node('8', label='FootbalStadium', station='Frankfurt Stadium')
G.add_node('16', label='Airport', station='Frankfurt Flughafen')
G.add_node('17', label='Zoo', station='Zoo')

G.add_nodes_from([('10', {'label': 'FrankfurtStation', 'station': 'Schweizerplatz'}),
                  ('13', {'label': 'FrankfurtStation', 'station': 'Frankfurt Griesheim'}),
                  ('19', {'label': 'FrankfurtStation', 'station': 'Ostendstraße'})])

G.add_edges_from([('1', '2'), ('2', '4'), ('4', '11'), ('11', '19'), ('19', '20'), ('20', '9'),
                  ('1', '7'), ('7', '8'), ('8', '16'),
                  ('1', '13'), ('1', '14'),('14', '15')],
                 type='S_Bahn')

G.add_edges_from([('1', '3'), ('4', '3'), ('3', '12'), ('3', '10'),('10', '9'), ('1', '5'), ('5', '6'), ('11', '17'), ('17', '18'), ('11', '12')],
                 type='U_Bahn')

G.add_edges_from([('1', '9'), ('9', '18')],
                 type='RE/RB_Bahn')
print(G.nodes)

pos = nx.circular_layout(G)
nx.draw(G, pos)


node_labels = nx.get_node_attributes(G, 'station')
edge_labels = nx.get_edge_attributes(G, 'type')
formatted_edge_labels = {(elem[0],elem[1]):edge_labels[elem] for elem in edge_labels}

nx.draw_networkx_labels(G, pos, labels=node_labels)
nx.draw_networkx_edge_labels(G,pos,edge_labels=formatted_edge_labels,font_color='red')

plt.show()