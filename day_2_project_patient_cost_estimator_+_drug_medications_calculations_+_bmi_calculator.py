# -*- coding: utf-8 -*-
"""Day 2 Project: Patient Cost Estimator + Drug/Medications Calculations + BMI Calculator

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1J4DqKDejwPyou7uD4Yvf7o6iPKv4t13C

Patient cost estimator
Example - 35F presents to SDEC following a recent diagnosis of Iron Deficiency Anaemia. Please use the Patient cost estimator below to calculate the total cost of their hospital visit:
"""

print("Welcome to the Patient Cost Estimator")
Insurance_cover = float(input("Insurance cover: £ "))
Out_of_pocket = float(input("Out of pocket: £ "))
Optional_donations = float(input("Optional Donations: 5 10 20 "))
Medication_cost = float(input("Medication cost: £ "))
Total_cost = Insurance_cover + Out_of_pocket + Optional_donations + Medication_cost
Optional_donations = Total_cost * Optional_donations / 100, 2
print(f"The total cost is: £ {Total_cost}")

"""Drug/Medication Calculations 101"""

print("Welcome to Drug/Medication Calculations 101")
Required_dose = float(input("What is the required dose (mcg/mg/ml)? "))
Dose_that_I_have = float(input("What is the dose that I have (mcg/mg/ml)? "))
volume_it_is_in = float(input("What is the volume it is in? (mcg/mg/ml)"))
Final_dose = Required_dose / Dose_that_I_have * volume_it_is_in
print(f"The calculated dose is (mcg/mg/ml): {Final_dose}")

"""BMI Calculator"""

height = 1.65
weight = 84
bmi = weight / height ** 2
print(bmi)
print(round(bmi, 2))

"""Example - Welcome to the Tip Calculator"""

print("Welcome to the Tip Calculator")
bill = float(input("What was the total bill? £ "))
tip = int(input("How much tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
bill_with_tip = round(bill * (1 + tip / 100) / people, 2)
print(bill_with_tip)
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
print(f"Each person should pay: £{final_amount}")