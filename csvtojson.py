import csv, json

csvFilePath_fips = "fips.csv"
jsonFilePath_fips = "plotly/fips.json"

arr = []
with open (csvFilePath_fips) as csvFile:
    csvReader = csv.DictReader(csvFile)
    print(csvReader)
    for csvRow in csvReader:
        arr.append(csvRow)

with open(jsonFilePath_fips, "w") as jsonFile:
    jsonFile.write(json.dumps(arr, indent = 4))


csvFilePath_county = "us-counties.csv"
jsonFilePath_county = "plotly/counties.json"

arr = []
with open (csvFilePath_county) as csvFile:
    csvReader = csv.DictReader(csvFile)
    print(csvReader)
    for csvRow in csvReader:
        arr.append(csvRow)

with open(jsonFilePath_county, "w") as jsonFile:
    jsonFile.write(json.dumps(arr, indent = 4))


csvFilePath_state = "us-states.csv"
jsonFilePath_state = "plotly/states.json"

arr = []
with open (csvFilePath_state) as csvFile:
    csvReader = csv.DictReader(csvFile)
    print(csvReader)
    for csvRow in csvReader:
        arr.append(csvRow)

with open(jsonFilePath_state, "w") as jsonFile:
    jsonFile.write(json.dumps(arr, indent = 4))