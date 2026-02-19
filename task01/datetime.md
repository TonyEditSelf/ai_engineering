**# -----------------------------**

**# DATETIME MODULE CHEAT SHEET**

**# -----------------------------**



**import datetime**



**# -----------------------------**

**# 1. DATE - year, month, day**

**# -----------------------------**

**d = datetime.date(2026, 7, 15)**

**print("Date:", d)**

**print("Year:", d.year)**

**print("Month:", d.month)**

**print("Day:", d.day)**



**# Get today's date**

**today = datetime.date.today()**

**print("Today:", today)**



**# -----------------------------**

**# 2. TIME - hour, minute, second**

**# -----------------------------**

**t = datetime.time(14, 30, 45)**

**print("Time:", t)**

**print("Hour:", t.hour)**

**print("Minute:", t.minute)**

**print("Second:", t.second)**



**# -----------------------------**

**# 3. DATETIME - combines date + time**

**# -----------------------------**

**dt = datetime.datetime(2026, 7, 15, 14, 30, 45)**

**print("Datetime:", dt)**

**print("Date part:", dt.date())**

**print("Time part:", dt.time())**



**# Get current datetime**

**now = datetime.datetime.now()**

**print("Now:", now)**



**# -----------------------------**

**# 4. TIMEDELTA - duration between dates/times**

**# -----------------------------**

**future = datetime.date(2026, 7, 15)**

**delta = future - today**

**print("Days until future date:", delta.days)**



**# Add/subtract days**

**tomorrow = today + datetime.timedelta(days=1)**

**yesterday = today - datetime.timedelta(days=1)**

**print("Tomorrow:", tomorrow)**

**print("Yesterday:", yesterday)**



**# -----------------------------**

**# 5. FORMATTING DATES**

**# -----------------------------**

**formatted = dt.strftime("%d-%m-%Y %H:%M:%S")**

**print("Formatted datetime:", formatted)**



**# -----------------------------**

**# 6. PARSING STRINGS TO DATES**

**# -----------------------------**

**date\_str = "15/07/2026 14:30"**

**parsed\_dt = datetime.datetime.strptime(date\_str, "%d/%m/%Y %H:%M")**

**print("Parsed datetime:", parsed\_dt)**



