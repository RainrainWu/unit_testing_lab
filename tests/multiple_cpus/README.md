# Multiple CPUs

## Run Without `xdist` First
```bash
$ poetry run pytest
======================================================= test session starts ========================================================
platform darwin -- Python 3.10.2, pytest-7.1.2, pluggy-1.0.0
rootdir: /Users/rain.wu/Repositories/unit_testing_lab, configfile: pyproject.toml
plugins: xdist-2.5.0, forked-1.4.0
collected 26 items

test_multiple_cpu.py ..........................                                                                              [100%]

======================================================== 26 passed in 2.80s ========================================================

```

## Uncomment the Corresponding Configurations within `pyproject.toml`
Remember to comment out this part before playing another lab.
```toml
# Multiple CPUs
# addopts = "-n auto"
```

## Try Again

```bash
$ poetry run pytest
======================================================= test session starts ========================================================
platform darwin -- Python 3.10.2, pytest-7.1.2, pluggy-1.0.0
rootdir: /Users/rain.wu/Repositories/unit_testing_lab, configfile: pyproject.toml
plugins: xdist-2.5.0, forked-1.4.0
gw0 [26] / gw1 [26] / gw2 [26] / gw3 [26] / gw4 [26] / gw5 [26] / gw6 [26] / gw7 [26]
..........................                                                                                                   [100%]
======================================================== 26 passed in 0.88s ========================================================
```