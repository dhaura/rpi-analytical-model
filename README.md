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

$`P_{total}=C_1+p_{master}+\sum_{i=1}^{n_{worker}}p_{worker, i}`$

Where,

- $`p_{master}=C_2u_{master}+C_3m_{master}+p_{k, total, master}+C_8`$

- $`p_{worker, i}=p_{k, total, worker, i}+C_4`$

- $`p_{k, total}=p_{k, total, master}+p_{k, total, worker}=\sum_{i=1}^{n_k}p_{k, i}`$

- $`p_{k, total, master}=\sum_{i=1}^{n_{k, master}}p_{k, master, i}`$

- $`p_{k, total, worker}=\sum_{i=1}^{n_{k, worker}}p_{k, worker, i}=\sum_{i=1}^{n_{worker}}p_{k, total, worker, i}`$

- $`p_{k, total, worker, i}=\sum_{j=1}^{n_{k, worker, i}}p_{k, worker, i, j}`$

- $`p_{k, i}=C_5+C_6u_{k, i}+C_7m_{k, i}`$

Now the initial equation can be re-written as,

$` P_{total}=C_1+C_2u_{master}+C_3m_{master}+p_{k, total, master}+C_8+\sum_{i=1}^{n_{worker}}(p_{k, total, worker, i}+C_4)`$

$` P_{total}=C_1+C_2u_{master}+C_3m_{master}+p_{k, total, master}+C_8+\sum_{i=1}^{n_{worker}}p_{k, total, worker, i}+\sum_{i=1}^{n_{worker}}C_4`$

$` P_{total}=C_1+C_2u_{master}+C_3m_{master}+p_{k, total, master}+C_8+p_{k, total, worker}+C_4n_{worker}`$

Rearrange, 

$` P_{total}=C_1+C_8+C_2u_{master}+C_3m_{master}+C_4n_{worker}+p_{k, total, master}+p_{k, total, worker}`$

Consider $` C_1 + C_8 `$ as a single constant $` C_1 `$ and, replace $`p_{k, total, master}+p_{k, total, worker} `$ with $`p_{k, total} `$,

$` P_{total}=C_1+C_2u_{master}+C_3m_{master}+C_4n_{worker}+p_{k, total}`$ 

$` P_{total}=C_1+C_2u_{master}+C_3m_{master}+C_4n_{worker}+\sum_{i=1}^{n_k}p_{k, i}`$

$` P_{total}=C_1+C_2u_{master}+C_3m_{master}+C_4n_{worker}+\sum_{i=1}^{n_k}(C_5+C_6u_{k, i}+C_7m_{k, i})`$

Finally, following the above simplification steps, the equation is simplified to the following final equation.

$`P_{total}=C_1+C_2u_{master}+C_3m_{master}+C_4n_{worker}+C_5n_k+C_6\sum_{i=1}^{n_k}u_{k, i}+C_7\sum_{i=1}^{n_k}m_{k, i}`$

### Final Regression Model
After analyzing the above equation using linear regression models, the following analytical model (equivalent to linear regression model `v3`) was finalized for estimating the power consumption of the edge cluster.
 
$` P_{total}=C_1+C_2n_{worker}+C_3n_k+C_4u_{k,total} `$

Where,

 - $`u_{k, total}=\sum_{i=1}^{n_k}u_{k, i}`$
