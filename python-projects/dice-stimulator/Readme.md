A Python-based simulation tool designed to explore the statistical behavior of rolling multiple dice. This project serves as a practical application for investigating probability distributions and testing the effects of biased dice through character-based data visualization.

## Project Overview

Rolling dice represents a fundamental random experiment. While a single die possesses an equal probability for each face, rolling multiple dice creates complex outcome distributions. As the number of dice increases, the distribution of possible outcomes typically resembles a bell-shaped curve, illustrating key principles of the **Central Limit Theorem**.

The **dice_simulator.py** program allows users to:

- Simulate thousands of dice rolls instantaneously.
- Configure variables such as the number of dice, faces per die, and individual face weights.
- Analyze results through frequency tables and text-based histograms.
- Calculate comprehensive summary statistics.

## How to Run the Code

The user must have **Python** installed on their system. The simulation is executed via the command line using the following syntax:

```bash
python dice_simulator.py --dice 2 --faces 6 --rolls 1000 --weights 1,1,1,1,2,2 --bins 10
```

### Command Line Parameters

| Parameter | Description | Default |
|-----------|-------------|---------|
| `--dice` | The number of dice rolled in each experiment. | 1 |
| `--faces` | The number of faces on each die (e.g., 6 for a standard die). | 6 |
| `--rolls` | The total number of times the experiment is repeated. | 100 |
| `--weights` | A comma-separated list of weights to simulate biased dice. | Equal weights |
| `--bins` | The number of groups used to categorize results in the histogram. | 1 per outcome |

## Output Features

The program generates a detailed report of the experiment:

- **Frequency Distribution**: A table mapping every possible outcome to its specific frequency.
- **Text-Based Histogram**: A visual representation of the data distribution using asterisk markers.
- **Summary Statistics**:
    - **Mean**: The mathematical average of all outcomes.
    - **Median**: The middle value of the sorted dataset.
    - **Mode**: The outcome that appears most frequently.
    - **Variance**: A measure of how far outcomes are spread from the mean.
    - **Standard Deviation**: The average amount of variation in the dataset.

## Statistical Concepts Applied

### 1. Central Tendency

- **Mean (μ)**: Calculated as n∑x​.
- **Median**: The central point of the data; if the count is even, it averages the two middle values.
- **Mode**: The peak of the frequency distribution.

### 2. Dispersion

- **Variance (σ²)**: The average of the squared differences between each outcome and the mean.
- **Standard Deviation (σ)**: The square root of the variance, indicating the consistency of the results.

### 3. Binning and Grouping

To simplify large datasets, the program groups outcomes into bins. Each bin represents a range of values, ensuring the histogram remains readable even when the range of possible outcomes is vast.

## Learning Objectives

Through the use of this simulator, users gain experience in:

- **Random Number Generation**: Simulating stochastic processes in Python.
- **Statistical Analysis**: Processing and interpreting raw data.
- **Probability Visualization**: Observing how individual random events aggregate into predictable mathematical patterns.
