import csv

def dataSet(title,date,description):
    data = []
    for i in range(0,len(title)):
        temp = []
        temp.append(title[i].text)
        temp.append(date[i].text.split())
        temp.append(description[i].text)
        data.append(temp)
    return data





def exportToCSV(data):
    fields = ["Name","Date","Description"]
    file = open("data.csv","w")
    csvwriter = csv.writer(file)
    csvwriter.writerow(fields)
    csvwriter.writerows(data)
    file.close()
