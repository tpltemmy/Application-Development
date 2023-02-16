import streamlit as st 
from datetime import datetime, date

print("Due date calculator")
 
print("Please enter the date of conception")
conception_day = int(input("Day (DD): "))
conception_month = int(input("Month (MM): "))
conception_year = int(input("Year (YYYY): "))

#Calculating the date based on the inputs!!

start_date = datetime.datetime(conception_year, conception_month, conception_day)

pregnancy_length = 270
predicted_date = start_date + datetime.timedelta(days=pregnancy_length)
print(f"""
Your due date is approximately: {predicted_date}
 
Congratulations on your pregnancy!""")