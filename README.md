Start: 7:10

I started by reading the description and instructions included with the coding assignment.

After that, I went into full planning mode. I wanted to list out everything that I wanted to do with the data, and how I planned to accomplish it. Breaking things down can help get ideas flowing, and will make the task simpler. As the saying goes, "If you want to eat an airplane, you have to do it one bite at a time". The plan is included below:

* I want to read in all the data from the CSV. I would prefer to do this with a console command to which the user feeds a file name.
  * In order to receive the file name, I will use the input function.
  * In order to read the CSV file, I will use the open function.
  * I will use the comma as a regex to split the values in the CSV, and put each set of values in its own array.
  * I will also make sure to close the file after I am done using it.

* I want to then print out a list of days with the amount of miles completed in the specified day.
  * In order to get the days, I will use the aforementioned array of days from reading in the file.
  * In order to get the amount of miles, I will go through each of the days, and find the corresponding amount of miles associated with each.
  * In order to print it out, I will use the print function.

* **EXTRA:** I want to display the data in a nicer way.
  * I want to display a pie graph with each day having a slice.
    * I can do this with pandas.
  * I want to display a bar chart with each day being a bar.
    * I can do this with pandas.

* **EXTRA:** I want to export the data as a spreadsheet with the days, and their corresponding number of miles.
  * I believe I can do this with pandas.