import os
import json
import math
import datetime

fuel_level = float("500.5")
is_engine_active = True
crew_count = 5
mission_days = 12

total_rations = crew_count * mission_days * 3

ship_name = "Nebula-9"
print(f"Ship: {ship_name} | Fuel: {fuel_level} | Rations: {total_rations}")

cargo_list = ["Oxygen", "Water", "Batteries"]

cargo_list.append('Medkit')

coordinates = (54.2, -10.5, 99.0)

scanned_planets = {"Mars", "Jupiter"}

scanned_planets.add('Saturn')
crew_roles = {
    "Pilot" : "Zoe",
    "Engineer": "Kaylee"
}

can_jump_warp = 0

if fuel_level > 100:
    can_jump_warp = fuel_level

sensor_range = math.sqrt(144)

def count_countdown():
    for x in range(3, -1, -1):
        print(x)
        if x <= 0:
            print("BLastOff")


count_countdown()

oxygen = 3

while oxygen >= 0:
    print(f"Oxygen Level: {oxygen}")
    oxygen = oxygen - 1


if 'Medkit' in cargo_list:
    print("Ready")
else:
    print("Incomplete")

alien_signal = None

print(type(alien_signal))

# dest = input("Enter destination: ")

current_date = datetime.date.today()

try:
    100 / crew_count

except ZeroDivisionError:
    print('Zero division error')

print("Scucess")

file = open('inventory.txt', 'w')

file.write("Laptop: 10, Mouse: 50")

file = open('inventory.txt', 'r')

print(file.read())

product_data = {'id': 101, 'price': 99.9}

print(json.dumps(product_data))

action = "SAVE"

match action:
    case "SAVE":
        print("Saving file..")

    case "DELETE":
        os.remove('inventory.txt')
    case default:
        print('invalid command')