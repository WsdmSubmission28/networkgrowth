import numpy as np
import pandas as pd
from scipy import stats, integrate
import matplotlib.pyplot as plt
import seaborn as sns
import math
import itertools

class EdgeSampling:

  def __init__(self,data):
    self.data = data

  def plot(self):
    flatui = [ "#2ecc71", "#3498db", "#e74c3c"]
    marker = itertools.cycle(("o", "s", "^")) 
    sns.set_palette(sns.color_palette(flatui))
    fig, axes = plt.subplots(figsize=(16,18))
    i = 0
    for d in ["oc","15","mh","fb","db","wi"]:
      i+=1
      plt.subplot(4,2,i)
      plt.title(d, fontsize=30) 
      plt.plot(self.data[d]["node_num"],self.data[d]["influence_num"]/self.data[d]["edge_num"],'-o',label='I',marker=marker.next(),markersize = 15)
      plt.plot(self.data[d]["node_num"],(self.data[d]["random_num"])/self.data[d]["edge_num"],'-o',label='R',marker=marker.next(), markersize = 15)
      plt.plot(self.data[d]["node_num"],self.data[d]["homophily_num"]/self.data[d]["edge_num"],'-o',label='H',marker=marker.next(), markersize = 15)
#      plt.plot(self.data[d]["node_num"],(self.data[d]["p_2"])/self.data[d]["edge_num"],'-o',label='triangle',marker=marker.next())
      plt.grid(b=True, which='minor', linestyle='--')
      if i==1: 
        plt.legend(bbox_to_anchor=(0., 1, 2.3, 1), loc=3,ncol=3,mode="expand", borderaxespad=0.,markerscale=1.5,fontsize=28)
      plt.xscale('log')
      plt.xlabel("number of nodes")
      plt.ylabel("ratio")
      plt.gca().set_xlim(left=10)
      plt.ylim(0,1)
    plt.tight_layout()

  def plot_(self):
    flatui = [ "#2ecc71", "#3498db", "#e74c3c"]
    marker = itertools.cycle(("o", "s", "^", "v", ">", "<", "D","*")) 
    sns.set_palette(sns.color_palette(flatui))
    fig, axes = plt.subplots(figsize=(16,18))
    i = 0
    for d in ["oc","15","mh","fb","db","wi"]:
      i+=1
      plt.subplot(4,2,i)
      plt.title(d, fontsize=24) 
      plt.plot(self.data[d]["non_zero_num"],self.data[d]["influence_num"]/self.data[d]["non_zero_num"],'-o',label='I',marker=marker.next())
      plt.plot(self.data[d]["non_zero_num"],2*self.data[d]["random_num"]/self.data[d]["non_zero_num"],'-o',label='R',marker=marker.next())
      plt.plot(self.data[d]["non_zero_num"],(self.data[d]["random_num"]*2+self.data[d]["influence_num"])/self.data[d]["non_zero_num"],'-o',label='2R+I',marker=marker.next())
#      plt.plot(self.data[d]["node_num"],(self.data[d]["p_2"])/self.data[d]["edge_num"],'-o',label='triangle',marker=marker.next())
      plt.grid(b=True, which='minor', linestyle='--')
      plt.legend()
      plt.xscale('log')
      plt.xlabel("number of nodes")
      plt.ylabel("ratio")
      plt.gca().set_xlim(left=10)
      plt.ylim(0,1)
    plt.tight_layout()

