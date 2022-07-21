# Richard Mulholland
# Coding Assignment for Utah LTAP
# July 13th, 2022

import matplotlib.pyplot as plt

# The first two are the column numbers for their respective fields.
# The last one is the conversion between yards and miles.
date_updated_column_number = 84
length_yds_column_number = 115
yard_to_miles = 1760


def fix_date(date):
    new_date = date.split('/')

    date_day = new_date[0]
    date_month = new_date[1]
    date_year = new_date[2]

    return f"{date_year}/{date_month}/{date_day}"


def read_file(file_name):
    file_dictionary = {}

    file = open(file_name)
    # The first line is always the labels, so I end up just wasting it, so it is pure data I am using
    file.readline()

    for line in file:
        line.strip('\n')
        line_array = line.split(',')

        # This if else handles empty lines should they appear
        if len(line_array) <= 1:
            continue
        else:
            day = fix_date(line_array[date_updated_column_number].split(' ')[0])

            yards = float(line_array[length_yds_column_number])

            if day in file_dictionary:
                file_dictionary[day] += yards
            else:
                file_dictionary[day] = yards

    # Make sure to close the file!
    file.close()

    return file_dictionary


def find_year_data(data):
    years = []
    miles = []

    for date in data.keys():
        year = date.split('/')[0]

        if year in years:
            year_index = years.index(year)
            miles[year_index] + data[date] / yard_to_miles
        else:
            years.append(year)
            miles.append(data[date] / yard_to_miles)

    return years, miles


def plot_pie(data):
    years, miles = find_year_data(data)

    plt.pie(x=miles, labels=miles)
    plt.legend(years, loc='center')
    plt.title("Miles of road constructed per year")
    plt.show()


def plot_bar(data):
    years, miles = find_year_data(data)

    plt.bar(years, miles)
    plt.title("Miles of road constructed per year")
    plt.ylabel("Miles Constructed")
    plt.xlabel("Year")
    plt.show()


def export_csv(data, file_name):
    output = ""

    for day in data.keys():
        output += str(day) + ","
        output += str(data[day]) + "\n"

    file = open(file_name, 'w')
    file.write(output)
    file.close()


file_name = input("What is the name of the file you would like to use? \n")

miles_day_dictionary = read_file(file_name)

for date in sorted(miles_day_dictionary):
    print(f"\nThere were {miles_day_dictionary[date] / yard_to_miles} miles of road completed on {date}")

print("\n\nIt has now made two graphs, a pie chart, and a bar chart. "
      "\nYou will see the bar chart first. If you exit out of the window, you will then see the pie chart.")

plot_bar(miles_day_dictionary)
plot_pie(miles_day_dictionary)

export_name = input("What filename would you like to use for the exported csv? (Please end it with .csv)\n")

export_csv(miles_day_dictionary, export_name)
