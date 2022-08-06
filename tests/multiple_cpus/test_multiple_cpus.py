import logging
import string
from time import sleep

LOGGER = logging.getLogger(__name__)


TestMultipleCPUs = type(
    "TestMultipleCPUs",
    (object,),
    {
        f"test_multiple_cpu_{suffix}": lambda _: sleep(0.1)
        for suffix in string.ascii_lowercase
    },
)
