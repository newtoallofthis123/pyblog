from datetime import datetime, date
import string
import random

try:
    from .file import get_path
except ImportError:
    from file import get_path
import json
import sys
import os


def get_config():
    with open(get_path(['config.json']), 'r') as f:
        return json.loads(f.read())


def get_args():
    args = sys.argv[1:]
    query = ' '.join(sys.argv[3:])
    return {
        "cmd": args[0],
        "args": sys.argv[1],
        "query": query
    }


def hash_gen_engine():
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    whole = lower + upper + digits
    hash_string = random.sample(whole, 8)
    hash = "".join(hash_string)
    return hash


def censor(content):
    import re
    censor_node = re.compile(
        '([Ff][Uu]*[Cc]*[Kk]|[Ss]+[Ee]+[Xx]|[Dd]+[Ii]*[Cc]*[Kk]|[Pp][Us][Us][Yy]|[Pp][Oo]+[Rr]+[Nn])')
    censored = censor_node.sub("*CENSORED*", content)
    return censored


def time_cal():
    current_t = datetime.now()
    current_date = str(date.today())
    current_t_f = current_t.strftime("%H:%M:%S")
    time_date = f'{current_t_f} {current_date}'
    return time_date


def platform():
    import platform

    if platform.system() == "Windows":
        return "win"
    elif platform.system() in ["Linux", "Darwin"]:
        return "unix"
    else:
        return None


def cls():
    if platform() == "win":
        os.system("cls")
    elif platform() == "unix":
        os.system("clear")
    else:
        pass
