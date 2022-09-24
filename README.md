# GILsnooper.bt

## Example:

Run the example tool that starts a number of threads. Example below starts 20 threads.

```python3
python3 example/test.py 20
```

Run in a separate environment:
```
bpftrace GILsnooper.bt
```

Below is the example output. The example was monitored for ~17 seconds, ~0.4 seconds was spend context switching between the threads due to the GIL.
After that we see the amount of time was spend on each individual threads (`tid_time[thread_id]`).
GIL context switch historgram shows how long approximately each context switch took.
Finally, we show the total amount of context switchtes that occurred during monitoring.

```
# bpftrace GILsnooper.bt 
Attaching 6 probes...
^C
------------------------------------------------------------------------------------
Total exeuction time: 17151 ms
GIL time: 398 ms
@tid_time[137645]: 1559
@tid_time[137635]: 1576
@tid_time[137634]: 1581
@tid_time[137636]: 1596
@tid_time[137646]: 1601
@tid_time[137643]: 1616
@tid_time[137638]: 1618
@tid_time[137637]: 1632
@tid_time[137631]: 1633
@tid_time[137639]: 1648
@tid_time[137647]: 1663
@tid_time[137640]: 1673
@tid_time[137632]: 1686
@tid_time[137633]: 1706
@tid_time[137649]: 1723
@tid_time[137641]: 1742
@tid_time[137642]: 1746
@tid_time[137644]: 1756
@tid_time[137650]: 1773
@tid_time[137648]: 1809

GIL context switch histogram:
@gil_switch_hist: 
[0]                    1 |                                                    |
[1]                    0 |                                                    |
[2, 4)                 0 |                                                    |
[4, 8)                 1 |                                                    |
[8, 16)             3607 |@@@@@@@@@@@@@@@                                     |
[16, 32)           11857 |@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@|
[32, 64)            2149 |@@@@@@@@@                                           |
[64, 128)            208 |                                                    |
[128, 256)             1 |                                                    |
[256, 512)             1 |                                                    |



@context_switches: 16654
```
