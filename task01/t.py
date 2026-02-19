import datetime
import math

budget_str = 1500
total_budget = float(budget_str)
destination = "Paris"
travel_date = datetime.datetime(2026, 7, 15)
date_today = datetime.datetime.today()
days_until = (travel_date - datetime.datetime.today()).days
flight_hours = math.ceil(7.4)

is_international = True
can_afford = total_budget >= 1000 and is_international

cities_to_visit = ["Eiffel Tower", "Louvre", "Versailles"]
coordinates = (48.8566, 2.3522)

cities_to_visit.append("Montmartre")

packing_list = {"Passport", "Camera", "Charger"}

packing_list.add('Passport')
packing_list.add("Walking Shoes")

print(f"Trip to {destination.upper()} in {days_until} days!")
print(can_afford)
print(cities_to_visit)
print(packing_list)