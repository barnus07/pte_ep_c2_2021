try:
    raw_input_data = input("Please give me a duration in seconds: ")
    sum_of_seconds = int(raw_input_data)
    if sum_of_seconds < 0:
        print("Invalid input")
    elif sum_of_seconds == 0:
        print("now")
    else:
        seconds_in_minute = 60
        seconds_in_hour = 60 * seconds_in_minute  # 3600
        seconds_in_day = 24 * seconds_in_hour  # 86 400
        seconds_in_year = 365 * seconds_in_day  # 31 536 000

        years = sum_of_seconds // seconds_in_year
        sum_of_seconds = sum_of_seconds - years * seconds_in_year

        days = sum_of_seconds // seconds_in_day
        sum_of_seconds = sum_of_seconds - days * seconds_in_day

        hours = sum_of_seconds // seconds_in_hour
        sum_of_seconds = sum_of_seconds - hours * seconds_in_hour

        minutes = sum_of_seconds // seconds_in_minute
        seconds = sum_of_seconds - minutes * seconds_in_minute

        number_of_units = 0
        if years > 0:
            number_of_units += 1
        if days > 0:
            number_of_units += 1
        if hours > 0:
            number_of_units += 1
        if minutes > 0:
            number_of_units += 1
        if seconds > 0:
            number_of_units += 1

        output = ""
        if years > 0:
            output += str(years) + " year"
            if years > 1:
                output += "s"
            if number_of_units > 2:
                output += ", "
            elif number_of_units == 2:
                output += " and "
            number_of_units -= 1
        if days > 0:
            output += str(days) + " day"
            if days > 1:
                output += "s"
            if number_of_units > 2:
                output += ", "
            elif number_of_units == 2:
                output += " and "
            number_of_units -= 1
        if hours > 0:
            output += str(hours) + " hour"
            if hours > 1:
                output += "s"
            if number_of_units > 2:
                output += ", "
            elif number_of_units == 2:
                output += " and "
            number_of_units -= 1
        if minutes > 0:
            output += str(minutes) + " minute"
            if minutes > 1:
                output += "s"
            if number_of_units > 2:
                output += ", "
            elif number_of_units == 2:
                output += " and "
            number_of_units -= 1
        if seconds > 0:
            output += str(seconds) + " second"
            if seconds > 1:
                output += "s"
            if number_of_units > 2:
                output += ", "
            elif number_of_units == 2:
                output += " and "
            number_of_units -= 1

        print(output)
except ValueError:
    print("Invalid input")
