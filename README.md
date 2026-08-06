# Restaurant Tips Data Analysis

A beginner-friendly data analysis project built with **pandas** and **Matplotlib**. It explores a real public dataset of restaurant tips to answer questions a small business owner would care about: how much do customers tip, when is the restaurant busiest, and what drives tip size.

This project demonstrates:
- Loading and inspecting data with pandas
- Grouping and aggregating (groupby, mean, mode)
- Creating clear charts with Matplotlib
- Turning data into short, readable findings

## Data

The dataset is the classic **Tips** dataset (244 restaurant visits). It is committed in `data/tips.csv` so the analysis is fully reproducible offline. Columns: `total_bill`, `tip`, `sex`, `smoker`, `day`, `time`, `size`.

## How to run

```bash
pip install -r requirements.txt
python analysis.py
```

The script prints key findings and saves charts into `output/`.

## Sample findings

The analysis script writes its findings to [`output/findings.md`](output/findings.md), so the
numbers always match the code. At a glance:

- Average tip percentage is around **16%** of the total bill.
- Saturday and Sunday are the busiest days.
- Lunch has a slightly higher average tip percentage than dinner.
- Larger parties tend to spend more, and tips grow with the bill.

## Charts

| Chart | Description |
|---|---|
| `output/bill_distribution.png` | Spread of total bill amounts |
| `output/avg_tip_by_day.png` | Average tip across the week |
| `output/bill_vs_tip.png` | Tip vs bill, coloured by party size |
| `output/tip_pct_by_time.png` | Tip percentage by meal time |
| `output/findings.md` | Auto-generated findings summary |

## Status

Portfolio project as part of my [learning roadmap](https://github.com/unaboss/unaboss). Comments, issues and pull requests are welcome.
