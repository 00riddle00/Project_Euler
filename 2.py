# algorithm complexity:

def sum(prev = None, current = None, sum_current = 0, max_val = None):

    if not current:
        current = 1
        prev = current
        # sum_current = 0

    if not current%2:
        sum_current += current

    next = current + prev

    if next < max_val:
        sum_current = sum(current, next, sum_current, max_val)

    return sum_current

result = sum(max_val=4000000)
print("result", result)
