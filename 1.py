# algorithm complexity: O(n)

def solution(maximum):

    multiples = []

    for i in range(1, maximum):
        if not i%3 or not i%5:
            multiples.append(i)

    return sum(multiples)

result = solution(1000)
print("result", result)
