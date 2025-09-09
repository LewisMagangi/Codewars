def high_and_low(numbers):
    numbers_list = (int(num) for num in numbers.split())
    sorted_string = sorted(numbers_list)
    result = f'{sorted_string[-1]} {sorted_string[0]}'
    return result
    