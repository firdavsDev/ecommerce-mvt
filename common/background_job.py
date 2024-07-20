"""
Run functions in the background decorator for Django.
"""

import threading
from functools import wraps


def run_in_background(func):
    """
    Run the function in the background.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        thread = threading.Thread(target=func, args=args, kwargs=kwargs)
        thread.start()

    return wrapper


"""
Example usage:

from common.background_job import run_in_background

@run_in_background
def my_function():
    print('Hello world')

my_function()

"""
