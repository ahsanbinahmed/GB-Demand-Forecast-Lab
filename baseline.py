"""Lesson 1: predict demand from the same settlement period seven days earlier."""
import argparse
import csv
from datetime import date, timedelta
from pathlib import Path
from statistics import mean


def evaluate(path):
    with path.open(newline="", encoding="utf-8-sig") as source:
        demand = {}
        for row in csv.DictReader(source):
            key = (date.fromisoformat(row["date"]), int(row["period"]))
            if key in demand:
                raise ValueError(f"Duplicate observation: {key}")
            demand[key] = float(row["actual_mw"])

    errors = []
    eligible = 0
    if not demand:
        raise ValueError("No demand observations.")
    first_date = min(day for day, _ in demand)

    for (day, period), actual in sorted(demand.items()):
        prior_day = day - timedelta(days=7)
        if prior_day < first_date:
            continue
        eligible += 1
        forecast = demand.get((prior_day, period))
        if forecast is not None:
            errors.append(actual - forecast)

    if not errors:
        raise ValueError("No observations could be paired seven days apart.")
    return len(errors), eligible, mean(map(abs, errors)), mean(errors)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("csv", type=Path, help="CSV with date, period and actual_mw")
    scored, eligible, mae, bias = evaluate(parser.parse_args().csv)
    print(f"Scored {scored}/{eligible} observed targets after the first seven days.")
    print(f"MAE: {mae:.2f} MW")
    print(f"Bias (actual minus forecast): {bias:+.2f} MW")
