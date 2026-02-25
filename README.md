Time Calculator (FreeCodeCamp)
A Python implementation of a time calculator, developed as the second project for the Scientific Computing with Python certification.

Project Overview
The goal of this project was to create an add_time function that takes a start time (in 12-hour format), a duration time, and an optional starting day of the week. The function calculates the end time, properly handling day transitions and AM/PM shifts, and returns the result in a formatted string.

Key Features
- 12-Hour Format Logic: Accurately handles the transition between AM and PM, including the specific case of 12:00.
- Day Tracking: Automatically calculates how many days have passed (e.g., "(next day)" or "(n days later)").
- Optional Day of the Week: Dynamically identifies the future day of the week if an optional starting day is provided (case-insensitive).
- Flexible Duration: Supports durations that can exceed 24 hours, correctly incrementing the day count.

Technical Skills Applied
- Mathematical Logic: Utilized floor division (//) and the modulo operator (%) to handle time overflows and day cycles.
- String Parsing: Used .split() and map() to efficiently extract and convert time components from strings.
- Code Optimization: Refactored the initial logic from a series of complex nested conditionals into a streamlined, arithmetic-based approach for better readability and performance.
- Data Structures: Used lists to manage and index the days of the week, allowing for easy calculation of future days using cyclic indexing.

Learning Reflections
This project taught me how to handle edge cases in 12-hour time formats (like 12:00 AM/PM) and the value of refactoring. I learned that converting everything to a base unit (minutes) before performing calculations often simplifies complex logic significantly.

Created by Chicot-q
