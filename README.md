# Multicore NOC Traffic Latency Optimization
SA (Simulated Annealing) for 64 cores NOC;

STAGE for 64 cores NOC


# Sample computed weighted latency of 8x8 Cores NOC
Mesh Grid
![image](https://user-images.githubusercontent.com/50343656/124329998-c8a0a980-db49-11eb-8201-be2d996cd7b5.png)

Sample Optimized Grid
![image](https://user-images.githubusercontent.com/50343656/124330020-d5bd9880-db49-11eb-81eb-4ee938899bb7.png)

            minimized traffic weighted zero-load latency

| Optimize Algorithm      | uniform _traffic           | random_traffic  |complement _traffic|
| ------------- |:-------------:| -----:|-----:|
| Original mesh      | 8596.112898349664 | 10855.716749642652 |2513.2339481947247|
| Simulated Annealing algorithm      | 4283.280548990766     | 7711.38961102337 |1151.425702472076|
| STAGE algorithm(Random Forest Regression)  |4701.621801904169         | 6074.573367198096 |1223.1736422085202|
| STAGE algorithm(Linear Regression)  | 4005.5494987918637    |5279.470931016056 |1063.157618546288|

