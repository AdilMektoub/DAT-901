import pandas as pd
import numpy as np

df = pd.read_csv("data/titanic.csv", sep=",")

print(df[:10])

age_null = df["age"].isna().sum()
sum_age = df.shape[0] - age_null

print("age {} non-null {} null".format(sum_age, age_null))

df_survived = df[df["survived"] == 1]
total_s = df_survived.shape[0]
age_s = np.round(df_survived["age"].mean(), 3)
fare_s = np.round(df_survived["fare"].mean(), 3)

print("SURVIVED ----------------")
print("Total: {}".format(total_s))
print("Age: {}".format(age_s))
print("Fare: {}".format(fare_s))

df_dead = df[df["survived"] == 0]
total_d = df_dead.shape[0]
age_d = np.round(df_dead["age"].mean(), 3)
fare_d = np.round(df_dead["fare"].mean(), 3)

print("\nDEAD --------------------")
print("Total: {}".format(total_d))
print("Age: {}".format(age_d))
print("Fare: {}".format(fare_d))

total = df.shape[0]
percentage_s = np.round(total_s / total * 100, 2)

total_m = df[df["sex"] == "male"].shape[0]
total_f = df[df["sex"] == "female"].shape[0]
women_s = df[(df["survived"] == 1) & (df["sex"] == "female")].shape[0]
men_s = df[(df["survived"] == 1) & (df["sex"] == "male")].shape[0]
print("\nSTATISTICS --------------")
print("Survivors: {}%".format(percentage_s))
print("Male surviving chances: {} - {}%".format(
    men_s, np.round(men_s / total_m * 100), 2))
print("Female surviving chances: {} - {}%".format(
    women_s, np.round(women_s / total_f * 100), 2))

total_first = df[df["pclass"] == 1].shape[0]
total_second = df[df["pclass"] == 2].shape[0]
total_third = df[df["pclass"] == 3].shape[0]
first_class = df[(df["survived"] == 1) & (df["pclass"] == 1)].shape[0]
second_class = df[(df["survived"] == 1) & (df["pclass"] == 2)].shape[0]
third_class = df[(df["survived"] == 1) & (df["pclass"] == 3)].shape[0]

print("First Class surviving chances: {}%".format(
    np.round(first_class / total_first * 100, 2)))
print("Second Class surviving chances: {}%".format(
    np.round(second_class / total_second * 100, 2)))
print("Third Class surviving chances: {}%".format(
    np.round(third_class / total_third * 100, 2)))

total_zero = df[df["age"] <= 10].shape[0]
total_ten = df[(df["age"] > 10) & (df["age"] <= 20)].shape[0]
total_twenty = df[(df["age"] > 20) & (df["age"] <= 30)].shape[0]
total_thirty = df[(df["age"] > 30) & (df["age"] <= 40)].shape[0]
total_forty = df[(df["age"] > 40) & (df["age"] <= 50)].shape[0]
total_fifty = df[(df["age"] > 50) & (df["age"] <= 60)].shape[0]
total_sixty = df[(df["age"] > 60) & (df["age"] <= 70)].shape[0]
total_seventy = df[df["age"] > 70].shape[0]

zero_s = df[(df["age"] <= 10) & (df["survived"] == 1)].shape[0]
ten_s = df[(df["age"] > 10) & (df["age"] <= 20) &
           (df["survived"] == 1)].shape[0]
twenty_s = df[(df["age"] > 20) & (df["age"] <= 30) &
              (df["survived"] == 1)].shape[0]
thirty_s = df[(df["age"] > 30) & (df["age"] <= 40) &
              (df["survived"] == 1)].shape[0]
forty_s = df[(df["age"] > 40) & (df["age"] <= 50) &
             (df["survived"] == 1)].shape[0]
fifty_s = df[(df["age"] > 50) & (df["age"] <= 60) &
             (df["survived"] == 1)].shape[0]
sixty_s = df[(df["age"] > 60) & (df["age"] <= 70) &
             (df["survived"] == 1)].shape[0]
seventy_s = df[(df["age"] > 70) & (df["survived"] == 1)].shape[0]

df_age = [[
    np.round(zero_s / total_zero * 100, 2),
    np.round(ten_s / total_ten * 100, 2),
    np.round(twenty_s / total_twenty * 100, 2),
    np.round(thirty_s / total_thirty * 100, 2),
    np.round(forty_s / total_forty * 100, 2),
    np.round(fifty_s / total_fifty * 100, 2),
    np.round(sixty_s / total_sixty * 100, 2),
    np.round(seventy_s / total_seventy * 100, 2),
    #   np.round(eighty_s / total_eighty * 100, 2)
]]

df_age = pd.DataFrame(df_age,
                      columns=[
                          "0-10", "10-20", "20-30", "30-40", "40-50", "50-60",
                          "60-70", "70+"
                      ])

print("Surviving chances based on age range: ")
print(df_age)