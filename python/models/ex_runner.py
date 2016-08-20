import sys
import networkx as nx
import pandas as pd
from models.ex import ExponentialModel
from network_global_stats.average_degree import AvgDegree
import math
from ml.ml import ML
import numpy as np
from multiprocessing.pool import ThreadPool


class ExponentialModelRunner:

  def __init__(self,folder,sizes,idx):
    self.sizes = sizes
    self.folder = folder
    self.idx = idx

  def run(self,p,q,r,s,N):
    G = nx.Graph()
    model = ExponentialModel(p,q,r,s,N)
    for size in self.sizes:
      model.run(size)
      self.write_out(size,model)

  def write_out(self,size,model):
    data = self.compute_distribution(model.G)
    self.write_out_distribution(size,model,data)
    if (len(data) >= 3):
      (avg,ml) = self.compute_stats(data)
      self.write_out_stats(size,model,avg,ml)

  def compute_distribution(self,G):
    degrees = G.degree()
    dist = {}
    for node in degrees:
      degree = degrees[node]
      if degree not in dist:
        dist[degree] = 0
      dist[degree]+=1
    data = []
    for degree in dist:
      data.append([degree,dist[degree]])  
    return np.array(data)

  def compute_stats(self,data):
    avg = AvgDegree(data,0,1)
    avg.run()
    avg = avg.get()
    ml = ML(data,0,1)
    ml.compute_alphas()
    ml.compute_KS()
    return (avg,ml)

  def write_out_distribution(self,size,model,data):
    f_out = open(self.folder + "/dist_ex_" + str(int(size)) + "_" + str(model.p) + "_" + str(model.q) + "_" + str(model.r) + "_" + str(model.s) + "_" + str(model.N)  + "_" + str(self.idx),"w")
    for i in range(len(data)):
      f_out.write(str(data[i][0]) + " " + str(data[i][1]) + "\n")
    f_out.close()
    out = self.folder + "/graph_ex_" + str(int(size)) + "_" + str(model.p) + "_" + str(model.q) + "_" + str(model.r) + "_" + str(model.s) + "_" + str(model.N)  + "_" + str(self.idx)
    nx.write_edgelist(model.G,out)

  def write_out_stats(self,size,model,avg,ml):
    f_out = open(self.folder + "/stats_ex_" + str(model.p) + "_" + str(model.q) + "_" + str(model.r) + "_" + str(model.s) + "_" + str(model.N) + "_" + str(self.idx),'a')
    (alpha , xmin, ks )= ml.get_best_KS()
    f_out.write(str(size) + " ")
    f_out.write(str(alpha - 2) + " ")
    f_out.write(str(avg)  + " ")
    f_out.write(str(ml.alphas[-1] - 2) + " " )
    f_out.write(str(1 / float(alpha - 2))  + " ")
    f_out.write(str(1 / float(avg - 1))  + "\n")
    f_out.close()
