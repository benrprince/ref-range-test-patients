# Author: Ben Prince
# Version: 1.2
# Description: Used to figure out the number of test patients needed
#              based on the sex and age ranges given in the DCW

# Initial build that read from a txt file
# try:
#     with open('data.txt', 'r') as infile:
#         for line in infile:
#             line = line.strip()
#             ref_range = line.split(",")
#             ref_range[1] = int(ref_range[1])
#             ref_range[2] = int(ref_range[2])
#             if ref_range[0] == 'Male':
#                 m_list.append(ref_range)
#             elif ref_range[0] == 'Female':
#                 f_list.append(ref_range)
#             else:
#                 u_list.append(ref_range)
#
# except FileNotFoundError:
#     print("can't find the file")

import xlrd
import xlwt

m_list = []
f_list = []
u_list = []

# minutes for 1 week. This can change
overlap = 10080

xl_workbook = xlrd.open_workbook('TestData.xlsx')
sheet = xl_workbook.sheet_by_index(0)

for i in range(1, sheet.nrows):
    temp_list = []
    if str(sheet.cell_value(i, 0)) == 'Male':
        temp_list.append(str(sheet.cell_value(i, 0)))
        temp_list.append(int(sheet.cell_value(i, 1)))
        temp_list.append(int(sheet.cell_value(i, 2)))
        m_list.append(temp_list)
    elif str(sheet.cell_value(i, 0)) == 'Female':
        temp_list.append(str(sheet.cell_value(i, 0)))
        temp_list.append(int(sheet.cell_value(i, 1)))
        temp_list.append(int(sheet.cell_value(i, 2)))
        f_list.append(temp_list)
    else:
        temp_list.append(str(sheet.cell_value(i, 0)))
        temp_list.append(int(sheet.cell_value(i, 1)))
        temp_list.append(int(sheet.cell_value(i, 2)))
        u_list.append(temp_list)


def sort_ranges(range_list):
    for r in range(1, len(range_list)):
        key = range_list[r]

        j = r-1
        while j >= 0 and key[2] < range_list[j][2]:
            range_list[j+1] = range_list[j]
            j -= 1
        range_list[j+1] = key


def recur_fun(p_list, range_list):
    if range_list:
        new_list = []
        range_compare = range_list[0][2]
        for r in range_list[1:]:
            if r[1] > range_compare or (range_compare - r[1]) < overlap:
                new_list.append(r)
        # TODO: Add if statement for items that will be negative if subtracting overlap
        p_list.append([range_list[0][0], (range_list[0][2] - overlap)])
        return recur_fun(p_list, new_list)
    else:
        return p_list


def test_patient_list(range_list):
    p_list = []
    sort_ranges(range_list)
    return recur_fun(p_list, range_list)

# TODO: Make sure there is always a patient that starts at age 0


print(test_patient_list(m_list))
print(test_patient_list(f_list))
print(test_patient_list(u_list))

# Write to a new workbook
wb = xlwt.Workbook()
patients = wb.add_sheet('Patients')

# Set up Doc
patients.write(0, 0, 'Sex', xlwt.Style.easyxf("font: bold on"))
patients.write(0, 1, 'Age', xlwt.Style.easyxf("font: bold on"))

m_list = test_patient_list(m_list)
m_len = len(m_list)
f_list = test_patient_list(f_list)
f_len = len(f_list)
u_list = test_patient_list(u_list)
u_len = len(u_list)


# import male data
for i in range(1, m_len):
    patients.write(i, 0, m_list[i-1][0])
    patients.write(i, 1, m_list[i-1][1])

# import female data
for i in range(m_len, f_len + m_len):
    patients.write(i, 0, f_list[i - m_len][0])
    patients.write(i, 1, f_list[i - m_len][1])

# import undefined or unknown data
for i in range(m_len + f_len, m_len + f_len + u_len):
    patients.write(i, 0, u_list[i - (m_len+f_len)][0])
    patients.write(i, 1, u_list[i - (m_len+f_len)][1])

wb.save('patients.xls')
