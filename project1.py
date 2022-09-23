#!/usr/bin/env python3
# below is main function
def main():

    birth_month_raw = input("Please enter the month you were born (eg. january, february etc): ")
    while (birth_month_raw == "") or (birth_month_raw.isdigit()):
        birth_month_raw = input("Please enter a valid month: ")

    birth_month = birth_month_raw.lower().strip()[:3]
    print(birth_month)

    birth_day_raw = input("Please enter the day of the month you were born (eg. 20, 15 etc): ")
    while (birth_day_raw == '') or (birth_day_raw.isdigit() == False):
        birth_day_raw = input("Please enter a valid day: ")

    if birth_day_raw.isdigit():
        birth_day = int(birth_day_raw)

    if (birth_month == "mar" and birth_day >= 21) or (birth_month == "apr" and birth_day <= 19):
        print("Your zodiac sign is Aries")

    elif (birth_month == "apr" and birth_day >= 20) or (birth_month == "may" and birth_day <= 20):
        print("Your zodiac sign is Taurus")

    elif (birth_month == "may" and birth_day >= 21) or (birth_month == "jun" and birth_day <= 21):
        print("Your zodiac sign is Gemini")

    elif (birth_month == "jun" and birth_day >= 22) or (birth_month == "jul" and birth_day <= 22):
        print("Your zodiac sign is Cancer")

    elif (birth_month == "jul" and birth_day >= 23) or (birth_month == "aug" and birth_day <= 22):
        print("Your zodiac sign is Leo")

    elif (birth_month == "aug" and birth_day >= 23) or (birth_month == "sep" and birth_day <= 22):
        print("Your zodiac sign is Virgo")

    elif (birth_month == "sep" and birth_day >= 23) or (birth_month == "oct" and birth_day <= 23):
        print("Your zodiac sign is Libra")

    elif (birth_month == "oct" and birth_day >= 24) or (birth_month == "nov" and birth_day <= 21):
        print("Your zodiac sign is Scorpio")

    elif (birth_month == "nov" and birth_day >= 22) or (birth_month == "dec" and birth_day <= 21):
        print("Your zodiac sign is Sagittarius")

    elif (birth_month == "dec" and birth_day >= 22) or (birth_month == "jan" and birth_day <= 19):
        print("Your zodiac sign is Capricorn")

    elif (birth_month == "jan" and birth_day >= 20) or (birth_month == "feb" and birth_day <= 18):
        print("Your zodiac sign is Aquarius")

    elif (birth_month == "feb" and birth_day >= 19) or (birth_month == "mar" and birth_day <= 20):
        print("Your zodiac sign is Pisces")

    else:
        print("You have entered wrong information")

main()