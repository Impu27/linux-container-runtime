# Task 4 — Metrics & Data-Driven Scheduling

## Goal
Demonstrate data-driven scheduling by collecting CPU metrics,
analyzing system load, and making scheduling decisions.

## Metrics Source
- /proc/stat (system CPU usage)
- Sampling interval: 1 second

## Data Collection
CPU usage recorded into CSV format:
timestamp, cpu_usage_percent

## Scheduling Logic
If CPU usage < 60% → schedule container  
Else → delay scheduling

## Visualization
CPU usage plotted over time with threshold line using matplotlib.

## Result
Successfully demonstrated metrics-based scheduling decisions
similar to container orchestrators and autoscalers.
