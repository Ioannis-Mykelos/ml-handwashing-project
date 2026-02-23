"""Data loading utilities for the handwashing analysis."""

from pathlib import Path
from typing import Optional

import pandas as pd

from config import MONTHLY_DEATHS_FILE, YEARLY_DEATHS_FILE


def load_yearly_deaths(path: Optional[Path] = None) -> pd.DataFrame:
    """Load yearly deaths by clinic data."""
    csv_path = path or YEARLY_DEATHS_FILE
    return pd.read_csv(csv_path)


def load_monthly_deaths(path: Optional[Path] = None) -> pd.DataFrame:
    """Load monthly deaths data with parsed dates."""
    csv_path = path or MONTHLY_DEATHS_FILE
    return pd.read_csv(csv_path, parse_dates=["date"])
