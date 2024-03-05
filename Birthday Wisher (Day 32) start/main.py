import smtplib
from  datetime import datetime
import pandas
import random

my_email: str="m91278265@gmail.com"
password="ztxilavzyzshzbnr"

today=datetime.now()
today_tuple = (today.month,today.day)

data=pandas.read_csv("birthday.csv")
birthdays_dict={
    (birthday_month,birthday_day):data_row
}
birthdays_dict={(data_row["month"],data_row["day"]): data_row for (index,data_row) in data.iterrows()}

if today_tuple in birthdays_dict:
    birthdays_person=birthdays_dict[today_tuple]
    file_path=f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents=letter_file.read()
        contents=contents.replace("[name]",birthdays_person["name"])

    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs="mrityu2104@yahoo.in", msg=contents)
    connection.close()


