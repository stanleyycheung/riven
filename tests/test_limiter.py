import datetime
from unittest.mock import MagicMock
from riven.limiter import rate_limiter


class TestLimiter:

    def test_limter_one_second_limit(self):
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
            assert right - 1 - left <= 20
            left += 1
