# Handwashing Project

A data analysis project reanalyzing the historical data that led Dr. Ignaz Semmelweis to discover the importance of handwashing in medical practice.

## 📖 Historical Context

In 1847, the Hungarian physician Ignaz Semmelweis made a breakthrough discovery: he discovered handwashing. Contaminated hands were a major cause of childbed fever, and by enforcing handwashing at his hospital, he saved hundreds of lives.

Dr. Ignaz Semmelweis was a Hungarian physician born in 1818 and active at the Vienna General Hospital. He was troubled by *childbed fever*: a deadly disease affecting women who had just given birth. In the early 1840s at the Vienna General Hospital, as many as 10% of the women giving birth died from it. He discovered that the cause of childbed fever was the contaminated hands of the doctors delivering the babies.

## 🎯 Project Overview

This project reanalyzes the data that made Semmelweis discover the importance of handwashing. The analysis includes:

- **Yearly mortality analysis** comparing two clinics at Vienna General Hospital (1841-1846)
- **Monthly mortality analysis** showing the impact of handwashing implementation (starting June 1847)
- **Statistical analysis** including bootstrap confidence intervals to quantify the reduction in mortality rates
- **Data visualization** demonstrating the dramatic effect of handwashing on patient outcomes

## ✨ Key Findings

The analysis reveals that handwashing reduced the proportion of deaths by approximately **8 percentage points** - from around 10% on average to just 2%. This represents a massive improvement in patient outcomes and demonstrates the critical importance of hygiene in medical practice.

## 🚀 Features

- Data loading and preprocessing with pandas
- Proportion calculations and statistical analysis
- Time series visualization of mortality rates
- Bootstrap analysis for confidence interval estimation
- Comparison of mortality rates before and after handwashing implementation
- Comprehensive test suite
- Pre-commit hooks for code quality
- CI/CD pipeline with GitHub Actions

## 📋 Requirements

- Python >= 3.12
- See `pyproject.toml` for complete dependency list

### Main Dependencies

- pandas >= 2.0.0
- numpy < 2.0.0
- matplotlib >= 3.10.3
- scipy >= 1.14.1
- pytest >= 8.4.2

## 📦 Installation

This project uses Poetry for dependency management.

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd ml-handwashing-project
   ```

2. **Install Poetry** (if not already installed):
   ```bash
   pip install poetry
   ```

3. **Install dependencies:**
   ```bash
   poetry install
   ```

4. **Activate the virtual environment:**
   ```bash
   poetry shell
   ```

## 📁 Project Structure

```
ml-handwashing-project/
├── .github/
│   └── workflows/
│       └── pylint-precommits-pytest.yml    # CI/CD pipeline
├── src/
│   └── Handwashing project.py              # Main analysis script
├── test/
│   ├── conftest.py                         # Pytest fixtures
│   └── test_one.py                         # Test suite
├── datasets/                               # Data directory (create if needed)
│   ├── yearly_deaths_by_clinic.csv         # Yearly mortality data
│   └── monthly_deaths.csv                  # Monthly mortality data
├── .pre-commit-config.yaml                 # Pre-commit hooks configuration
├── pyproject.toml                          # Poetry dependencies and tool configs
└── README.md                               # This file
```

## 🔧 Usage

### Running the Analysis

1. **Ensure data files are available:**
   - Place `yearly_deaths_by_clinic.csv` and `monthly_deaths.csv` in the `datasets/` directory
   - Or update the file paths in the script to match your data location

2. **Run the main analysis script:**
   ```bash
   python src/"Handwashing project.py"
   ```

   Note: The script contains Jupyter notebook-style code. For production use, consider refactoring into functions.

### Running Tests

```bash
pytest
```

Or with verbose output:

```bash
pytest -v
```

### Code Quality Checks

**Run pre-commit hooks:**
```bash
pre-commit run --all-files
```

**Run pylint:**
```bash
pylint src/ test/
```

## 📊 Data Format

### yearly_deaths_by_clinic.csv
Expected columns:
- `year`: Year (1841-1846)
- `births`: Number of births
- `deaths`: Number of deaths
- `clinic`: Clinic identifier ("clinic 1" or "clinic 2")

### monthly_deaths.csv
Expected columns:
- `date`: Date (YYYY-MM-DD format)
- `births`: Number of births
- `deaths`: Number of deaths

## 🧪 Testing

The project includes a comprehensive test suite using pytest. Tests are located in the `test/` directory and use fixtures defined in `conftest.py`.

Run tests with:
```bash
pytest
```

## 🔍 Code Quality

This project maintains high code quality standards through:

- **Black** for code formatting
- **isort** for import sorting
- **flake8** for linting
- **mypy** for type checking
- **pylint** for code analysis
- **Pre-commit hooks** to enforce standards before commits
- **GitHub Actions** for CI/CD

## 📝 Development

### Setting up Pre-commit Hooks

```bash
pre-commit install
```

This will automatically run code quality checks before each commit.

### Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Ensure all tests pass and code quality checks succeed
5. Submit a pull request

## 👤 Author

**Ioannis**
- Email: qmichel05@hotmail.com

## 🙏 Acknowledgments

- Dr. Ignaz Semmelweis for his groundbreaking work in medical hygiene
- The Vienna General Hospital for maintaining detailed records of births and deaths
- The data science community for preserving and analyzing this historical dataset

## 📚 References

- Semmelweis, I. (1861). *Die Ätiologie, der Begriff und die Prophylaxis des Kindbettfiebers* (The Etiology, Concept, and Prophylaxis of Childbed Fever)
- Historical data from Vienna General Hospital (1841-1848)
