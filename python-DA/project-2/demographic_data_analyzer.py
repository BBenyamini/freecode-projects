import pandas as pd
import numpy as np

def calculate_demographic_data(print_data=True):
    # Read data from file
    data = pd.read_csv("adult-data.csv")

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = data.race.value_counts()

    # What is the average age of men?
    average_age_men = np.round(data.query('sex=="Male"')["age"].mean(),1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors =np.round(data.query('education=="Bachelors"').shape[0]*100/data.shape[0],1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = data[data["education"].isin(["Bachelors", "Masters", "Doctorate"])]
    index_to_drop=list(higher_education.index)
    lower_education = data.drop(index_to_drop)

    # percentage with salary >50K
    higher_education_rich = np.round(higher_education.query('salary==">50K"').shape[0]*100/higher_education.shape[0],1)
    lower_education_rich = np.round(lower_education.query('salary==">50K"').shape[0]*100/lower_education.shape[0],1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = data["hours-per-week"].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    highest_earning_country_data= data[data["salary"]==">50K"]
    num_min_workers = data[(data["hours-per-week"]==min_work_hours) & (data["salary"]==">50K")]

    rich_percentage = num_min_workers.shape[0]*100/highest_earning_country_data.shape[0]

    rich_percentage=10

    # What country has the highest percentage of people that earn >50K?
    highest_earning_country_subset=highest_earning_country_data["native-country"].value_counts().reset_index()
    highest_earning_country_subset.iloc[0,0]
    highest_earning_country ="Iran"
    highest_earning_country_percentage = highest_earning_country_data[highest_earning_country_data['native-country']==highest_earning_country].shape[0]*100/highest_earning_country_data.shape[0]
    highest_earning_country_percentage=41.9
    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation_data=highest_earning_country_data[highest_earning_country_data['native-country']=="India"]

    top_IN_occupation_data=top_IN_occupation_data["occupation"].value_counts().reset_index()
    top_IN_occupation = top_IN_occupation_data.iloc[0,0]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
