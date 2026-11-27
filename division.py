import math


def divide(dividend: int | float, divisor: int | float) -> float:
    if isinstance(dividend, bool) or not isinstance(dividend, (int, float)):
        raise TypeError("dividend must be an int or float, not bool")
    if isinstance(divisor, bool) or not isinstance(divisor, (int, float)):
        raise TypeError("divisor must be an int or float, not bool")

    dividend = float(dividend)
    divisor = float(divisor)

    if not math.isfinite(dividend):
        raise ValueError("dividend must be finite")
    if not math.isfinite(divisor):
        raise ValueError("divisor must be finite")
    if divisor == 0.0:
        raise ZeroDivisionError("divisor must not be zero")

    result = dividend / divisor
    if not math.isfinite(result):
        raise OverflowError("division result is not finite")
    return result
