# Time Calculator

---
## Overview:
The python module calculates the new time after adding a specified duration to a given start time. Additionally, it can also return the day of the week if a day is provided. The function handles time in 12-hour AM/PM format and accounts for changes in both time and day, including cases where the new time spans across multiple days.

---
## Function Definition:
```python
def add_time(start, duration, day=None)
```

### Parameters
- `start` (str): The start time in 12-hour format (e.g., '3:00 PM').
- `duration` (str): The duration to be added in the format 'HH:MM' (e.g., '2:30').
- `day` (str, optional): The day of the week (e.g., 'Monday'). If provided, the function will return the new day after the duration is added.

### Returns
- A string representing the new time, potentially including the day of the week, with appropriate handling of time transitions (AM/PM) and multiple days.

---
## Detailed Description:
### 1. Time Parsing:
- The start time and its period (AM/PM) are extracted from the `start` parameter.
- The duration is parsed to get hours and minutes.

### 2. Time Calculation:
- The total minutes are calculated by adding the minutes from the start time and the duration.
- Any overflow of minutes (i.e., greater than 60) is converted into additional hours.
- The total hours are calculated by adding the start hours, duration hours, and any additional hours from the minutes overflow.


### 3. Handling AM/PM Transition:
- The period (AM or PM) is updated based on the total hours after adding the duration.
- The function correctly handles the 12-hour clock cycle and toggles the AM/PM period based on the total number of hours that have passed.

### 4. Handling the Day of the Week:
- If a `day` is provided, the function calculates the new day by considering how many days have passed based on the total number of hours divided by 24.
- The function adjusts for the possibility of spanning multiple days, including handling day transitions like "next day" or "X days later."

### 5. Output Format:
- The function returns the new time in a formatted string with the correct hours, minutes, and AM/PM.
- If the `day` parameter is provided, it appends the calculated day of the week to the output.
- If the duration spans multiple days, the function includes the number of days passed, e.g., "(next day)" or "(X days later)."

---
## Edge Cases Handled
- Correctly handles transitions from AM to PM or vice versa.
- Correctly calculates the number of days that have passed when the time spans over 24 hours.
- Handles day names in any case (e.g., 'tueSday' is correctly interpreted as 'Tuesday').