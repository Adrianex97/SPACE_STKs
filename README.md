# SPACE_STKs: Stock Price Forecasting for Space Industry Companies 🚀

This project uses **Prophet** to forecast stock prices for major space-related companies. It leverages historical stock data from **Yahoo Finance** and provides 1-year price predictions, complete with trend, seasonality, and uncertainty intervals.

## Overview

This repository contains Python code that:
- Downloads 1 year of historical stock data for 11 major space-related companies using the `yfinance` library.
- Trains a **Prophet** forecasting model for each company.
- Forecasts the next 365 days of stock prices.
- Displays **interactive Plotly graphs** for stock price trends, with confidence intervals.
- Analyzes the trend and seasonality of each stock.

## Companies Included
The project includes stock price forecasts for the following companies:
- Rocket Lab (RKLB)
- Intuitive Machines (LUNR)
- Redwire (RDW)
- Maxar Technologies (MAXR)
- Aerojet Rocketdyne (AJRD)
- And more...

## Features
- **Interactive Plots**: Visualize predicted stock trends using Plotly.
- **Prophet Model**: Train models to predict future stock prices.
- **Seasonality and Trend Analysis**: Understand the factors influencing stock price fluctuations.

## Installation & Usage

Follow these steps to get started with the project:

### 1. Clone the repository:
```bash
git clone https://github.com/your-username/SPACE_STKs.git
cd SPACE_STKs