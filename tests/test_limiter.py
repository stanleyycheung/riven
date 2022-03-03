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

        start = 0
        for i in range(1, len(called_times)):
            if called_times[i] - called_times[start] >= datetime.timedelta(0, 1):
                assert i - start - 1 <= 20
                start = i
