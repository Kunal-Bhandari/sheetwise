"""
Benchmark and Visualization Script for SheetWise

- Runs compression and analysis on a set of sample spreadsheets
- Collects metrics (compression ratio, time, memory, etc.)
- Generates beautiful charts using seaborn/matplotlib
- Saves charts for documentation/website
"""
import os
import time
import glob
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from memory_profiler import memory_usage
from sheetwise import SpreadsheetLLM

# Directory with sample spreadsheets (user should update this path)
SAMPLES_DIR = "benchmarks/samples"
RESULTS_DIR = "benchmarks/results"
CHARTS_DIR = "benchmarks/charts"
os.makedirs(RESULTS_DIR, exist_ok=True)
os.makedirs(CHARTS_DIR, exist_ok=True)

# Find all .xlsx and .csv files in the samples directory
sample_files = glob.glob(os.path.join(SAMPLES_DIR, "*.xlsx")) + glob.glob(os.path.join(SAMPLES_DIR, "*.csv"))

results = []

for file in sample_files:
    print(f"Processing: {file}")
    df = pd.read_excel(file) if file.endswith(".xlsx") else pd.read_csv(file)
    sllm = SpreadsheetLLM()
    # Time and memory for compression
    start = time.time()
    mem_usage, compressed = memory_usage((sllm.compress_spreadsheet, (df,)), retval=True, max_usage=True)
    elapsed = time.time() - start
    stats = sllm.get_encoding_stats(df)
    results.append({
        "file": os.path.basename(file),
        "rows": df.shape[0],
        "cols": df.shape[1],
        "compression_ratio": stats["compression_ratio"],
        "token_reduction": stats["token_reduction_ratio"],
        "sparsity": stats["sparsity_percentage"],
        "time_sec": elapsed,
        "max_mem_mb": mem_usage
    })

# Save results as CSV
results_df = pd.DataFrame(results)
results_df.to_csv(os.path.join(RESULTS_DIR, "benchmark_results.csv"), index=False)

# Plot: Compression Ratio vs. File Size
sns.set_theme(style="whitegrid")
plt.figure(figsize=(8,5))
sns.scatterplot(
    data=results_df,
    x="rows",
    y="compression_ratio",
    size="cols",
    hue="sparsity",
    palette="viridis",
    legend="brief"
)
plt.title("Compression Ratio vs. File Size")
plt.xlabel("Rows in Spreadsheet")
plt.ylabel("Compression Ratio")
plt.tight_layout()
plt.savefig(os.path.join(CHARTS_DIR, "compression_vs_size.png"))

# Plot: Processing Time vs. File Size
plt.figure(figsize=(8,5))
sns.scatterplot(
    data=results_df,
    x="rows",
    y="time_sec",
    size="cols",
    hue="compression_ratio",
    palette="mako",
    legend="brief"
)
plt.title("Processing Time vs. File Size")
plt.xlabel("Rows in Spreadsheet")
plt.ylabel("Processing Time (sec)")
plt.tight_layout()
plt.savefig(os.path.join(CHARTS_DIR, "time_vs_size.png"))

# Plot: Max Memory Usage
plt.figure(figsize=(8,5))
sns.barplot(
    data=results_df.sort_values("max_mem_mb", ascending=False),
    x="file",
    y="max_mem_mb",
    palette="crest"
)
plt.title("Max Memory Usage per File")
plt.xlabel("File")
plt.ylabel("Max Memory Usage (MB)")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig(os.path.join(CHARTS_DIR, "memory_usage.png"))

print(f"\nBenchmark complete! Results saved to {RESULTS_DIR} and charts to {CHARTS_DIR}.")
