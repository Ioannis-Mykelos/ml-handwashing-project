"""Plotting utilities for the handwashing analysis."""

import pandas as pd


def plot_yearly_clinic_proportions(
    clinic_1: pd.DataFrame,
    clinic_2: pd.DataFrame,
):
    """Plot yearly mortality proportions for the two clinics."""
    ax = clinic_1.plot(x="year", y="proportion_deaths", label="Clinic 1")
    clinic_2.plot(
        x="year",
        y="proportion_deaths",
        label="Clinic 2",
        ax=ax,
        ylabel="Proportion deaths",
    )
    return ax


def plot_monthly_mortality(monthly: pd.DataFrame):
    """Plot monthly mortality proportion over time."""
    ax = monthly.plot(x="date", y="proportion_deaths", ylabel="Proportion deaths")
    return ax


def plot_before_after_handwashing(
    before_washing: pd.DataFrame,
    after_washing: pd.DataFrame,
):
    """Plot mortality proportions before and after handwashing."""
    ax = before_washing.plot(
        x="date",
        y="proportion_deaths",
        label="Before handwashing",
    )
    after_washing.plot(
        x="date",
        y="proportion_deaths",
        label="After handwashing",
        ax=ax,
        ylabel="Proportion deaths",
    )
    return ax
