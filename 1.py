
# algorithm complexity: O(n)
# TODO

debug = True

def solution(maximum):

    multiples = []

    for i in range(1, maximum):
        if not i%3 or not i%5:
            multiples.append(i)

    return sum(multiples)

max_limit = 1000

result = solution(max_limit)

if debug:
    print("result", result)
