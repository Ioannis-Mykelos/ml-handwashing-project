"""Core analysis functions for the handwashing project."""

from __future__ import annotations

from typing import Tuple

import pandas as pd

from config import HANDWASHING_START_DATE, N_BOOTSTRAP_SAMPLES


def add_mortality_proportion(data: pd.DataFrame) -> pd.DataFrame:
    """Return a copy of the data with a proportion_deaths column."""
    result = data.copy()
    result["proportion_deaths"] = result["deaths"] / result["births"]
    return result


def split_by_clinic(yearly: pd.DataFrame) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """Split yearly data into separate dataframes for clinic 1 and clinic 2."""
    clinic_1 = yearly[yearly["clinic"] == "clinic 1"]
    clinic_2 = yearly[yearly["clinic"] == "clinic 2"]
    return clinic_1, clinic_2


def split_before_and_after_handwashing(
    monthly: pd.DataFrame,
) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """Split monthly data into periods before and after handwashing."""
    handwashing_start = pd.to_datetime(HANDWASHING_START_DATE)
    before_washing = monthly[monthly["date"] < handwashing_start]
    after_washing = monthly[monthly["date"] >= handwashing_start]
    return before_washing, after_washing


def mortality_mean_difference(
    before_washing: pd.DataFrame,
    after_washing: pd.DataFrame,
) -> float:
    """Compute the mean difference in mortality (after - before)."""
    before_proportion = before_washing["proportion_deaths"]
    after_proportion = after_washing["proportion_deaths"]
    return float(after_proportion.mean() - before_proportion.mean())


def bootstrap_mortality_difference_ci(
    before_washing: pd.DataFrame,
    after_washing: pd.DataFrame,
    n_bootstrap: int = N_BOOTSTRAP_SAMPLES,
) -> Tuple[float, float]:
    """Estimate a 95% bootstrap confidence interval for the mortality difference."""
    before_proportion = before_washing["proportion_deaths"]
    after_proportion = after_washing["proportion_deaths"]

    boot_mean_diff = []
    for _ in range(n_bootstrap):
        boot_before = before_proportion.sample(frac=1, replace=True)
        boot_after = after_proportion.sample(frac=1, replace=True)
        boot_mean_diff.append(boot_after.mean() - boot_before.mean())

    confidence_interval = pd.Series(boot_mean_diff).quantile([0.025, 0.975])
    lower, upper = confidence_interval.iloc[0], confidence_interval.iloc[1]
    return float(lower), float(upper)
