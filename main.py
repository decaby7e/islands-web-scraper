#!/usr/bin/python3

"""
This script was made by Jack Polk (decaby7e) in response to the
tedious nature of Project 1 for the STA 3032 Engineering Statistics
class offered at UF during Summer A of 2020. It scrapes the site 
https://islands.smp.uq.edu.au/ and returns a usable JSON & CSV file.

"""

import json
import sys
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException

from settings import *


#
# Selenium initalization
#


print('INFO  Initalizing Selenium...')

driver = webdriver.Firefox()
driver.get("https://islands.smp.uq.edu.au")

# Login
driver.find_element_by_xpath("/html/body/div[3]/form/div/div[1]/input").send_keys(USERNAME)
driver.find_element_by_xpath("/html/body/div[3]/form/div/div[2]/input").send_keys(PASSWORD)
driver.find_element_by_xpath("/html/body/div[3]/form/div/div[3]/input").click()

# Go to island
driver.get(f"https://islands.smp.uq.edu.au/village.php?{VILLAGE}")


#
# Get all the residents
#


print('INFO  Fetching residents...')

# DEBUG: Get all the residents from a JSON
resident_list = json.load(open('backup.json'))

# resident_list = []

# for i in HOUSE_LIST:

#     driver.execute_script(f"getHouse({i - 1})")
#     time.sleep(1.4)
#     resident_table = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/table[1]")
#     resident_rows = resident_table.find_elements_by_tag_name("tr")

#     for row in resident_rows:
#         name = row.find_element_by_class_name("resident").text
#         gender = row.find_element_by_class_name("gender").text
#         age = row.find_element_by_class_name("age").text
#         resident_link = row.find_element_by_tag_name("a")
#         resident_id = resident_link.get_attribute("href")[-10:]

#         if gender == "♀":
#             gender = "female"
#         elif gender == "♂":
#             gender = "male"

#         if gender == GENDER and (int(age) >= 20 and int(age) <= 79):
#             if VERBOSE:
#                 print(f'DEBUG    Adding {name} ({gender}, {age}) from {i}')
#             resident_list.append(
#                 {
#                     "name": name,
#                     "gender": gender,
#                     "age": age,
#                     "id": resident_id,
#                     "home_num": i,
#                     "tests": {},
#                 }
#             )


#
# Ask for consent from residents
#


print('INFO  Obtaining consent from residents...')

print('DEBUG  Not implemented!')


#
# Run tests (Javascript) on all residents
#


# print('INFO  Running tests on residents...')

# test_list = [
#     "bloodpressure",
#     "temperature",
#     "peakflow",
#     "vocalfreq",
#     "memorycards",
#     "questionnaire"
# ]

# for test in test_list:
#     for resident in resident_list:
#         if VERBOSE:
#             print(f'DEBUG    Testing {resident["name"]} w/ {test}')
#         # Go to the resident page
#         driver.get(f"https://islands.smp.uq.edu.au/islander.php?id={resident['id']}")

#         driver.execute_script(f'startTask("{test}")')

#     time.sleep(110)


#
# Collect test results
#


# print('INFO  Extracting test results from website...')

# for resident in resident_list:

#     print(f' == {resident["name"]} ==')

#     # task_pane = driver.find_element_by_xpath('//*[@id="t2"]')
#     driver.get(f"https://islands.smp.uq.edu.au/islander.php?id={resident['id']}")
#     driver.execute_script("change_tab('t2')")
#     tests = driver.find_elements_by_class_name("taskresult")

#     print(f'DEBUG  {len(tests)} tests')

#     test_collection = {
#         "bp": '',
#         "temp": '',
#         "flow": '',
#         "vocal": '',
#         "memory": '',
#         "university": '',
#         "run": '',
#         "bike": '',
#         "swim": '',
#         "smoke": '',
#         "drink": '',
#         "chocolate": '',
#         "pizza": '',
#         "sleep": '',
#         "attractive": '',
#         "superpower": '',
#     }

#     for test in tests:

#         try:
#             test_type = test.find_element_by_class_name("taskresulttask").text
#         except NoSuchElementException:
#             if VERBOSE:
#                 print('DEBUG  Skipping extra taskresult...')
#             continue

#         try:
#             print(f'INFO  Processing {test_type} ({test.find_element_by_class_name("taskresultresult").text})')
#         except Exception:
#             pass

#         if test_type == "Blood Pressure":
#             test_collection["bp"] = test.find_element_by_class_name("taskresultresult").text
#         elif test_type == "Body Temperature":
#             test_collection["temp"] = test.find_element_by_class_name("taskresultresult").text
#         elif test_type == "Peak Flow Meter":
#             test_collection["flow"] = test.find_element_by_class_name("taskresultresult").text
#         elif test_type == "Vocal Frequency":
#             test_collection["vocal"] = test.find_element_by_class_name("taskresultresult").text
#         elif test_type == "Memory Test Cards":
#             test_collection["memory"] = test.find_element_by_class_name("taskresultresult").text
#         elif test_type == "":
#             try:
#                 survey_results = test.find_elements_by_class_name("taskresultresponse")

#                 test_collection["university"] = survey_results[0].text
#                 test_collection["run"] = survey_results[1].text
#                 test_collection["bike"] = survey_results[2].text
#                 test_collection["swim"] = survey_results[3].text
#                 test_collection["smoke"] = survey_results[4].text
#                 test_collection["drink"] = survey_results[5].text
#                 test_collection["chocolate"] = survey_results[6].text
#                 test_collection["pizza"] = survey_results[7].text
#                 test_collection["sleep"] = survey_results[8].text
#                 test_collection["attractive"] = survey_results[9].text
#                 test_collection["superpower"] = survey_results[10].text
#             except Exception:
#                 if VERBOSE:
#                     print('DEBUG  Skipping blank test section...')
#         else:
#             print("WARN  Found a test we didn't perform...")

#     resident["tests"] = test_collection

# Export information to CSV / JSON

print('INFO  Exporting to JSON...')
with open('export.json', 'w') as export:
    json.dump(resident_list, export)

print('INFO  Exporting to CSV...')
with open('export.csv', 'w') as export:
    for resident in resident_list:
        line = (f"{resident['home_num']}|"
            f"{resident['name']}|"
            f"{resident['gender']}|"
            f"{resident['age']}|"
            f"{resident['tests']['bp']}|"
            f"{resident['tests']['temp']}|"
            f"{resident['tests']['flow']}|"
            f"{resident['tests']['vocal']}|"
            f"{resident['tests']['memory']}|"
            f"{resident['tests']['university']}|"
            f"{resident['tests']['run']}|"
            f"{resident['tests']['bike']}|"
            f"{resident['tests']['swim']}|"
            f"{resident['tests']['smoke']}|"
            f"{resident['tests']['drink']}|"
            f"{resident['tests']['chocolate']}|"
            f"{resident['tests']['pizza']}|"
            f"{resident['tests']['sleep']}|"
            f"{resident['tests']['attractive']}|"
            f"{resident['tests']['superpower']}|")
        export.write(line + '\n')


driver.close()
