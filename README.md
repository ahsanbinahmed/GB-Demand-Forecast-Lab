# GB Demand Forecast Lab

Can we forecast Great Britain's half-hourly national electricity demand a day ahead using past observations and information available before delivery?

This is an independent forecast. NESO's published forecasts and the [fixed correction experiment](https://github.com/ahsanbinahmed/NESOdemandforecast) will serve as external benchmarks. The first experiment covers settlement periods 1–4 (00:00–02:00 UK time on ordinary days), with the previous day's 09:15 UK cutoff.

## Lesson 1: same half-hour last week

```sh
python baseline.py observations.csv
```

Input columns: `date` (YYYY-MM-DD), `period` (1–4), and `actual_mw`. Use one row per date and period. Prepare this lesson's input by excluding UK clock-change dates and using outturn observations available before their forecast cutoff. The script assumes this input preparation has already been done. It matches the exact calendar date seven days earlier, so a missing date never slips the lookup to the wrong weekday. The first seven days provide history; later observed targets without a match are counted in coverage. This coverage denominator counts observed targets; the full evaluation will also audit missing target observations against the expected periods.

An example with invented data: if last Tuesday's 00:00–00:30 demand was 24,000 MW, this Tuesday's forecast for that interval is 24,000 MW. If demand is 24,300 MW, signed error (actual minus forecast) is +300 MW and absolute error is 300 MW.

## Experiment plan

1. Use Elexon [National Demand Outturn](https://bmrs.elexon.co.uk/demand-forecast) as actual demand. Archive publication times, missing intervals and clock-change handling.
2. Compare same-half-hour last week with a historical weekday-and-slot median and regularised linear regression. Use only features known by the cutoff.
3. Select options on chronological 2025 validation folds. Score the frozen pipeline on 2026 as a historical evaluation, and subsequently save predictions before delivery for prospective evaluation.
4. Compare all models with NESO and corrected NESO on identical intervals. Report MAE, signed bias, coverage and error breakdowns. Document missed peaks and unusual days.
5. Test boosted trees for nonlinear effects and neural networks as a challenger once the baseline and evaluation are reliable. Expand to all-day forecasts after the initial experiments.

The baseline script is available. Historical data assembly, regression and benchmark results are pending.
