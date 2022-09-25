import datetime
import time
from unittest.mock import MagicMock
from riven.limiter import CALLS_ONE_SEC_LIMIT, CALLS_TWO_MIN_LIMIT, rate_limiter


class TestLimiter:

    def test_limiter_one_second_limit(self):
        called_times = []

        @rate_limiter
        def mock_function(num):
            request = MagicMock()
            request.from_cache = False
            request.__repr__ = lambda _: f"Requesting: {num}"
            called_times.append(datetime.datetime.now())
            return request

        for i in range(100):
            mock_function(i)

        left, right = 0, 0
        while right < len(called_times):
            while right < len(called_times) and called_times[right] - called_times[left] <= datetime.timedelta(0, 1):
                right += 1
            assert right - 1 - left <= CALLS_ONE_SEC_LIMIT
            left += 1

    def test_limiter_two_minute_limit(self):
        called_times = []

        @rate_limiter
        def mock_function(num):
            request = MagicMock()
            request.from_cache = False
            request.__repr__ = lambda _: f"Requesting: {num}"
            called_times.append(datetime.datetime.now())
            time.sleep(0.1)
            return request

        for i in range(150):
            mock_function(i)

        left, right = 0, 0
        while right < len(called_times):
            while right < len(called_times) and called_times[right] - called_times[left] <= datetime.timedelta(0, 120):
                right += 1
            assert right - 1 - left <= CALLS_TWO_MIN_LIMIT
            left += 1
