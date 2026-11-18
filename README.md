# GB Demand Forecast Lab

Public-data forecasting of Great Britain's national electricity demand for the four half-hours between midnight and 02:00 UK time.

Developed by **Ahsan bin Ahmed**. The project combines energy-system analysis, chronological model validation, feature engineering and comparative forecast evaluation.

## Historical results through 18 November 2026

The blended demand model recorded **461.6 MW MAE**, compared with **509.0 MW** for NESO's original forecast on **1,248 matched half-hours**. This is a **9.3% reduction in average absolute forecast error**.

| Forecast | MAE MW | Bias MW |
|---|---:|---:|
| Demand-history and weather baseline | 784.1 | +95.4 |
| Overnight level-and-shape model with embedded-wind forecasts | 508.7 | +74.7 |
| Regression incorporating a physical wind-change adjustment | 492.1 | -35.9 |
| **Demand Lab blended forecast** | **461.6** | **+16.9** |
| NESO original demand forecast | 509.0 | +215.8 |
| NESO plus the separate fixed correction | 483.5 | +90.8 |

Coverage is 312 eligible nights from 1 January to 18 November 2026. All entries use identical matched intervals. Positive bias means demand was underforecast on average.

## The forecasting problem

National Demand reflects the transmission-system generation requirement. Embedded wind generation reduces the amount drawn from transmission. Adding archived embedded-wind forecasts substantially improved the initial demand-history and temperature models.

Demand Lab combines a forecast of the overnight average and half-hourly shape, a boosted-tree forecast, and a regression with an explicit embedded-wind change adjustment. The model uses public NESO embedded-generation forecasts as upstream inputs. NESO's published demand forecast provides the benchmark.

## November 2026 historical reconstruction

| Forecast | Matched half-hours | MAE MW | Bias MW |
|---|---:|---:|---:|
| NESO original | 64 | 556.8 | +416.1 |
| Fixed Demand Correction | 64 | 487.7 | +291.1 |
| **Demand Lab** | **64** | **415.7** | **+137.7** |

Demand Lab reduced MAE by **141.1 MW, or 25.3%**, across the 16 matched nights and had lower daily MAE on 10 of them.

The aggregate advantage was concentrated on 12 and 14 November. Across the other 14 matched nights, Demand Lab MAE was 418.0 MW and NESO MAE was 407.7 MW. On 17 November, Demand Lab performed worse; on 18 November it performed better.

[Daily results for 1–18 November](reports/november-2026.md)

## Development and validation

| Stage | Work completed |
|---|---|
| Benchmarking | Compared same-half-hour daily and weekly naive forecasts with actual demand. |
| Statistical models | Tested linear regression, calendar effects and additive temperature curves. |
| Error diagnosis | Examined monthly, weekday, holiday and overnight-level versus shape errors. |
| Richer inputs | Added recent morning demand, longer demand history, temperature changes and seasonal features. |
| Model comparison | Evaluated boosted trees, regression, neural-network experiments and an approximation trained on NESO's archived demand forecasts. |
| Physical feature | Added archived embedded-wind forecasts, followed by a level-and-shape design and a blend chosen from 2025 validation results. |

Training began with earlier public data from 2023 onward. Component settings and blend weights were selected using chronological 2025 validation predictions. The historical 2026 simulation refitted components monthly using earlier observations.

The 2026 period has been inspected repeatedly during development. Results are historical development evidence. Prospective performance recording is the next evaluation stage.

## Scope and timing

- Four half-hours ending at 00:30, 01:00, 01:30 and 02:00 UK time.
- Latest eligible NESO demand forecast by 09:15 UK time on the previous day.
- Actual demand measured using Elexon Initial National Demand Outturn.
- Matched coverage excludes clock-change-affected inputs and missing source records.
- Embedded-wind forecast production timestamps precede cutoff by at least one hour. Exact historical public-availability times are absent, so that buffer is an assumption.
- Weather uses archived forecast lead times. Exact historical weather delivery times remain unverified.

MAE averages absolute errors. Bias averages actual minus forecast. Forecast-accuracy improvements measure changes in forecast error. Operational electricity, cost and carbon impacts require a separate decision and dispatch evaluation.

## Related project

[Demand Correction](https://github.com/ahsanbinahmed/NESOdemandforecast) applies a fixed historical adjustment to NESO's demand forecasts.

## Sources

[Elexon demand data](https://bmrs.elexon.co.uk/demand-forecast) · [NESO embedded-generation forecasts](https://www.neso.energy/data-portal/embedded-wind-and-solar-forecasts) · [Open-Meteo archived weather forecasts](https://open-meteo.com/en/docs/previous-runs-api) · [GOV.UK bank holidays](https://www.gov.uk/bank-holidays.json)
