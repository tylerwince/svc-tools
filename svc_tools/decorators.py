"""Decorators that enable easy modifications to function behavior."""
import logging
import time
from functools import wraps
from typing import Callable

LOG = logging.getLogger("svc_tools")


def timer(log_level: Callable):
    """Time a function and log the time it took to execute.

    If you want to know how long a function takes to execute
    ang log alongside your application logs, then decorate
    your function with this.

    :param log_level: logging method to use in call
    :returns: Whatever your original function returns

    Usage ::
      >>> from svc_tools import timer
      >>> from time import sleep
      >>> import logging
      >>> @timer(logging.warning)
      >>> def myFunc(sleep_time):
      ...     # whatever you want to time
      ...     sleep(sleep_time)
      >>> myFunc(10)
      WARNING:root:myFunc took 10.000502109527588 to run.

    """

    def decorator(func):
        """Decorate the original function."""

        @wraps(func)
        def new_timed_func(*args, **kwargs):
            """Do the timing."""
            start_time = time.time()
            returned_value = func(*args, **kwargs)
            total_time = time.time() - start_time
            log_level(f"{func.__name__} took {total_time} to run.")
            return returned_value

        return new_timed_func

    return decorator
