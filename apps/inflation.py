import apps
import os
import requests
import json


# clear screen command
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# input check function
def inpCheck(userinput):
    if userinput == "quittomain":
        return "__QUIT_MAIN__"
    elif userinput == "quittocmd":
        clear()
        exit()
    elif userinput == "restart":
        return "__RESTART__"
    return

# main function
def main():
    print("Welcome to the FINANCIER™ INFLATION CALCULATOR. To return the main menu, type \"quittomain\". To quit the program, type \"quittocmd\"")
    input("Press ENTER/RETURN to continue.")
    clear()
    headers = {'Content-type': 'application/json'}
    data = json.dumps({"seriesid": ['CUUR0000AA0'],"startyear": startyear, "endyear": endyear})
    p = requests.post('https://api.bls.gov/publicAPI/v1/timeseries/data/', data=data, headers=headers)
    json_data = json.loads(p.text)
    for series in json_data['Results']['series']:
        for item in series['data']:
            if year == startyear:
                year = item['year']
            if period == months[month]:
                startyearcpi = item['value']
        print(x)