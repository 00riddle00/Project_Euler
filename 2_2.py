
def fibonacci_sum(max_val):

    prev = 1
    current = 1
    sum_current = 0

    while current < max_val:
        if not current%2:
            sum_current += current
        current, prev = current + prev, current
    return sum_current

result = fibonacci_sum(max_val=4000000)
print("result", result)
