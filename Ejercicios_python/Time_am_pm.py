def add_time(time_right_now, add_time, Weekend):
    # Minuts Hour day and week
    time_now = time_right_now.strip()
    plus_time = add_time.strip()
    next_day = False
    day = 0
    change_minut_to_hour = 0
    latin_time = ""
    Actual_time = ""
    loop_count = 0
    day_text = ""

    fixed_number_of_time = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    fixed_weekend = [
        'monday', 'tuesday', 'wednesday', 'thursday', 'firday', 'saturday',
        'sunday'
    ]
    latin_time = time_now[time_now.find(" ") + 1:len(time_now)]

    if latin_time == "am":
        next_day = True
    elif latin_time == "pm":
        next_day = False

    # GET AND ADD HOUR
    hour_now = int(time_now[0:time_now.find(":")])

    add_hour_now = int(plus_time[0:plus_time.find(":")])

    # GET AND ADD MINUT
    minut_now = int(time_now[time_now.find(":") +
                             1:len(time_now) - 2])
    add_minut = int(plus_time[plus_time.find(":") + 1:len(plus_time)])

    # START WITH THE POSITION WE INDICATE RECIEVE THE POSTION
    if hour_now == 0:

        index_hour = fixed_number_of_time.index(12)

    elif hour_now in fixed_number_of_time:
        index_hour = fixed_number_of_time.index(hour_now)

    index_weekend = fixed_weekend.index(Weekend.lower())

    total_minuts = minut_now + add_minut

    while True:
        if total_minuts >= 60:
            change_minut_to_hour = change_minut_to_hour + 1
            if total_minuts > 60:
                total_minuts = total_minuts - 60
            else:
                total_minuts = 60 - total_minuts
                break
        else:
            break

    total_hour = add_hour_now + change_minut_to_hour

    while True:

        if loop_count <= total_hour:

            time = fixed_number_of_time[index_hour]
            weekend = fixed_weekend[index_weekend]

            if time == 12 and next_day == False:

                index_hour = 0
                latin_time = "pm"
                time = 12
                next_day = True
                total_minuts = total_minuts
                loop_count = loop_count + 1

            elif time == 12 and next_day == True:
                index_hour = 0
                latin_time = "am"
                next_day = False
                time = 0

                if loop_count == 0:
                    day = 0
                else:
                    day = day + 1
                    if day == 1:
                        day_text = "(next day)"
                    else:
                        day_text = str(day) + " " + "day later"

                    if weekend.lower() == "sunday":
                        weekend = fixed_weekend[index_weekend]
                        index_weekend = 0
                    else:

                        index_weekend = index_weekend + 1
                        weekend = fixed_weekend[index_weekend]

                loop_count = loop_count + 1
            else:
                time = fixed_number_of_time[index_hour]
                index_hour = index_hour + 1
                loop_count = loop_count + 1



        else:
            break

    Actual_time = "{00:002d}".format(time) + ":" + "{:002d}".format(
        total_minuts) + " " + day_text + " " + latin_time + " " + weekend.capitalize()
    return Actual_time.strip()


print(add_time("08:00 pm", "205:00", "FIRDAY"))
