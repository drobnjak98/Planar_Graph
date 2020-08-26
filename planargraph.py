# -*- coding: utf-8 -*-

import networkx as nx
import matplotlib.pyplot as plt

graph = {'s1': ['v', 't1','w'],
     's2': ['t1','s1'],
     's3': ['v','w'],
     's4': ['x','y'],
     'x': ['v','w'],
     'v': ['t1', 'w'],
     'w': ['y','t1','t2'],
     'y': ['v','t1','t2'],
     't1': [],
     't2': [],
     }
graph

def planar(G):
    fig = plt.figure()
    fig.show()

    graph = nx.DiGraph()

    for v in G.keys():
        graph.add_node(v)

    for delta in G.items():
        for w in delta[1]:
            graph.add_edge(delta[0],w)

    nx.draw_planar(graph,with_labels = True, alpha=1)
    fig.canvas.draw()
    plt.show()
    
def nonplanar(G):
    fig = plt.figure()
    fig.show()

    graph = nx.DiGraph()

    for v in G.keys():
        graph.add_node(v)

    for delta in G.items():
        for w in delta[1]:
            graph.add_edge(delta[0],w)
    nx.draw_networkx(graph, with_labels = True, alpha=1)

    fig.canvas.draw()
    plt.show()
        

    nonplanar(graph)
    planar(graph)
    