'''
  Functional Summary
      Statistics Canada ("StatsCan") is extensive, and contains various forms of data collected by the various provinces and territories within the country.  In our project we will consider what questions we can answer using the data in this archive.  The project is open-ended, allowing you to answer questions of interest to your group (coming up with questions will be our first milestone task).

The data provided is extensive, and will therefore take significant time to process.  A good strategy therefore is to pull out portions of the data relevant to particular questions so that your code doesn't need to keep re-processing the full data set.


# Lab Data

In this lab, we wish to create a set of tools that will allow us to get data associated with job vacancies for computing professionals by province.

We will extract data from the StatsCan data set provided for you here [`14100328-eng.zip`](https://uoguelphca-my.sharepoint.com/:u:/r/personal/ahamil01_uoguelph_ca/Documents/CIS2250-W24-Lab6/14100328-eng.zip?csf=1&web=1&e=qXIqfk)

The above link is cached for you on campus via OneDrive, but it is originally from Statistics Canada [https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1410032805](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1410032805).   You may also download it from there, where it is referred to as the "full data set".

In this zip archive are two .csv files:
* `14100328.csv` -- a CSV file with 37,888,313 rows. 
* `14100328_MetaData.csv` -- a CSV file that describes the other file.

If we look in the `14100328.csv` file, we can see that the header describes the fields below.    You can print the first 10 lines of a file in a terminal using a command like this:

	head 14100328.csv

For each there is information by field in the MetaData file.

* `REF_DATE`	reference date
* `GEO`	(Dimension ID 1) geographical region
* `DGUID`	geographical region ID code
* `National Occupational Classification`	(Dimension ID 2) one of 692 categories as listed in the meta-data file
* `Job vacancy characteristics` (Dimension ID 3) *e.g.* "Full-time", "Part-time"
* `Statistics`	(Dimension ID 4) "`Job vacancies`", "`Proportion of job vacancies`" or "`Average offered hourly wage`"
* `UOM`	"Unit of Measure"
* `UOM_ID`	"Unit of Measure ID"
* `SCALAR_FACTOR`	describes the measurement type -- for this data always `units`
* `SCALAR_ID`	ID for scalar factor
* `VECTOR`	StatsCan vector code
* `COORDINATE`	StatsCan cube coordinate
* `VALUE`	the value that is being reported in fixed decimal notation (see "`DECIMALS`" below)
* `STATUS`	encoded according to the meta data file
* `SYMBOL`	always blank for this data
* `TERMINATED`	always blank for this data
* `DECIMALS`	number of decimals to use when interpreting the value (multiply the `VALUE` by `10e-{DECIMALS}` to get a true floating point value)

We have also provided a subset of this table for you for debugging purposes in the `141003280-Ontario-2023-extract.csv` file as part of the lab download.  This small extract contains only a subset of data from 2023 from the larger file, but it is still 16,297 lines, even though it is only 0.043% of the full data set!

'''

import sys
import csv


def main(argv):

    if len(argv) != 4:
        print("Error: Incorrect number of command line parameters.")
        sys.exit(1)

    fileName1 = argv[1]
    fileName2 = argv[2]
    occupation = argv[3]
    # minEd = argv[4]

    try:
        data_1 = open(fileName1, encoding="utf-8-sig")
    except IOError as err:
        print("Unable to open names file '{}' : {}".format(
                fileName1, err), file=sys.stderr)
        sys.exit(1)

    try:
        data_2 = open(fileName2, encoding="utf-8-sig")
    
    except IOError as err:
        print("Unable to open names file '{}' : {}".format(
                fileName2, err), file=sys.stderr)
        sys.exit(1)

    education_requirements = {
    0: "No minimum level of education required",
    1: "High school diploma or equivalent",
    2: "Non-university certificate or diploma",
    3: "University certificate or diploma below bachelor's level",
    4: "Bachelor's degree"
    }
    
    data_reader1 = csv.reader(data_1)
    data_reader2 = csv.reader(data_2)

    for row in data_reader1:
        province = row[1]
        occupationData=row[3]
        education_level =row[4]

        for key, value in education_requirements.items():
            if occupationData == occupation and education_level == value:
                print(row[1] + "," + row[3] + "," + row[4]+ ","+ row[5] + "," + row[12])

    for row in data_reader2:
        province = row[1]
        occupationData=row[3]
        education_level = row[4]

        for key, value in education_requirements.items():
            if occupationData == occupation and education_level == value:
                print(province + "," + row[3] + "," + row[4]+ ","+ row[5] + "," + row[12])


main(sys.argv)

