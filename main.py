import pandas
import datetime as dt
import random
import smtplib
import os

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")


def send_birthday_email(persons_birthdays):
    letter_number = random.randint(1, 3)
    with open(f"./letter_templates/letter_{letter_number}.txt") as letter_file:
        message = letter_file.read()

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        for person in persons_birthdays:
            person_name = person["name"]
            person_email = person["email"]
            message = message.replace("[NAME]", person_name)
            connection.sendmail(
                from_addr=EMAIL,
                to_addrs=person_email,
                msg=f"Subject:Happy Birthday\n\n{message}"
            )
            message = message.replace(person_name, "[NAME]")


data = pandas.read_csv("birthdays.csv")


# current day day and month
now = dt.datetime.now()
now_month = now.month
now_day = now.day

birthdays = []

for i, row in data.iterrows():
    if now_month == row["month"] and now_day == row["day"]:  # if someone's birthday matches today
        name = row["name"]
        email = row["email"]
        new_dict = {"name": name, "email": email}
        birthdays.append(new_dict)

send_birthday_email(birthdays)









