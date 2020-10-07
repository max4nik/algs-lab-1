import sys

from algorithms.chainsaw_manager import ChainsawManager
from helpers import csv_reader, algo_analysis

if __name__ == '__main__':

    # reads file name from terminal else user must input name
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
    else:
        file_name = input('Enter file name: ')

    # defining quicksort properties
    chainsaws_quicksort = csv_reader.read_chainsaws_from_csv(file_name)
    quicksort = ChainsawManager.sort_rolls_per_minute_asc_quicksort(chainsaws_quicksort, 0,
                                                                    len(chainsaws_quicksort) - 1)
    deltatime_quicksort = algo_analysis.get_function_time('quicksort')
    quicksort_result = [chainsaw.rolls_per_minute for chainsaw in chainsaws_quicksort]

    # defining insertion sort properties
    chainsaws_insertion = csv_reader.read_chainsaws_from_csv(file_name)
    insertion = ChainsawManager.sort_power_in_watt_desc_insertion(chainsaws_insertion)
    deltatime_insertion = algo_analysis.get_function_time('insertion')
    insertion_result = [chainsaw.power_in_watt for chainsaw in chainsaws_insertion]

    # quicksort algorithm representation
    print(algo_analysis.represent_algorithm('Quicksort', deltatime_quicksort, algo_analysis.quicksort_swap_counter,
                                            algo_analysis.quicksort_comparison_counter, quicksort_result))

    # insertion sort algorithm representation
    print(algo_analysis.represent_algorithm('Insertion', deltatime_insertion, algo_analysis.insertion_swap_counter,
                                            algo_analysis.insertion_comparison_counter, insertion_result))
