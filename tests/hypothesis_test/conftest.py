from hypothesis import settings

HYPOTHESIS_PROFILES = {
    "fast": {"max_examples": 20},
    "benchmark": {"max_examples": 100, "deadline": 20},
}


for name, configs in HYPOTHESIS_PROFILES.items():
    settings.register_profile(name, **configs)

settings.load_profile("fast")
