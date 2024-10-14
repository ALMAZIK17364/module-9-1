def apply_all_func(int_list, *functions):
    results = {}
    for cur_func in functions:
        results[cur_func.__name__] = cur_func(int_list)

    return results

print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))