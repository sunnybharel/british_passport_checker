import time
from selenium import webdriver

driver = webdriver.Firefox()
driver.implicitly_wait(30)
driver.maximize_window()

base_url = "https://www.passport.service.gov.uk/track"

#Change details below before running
ref_num = "PEX 111 222 3333"
email = "yourname@mymail.com"
day = "22"
month = "12"
year = "1888"
#Change details above before running

driver.get(base_url)

search_field = driver.find_element_by_id("reference")
search_field.clear()

search_field.send_keys(ref_num)
search_field.submit()

search_email = driver.find_element_by_id("applicant-email")
search_email.clear()
search_email.send_keys(email)
search_email.submit()

search_date_of_birth_day  = driver.find_element_by_id("date-of-birth-day")
search_date_of_birth_day.clear()
search_date_of_birth_day.send_keys(day)

search_date_of_birth_month = driver.find_element_by_id("date-of-birth-month")
search_date_of_birth_month.clear()
search_date_of_birth_month.send_keys(month)

search_date_of_birth_year = driver.find_element_by_id("date-of-birth-year")
search_date_of_birth_year.clear()
search_date_of_birth_year.send_keys(year)
search_date_of_birth_year.submit()

status = driver.find_element_by_xpath("/html/body/div[2]/main/div/div[3]/table/tbody/tr[1]/td[1]")
timestamp = driver.find_element_by_xpath("/html/body/div[2]/main/div/div[3]/table/tbody/tr[1]/td[2]")
print (timestamp.text + "\t" + status.text)

driver.close()

