

# algorithm complexity:

def sum(current = None, max_val = None):

    if not current:
        current = 1
        prev = current
        sum_current = 0

    if not current%2:
        sum_current += current

    next = current + prev

    if next < max_val:
        sum_current = sum(next)

    return sum_current

max_val = 10

suma = sum(max_val=max_val)
print("s", suma)
