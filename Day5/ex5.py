"""Day 5 exercise"""

import datetime as dt
import json
import logging
import mysql.connector
import config as cfg

logging.basicConfig(
    filename="test.log",
    level=logging.INFO,
    format="%(asctime)s:%(levelname)s:%(message)s"
)

H_NAME = cfg.names["host"]
U_NAME = cfg.names["user"]
P_NAME = cfg.names["passwd"]
D_NAME = cfg.names["database"]

my_conn = mysql.connector.connect(host=H_NAME, user=U_NAME, passwd=P_NAME, database=D_NAME)
print(my_conn)
my_cursor = my_conn.cursor()

class UserInfo:
    """User Info class"""
    def validate_age(self, gender, dob):
        """validate age method"""
        today = dt.date.today()
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
        gender = gender.lower()
        if gender == "m" and age < 21:
            return "Invalid"
        elif gender == "f" and age < 18:
            return "Invalid"
        else:
            return "Valid"

    def validate_nationality(self, nationality):
        """validate nationality method"""
        nationality = nationality.lower()
        if nationality == "indian" or nationality == "american":
            return "Valid"
        else:
            return "Invalid"

    def validate_state(self, state):
        """validate state method"""
        state = state.lower()
        state = state.replace(" ","")
        states = ["andhrapradesh","arunachalpradesh",
                  "assam","bihar","chhattisgarh","karnataka",
                  "madhyapradesh","odisha","tamilnadu","telangana", "westbengal"]
        if state in states:
            return "Valid"
        else:
            return "Invalid"

    def validate_salary(self, salary):
        """validate salary method"""
        if salary>=10000 and salary<=90000:
            return "Valid"
        else:
            return "Invalid"

    def validate_pan(self, pan):
        """validate pan method"""
        my_cursor.execute("select Request_received from "
                          "request_info where  PAN_Number='{}'".format(pan))
        pan_date = my_cursor.fetchone()
        if pan_date is not None:
            my_cursor.execute("SELECT DATEDIFF(CURDATE(),Request_received) "
                              "from request_info where  PAN_Number='{}'".format(pan))
            no_of_days = my_cursor.fetchone()
            no_of_days = int(no_of_days[0])
            print(no_of_days)
            if no_of_days < 5:
                return "Invalid"
            else:
                return "Valid"
        else:
            return "Valid"

obj=UserInfo()

FIRST_NAME = input("Enter first name: ")
MIDDLE_NAME = input("Enter middle name: ")
LAST_NAME = input("Enter last name: ")
D_O_B = input("Enter dob YYYY-MM-DD: ")
D_O_B = dt.datetime.strptime(D_O_B, '%Y-%m-%d')
D_O_B = D_O_B.date()
GENDER_NAME = input("Enter gender: ")

FLAG_NAME = 0
if FLAG_NAME == 0:
    RESPONSE_NAME = obj.validate_age(GENDER_NAME, D_O_B)
    print(RESPONSE_NAME)
    if RESPONSE_NAME != 'Valid':
        REASON_NAME = "Invalid age"
        print(REASON_NAME)
        FLAG_NAME = 1

if FLAG_NAME == 0:
    NATIONALITY_NAME = input("Enter Nationality: Indian/American :")
    RESPONSE_NAME = obj.validate_nationality(NATIONALITY_NAME)
    print(RESPONSE_NAME)
    if RESPONSE_NAME != 'Valid':
        REASON_NAME = "Invalid nationality"
        print(REASON_NAME)
        FLAG_NAME = 1
else:
    NATIONALITY_NAME = "Invalid"

if FLAG_NAME == 0:
    CURRENT_CITY = input("Enter current city: ")
    STATE_NAME = input("Enter State: ")
    RESPONSE_NAME = obj.validate_state(STATE_NAME)
    print(RESPONSE_NAME)
    if RESPONSE_NAME != 'Valid':
        REASON_NAME = "Invalid State"
        print(REASON_NAME)
        FLAG_NAME = 1
else:
    CURRENT_CITY = "Invalid"
    STATE_NAME = "Invalid"

if FLAG_NAME == 0:
    PIN_CODE = input("Enter Pin code: ")
    QUALIFICATION_NAME = input("Enter Qualification: ")
    SALARY_OF_PERSON = float(input("Enter Salary: "))
    RESPONSE_NAME = obj.validate_salary(SALARY_OF_PERSON)
    print(RESPONSE_NAME)
    if RESPONSE_NAME != 'Valid':
        REASON_NAME = "Invalid Salary"
        print(REASON_NAME)
        FLAG_NAME = 1
else:
    PIN_CODE="Invalid"
    QUALIFICATION_NAME="Invalid"
    SALARY_OF_PERSON=0

if FLAG_NAME == 0:
    PAN_NUMBER = input("Enter pan number: ")
    RESPONSE_NAME = obj.validate_pan(PAN_NUMBER)
    print(RESPONSE_NAME)
    if RESPONSE_NAME != 'Valid':
        REASON_NAME = "number of days is not less than 5"
        print(REASON_NAME)
        FLAG_NAME = 1
else:
    PAN_NUMBER = "Invalid"

if FLAG_NAME == 0:
    now = dt.datetime.now()
    REASON_NAME = "Eligible"
    print(REASON_NAME)
else:
    now = dt.datetime.now()

my_cursor.execute("INSERT INTO request_info("
                    "First_Name,Middle_Name,Last_Name,DOB,Gender,"
                    "Nationality,Current_City,State,Pin_code,Qualification,"
                    "Salary,PAN_Number,Request_received) "
                    "VALUES ('{}','{}','{}','{}','{}','{}','{}',"
                    "'{}','{}','{}','{}','{}','{}')".format(FIRST_NAME,
                    MIDDLE_NAME, LAST_NAME, D_O_B, GENDER_NAME, NATIONALITY_NAME,
                    CURRENT_CITY, STATE_NAME, PIN_CODE, QUALIFICATION_NAME,
                    SALARY_OF_PERSON, PAN_NUMBER, now))
my_conn.commit()


my_cursor.execute("SELECT max(Request_id) FROM Request_info")
my_curr_id = my_cursor.fetchone()
my_curr_id = int(my_curr_id[0])
dictation = {"Request_id ": my_curr_id, "Response ": RESPONSE_NAME, "Reason ": REASON_NAME}
dictation = json.dumps(dictation)
print(dictation)
logging.info(dictation)


my_cursor.execute("INSERT INTO response_info(Request_id,reponse) "
                  "VALUES ('{}','{}')".format(my_curr_id, dictation))
my_conn.commit()
