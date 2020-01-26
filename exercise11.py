age_ask = input("How old are you in years?")
age_years = int(age_ask)
age_months = age_years * 12
age_secs = ((age_years * 365.25) * 24) * 3600
print(f"{age_years} year(s) are equal to {age_months} months and the same as {age_secs:.0f} seconds.")