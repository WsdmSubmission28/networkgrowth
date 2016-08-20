import networkx as nx
import random as rnd
import sys
import copy
import math

class ExponentialModel:

  def __init__(self,p,q,r,s,N):
    self.p = float(p)
    self.q = float(q)
    self.r = float(r)
    self.s = float(s)
    self.N = int(N)
    self.G = nx.Graph()
    self.F = nx.Graph()
    self.node = 0
    self.homo = 1
    e = (self.p + self.r)/(self.p + self.q + 2 * self.r) * self.N
    print e
    for i in range(self.N):
      self.F.add_node(self.node)
      self.G.add_node(self.node)
      self.node+=1
    for i in range(int(e+1)):
      self.G.add_edge(i,i+1)
    self.F.add_edge(0,2)
    self.F.add_edge(3,5)

  def run(self,node_num):
    while self.node < node_num:
      n = self.node
      print n,self.G.number_of_edges()*2/float(self.G.number_of_nodes()),self.F.number_of_edges(),self.homo
      self.homophily()
      self.random_edge(n)
      self.random_influence(n)
      self.random_root(n)

  def homophily(self):
      idxs =  range(self.F.number_of_nodes())
      rnd.shuffle(idxs)
      for j in range(self.F.number_of_nodes()):
        idx = idxs[j]
        num = float(self.F.degree()[idx]) * self.s
        num = self.get_rand(num)
        for k in range(num):
          l= self.pref(self.G)
          while l == idx or self.F.has_edge(idx,l) or self.G.has_edge(idx,l):
            l = self.pref(self.G)
          self.G.add_edge(idx,l)
          self.F.add_edge(idx,l)

  def random_root(self,n):
    num = self.get_rand(n * self.q)
    for l in range(num):
      self.F.add_node(self.node)
      self.G.add_node(self.node)
      self.node+=1

  def random_edge(self,n):
    num = self.get_rand(n * self.r)
    for l in range(num):
      self.G.add_edge(self.node,self.node+1)
      self.F.add_node(self.node)
      self.F.add_node(self.node+1)
      self.node+=2


  def random_influence(self,n):
    num = self.get_rand(n * self.p)
    for l in range(num):
      k = rnd.randint(0,self.G.number_of_nodes()-1)
      self.G.add_edge(self.node,k)
      self.F.add_node(self.node)
      self.node+=1

  def pref(self,graph):
    num = rnd.randint(0,graph.number_of_edges()*2)
    degrees = graph.degree()
    ii = 0
    summ=degrees[ii]
    while summ < num:
      ii+=1;
      summ+=degrees[ii]
    return ii

  def get_rand(self,val):
    if val > 0 and rnd.random() < (val-int(val)):
      return int(val + 1)
    return int(val)
