import util.lrloader as lrd

# V1 - Not normalized
X_sample = [[1187612200.712264, 673290.5449273121, 2, 4, 2460314074.985385, 311636.2853386947]]
lrd.load_and_predict('final-test-data-v1.csv', X_sample, 8.508, 'v1-not-normalized', False)

# V1 - Normalized
X_sample = [[1187612200.712264, 673290.5449273121, 2, 4, 2460314074.985385, 311636.2853386947]]
lrd.load_and_predict('final-test-data-v1.csv', X_sample, 8.508, 'v1', True)

# V2
X_sample = [[2, 4, 2460314074.985385, 311636.2853386947]]
lrd.load_and_predict('final-test-data-v2.csv', X_sample, 8.508, 'v2', True)

# V3
X_sample = [[2, 4, 2460314074.985385]]
lrd.load_and_predict('final-test-data-v3.csv', X_sample, 8.508, 'v3', True)

# V4
X_sample = [[2, 2460314074.985385]]
lrd.load_and_predict('final-test-data-v4.csv', X_sample, 8.508, 'v4', True)
