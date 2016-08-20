import sys
import math


class NetworkGlobalStatsFromTimeline:

  def __init__(self,file_name,out_file):
    self.f = open(file_name,'r')
    self.f_out = open(out_file,'w')
    self.f_out.write("node_num,zero_num,non_zero_num,avg_degree,max_degree,d/K-1")
    self.node_num = 0
    self.zero_num = 0
    self.avg_degree = 0
    self.edge_num = 0
    self.degrees = {}
    self.max_degree = 0

  def run(self):
    scale = 1
    for line in self.f:
      records = line.split(" ")
      node_a = int(records[1])
      node_b = int(records[2])
      self.add_node(node_a)
      self.add_node(node_b)
      self.update_degrees(node_a,node_b)
      log_size = int(math.log(len(self.degrees),2))
      if log_size >= scale:
        self.write_into_file(scale)
        scale+=1
    self.write_into_file(scale)

  def add_node(self,node):
    if node != - 1 and node not in self.degrees:
      self.degrees[node] = 0
      self.zero_num+=1

  def update_degrees(self,node_a,node_b):
    if node_b != -1:
      self.degrees[node_a]+=1
      self.degrees[node_b]+=1
      self.edge_num+=1
      if self.degrees[node_a] == 1:
        self.zero_num-=1
      if self.degrees[node_b] == 1:
        self.zero_num-=1
      if self.degrees[node_a] > self.max_degree:
        self.max_degree = self.degrees[node_a]
      if self.degrees[node_b] > self.max_degree:
        self.max_degree = self.degrees[node_b]

  def write_into_file(self,scale):
    self.node_num = len(self.degrees)
    self.non_zero_num = self.node_num - self.zero_num
    self.avg_degree = self.edge_num * 2 / float(self.node_num)
    self.f_out.write(str(self.node_num) + ",")
    self.f_out.write(str(self.zero_num) + ",")
    self.f_out.write(str(self.non_zero_num) + ",")
    self.f_out.write(str(self.avg_degree) + ",")
    self.f_out.write(str(self.max_degree) + ",")
    if self.non_zero_num > 0:
      self.f_out.write(str(self.avg_degree / float(self.non_zero_num) * float(self.node_num) -1) + "\n")
    else:
      self.f_out.write( "0\n")
