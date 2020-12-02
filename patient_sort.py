# Author: Ben Prince
# Version: 1.2
# Description: Used to figure out the number of test patients needed
#              based on the sex and age ranges given in the DCW

def sort_ranges(range_list):
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
        return p_list


def test_patient_list(range_list, overlap):
    p_list = []
    sort_ranges(range_list)
    return recur_fun(p_list, range_list, overlap)

# TODO: Make sure there is always a patient that starts at age 0
