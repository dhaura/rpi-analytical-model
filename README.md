# Analytical Model for Power Prediction in a Raspberry Pi Cluster

## Experimental Setup
The experimental setup (for data collection) was created with three `Raspberry Pi 3 Model B Plus` devices, using `K3s` as the container orchestration system.

The experiment was conducted by differentiating the number of containers deployed
and the number of requests sent while the power consumption and other utilization
parameters were logged. The following tools were used for the said purpose.
* **kubectl** - Control the number of containers deployed.
* **JMeter** - Control the number of requests sent to the application.
* Developed **[Kubernetes Logger](https://github.com/Lakshan-Banneheke/rpi-logger/blob/main/rpi-logger-v3.py)** - Log Utilization parameters of the edge cluster.
* **USB Power Meter** - Measure power consumption of the edge cluster.
* Developed **[Data Parser](https://github.com/Lakshan-Banneheke/rpi-logger/blob/main/Parser/test-data-parser.py)** - Aggregate the final dataset.

## Dataset
Collected datasets for each version of the linear regression model can be found in `data` folder.

## How to Train the Model

In order to run the regression model, you need to have `python3` installed as a prerequisite. Since the `v3` regression model was the most accurate, use the following steps to retrain it.  
1. Run the following command to install all the required packages.
```shell
pip install -r requirements.txt
```
2. Navigate into `linear-regression` folder.
```shell
cd linear-regression
```
3. Run any linear regression model as follows.
```shell
python3 linear-regression-v3.py
```
After training is complete, the results can be found in the `models` folder as follows.
- Coefficients of the trained model: `models`>`coefficients`>`*-v3-coefficients.csv`
- Performance metrics of the trained model:`models`>`metrics`>`*-v3-metrics.csv`
- Saved model:`models`>`*-v3.joblib`

Furthermore, in order to visualize the data set, run the following python script at the root folder.
```shell
python3 exploratory-data-analysis.py
```
Data visualizations can be found in `figures`>`eda` folder.

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

### Analytical Model - Final Version
Instead of evaluating the power usage of individual containers, the decision was made to calculate the overall power consumption of the edge cluster by combining the power consumption of the master node and active worker nodes. This approach allows for a clearer understanding of how containers contribute to power consumption, as their power usage is reflected in the power consumption of the node they are assigned to.

The power consumption of the master node consists of its CPU and memory utilization contributions and the power attributed to the containers deployed in the master node. Since the major power consumption of a worker node consists of the containers that are deployed in the node, they are attributed to the power consumption of that node.

![11](https://user-images.githubusercontent.com/57411348/230965175-9f7bb6ab-57e6-4d2b-8f12-13bfb05a6afb.png)
![1](https://user-images.githubusercontent.com/57411348/230965195-63a4b4d6-4ec2-4408-81e5-c64159a52244.png)

### Final Regression Model
After analyzing the above equation using linear regression models, the following analytical model (equivalent to linear regression model `v3`) was finalized for estimating the power consumption of the edge cluster.

<img src="https://github.com/dhaura/rpi-analytical-model/assets/57411348/d2c70981-791c-4d89-80c5-9a2295b63f5f" alt="lr-model">
