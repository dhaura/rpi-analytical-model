"""

V1 - Not Normalized

Input Parameters (6)

1. Master CPU Utilization (nano cores)
2. Master Memory Utilization (KB)
3. Number of Worker Nodes
4. Number of Containers
5. Container CPU Utilization Sum (nano cores)
6. Container Memory Utilization Sum (KB)

"""

import util.lrtrainer as lrt

# Sample
X_sample = [[1187612200.712264, 673290.5449273121, 2, 4, 2460314074.985385, 311636.2853386947]]
lrt.train_model('final-test-data-v1.csv', X_sample, 8.508, 'v1-not-normalized', False)
