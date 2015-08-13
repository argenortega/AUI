__author__ = 'Argen'

import networkx as nx
import matplotlib.pyplot as plt
import pylab as pl
import pymc as mc

from pymc.examples import disaster_model

G = nx.Graph()
nx.draw(G)
plt.show()


'''
G.add_nodes_from([2,3])
H=nx.path_graph(10)
G.add_node(H)

G.add_edge(1,2)
e=(2,3)
G.add_edge(*e)# unpack edge tuple*
G.add_edges_from([(1,2),(1,3)])
'''

'''
nodename = pymc.Bernoulli('nodename', 0.2)
probNodeName = mc.Lambda('probNodeName', lambda conditionalNode = conditionalNode: pylab.where(conditionalNode, 0.01, 0.4))
nodename = mc.Bernoulli('nodename', probNodeName)
value=[1.0], observed=True


# sprinkler.py
'''
G_obs = [1.]
print G
N = len(G_obs)
print N


R = mc.Bernoulli('R', .2, value=pl.ones(N))

p_S = mc.Lambda('p_S', lambda R=R: pl.where(R, .01, .4),
                doc='Pr[S|R]')
S = mc.Bernoulli('S', p_S, value=pl.ones(N))

p_G = mc.Lambda('p_G', lambda S=S, R=R:
                pl.where(S, pl.where(R, .99, .9), pl.where(R, .8, 0.)),
                doc='Pr[G|S,R]')
G = mc.Bernoulli('G', p_G, value=G_obs, observed=True)

m.nodename.stats()['mean']
