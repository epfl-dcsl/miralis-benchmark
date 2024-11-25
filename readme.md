## Intermediate results - useful for a first approximation

#### Trap Miralis <--> Virtual firmmware - visionfive 2 board - default policy

[Info  | miralis::virt] > Average measure : 982 Statistics : Statistics { mean: 965, min: 957, max: 1791, p25: 958, p50: 962, p75: 962, p95: 967, p99: 1138 } \
[Info  | miralis::virt] > Average measure : 981 Statistics : Statistics { mean: 960, min: 957, max: 1219, p25: 958, p50: 962, p75: 962, p95: 966, p99: 967 } \
[Info  | miralis::virt] > Average measure : 981 Statistics : Statistics { mean: 961, min: 957, max: 1181, p25: 958, p50: 962, p75: 962, p95: 966, p99: 967 } \
[Info  | miralis::virt] > Average measure : 983 Statistics : Statistics { mean: 964, min: 957, max: 1455, p25: 958, p50: 962, p75: 962, p95: 967, p99: 1132 }

#### Trap Miralis <--> S-mode payload - visionfive 2 board - default policy 

[Info  | miralis::virt] > Average measure : 5657 Statistics : Statistics { mean: 5653, min: 5624, max: 6300, p25: 5645, p50: 5652, p75: 5662, p95: 5666, p99: 5678 } \
[Info  | miralis::virt] > Average measure : 5655 Statistics : Statistics { mean: 5652, min: 5622, max: 6175, p25: 5644, p50: 5652, p75: 5662, p95: 5666, p99: 5670 } \
[Info  | miralis::virt] > Average measure : 5655 Statistics : Statistics { mean: 5652, min: 5622, max: 6175, p25: 5644, p50: 5652, p75: 5662, p95: 5666, p99: 5670 } \
[Info  | miralis::virt] > Average measure : 5653 Statistics : Statistics { mean: 5657, min: 5624, max: 8838, p25: 5646, p50: 5656, p75: 5664, p95: 5669, p99: 5686 } 

#### Coremark pro -- visionfive 2 board - miralis - default policy

| Workload Name            | MultiCore (iter/s) | SingleCore (iter/s) | Scaling |
|--------------------------|--------------------|----------------------|---------|
| cjpeg-rose7-preset       | 138.89            | 39.37               | 3.53    |
| core                     | 1.34              | 0.33                | 4.06    |
| linear_alg-mid-100x100-sp| 58.55             | 16.14               | 3.63    |
| loops-all-mid-10k-sp     | 2.06              | 0.57                | 3.61    |
| nnet_test                | 2.59              | 0.77                | 3.36    |
| parser-125k              | 23.67             | 7.75                | 3.05    |
| radix2-big-64k           | 179.76            | 55.91               | 3.22    |
| sha-test                 | 125.00            | 39.53               | 3.16    |
| zip-test                 | 74.07             | 23.26               | 3.18    |

| Mark Name                | MultiCore         | SingleCore           | Scaling |
|--------------------------|-------------------|----------------------|---------|
| CoreMark-PRO             | 2717.72          | 796.81               | 3.41    |


#### Yahoo benchmark - memcached - visionfive2board - miralis - default policy - client located on the visionfive2 board


##### Overall Metrics

| Metric                  | Value                  |
|-------------------------|------------------------|
| RunTime (ms)           | 7622                  |
| Throughput (ops/sec)   | 131.19916032537392    |

##### Garbage Collection Metrics

| GC Type                 | Count | Time (ms) | Time (%)          |
|-------------------------|-------|-----------|-------------------|
| Copy                   | 6     | 57        | 0.7478352138546313 |
| MarkSweepCompact       | 0     | 0         | 0.0               |
| **Total**              | 6     | 57        | 0.7478352138546313 |

#####  READ Operation Metrics

| Metric                  | Value      |
|-------------------------|------------|
| Operations             | 511        |
| Average Latency (us)   | 6910.51    |
| Min Latency (us)       | 3026       |
| Max Latency (us)       | 100415     |
| 95th Percentile (us)   | 10967      |
| 99th Percentile (us)   | 11751      |
| Return=OK             | 511        |

#####  CLEANUP Operation Metrics

| Metric                  | Value      |
|-------------------------|------------|
| Operations             | 1          |
| Average Latency (us)   | 17608.0    |
| Min Latency (us)       | 17600      |
| Max Latency (us)       | 17615      |
| 95th Percentile (us)   | 17615      |
| 99th Percentile (us)   | 17615      |

##### UPDATE Operation Metrics

| Metric                  | Value      |
|-------------------------|------------|
| Operations             | 489        |
| Average Latency (us)   | 5382.12    |
| Min Latency (us)       | 2920       |
| Max Latency (us)       | 403199     |
| 95th Percentile (us)   | 6935       |
| 99th Percentile (us)   | 7895       |
| Return=OK             | 489        |

