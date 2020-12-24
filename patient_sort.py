# Author: Ben Prince
# Version: 1.2
# Description: Used to figure out the number of test patients needed
#              based on the sex and age ranges given in the DCW

def sort_ranges(range_list):
    """Sorts the list of ages passed in by usnig the 
    insertion sort method. Return: void, just sorts
    the list that is passed in."""
    for r in range(1, len(range_list)):
        key = range_list[r]

        j = r-1
        while j >= 0 and key[2] < range_list[j][2]:
            range_list[j+1] = range_list[j]
            j -= 1
        range_list[j+1] = key


def recur_fun(p_list, range_list, overlap):
    if range_list:
        new_list = []
        range_compare = range_list[0][2]
        for r in range_list[1:]:
            if r[1] > range_compare or (range_compare - r[1]) < overlap:
                new_list.append(r)
        # TODO: Add if statement for items that will be negative if subtracting overlap
        p_list.append([range_list[0][0], (range_list[0][2] - overlap)])
        return recur_fun(p_list, new_list, overlap)
    else:
        # Checks if there is a test patient with the age of 0. If not one is added.
        if p_list[0][1] != 0:
            p_list.insert(0, [p_list[1][0], 0])
        return p_list


def test_patient_list(range_list, overlap):
    """Initializes the test patient list and sorts the age ranges
    from least to greatest range start dates. Returns: the
    recusion function with its first iteration."""
    p_list = []
    sort_ranges(range_list)
    return recur_fun(p_list, range_list, overlap)
