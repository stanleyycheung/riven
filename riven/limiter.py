import datetime
from time import sleep
from typing import Callable

CALLS_ONE_SEC_LIMIT = 20
CALLS_TWO_MIN_LIMIT = 100


def rate_limiter(func: Callable) -> Callable:
    call_times: list[datetime.datetime] = []
    total_call_count = 0

    def wrapper(*args, **kwargs):
        nonlocal call_times
        nonlocal total_call_count
        num_calls = len(call_times)
        now_time = datetime.datetime.now()
        # deal with first request
        if not call_times:
            call_times.append(now_time)
            return func(*args, **kwargs)
        # find when was the first API call 1 second and 2 min ago
        idx_one = 0
        idx_two = 0
        for idx, time in enumerate(call_times):
            if now_time - time >= datetime.timedelta(0, 119):
                idx_two = idx
            elif now_time - time >= datetime.timedelta(0, 0.9):
                idx_one = idx

        calls_within_two_min = num_calls - idx_two
        if calls_within_two_min >= CALLS_TWO_MIN_LIMIT:
            print(
                f'Calling too many calls within 2 mins (limit {CALLS_TWO_MIN_LIMIT}), sleeping 120 sec')
            sleep(121)
            call_times = []
        calls_within_one_sec = num_calls - idx_one
        if calls_within_one_sec > CALLS_ONE_SEC_LIMIT:
            print(
                f'Calling too many calls within 1 sec (limit {CALLS_ONE_SEC_LIMIT}), sleeping 1 sec')
            sleep(1)

        request = func(*args, **kwargs)
        if not request.from_cache:
            total_call_count += 1
            # add to list to track when we called API
            if len(call_times) == 100:
                call_times = call_times[1:]
            call_times.append(now_time)
            print(f'Calling: {args[0]}')
            print(f'API called {total_call_count} times')
        return request
    return wrapper
