
# Student Result Analysis System

A Python-based data analysis project that processes student academic records to generate performance insights and visualizations.

## Overview
This project analyzes a dataset of student marks across five subjects to identify performance trends, top performers, and students requiring academic support.

## Features
- Calculates the average marks for each student across all subjects
- Identifies the top-performing student (topper)
- Flags students who have failed (marks below 33 in any subject)
- Computes subject-wise average performance across the class
- Generates three visualizations:
  - Subject-wise average marks (bar chart)
  - Top 5 performing students (bar chart)
  - Distribution of student averages (histogram)

## Tech Stack
- **Python**
- **Pandas** — data manipulation and analysis
- **Matplotlib** — data visualization

## Files in this Repository
| File | Description |
|---|---|
| `analysis.py` | Main script containing all analysis logic |
| `Student record.csv` | Dataset containing student marks |
| `subject_wise_average.png` | Bar chart of average marks per subject |
| `top5_students.png` | Bar chart of top 5 performing students |
| `marks_distribution.png` | Histogram showing distribution of average scores |

## Key Insights
The analysis revealed that subject-wise averages were fairly consistent across the class, indicating no single subject was disproportionately difficult. This was determined through comparative statistical analysis using Pandas'
