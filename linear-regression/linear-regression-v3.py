"""

V3 - Normalized

Input Parameters (3)

1. Number of Worker Nodes
2. Number of Container
3. Container CPU Utilization Sum (nano cores)

"""

import util.lrtrainer as lrt

# Sample
X_sample = [[2, 4, 2460314074.985385]]
lrt.train_model('final-test-data-v3.csv', X_sample, 8.508, 'v3', True)
