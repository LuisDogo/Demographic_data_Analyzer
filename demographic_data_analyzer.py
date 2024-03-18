import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")
    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df.groupby("race")["race"].count()

    # What is the average age of men?
    average_age_men = round(df.loc[df["sex"] == "Male", "age"].mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round(len(df[df["education"] == "Bachelors"])/len(df), 3)*100
    # What percentage of people without advanced education make more than 50K?
    
    # with and without `Bachelors`, `Masters`, or `Doctorate`

    higher_education = df[df["education"].isin(["Bachelors","Masters","Doctorate"])]
    lower_education = df[~df["education"].isin(["Bachelors","Masters","Doctorate"])]

    # percentage with salary >50K
    
    rich = df[df["salary"] == ">50K"]

    high_ed_rich = higher_education.merge(rich, how = "inner")
    low_ed_rich = lower_education.merge(rich, how = "inner")

    higher_education_rich = round(len(high_ed_rich)/len(higher_education), 3) * 100
    lower_education_rich = round(len(low_ed_rich)/len(lower_education), 3) * 100

    # What is the minimum number of hours a person works per week (hours-per-week feature)?

    min_work_hours = df["hours-per-week"].min()
    min_work_hours_df = df[df["hours-per-week"] == min_work_hours]

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    
    min_rich = min_work_hours_df.merge(rich, how = "inner")
    
    num_min_workers = len(min_work_hours_df)
    
    rich_percentage = round(len(min_rich)/num_min_workers, 3) * 100

    # What country has the highest percentage of people that earn >50K?

    people_by_country = df.groupby("native-country").age.count()
    rich_by_country = rich.groupby("native-country").age.count()
    a = pd.DataFrame()["percentage_rich"] = (rich_by_country / people_by_country)*100

    highest_earning_country = a.idxmax()
    highest_earning_country_percentage = round(a.max(),1)

    # Identify the most popular occupation for those who earn >50K in India.
    india = df[df["native-country"] == "India"]
    rich_india = india.merge(rich)
    rich_oc = rich_india.groupby("occupation").count()

    top_IN_occupation = rich_oc.age.idxmax()

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
