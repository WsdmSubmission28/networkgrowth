import sys
import math
from models.ex_runner import ExponentialModelRunner
from multiprocessing.pool import ThreadPool



sizes = []
for n in range(6,18):
  size = math.pow(2,n)
  sizes.append(size)

folder = sys.argv[1]
parameters = sys.argv[2].split(",")
p = parameters[0]
q = parameters[1]
r = parameters[2]
s = parameters[3]
N = parameters[4]
idx = parameters[5]
model_runner = ExponentialModelRunner(folder,sizes,idx)
model_runner.run(p,q,r,s,N)
