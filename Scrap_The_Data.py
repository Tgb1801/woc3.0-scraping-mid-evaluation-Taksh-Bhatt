
from selenium import webdriver
import json

PATH = "C:\Program Files (x86)\chromedriver.exe"

options = webdriver.ChromeOptions()
options.headless = True

main_driver = webdriver.Chrome(PATH, options=options)

driver = webdriver.Chrome(PATH, options=options)

url = input("Enter the url of the Organisations page: ")

main_driver.get(url)

links = main_driver.find_elements_by_tag_name("a")


data = []

tech_stack = []

i = 3

while 1:
    dict1 = {}
    link = links[i].get_attribute("href")
    driver.get(link)
    try:
        dict1['name'] = driver.find_element_by_class_name("banner__title").text
        dict1['url'] = link
        dict1['tech_stacks'] = []
        texts = driver.find_element_by_class_name("org__meta").find_element_by_tag_name("ul").find_elements_by_tag_name("li")

        for j in range(len(texts)):
            tech_stack.append(texts[j].text)
            dict1['tech_stacks'].append(texts[j].text)

        data.append(dict1)
        i += 1
    except Exception:
        break


with open('Main_Data_Storage.json', 'w') as file:
    json.dump(data, file)

tech_stack.sort()

for i in range(1, len(tech_stack)):
    if i < len(tech_stack):
        if tech_stack[i] == tech_stack[i-1]:
            tech_stack.pop(i)
            i -= 1
    else:
        break

with open('All_Tech_Stacks.json', 'w') as file:
    json.dump(tech_stack, file)


with open('All_Tech_Stacks.json', 'r') as file:
    data = json.load(file)

index = []
count = 0
for i in range(1, len(data)):
    if data[i-1] == data[i]:
        index.append(i - count)
        count += 1

for i in range(len(index)):
    data.pop(index[i])

with open('All_Tech_Stacks.json', 'w') as file:
    json.dump(data, file)


with open('All_Tech_Stacks.json', 'r') as file:
    data = json.load(file)

dict1 = {}

for i in range(len(data)):
    dict1[data[i]] = []


with open('Main_Data_Storage.json', 'r') as file:
    main_data = json.load(file)


index = 0

for i in range(len(main_data)):
    for j in range(len(main_data[i]['tech_stacks'])):
        dict1[main_data[i]['tech_stacks'][j]].append(index)

    index += 1


with open('Tech_stacks_and_orgs.json', 'w') as file:
    json.dump(dict1, file)




