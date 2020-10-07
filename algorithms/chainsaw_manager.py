from helpers import algo_analysis


class ChainsawManager:
    @staticmethod
    def sort_power_in_watt_desc_insertion(chainsaw_list):
        """
        INSERTION
        sorting list of chainsaws in descending order using insertion sort method with average time complexity of O(n^2)
        :param chainsaw_list: list of chainsaws to sort
        """
        for iterator in range(1, len(chainsaw_list)):
            value_to_sort = chainsaw_list[iterator].power_in_watt
            while iterator > 0 and value_to_sort > chainsaw_list[iterator - 1].power_in_watt:
                algo_analysis.insertion_comparison_counter += 2
                chainsaw_list[iterator], chainsaw_list[iterator - 1] = chainsaw_list[iterator - 1], chainsaw_list[
                    iterator]
                algo_analysis.insertion_swap_counter += 1
                iterator -= 1

    @staticmethod
    def sort_rolls_per_minute_asc_quicksort(chainsaw_list, low_index, high_index):
        """
        QUICKSORT
        sorting list of chainsaws in ascending order using quicksort sort method with average time complexity of O(nlog(n))
        :param chainsaw_list: list of chainsaws to sort
        :param low_index: starting index
        :param high_index: ending index
        :return: returns same list, if it`s only one element there
        """
        if len(chainsaw_list) == 1:
            return chainsaw_list
        if low_index < high_index:
            median = ChainsawManager._get_best_pivot(chainsaw_list, low_index, high_index)
            chainsaw_list[median], chainsaw_list[high_index] = chainsaw_list[high_index], chainsaw_list[median]
            algo_analysis.quicksort_swap_counter += 1
            pivot_index = ChainsawManager._partition(chainsaw_list, low_index, high_index)
            ChainsawManager.sort_rolls_per_minute_asc_quicksort(chainsaw_list, low_index, pivot_index - 1)
            ChainsawManager.sort_rolls_per_minute_asc_quicksort(chainsaw_list, pivot_index + 1, high_index)

    @staticmethod
    def _partition(chainsaw_list, low_index, high_index):
        """
        QUICKSORT
        places best pivot from _get_best_pivot() in the end of the list, then places all smaller then pivot to left
        and all bigger then pivot to right, then swaps pivot between smaller and bigger
        :param chainsaw_list: list of chainsaws to divide
        :param low_index: starting index
        :param high_index: ending index
        :return: returns index between smaller and bigger elements then pivot where pivot was placed at the end of iteration
        """
        pivot = chainsaw_list[high_index].rolls_per_minute
        border = low_index - 1
        for iterator in range(low_index, high_index):
            if chainsaw_list[iterator].rolls_per_minute <= pivot:
                algo_analysis.quicksort_comparison_counter += 1
                border += 1
                chainsaw_list[border], chainsaw_list[iterator] = chainsaw_list[iterator], chainsaw_list[border]
                algo_analysis.quicksort_swap_counter += 1
        chainsaw_list[border + 1], chainsaw_list[high_index] = chainsaw_list[high_index], chainsaw_list[border + 1]
        algo_analysis.quicksort_swap_counter += 1
        return border + 1

    @staticmethod
    def _get_best_pivot(chainsaw_list, low_index, high_index):
        """
        QUICKSORT
        takes first and last element from the list, calculates middle, then compare them and returns median as a pivot
        :param chainsaw_list: list of chainsaws to
        :param low_index: starting index
        :param high_index: ending index
        :return: median of first, middle and last elements
        """
        middle_index = (low_index + high_index) // 2
        pivot = high_index
        if chainsaw_list[low_index].rolls_per_minute < chainsaw_list[middle_index].rolls_per_minute < \
                chainsaw_list[high_index].rolls_per_minute:
            algo_analysis.quicksort_comparison_counter += 2
            pivot = middle_index
        elif chainsaw_list[low_index].rolls_per_minute < chainsaw_list[high_index].rolls_per_minute:
            algo_analysis.quicksort_comparison_counter += 1
            pivot = low_index
        return pivot
