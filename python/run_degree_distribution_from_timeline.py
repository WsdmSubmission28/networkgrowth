import sys
from network_stats.degree_distribution_from_timeline import DegreeDistributionFromTimeline

file_name = sys.argv[1]
out_location = sys.argv[2]
prefix = sys.argv[3]

degree_distribution = DegreeDistributionFromTimeline(file_name,out_location,prefix)
degree_distribution.run()
