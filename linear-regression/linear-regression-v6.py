"""

V6 - Normalized

Input Parameters (4)

1. Number of Worker Nodes
2. Number of Containers
3. Squared Number of Containers
4. Container CPU Utilization Sum (nano cores)

"""

import util.lrtrainer as lrt

# Sample
X_sample = [[2, 4, 4, 2460314075]]
lrt.train_model('final-test-data-v6.csv', X_sample, 8.508, 'v6', True)
