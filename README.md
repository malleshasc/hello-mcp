# Python Calculator Project

A simple calculator implementation in Python with comprehensive test coverage.

## Features

- Basic arithmetic operations:
  - Addition
  - Subtraction
  - Multiplication
  - Division
  - Power function

## Code Quality

- 100% test coverage with 19 test cases covering positive and negative scenarios
- GitHub Actions workflow to ensure code quality
- Automated deployment to production branch when coverage is 100%

## Project Structure

- `calculator.py` - The main calculator implementation
- `test_calculator.py` - Comprehensive pytest test suite
- `coverage_report.txt` - Test coverage report
- `.github/workflows/python-test.yml` - GitHub Actions workflow

## Test Coverage Summary

```
Name            Stmts   Miss  Cover
-----------------------------------
calculator.py      13      0   100%
-----------------------------------
TOTAL              13      0   100%
```

## How to Run Tests

```bash
# Install dependencies
pip install pytest pytest-cov

# Run tests with coverage
pytest --cov=calculator
```
