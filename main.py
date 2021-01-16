import json
import csv
import smtplib
from email.message import EmailMessage

with open('All_Tech_Stacks.json', 'r') as file:
    all_tech = json.load(file)

print(all_tech)

user_tech_list = []

while 1:
    choice = int(input("Enter 1 to enter the tech stack that you know from the above list or enter -1 to exit: "))
    if choice == -1:
        break
    else:
        tech = input("Enter the tech stack: ")
        user_tech_list.append(tech)

with open('Main_Data_Storage.json', 'r') as file:
    main_data = json.load(file)

with open('Tech_stacks_and_orgs.json', 'r') as file:
    tech_and_orgs = json.load(file)

final_list = []

indexes = []

for i in range(200):
    indexes.append(0)

for tech in user_tech_list:
    try:
        for i in range(len(tech_and_orgs[tech])):
            if indexes[tech_and_orgs[tech][i]] == 0:
                final_list.append(main_data[tech_and_orgs[tech][i]])
                indexes[tech_and_orgs[tech][i]] = 1
    except Exception as e:
        print(e, "was not found in the above list of tech stacks.")

with open('To_send_csv_file.csv', 'w', encoding='utf8') as file:
    fieldnames = ['Organisation', 'URL', 'Tech Stacks']
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()

    for dictionary in final_list:
        dict2 = {}
        dict2['Organisation'] = dictionary['name']
        dict2['URL'] = dictionary['url']
        dict2['Tech Stacks'] = dictionary['tech_stacks']
        writer.writerow(dict2)

Email_Add = input("Enter your email address: ")
Email_Pass = input("Enter your password: ")

msg = EmailMessage()

msg['Subject'] = 'List of organisations which used tech stacks that you know.'
msg['From'] = Email_Add
msg['To'] = Email_Add

msg.set_content('Please find attached a csv file that contains the list of organisations which used tech stacks that you know.')

with open('To_send_csv_file.csv', 'rb') as f:
    file_data = f.read()
    file_name = "Details.csv"

msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(Email_Add, Email_Pass)
    smtp.send_message(msg)


