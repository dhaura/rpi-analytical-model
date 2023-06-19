"""

V7 - Normalized

Input Parameters (5)

1. Number of Worker Nodes
2. Number of Containers
3. Squared Number of Containers
4. Container CPU Utilization Sum (nano cores)
5. Squared Container CPU Utilization Sum (nano cores)

"""

import util.lrtrainer as lrt

# Sample
X_sample = [[2, 4, 4, 2460314075, 6053145347643110000]]
lrt.train_model('final-test-data-v7.csv', X_sample, 8.508, 'v7', True)
