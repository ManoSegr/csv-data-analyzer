CSV Data Analyzer
A professional Python tool for comprehensive CSV data analysis with statistical reporting and database integration.
Features

Intelligent Data Processing: Automatic column type detection (numerical vs categorical)
Statistical Analysis: Complete descriptive statistics with outlier detection
Data Validation: Robust CSV parsing with multiple encoding support
Database Export: SQLite integration with optimized schema generation
Professional Reporting: Clean, formatted analysis reports
Sample Data Generation: Creates realistic datasets for testing

Technologies Used

Python 3.x
CSV Processing & Validation
Statistical Analysis
SQLite Database Integration
Data Type Detection Algorithms

Key Capabilities
📊 Comprehensive Analysis

Automatic numerical/categorical column detection
Descriptive statistics (mean, median, quartiles, standard deviation)
Frequency analysis for categorical data
Missing data identification and reporting

🔍 Statistical Insights

Outlier detection using IQR method
Distribution analysis
Cross-tabulation between variables
Data quality assessment

💾 Data Management

Smart database schema creation
Optimized SQL data types
Data export and backup capabilities
Multiple file format support

Sample Output
DATASET OVERVIEW
================
File: sales_data.csv
Size: 500 rows × 7 columns

Columns:
   1. Date          (Categorical)
   2. Product       (Categorical)
   3. Price         (Numerical)
   4. Quantity      (Numerical)
   5. Region        (Categorical)

PRICE - ANALYSIS
----------------
Count:      500
Mean:       524.67
Median:     498.50
Min:        52.30
Max:        999.80
Std Dev:    287.45
Business Applications

Data Auditing: Validate and clean business datasets
Market Research: Analyze survey and sales data
Quality Control: Identify data inconsistencies and outliers
Business Intelligence: Extract insights from operational data
Reporting: Generate executive-ready data summaries

Installation & Usage
bash# Clone repository
git clone https://github.com/ManoSegr/csv-data-analyzer.git

# Run the analyzer
python csv_analyzer_clean.py

# Analyze your own CSV file
analyzer = CSVAnalyzer()
analyzer.load_csv("your_data.csv")
analyzer.generate_report()
Technical Features

Multi-encoding Support: Handles UTF-8, Latin-1, CP1252 encodings
Error Handling: Graceful handling of malformed CSV files
Memory Efficient: Optimized for large datasets
Cross-platform: Works on Windows, Mac, and Linux

Output Files

SQLite Database: Structured data storage with proper typing
Analysis Reports: Comprehensive statistical summaries
Sample Datasets: Realistic test data for demonstration

Professional Use Cases

Data Migration: Validate data before system migrations
Compliance Reporting: Generate audit-ready data reports
Performance Analytics: Analyze business KPIs and metrics
Research Analysis: Process academic or market research data


Enterprise-grade CSV analysis tool built with Python for reliable data processing.
