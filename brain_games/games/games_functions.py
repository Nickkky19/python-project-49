def is_even(temp_number: int) -> bool:
    return temp_number % 2 == 0


def is_prime(temp_number: int) -> bool:
    if temp_number == 2:
        return True
    for i in range(2, temp_number // 2 + 1):
        if not temp_number % i:
            return False
    return True


def make_list_with_step(list_length: int,
                        list_start: int,
                        list_step: int) -> list:
    result_list = [list_start]
    for i in range(list_length):
        result_list.append(result_list[i] + list_step)
    return result_list
