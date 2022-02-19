import datetime
from time import sleep

def rate_limiter(func):
    call_times = []
    def wrapper(*args, **kwargs):
        nonlocal call_times
        num_calls = len(call_times)
        now_time = datetime.datetime.now()
        # add to list to track when we called API
        call_times.append(now_time)
        # find when was the first API call 1 second and 2 min ago
        idx_two = None
        for idx, time in enumerate(call_times):
            if idx_two is None and time > now_time - datetime.timedelta(0, 120):
                idx_two = idx
            elif time > now_time - datetime.timedelta(0, 1):
                break
            elif time < now_time - datetime.timedelta(0, 1):
                call_times.pop(idx)
        calls_within_one_sec = num_calls - idx + 1
        if calls_within_one_sec > 20:
            print('Calling too many calls within 1 second (limit 20)')
            # TODO: make a smart way to sleep not as long
            sleep(1)
        calls_within_two_min = num_calls - idx_two + 1
        if calls_within_two_min > 100:
            print('Calling too many calls within 2 mins (limit 100)')
            sleep(120)
        print(f'API called {num_calls} times')
        return func(*args, **kwargs)
    return wrapper