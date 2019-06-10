import requests

def user_menu():

    user_input=input("""Hi! What would you like to do
    1. PNR Status
    2. Train running status
    3. Train Route
    4. Trains between stations
    5. Seat Availability""")


    if user_input=='1':
        #check PNR
        check_pnr()
    elif user_input=='2':
        #running status
        check_running_status()
    elif user_input=='3':
        #train route
        show_train_route()
    elif user_input=='4':
        #between station
        show_train_between_stations()
    elif user_input=='5':
        #seat avail
        check_seat_availability()
    else:
        print('Bye')

def check_pnr():

    pnr=input('Enter pnr')

    response=requests.get('https://api.railwayapi.com/v2/pnr-status/pnr/' + pnr + '/apikey/wzpflrjekw')
    json_text=response.json()
    print(json_text['passengers'])

def check_running_status():

    train_no=input('Enter the train number')
    doj=input('Enter the date of journey')

    response = requests.get('https://api.railwayapi.com/v2/live/train/' + train_no + '/date/' + doj + '/apikey/wzpflrjekw')
    json_text = response.json()

    print(json_text['position'])


def show_train_route():

    train_no=input('Enter train number')
    response=requests.get('https://api.railwayapi.com/v2/route/train/' + train_no + '/apikey/wzpflrjekw')

    json_text=response.json()

    for i in json_text['route']:
        print(i['station']['name'])

def show_train_between_stations():

    source=input('Enter source station code')
    destination=input('Enter destination station code')
    doj=input('Enter date of journey')

    response=requests.get('https://api.railwayapi.com/v2/between/source/' + source + '/dest/' + destination + '/date/' + doj + '/apikey/wzpflrjekw')

    json_text = response.json()

    for i in json_text['trains']:
        print(i['name'])

def check_seat_availability():
    # do it yourself
    pass


user_menu()