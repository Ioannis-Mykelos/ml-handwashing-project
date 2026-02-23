"""Configuration for the handwashing analysis project."""

from datetime import datetime
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "datasets"

YEARLY_DEATHS_FILE = DATA_DIR / "yearly_deaths_by_clinic.csv"
MONTHLY_DEATHS_FILE = DATA_DIR / "monthly_deaths.csv"

# Date when mandatory handwashing started at the clinic
HANDWASHING_START_DATE = datetime(1847, 6, 1)

# Number of bootstrap resamples to use when estimating the confidence interval
N_BOOTSTRAP_SAMPLES = 3000
