# DeepLearning Inference Optimizer

A lightweight Python benchmarking tool to visualize the performance of matrix operations at scale — inspired by GPU memory access patterns. Built to simulate how matrix size impacts computational latency, this tool provides an intuitive plot for performance analysis.

## 🚀 Features

- Benchmarks matrix multiplication for various sizes (128×128 to 1024×1024)
- Visualizes timing performance with Matplotlib
- Simulates concepts like GPU-style tile/block access (CPU only)
- Minimal setup, fast execution, beginner-friendly

## 🛠️ Tech Stack

- Python 3
- NumPy
- Matplotlib

## 📊 What It Demonstrates

This project showcases your understanding of:

- Performance tuning and benchmarking
- Data visualization for algorithm analysis
- Efficient matrix computation fundamentals
- Setting up and pushing code using Git + GitHub

## 📁 Project Structure

DeepLearning_Inference_Optimizer/
│
├── src/
│ ├── run_benchmark.py # Main script for benchmarking
│ └── matrix_perf_plot.png # Output plot of benchmark timings
└── README.md

bash
Copy code

## 🧪 How to Run

```bash
# Navigate into the project folder
cd DeepLearning_Inference_Optimizer/src

# Activate virtual environment (if used)
source ../venv/bin/activate

# Run benchmark
python3 run_benchmark.py
