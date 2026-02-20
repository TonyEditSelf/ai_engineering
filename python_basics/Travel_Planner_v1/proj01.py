import os
import array
import datetime
import math
import json

budget_str = 1500
total_budget = float(budget_str)
destination = "Paris"
duration = 7
travel_date = datetime.datetime(2026, 7, 15)
date_today = datetime.datetime.today()
days_until = (travel_date - datetime.datetime.today()).days

flight_hours = math.ceil(7.4)

print(f"Trip to {destination.upper()} in {days_until} days!")

is_international = True
can_afford = total_budget >= 1000 and is_international

cities_to_visit = ["Eiffel Tower", "Louvre", "Versailles"]
coordinates = (48.8566, 2.3522)

cities_to_visit.append("Montmartre")

packing_list = {"Passport", "Camera", "Charger"}

packing_list.add('Passport')
packing_list.add("Walking Shoes")

trip_info = {
    "dest": destination,
    "budget": total_budget,
    "tags": ["Culture", "Food"]
}

user_notes = None

user_notes = input("Any special requests? ")

additional_funds = None

while additional_funds == None or additional_funds < 0:

    try:
        additional_funds = float(input('How much additional fund are you ready to spare from 0 or upwards? '))

        if additional_funds >=0:
            print("Sure lets manage with this ")

        else:
            print("Enter a value greater than or equal to 0 ")

    except ValueError:

        print('Please insert a numeric value ')

def calculate_daily_spend(total, days):
    return total/days

per_day_spending = calculate_daily_spend(total_budget, duration)

print(f"Per Day Spending: {per_day_spending}")

if total_budget > 2000:
    print('Luxury Trip')
else:
    print("Budget Trip")

transport_mode = "Train"

match transport_mode:
    case 'Train':
        print("Scenic Trip")
    case "Flight":
        print("Fast")
    case "Car":
        print("Flexible")

countdown = 5
while countdown >= 0:
    print(countdown)
    countdown -= 1

for x in range(1, 4):
    print(f"Day {x}")

json_data = json.dumps(trip_info)
print(json_data)

fileread = open('itinerary.txt', 'w')
fileread.write(f"Trip to {destination} in {days_until} days")
fileread.close()

with open('itinerary.txt', 'r') as file_content:
    x = file_content.read()

print(x)

with open('itinerary.txt', 'a') as file:
    file.write(f"\nEstimated Flight Hours: {flight_hours}" )

with open('itinerary.txt', 'r') as file:
    x = file.read()
    print(x)

expenses = array.array('d', [120.5, 45.0, 80.75])

print(expenses[0])

os.remove('temp.txt')