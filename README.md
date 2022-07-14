###BASIC ASSIGNMENT:

Start: 7:10 PM

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


After I was done with planning, I committed my project and pushed it to GitHub. I then got to work on the code itself. I also imported the CSV, as that might be helpful. 

I had a hard time reading the CSV in PyCharm (my Python editor of choice), and so I uploaded it to Google Sheets. I did this in order to get a better idea of what the document was telling me, and where to get the information I am looking for. I saw that there were multiple dates, and took _Date Updated_ to be the column with when the project was complete. I saw that at the end of the CSV, there is a _LengthYds_ column, and used that for the length of road built. I looked up the conversion between yards and miles, as that will be helpful later in my project. For anyone curious, it is 1,760 yards to a mile.

I was parsing through the data well, but was getting stuck due to the extra empty line at the bottom of the CSV. In order to deal with this, I checked to see if a line was only whitespace. I looked up how to do this on the internet, but none of them seemed to work, so I figured out my own workaround. I also found out that there is a part in the CSV (line 83) that has a line split in two for some reason. I fixed that.

I was thinking, and I figured that a dictionary would probably work better for storing the day and miles completed pair. I looked up a quick refresher on those to jog my memory.

I got the basic assignment done, but wanted to sort it to make it look much nicer. I used the sorted function to do that, but had to look that up as well.

End: 9:24 PM

Time Taken: 2 hours and 14 min


<br>

###EXTRA:

Start: 9:54 PM

I would like to start off this section by stating that I have not done too much with pandas, so this may be a lot of documentation saying that I looked things up.

I started to use pandas, but found that it was not fitting my needs, and that matplotlib would likely work better for that. I decided to opt for matplotlib to display the graphs. I looked up how to display the graphs, as well as how to add titles and axes labels. I also looked up how to add a legend.

I found out pretty quickly that there are too many days, and so I displayed the charts by year instead.

I was able to complete the first part of the extra by 10:54 PM, so it took me about an hour. Most of this was due to me learning new material.

End First Part: 10:54 PM


<br>

###END

That is unfortunately all that I have time for. This has been a really fun and informative assignment. It has showed me a few points that I could improve on such as code styling, but has also shown me how much I know, and how much I can accomplish on my own. It was really fun to learn pandas, and then switch to learning matplotlib. I love both!


