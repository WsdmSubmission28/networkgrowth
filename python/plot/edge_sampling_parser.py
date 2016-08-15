import numpy as np
import pandas as pd
from scipy import stats, integrate
import matplotlib.pyplot as plt
import seaborn as sns
import math



class EdgeSamplingParser:

  def run(self,folder):
    header = ["node_num","non_zero_num","zero_num","avg_degree","edge_num","influence_num","homophily_num","random_num","p_0","p_1","p_2","p_3","p_4","p_5","p_6","p_7","p_8","p_9",'trans','avgc']
    self.data = {}
    for d in ["oc","mh","15","fb","sl","wn","uc","lk","mu","en","db","wi"]:
      self.data[d] = pd.read_csv(folder + "path_" + d, sep=' ', header=None,names=header)
      self.data["r_" + d] = pd.read_csv(folder + "path_r_" + d, sep=' ', header=None,names=header)
    return self.data


