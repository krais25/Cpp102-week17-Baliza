# Simulated Device Monitoring and Alert System

**Student Name:** Christian Joseph B. Baliza
**Student Number:** 2601298
**Section:** 1-CpE C

## Project Description
This program monitors simulated device temperature readings. It stores a list of readings, accepts new valid readings, and classifies each reading as NORMAL, WARNING, or CRITICAL. It also prints a numerical summary and an overall monitoring status. It was built for CPP102 Week 17 as a modular Python project.

## Features
- View all stored temperature readings
- Add a new reading (whole numbers from 0 to 100 only)
- Classify every reading (below 30 = NORMAL, 30 to 35 = WARNING, above 35 = CRITICAL)
- Generate a summary: count, total, average, minimum, maximum, category counts and percentages, overall status
- Reject invalid menu choices and invalid readings without crashing

## Requirements
- Python 3 (no external packages)

## How to Run
1. Open a terminal inside the Week17 folder.
2. Type: `python device_monitor.py`
   (On macOS or Linux, type: `python3 device_monitor.py`)

## Sample Output
```
Enter choice: 4

MONITORING SUMMARY
------------------
Number of readings  : 5
Total of readings   : 160
Average temperature : 32.00 °C
Minimum temperature : 28 °C
Maximum temperature : 37 °C

NORMAL   : 2 (40.00%)
WARNING  : 2 (40.00%)
CRITICAL : 1 (20.00%)

Overall Status: ATTENTION REQUIRED
```

## Test Cases
I performed 13 tests (the 10 required tests plus 3 extra tests). 13 passed and 0 failed. Full details are in [test_cases.md](test_cases.md).

## Known Limitations
- Readings are lost when the program closes (no file handling).
- Readings cannot be edited or deleted once added.
- Input with spaces, such as " 33", is rejected as invalid.
- The temperature limits (30 and 35) are fixed for this classroom simulation and are not real device-safety standards.

## Reflection
In this project, I learned how to combine lists, loops, selection, and functions into one complete program. Using separate functions made the code easier to understand and test. The most challenging part for me was input validation, especially boundary tests TC06 and TC07. I tried different values to understand how the program worked. If I improve this project in the future, I would add a feature that saves the readings to a file so the data will not be lost when the program closes.
