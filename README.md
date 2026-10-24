# SE Lab Experiment 10 - Code Review Automation

This repository contains a small Python program used to demonstrate automated
code quality analysis with CodeFactor.

## Program

`exp10_code_review.py`:

```python
def calculate_sum(a, b):
    result = a + b
    return result


if __name__ == "__main__":
    print("Sum:", calculate_sum(10, 20))
```

## Run

```bash
python exp10_code_review.py
```

Output:

```text
Sum: 30
```

## Code Quality

CodeFactor automatically analyzes this repository on every push and reports
the quality grade and any detected issues on its dashboard.
