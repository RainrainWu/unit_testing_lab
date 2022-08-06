# Categorizing

## Uncomment the Corresponding Configurations within `pyproject.toml`
Remember to comment out this part before playing another lab.
```toml
# Categorizing
# log_cli = 1
# log_cli_level = 'INFO'
# log_cli_format = '%(levelname)-8s | %(message)s (%(filename)s:%(lineno)s)'
# markers = [
#     "pre_commit: test cases to run while pre-commit hook is triggered.",
#     "ci: test cases to be collected during continuous integration.",
#     "benchmark: test cases for performance benchmarking.",
#     "integration(dependency): integration test cases (with external dependencies).",
# ]
```

## List All Pytest Markers
```bash
$ poetry run pytest --markers
@pytest.mark.pre_commit: test cases to run while pre-commit hook is triggered.

@pytest.mark.ci: test cases to be collected during continuous integration.

@pytest.mark.benchmark: test cases for performance benchmarking.

@pytest.mark.integration(dependency): integration test cases (with external dependencies).

...
```

## Try Different Groups of Test Cases
```bash
$ poetry run pytest -m "pre_commit"
```
```bash
$ poetry run pytest -m "ci"
```
```bash
$ poetry run pytest -m "benchmark"
```
```bash
$ poetry run pytest -m "integration"
```

## Associate with Command Line Options
You may notice that several test cases were skipped due to missing dependencies.
```bash
$ poetry run pytest -m "benchmark"
test_categorizing.py::TestCategorizingGroupB::test_categorizing_e 
---------------------------------------------------------- live log setup ----------------------------------------------------------
INFO     | dependencies required: {'redis'} (conftest.py:44)
INFO     | dependencies provided: set() (conftest.py:47)
SKIPPED (dependencies missing: {'redis'})
```

Let's try again with the dependencies.
```bash
$ poetry run pytest -m "integration" --dependency=postgresql --dependency=redis
```

## Composite Filtering on Markers
```bash
$ poetry run pytest -m "ci or integration" --dependency=postgresql --dependency=redis
```