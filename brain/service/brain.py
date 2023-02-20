from datetime import datetime, date
import string
import random


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
