![image](https://github.com/JLaydeJ/Project_1/assets/134284646/89f1495e-c91b-4c7b-9467-d260c0593ab7)
# Washington Powerball/Powerplay Lottery
Team Members: Erika Evergarden '2020', Jamee Jones '2021', Evan Woodard '2022'

# Project Description
“How can you best play the lottery?”

That question has two components:
1. What numbers can you pick to help your odds?
2. When can you play to win the most money?

To answer these questions, we looked for the most often drawn numbers and the highest dollar winnings, both filtered by day and by month. The goal of this project is to determine the frequency of the powerball/powerplay to increase our odds of maximizing our payout. 
 
# Data Source
The data source is from Kaggle https://www.kaggle.com/datasets/stetsondone/lottery-data-winning-numbers-and-jackpots as an aggregate .csv. This CSV file covers past lottery data in Washington State from June 2014 - November 2022. The original source was pulled from Lottery Corner - https://www.lotterycorner.com/wa/powerball/2022. 
This file includes the following data: 

date - date of winnings

weekday - day of week winnings were announced

winning numbers - string of winning numbers for jackpot

powerball - Winning powerball number; If your Powerball matches the one that is drawn you will get your $2 ticket purchase back and a couple of bucks more, for a total of $4.

powerplay - Winning powerplay number - for an additional $1 per play, the powerplay feature multiplies non-jackpot prizes. The multiplier number is randomly selected just before each drawing.

jackpot - total jackpot amount in USD

# Prepare the Data
We reduced our original CSV file from the years 2014 - 2022 to 2020 - 2022. We then sliced the CSV file into 3 separate CSV files for the years 2020, 2021, and 2022. Using Pandas, we were able to import the data, and then merge the combined year DataFrames into a single DataFrame. After merging the Dataframes, we will then use the data to solve our exploratory questions. 

# Exploratory Question 2020 - 20222
1. What were the most common powerball/powerplay numbers depending on the day?
![Screenshot 2023-08-01 222902](https://github.com/JLaydeJ/Project_1/assets/134284646/ab888862-c655-4da0-ab30-47db18dfde12)

The most often drawn Powerball number by day could be used as a data point to base your numbers on, but the data didn’t show enough significance to count on it. We grouped the data by date for each year, then combined each of the modes to calculate them for the three year span.

   
3. What were the most common powerball/powerplay numbers depending on the month?
![Screenshot 2023-08-01 222853](https://github.com/JLaydeJ/Project_1/assets/134284646/04028f18-ff8f-4135-8da9-1ec81b83d2ab)

According to our data between the years 2020 to 2022.  The powerball number that is randomly picked the most frequently every month is 18.  The powerplay number that is most often randomly picked every month is 2.  This data is acquired by taking a mode function of aggregate data.  This aggregate data is first grouped by weekdays, then these weekdays are grouped by their respective months.  By doing this, we are effectively performing a mode function over all selected weekdays per month.


3. What were the most common powerball/powerplay numbers overall?
![Screenshot 2023-08-01 222844](https://github.com/JLaydeJ/Project_1/assets/134284646/a4e85951-b7dc-42be-8699-b7a626596877)

This one is a little more interesting to us since two years have the same mode. Both 2020 and 2022 had a mode of 18. We did the same thing for this one, but grouped mode by year instead of month or day.


5. What are the top five greatest dollar months jackpot?
![Screenshot 2023-08-01 222834](https://github.com/JLaydeJ/Project_1/assets/134284646/bdcde997-e76d-4d82-b7f8-23ab67918f52)

According to our data between the years 2020 to 2022, 2022 (November, October, January) had the highest jackpot winnings. The findings were acquired by grouping the aggregate data by month and then applying the max function to find the top 5 maximum values. Since 2022 held the top 5 highest jackpot winnings, we decided to display the top 5 jackpot winnings for 2020 and 2021. The highest jackpot winnings were in November 2022 $120,000,000,000, October 2022 $1,000,000,000, $825,000,000, $700,000,000 and January 2022: $630,000,000.  

5. Which day of the week had the highest jackpot?

According to our data between the years 2020 to 2022, Wednesday had the highest jackpot winnings. The findings were acquired by grouping the aggregate data by weekday and then applying the max function to find the maximum values for each draw day. The highest jackpot winnings were drawn on Wednesday 2022 $120,000,000,000.  This is such a large jackpot that comparable to our other jackpot data it can be considered an outlier.

# ubiquitous-goggles
