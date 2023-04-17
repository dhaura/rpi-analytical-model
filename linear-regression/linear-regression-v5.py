"""

V3 - Normalized

Input Parameters (4)

1. Number of Worker Nodes
2. Number of Containers
3. Container CPU Utilization Sum (nano cores)
4. Squared Container CPU Utilization Sum (nano cores)

"""

import util.lrtrainer as lrt

# Sample
X_sample = [[2, 4, 2460314075, 6053145347643110000]]
lrt.train_model('final-test-data-v5.csv', X_sample, 8.508, 'v5', True)
