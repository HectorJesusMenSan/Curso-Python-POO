def array_conversion(arr):
    """
    Reduce la lista combinando elementos de dos en dos: primero sumando, luego multiplicando, y repite.
    @param arr:
    @return:
    """
    iteration = 1
    while len(arr) > 1:
        new_arr = []
        for i in range(0, len(arr), 2):
            if iteration % 2 == 1:
                new_arr.append(arr[i] + arr[i + 1])
            else:
                new_arr.append(arr[i] * arr[i + 1])
        arr = new_arr
        iteration += 1
    return arr[0]