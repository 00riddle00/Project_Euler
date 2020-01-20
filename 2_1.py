
def fibonacci_sum(prev = None, current = None, sum_current = 0, max_val = None):

    if not current:
        current = 1
        prev = current

    if not current%2:
        sum_current += current

    next = current + prev

    if next < max_val:
        sum_current = fibonacci_sum(current, next, sum_current, max_val)

    return sum_current


result = fibonacci_sum(max_val=4000000)
print("result", result)

