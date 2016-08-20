import sys
from network_stats.network_global_stats_timeline import NetworkGlobalStatsFromTimeline

file_name = sys.argv[1]
out_file_name = sys.argv[2]

network_global_stats = NetworkGlobalStatsFromTimeline(file_name,out_file_name)
network_global_stats.run()
