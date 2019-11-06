import time
from selenium import webdriver
#from selenium.webdriver.firefox.options import Options as FirefoxOptions

# options = FirefoxOptions()
# options.add_argument("--headless")
# driver = webdriver.Firefox(options=options)
driver = webdriver.Firefox()
driver.implicitly_wait(30)
driver.maximize_window()

base_url = "https://www.passport.service.gov.uk/track"
ref_num = "PEX 344 369 7300"
email = "sunnybharel@gmail.com"
day = "26"
month = "08"
year = "1981"

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

#/html/body/div[2]/main/div/div[3]/table/tbody/tr[1]/td[1] #-xpath
#.govuk-table__body > tr:nth-child(1) > td:nth-child(1) #css-selector


#if  not (driver.PageSource().Contains("We've received your")):
#  print(driver.find_element_by_id("header"))

time.sleep(15)
driver.close()

