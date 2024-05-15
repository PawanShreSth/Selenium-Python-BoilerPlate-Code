import os
from utils.utils import load_environment_variables

load_environment_variables()

def get_explicit_wait_time():
    try:
        time = int(os.getenv("EXPLICIT_WAIT_UP_TO"))
        return time
    except ValueError:
        print("Error: Cannot parse the string as an integer. Please specify integer in 'EXPLICIT_WAIT_UP_TO' environment variable")