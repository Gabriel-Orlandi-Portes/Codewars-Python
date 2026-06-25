def remove_smallest(numbers):
    if not numbers:
        return []

    result = numbers.copy()
    result.remove(min(result))
    return result