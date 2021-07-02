# Multicore NOC Traffic Latency Optimization
SA (Simulated Annealing) for 64 cores NOC;

STAGE for 64 cores NOC


Sample computed weighted latency of 8x8 Cores NOC
Mesh Grid
![image](https://user-images.githubusercontent.com/50343656/124329998-c8a0a980-db49-11eb-8201-be2d996cd7b5.png)
Optimized Grid
![image](https://user-images.githubusercontent.com/50343656/124330020-d5bd9880-db49-11eb-81eb-4ee938899bb7.png)

            minimized traffic weighted zero-load latency
uniform _traffic
Original mesh                                               8596.112898349664
Simulated Annealing algorithm                               4283.280548990766
STAGE algorithm(Random Forest Regression)                   4701.621801904169          
STAGE algorithm(Linear Regression)                          4005.5494987918637

random_traffic
Original mesh                                               10855.716749642652
Simulated Annealing algorithm                               7711.38961102337
STAGE algorithm(Random Forest Regression)                   6074.573367198096
STAGE algorithm(Linear Regression)                          5279.470931016056

complement _traffic
Original mesh                                               2513.2339481947247
Simulated Annealing algorithm                               1151.425702472076
STAGE algorithm(Random Forest Regression)                   1223.1736422085202
STAGE algorithm(Linear Regression)                          1063.157618546288

