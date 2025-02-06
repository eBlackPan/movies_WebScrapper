import csv


def dataSet(title,date,description):
    data = []
    for i in range(0,len(title)):
        temp = [
            title[i].text,
            ' '.join(date[i].text.split()),
            description[i].text.strip()
        ]
        data.append(temp)
    return data


def exportToCSV(data,encoding='utf-8'):
    fields = ["Name","Date","Description"]
    file = open("data.csv","a")
    csvwriter = csv.writer(file,lineterminator='\n')
    try:
        csvwriter.writerows(data)
    except:
        pass

    file.close()
