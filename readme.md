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

[OVERALL], RunTime(ms), 7622 \
[OVERALL], Throughput(ops/sec), 131.19916032537392 \
[TOTAL_GCS_Copy], Count, 6 \
[TOTAL_GC_TIME_Copy], Time(ms), 57 \
[TOTAL_GC_TIME_%_Copy], Time(%), 0.7478352138546313 \
[TOTAL_GCS_MarkSweepCompact], Count, 0 \
[TOTAL_GC_TIME_MarkSweepCompact], Time(ms), 0 \
[TOTAL_GC_TIME_%_MarkSweepCompact], Time(%), 0.0 \
[TOTAL_GCs], Count, 6 \
[TOTAL_GC_TIME], Time(ms), 57 \
[TOTAL_GC_TIME_%], Time(%), 0.7478352138546313 \
[READ], Operations, 511 \
[READ], AverageLatency(us), 6910.506849315068 \
[READ], MinLatency(us), 3026 \
[READ], MaxLatency(us), 100415 \
[READ], 95thPercentileLatency(us), 10967 \
[READ], 99thPercentileLatency(us), 11751 \
[READ], Return=OK, 511 \
[CLEANUP], Operations, 1 \
[CLEANUP], AverageLatency(us), 17608.0 \
[CLEANUP], MinLatency(us), 17600 \
[CLEANUP], MaxLatency(us), 17615 \
[CLEANUP], 95thPercentileLatency(us), 17615 \
[CLEANUP], 99thPercentileLatency(us), 17615 \
[UPDATE], Operations, 489 \
[UPDATE], AverageLatency(us), 5382.118609406953 \
[UPDATE], MinLatency(us), 2920 \
[UPDATE], MaxLatency(us), 403199 \
[UPDATE], 95thPercentileLatency(us), 6935 \
[UPDATE], 99thPercentileLatency(us), 7895 \
[UPDATE], Return=OK, 489 

#### Yahoo benchmark - redis - visionfive2board - miralis - default policy - client located on the visionfive2 board

[OVERALL], RunTime(ms), 2840 \
[OVERALL], Throughput(ops/sec), 352.11267605633805 \
[TOTAL_GCS_Copy], Count, 3 \
[TOTAL_GC_TIME_Copy], Time(ms), 42 \
[TOTAL_GC_TIME_%_Copy], Time(%), 1.4788732394366197 \
[TOTAL_GCS_MarkSweepCompact], Count, 0 \
[TOTAL_GC_TIME_MarkSweepCompact], Time(ms), 0 \
[TOTAL_GC_TIME_%_MarkSweepCompact], Time(%), 0.0 \
[TOTAL_GCs], Count, 3 \
[TOTAL_GC_TIME], Time(ms), 42 \
[TOTAL_GC_TIME_%], Time(%), 1.4788732394366197 \
[READ], Operations, 478 \
[READ], AverageLatency(us), 1933.3807531380753 \
[READ], MinLatency(us), 1583 \
[READ], MaxLatency(us), 79231 \
[READ], 95thPercentileLatency(us), 1927 \
[READ], 99thPercentileLatency(us), 2325 \
[READ], Return=OK, 478 \
[CLEANUP], Operations, 1 \
[CLEANUP], AverageLatency(us), 2967.0 \
[CLEANUP], MinLatency(us), 2966 \
[CLEANUP], MaxLatency(us), 2967 \
[CLEANUP], 95thPercentileLatency(us), 2967 \
[CLEANUP], 99thPercentileLatency(us), 2967 \
[UPDATE], Operations, 522 \
[UPDATE], AverageLatency(us), 1306.2471264367816 \
[UPDATE], MinLatency(us), 958 \
[UPDATE], MaxLatency(us), 22479 \
[UPDATE], 95thPercentileLatency(us), 1291 \
[UPDATE], 99thPercentileLatency(us), 10175 \
[UPDATE], Return=OK, 522 