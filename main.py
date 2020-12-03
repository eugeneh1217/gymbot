import selenium
from selenium import webdriver
import user_info

driver = webdriver.Chrome()

driver.get('https://warrior.uwaterloo.ca/Program/GetProgramDetails?courseId=cc2a16d7-f148-461e-831d-7d4659726dd1'
           '&semesterId=b0d461c3-71ea-458e-b150-134678037221')

# elements = [
#     (driver.find_element_by_xpath("/html/body/div[@id='mainContent']/div/b/div/"), "click"),
# ]

# for element in elements:
#     if element[1] == "click":
#         element[0].click()

list_group = driver.find_element_by_xpath("//html/body/div[@id='mainContent']/div/b/div")

cards = list_group.find_elements_by_tag_name("div")

for card in cards:
    if card.find_element_by_xpath("//div/div/h4/span").text == "Thursday, December 3, 2020": # user_info.gym_date_final
        if card.find_element_by_xpath("//div/div/h4/small").text == "11:00 AM to 11:45 AM": # user_info.gym_time_final
            card.find_element_by_xpath("//div/div/a").click()
