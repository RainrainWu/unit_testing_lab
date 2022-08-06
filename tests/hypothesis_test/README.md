# Testing with Hypothesis

## Turn on the Logger
Uncomment the config within `pyproject.toml` to observe execution details.
```bash
# log_cli = 1
# log_cli_level = 'INFO'
# log_cli_format = '%(levelname)-8s | %(message)s (%(filename)s:%(lineno)s)'
```

## Run the Unit Test
Check if the output show as expected.
```bash
$ poetry run pytest
```

## Benchmarking
Benchmark your code with test cases though heavier workloads.
1. Update the profile we registered inside `conftest.py`
```python
settings.load_profile("benchmark")
```
2. Run again
```bash
$ poetry run pytest
```

## Detailed Information
As a powerful data generating tool, it also provide some statistical features.
1. Turn off the logger first if you do not want too many spam output.
2. Give it a try with
```bash
$ poetry run pytest --hypothesis-show-statistics
```