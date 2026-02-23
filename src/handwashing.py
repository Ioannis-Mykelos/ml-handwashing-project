"""Entry point script for the handwashing analysis."""

import matplotlib.pyplot as plt

from analysis import (
    add_mortality_proportion,
    bootstrap_mortality_difference_ci,
    mortality_mean_difference,
    split_before_and_after_handwashing,
    split_by_clinic,
)
from data_loading import load_monthly_deaths, load_yearly_deaths
from plotting import (
    plot_before_after_handwashing,
    plot_monthly_mortality,
    plot_yearly_clinic_proportions,
)


def main() -> None:
    """Run the full handwashing analysis and show plots."""
    # Yearly data and clinic comparison
    yearly = add_mortality_proportion(load_yearly_deaths())
    clinic_1, clinic_2 = split_by_clinic(yearly)
    plot_yearly_clinic_proportions(clinic_1, clinic_2)

    # Monthly data and effect of handwashing over time
    monthly = add_mortality_proportion(load_monthly_deaths())
    plot_monthly_mortality(monthly)

    before_washing, after_washing = split_before_and_after_handwashing(monthly)
    plot_before_after_handwashing(before_washing, after_washing)

    # Quantify the effect of handwashing
    mean_diff = mortality_mean_difference(before_washing, after_washing)
    lower_ci, upper_ci = bootstrap_mortality_difference_ci(
        before_washing,
        after_washing,
    )

    print(f"Mean monthly mortality difference (after - before): {mean_diff:.4f}")
    print(f"95% bootstrap confidence interval: [{lower_ci:.4f}, {upper_ci:.4f}]")

    plt.show()


if __name__ == "__main__":
    main()
