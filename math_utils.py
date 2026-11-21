```python
def factorial(n: int) -> int:
    """Return n! for a non-negative integer n."""
    if not isinstance(n, int) or isinstance(n, bool) or n < 0:
        raise ValueError("n must be a non-negative integer")

    result = 1
    for value in range(2, n + 1):
        result *= value
    return result


def quadratic(a: float, b: float, c: float, x: float) -> float:
    """Evaluate the quadratic function f(x) = ax² + bx + c."""
    return a * x**2 + b * x + c
```