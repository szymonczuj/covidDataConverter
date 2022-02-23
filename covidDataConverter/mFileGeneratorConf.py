import csv, datetime
import codecs
from contextlib import closing
import requests

fields = []
rows = []

today = datetime.datetime.now()

fileName = "Conf" + str(today.strftime("%d")) + str(today.strftime("%m")) + str(today.strftime("%y")) + ".m"

inputData = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"
outputData = "C:/PATH/TO/M-FILES/DIRECTORY/" + fileName #Path to m-file

with closing(requests.get(inputData, stream=True)) as csvfile:
    reader = csv.reader(codecs.iterdecode(csvfile.iter_lines(), 'utf-8'))

    fields = next(reader)

    for row in reader:
        rows.append(row)

    totalRows = reader.line_num
    totalColumns = len(fields)

print("Output Matrix Size: [" + str(totalColumns) + "]x[" + str(totalRows) + "]")

confCases = "Conf=["

for row in rows:
    #if row[1] == "Antarctica" or row[1] == "Winter Olympics 2022": #Statement for skipping rows if not needed
    #    print("Skipping: " + row[1] + " " +  row[0])
    #    continue
    print("Processing: " + row[1] + " " +  row[0])
    for i in range(4, totalColumns):
        confCases = confCases + str(row[i]) + "\t"
    
    confCases = confCases + "\n"

confCases = confCases[:len(confCases)-2]    
confCases = confCases + "];"

print("\nWriting to file... \n" + outputData)

confCasesOutput = open(outputData, "w")
confCasesOutput.writelines(confCases)
confCasesOutput.close()


################################
###Autor skryptu: Szymon Czuj###
################################