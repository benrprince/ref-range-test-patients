# Author: Ben Prince
# Version: 1.2
# Description: Used to figure out the number of test patients needed
#              based on the sex and age ranges given in the DCW

import patient_sort as ps
import xlrd
import xlwt
import os


def patients(filename):
    m_list = []
    f_list = []
    u_list = []

    # minutes for 1 week. This can change
    overlap = 10080

    xl_workbook = xlrd.open_workbook(filename)
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

    # print(ps.test_patient_list(m_list, overlap))
    # print(ps.test_patient_list(f_list, overlap))
    # print(ps.test_patient_list(u_list, overlap))

    # Write to a new workbook
    wb = xlwt.Workbook()
    patients = wb.add_sheet('Patients')

    # Set up Doc
    patients.write(0, 0, 'Sex', xlwt.Style.easyxf("font: bold on"))
    patients.write(0, 1, 'Age', xlwt.Style.easyxf("font: bold on"))

    m_list = ps.test_patient_list(m_list, overlap)
    m_len = len(m_list)
    f_list = ps.test_patient_list(f_list, overlap)
    f_len = len(f_list)
    u_list = ps.test_patient_list(u_list, overlap)
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

    return wb
