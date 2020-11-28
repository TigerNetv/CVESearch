import datetime
import csv
from colored import fg, attr

whitecolor = fg('#FFFFFF')
redcolor = fg('#8B0000')
greencolor = fg('#009900')
timecolor = fg('#9400D3')
res = attr('reset')

now = datetime.datetime.now()
print('')
print(greencolor + '  ██████ ██    ██ ███████ ███████ ███████  █████  ██████   ██████ ██   ██' + res)
print(greencolor + ' ██      ██    ██ ██      ██      ██      ██   ██ ██   ██ ██      ██   ██' + res)
print(greencolor + ' ██      ██    ██ █████   ███████ █████   ███████ ██████  ██      ███████' + res)
print(greencolor + ' ██       ██  ██  ██           ██ ██      ██   ██ ██   ██ ██      ██   ██ ' + res)
print(greencolor + '  ██████   ████   ███████ ███████ ███████ ██   ██ ██   ██  ██████ ██   ██' + res)
print('')


with open("data/data.csv", encoding="utf8", errors='ignore') as csvfile:
    reader = csv.reader(csvfile, skipinitialspace=True)
    search = input(timecolor + now.strftime("%d/%m/%Y %H:%M:%S") + res + whitecolor +  " Search : " + res)
    for row in reader:
        for str in row:
            if search in str:
                print(row)