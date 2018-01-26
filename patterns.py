
# Format apppears as
# 1 if increase
# -1 if decrease
# 0 if static
# Example:
#   [1,1,1,-1,-1,-1]
#   Peak
def pattern_search(data,max_period,min_period,format):
    for x in range(min_period,max_period):
        for y in range(min_period,len(data)):

