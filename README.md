# Analytical Model for Power Prediction in a Raspberry Pi Cluster

## Resource Characterization
A multi-node edge computing cluster that utilizes a container orchestration system will be used. The edge environment will be characterized by;
* No. of active worker nodes
* No. of active containers
* No. of active optional containers
* Master node CPU utilization
* Master node memory utilization
* Total container CPU utilization
* Total container memory utilization

These data will be fed into the analytical model (except No. of active optional containers) in order to predict power consumption. No. of active optional containers will be fed into the brownout controller.

## Analytical Model
The data from the above resource characterization will be taken as input by the analytical model, as shown in Figure .The analytical model will use the above data to compute the power consumption. The model is developed and evaluated using a power meter which gives the power consumption of the application running on the edge cluster.

### Inputs
* Resource Characterization - Characterization of edge computing cluster
* Power consumption reading of edge cluster (for implementation and verification purposes)

### Outputs
* Computed power consumption
