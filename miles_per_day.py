# Richard Mulholland
# Coding Assignment for Utah LTAP
# July 13th, 2022

object_id_column_number = 0
date_updated_column_number = 84
length_yds_column_number = 115
miles_day_dictionary = {}


def fix_date(date):
    new_date = date.split('/')

    date_day = new_date[0]
    date_month = new_date[1]
    date_year = new_date[2]

    return f"{date_year}/{date_month}/{date_day}"


def read_file(file_name):
    file_dictionary = {}

    file = open(file_name)
    # I am wasting the first line in effect so that I can ensure that all the values are the type I expect
    file.readline()

    for line in file:
        line.strip('\n')
        line_array = line.split(',')

        if len(line_array) <= 1:
            continue
        else:
            day = fix_date(line_array[date_updated_column_number].split(' ')[0])

            yards = float(line_array[length_yds_column_number])

            if day in file_dictionary:
                file_dictionary[day] += yards
            else:
                file_dictionary[day] = yards

    return file_dictionary


file_name = input("What is the name of the file you would like to use? \n")

miles_day_dictionary = read_file(file_name)

for date in sorted(miles_day_dictionary):
    print(f"\nThere were {miles_day_dictionary[date]/1760} miles of road completed on {date}")
