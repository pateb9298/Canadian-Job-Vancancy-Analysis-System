import sys
import csv

def main(argv):

    if len(argv) != 4:
        print("Error: Incorrect number of command line parameters.")
        sys.exit(1)

    fileName = argv[3]
    occupationOne = argv[1]
    occupationTwo = argv[2]

    try:
        data_fh = open(fileName, encoding="utf-8-sig")

    except IOError as err:
        print("Unable to open names file '{}' : {}".format(
                fileName, err), file=sys.stderr)
        sys.exit(1)

    data_reader = csv.reader(data_fh)

    jobCounter1 = float(0)
    jobCounter2 = float(0)



    for row in data_reader:

        if ((row[3] == occupationOne) and (row[5] == "Job vacancies")):
             if ((row[12] == '')):
                 numJobs = float(0)
             else:
                numJobs = float(row[12]) 
             #print("row:", row)
             #print("counter1",jobCounter1,"numJobs", numJobs)
             #print(" ")
             jobCounter1 += numJobs
        if ((row[3] == occupationTwo) and (row[5] == "Job vacancies")):
             numJobs = float(0)
             if ((row[12] == '')):
                 numJobs = float(0)
             else:
                numJobs = float(row[12]) 
             jobCounter2 += numJobs
             #print("row:", row)
             #print("counter2",jobCounter2,"numJobs", numJobs)
             #print(" ")

    print("Occupation, Total Job Vacancies:")
    print(occupationOne,",",jobCounter1)
    print(occupationTwo,",",jobCounter2)
main(sys.argv)