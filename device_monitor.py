"""Simulated Device Monitoring and Alert System (CPP102 Week 17)."""


def get_initial_readings():
    """Return the starting list of simulated temperature readings in °C."""
    return [28, 31, 35, 37, 29]


def is_whole_number(text):
    """Return True if text is a whole number such as 33 or -5."""
    if len(text) == 0:
        return False
    start = 0
    if text[0] == "-":  # a minus sign is allowed only at the front
        start = 1
    if start == len(text):  # the text is only "-"
        return False
    for index in range(start, len(text)):
        if text[index] not in "0123456789":
            return False
    return True


def validate_reading(text, lowest, highest):
    """Return an error message for invalid text, or "" if the reading is valid."""
    if len(text) == 0:
        return "Invalid input. The reading cannot be empty."
    if not is_whole_number(text):
        return "Invalid input. Enter a whole number only."
    if int(text) < lowest or int(text) > highest:
        return f"Invalid reading. Enter a value from {lowest} to {highest}."
    return ""


def add_reading(readings, lowest, highest):
    """Ask for one reading and add it to the list only if it is valid."""
    text = input("Enter new reading: ")
    message = validate_reading(text, lowest, highest)
    print()
    if message == "":
        readings.append(int(text))
        print("Reading added successfully.")
    else:
        print(message)


def classify_reading(reading, warning_limit, critical_limit):
    """Return NORMAL, WARNING, or CRITICAL for one reading."""
    if reading < warning_limit:
        return "NORMAL"
    elif reading <= critical_limit:  # boundary: 35 is still WARNING, not CRITICAL
        return "WARNING"
    else:
        return "CRITICAL"


def compute_total(readings):
    """Return the total of all readings (computed with a loop)."""
    total = 0
    for reading in readings:
        total = total + reading
    return total


def compute_average(readings):
    """Return the average of all readings."""
    return compute_total(readings) / len(readings)


def find_minimum(readings):
    """Return the smallest reading (starts from the first reading, not 0)."""
    minimum = readings[0]
    for reading in readings:
        if reading < minimum:
            minimum = reading
    return minimum


def find_maximum(readings):
    """Return the largest reading (starts from the first reading, not 0)."""
    maximum = readings[0]
    for reading in readings:
        if reading > maximum:
            maximum = reading
    return maximum


def count_category(readings, warning_limit, critical_limit, category):
    """Return how many readings belong to the given category."""
    count = 0
    for reading in readings:
        if classify_reading(reading, warning_limit, critical_limit) == category:
            count = count + 1
    return count


def compute_percentage(count, total_count):
    """Return count as a percentage of total_count."""
    return count / total_count * 100


def determine_overall_status(warning_count, critical_count):
    """Return the overall status: CRITICAL is checked first, then WARNING."""
    if critical_count >= 1:
        return "ATTENTION REQUIRED"
    elif warning_count >= 1:
        return "MONITOR"
    else:
        return "NORMAL"


def display_menu():
    """Print the main menu."""
    print("SIMULATED DEVICE MONITORING SYSTEM")
    print("----------------------------------")
    print("[1] View Readings")
    print("[2] Add Reading")
    print("[3] Classify Readings")
    print("[4] Generate Summary")
    print("[5] Exit")
    print()


def display_readings(readings):
    """Print every reading with its position number."""
    print("CURRENT READINGS")
    print("----------------")
    position = 1
    for reading in readings:
        print(f"Reading {position}: {reading} °C")
        position = position + 1


def display_classification(readings, warning_limit, critical_limit):
    """Print every reading with its classification."""
    print("READING CLASSIFICATION")
    print("----------------------")
    for reading in readings:
        print(f"{reading} °C -> {classify_reading(reading, warning_limit, critical_limit)}")


def display_summary(readings, warning_limit, critical_limit):
    """Print the numerical summary and the overall monitoring status."""
    number = len(readings)
    normal = count_category(readings, warning_limit, critical_limit, "NORMAL")
    warning = count_category(readings, warning_limit, critical_limit, "WARNING")
    critical = count_category(readings, warning_limit, critical_limit, "CRITICAL")

    print("MONITORING SUMMARY")
    print("------------------")
    print(f"Number of readings  : {number}")
    print(f"Total of readings   : {compute_total(readings)}")
    print(f"Average temperature : {compute_average(readings):.2f} °C")
    print(f"Minimum temperature : {find_minimum(readings)} °C")
    print(f"Maximum temperature : {find_maximum(readings)} °C")
    print()
    print(f"NORMAL   : {normal} ({compute_percentage(normal, number):.2f}%)")
    print(f"WARNING  : {warning} ({compute_percentage(warning, number):.2f}%)")
    print(f"CRITICAL : {critical} ({compute_percentage(critical, number):.2f}%)")
    print()
    print(f"Overall Status: {determine_overall_status(warning, critical)}")


def main():
    """Control the program: show the menu until the user chooses Exit."""
    readings = get_initial_readings()
    warning_limit = 30   # 30 and above is WARNING
    critical_limit = 35  # above 35 is CRITICAL
    lowest = 0
    highest = 100

    running = True
    while running:
        display_menu()
        choice = input("Enter choice: ")
        print()

        if choice == "1":
            display_readings(readings)
        elif choice == "2":
            add_reading(readings, lowest, highest)
        elif choice == "3":
            display_classification(readings, warning_limit, critical_limit)
        elif choice == "4":
            display_summary(readings, warning_limit, critical_limit)
        elif choice == "5":
            print("Thank you for using the Device Monitoring System.")
            running = False
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")
        print()


main()
