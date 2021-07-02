ref-range-test-patients
Author: Ben Prince
Version: 1.2
Description: This program takes in an excel file with a list of age ranges for a specific sex and
             and returns an excel file with all of the test patients needed to adequately test the
             reference ranges that were built. This should effectively cut the number of test
             patients needed by half.
             
Input Excel Requirements: First row is not read because it is expected to have headers (sex, age
                          from, age to). Male and Female should have normal capitalization. The
                          Unknown/Undifferentiated sex doesn't have any requirements (added to the
                          u_list from an else statement so anything that isn't spelled correctly
                          will fall into the u_list). Age to and age from should be in minutes in
                          the document. The reference range audit ran in DVD returns age ranges in
                          minutes so this should not be a problem.
                          
Program Internal Explanation: TODO
                          
Output Excel File: Output is 2 columns: Sex and Age. These pairs should be used to create test 
                   patients. As of now (V 1.2) the output age is in minutes.
                   
Example Excel Input:

![image](https://user-images.githubusercontent.com/55722294/124276258-2c56b280-db09-11eb-93d4-806cd7765c8a.png)
