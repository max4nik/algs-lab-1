import timeit

# counts amount of element swaps in algorithm
quicksort_swap_counter = insertion_swap_counter = 0

# counts amount of element comparisons in algorithm
quicksort_comparison_counter = insertion_comparison_counter = 0


def get_function_time(function_name):
    """
    measures function execution time using timeit lib
    :param function_name: function to measure
    :return: function execution time
    """
    return timeit.timeit(function_name, 'from __main__ import ' + function_name)


def represent_algorithm(algorithm_name, execution_time, amount_of_swaps, amount_of_comparison, result):
    """

    :param algorithm_name: name of algorithm to represent
    :param execution_time: algorithm execution time
    :param amount_of_swaps: algorithm swipes counter
    :param amount_of_comparison: algorithm comparison counter
    :param result: list of result values
    :return: visual representation of algorithm main properties for user
    """
    return algorithm_name.center(50, '-') + '\n' + \
           'Time: ' + str(execution_time) + '\n' + \
           'Amount of swaps: ' + str(amount_of_swaps) + '\n' + \
           'Amount of comparisons: ' + str(amount_of_comparison) + '\n' + \
           'Result: ' + str(result) + '\n'
