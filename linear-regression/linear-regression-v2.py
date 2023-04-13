"""

V2 - Normalized

Input Parameters (4)

1. Number of Worker Nodes
2. Number of Container
3. Container CPU Utilization Sum (nano cores)
4. Container Memory Utilization Sum (KB)

"""

import util.lrtrainer as lrt

# Sample
X_sample = [[2, 4, 2460314074.985385, 311636.2853386947]]

lrt.train_model('final-test-data-v2.csv', X_sample, 8.508, 'v2', True)
