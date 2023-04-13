"""

V4 - Normalized

Input Parameters (2)

1. Number of Worker Nodes
2. Container CPU Utilization Sum (nano cores)

"""

import util.lrtrainer as lrt

# Sample
X_sample = [[2, 2460314074.985385]]

lrt.train_model('final-test-data-v4.csv', X_sample, 8.508, 'v4', True)
