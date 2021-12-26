finding_target = 14
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


def is_existing_target_number_binary(target, array):
    find_count = 0
    for number in array :
        find_count+=1
        if target == number:
            print(find_count)
            return True

    return False


result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result)