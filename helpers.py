def get_possibilities(n):
    combinations = []
    numbers = [x for x in range(1, n + 1)]
    find_combination(0, 0, [], combinations, n, numbers)

    return combinations


def find_combination(i, sum, current, combinations, target, numbers):
    if sum == target:
        combinations.append(current.copy())
        return

    if i >= len(numbers) or sum > target:
        return

    current.append(numbers[i])
    find_combination(i + 1, sum + numbers[i], current, combinations, target, numbers)

    current.pop()
    find_combination(i + 1, sum, current, combinations, target, numbers)


def flatten(ls):
    flattened = []
    for element in ls:
        for item in element:
            flattened.append(item)

    return flattened
