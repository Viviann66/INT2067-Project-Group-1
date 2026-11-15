#make a calendar system with email reminders, event marking, etc.
'''
This code is my own individual and original work with very limited AI assistant. For any
part of codes that are referenced to, supported by AI, acknowledgement will be specified
'''

#Library imports:
import smtplib #to send email reminders to the user
from datetime import datetime #to check date validity

#Configuring SMTP:
HOST = "smtp.gmail.com" #host for gmail sender email
PORT = 587 #default ports

FROM_EMAIL = "burnerint2067@gmail.com" #sender email
TO_EMAIL = "" #placeholder recipient
PASSWORD = "yqyi lmuu qvbx vwyg" #default app password
#(Gmail requires an app password to approve sending emails through a gmail account)
#(Otherwise, it will be flagged and not sent)

#store sender email and password in a file:
with open("sender.txt", "w") as file:
    file.write(FROM_EMAIL)
    file.write(PASSWORD)

#create recipients file to store all recipients later:
with open("recipients.txt", "w") as text:
    pass

MESSAGE = "" #placeholder message

#Dictionary to store marked dates:
calendar = {}

#Command Functions (Mark, Delete, Check, Reschedule, Reminder):
def mark_date(event, date):

    #check if the event is a unique one, then mark it if so
    if event not in calendar:
        calendar[event] = date
        return f"Date saved {date.strftime('%d-%m-%Y')}."
    else:
        return "Event already logged."

def delete_date(event):

    #check if event marked, and delete if so
    if event in calendar.keys():
        return f"Deleted event for {calendar.pop(event)}."
    else:
        return "Event not found."

def check_dates():

    #stop if no events marked yet
    if not calendar: 
        return "No events marked yet."

    #output all dates if at least one marked
    for event, date in calendar.items():
        print(f"{event} - on {date.strftime('%d-%m-%Y')}\n")

    return "All events displayed."

def reschedule_event(event, newDate):

    #checking if event exists, then changing value
    if event in calendar:
        calendar[event] = newDate
        return f"Event '{event}' rescheduled to {newDate.strftime('%d-%m-%Y')}."
    else:
        return "Event not found."

def reminder_on_or_off(event):

    #collecting and storing recipient mails
    TO_EMAIL = input("Enter your recipient email: ")
    with open("recipients.txt", "a") as file:
        file.write(TO_EMAIL + "\n")

    #formatting to our usual date style
    dateFormatted = calendar[event].strftime('%d-%m-%Y')

    #creating email message
    MESSAGE = f"""Subject: REMINDER {event} 
Hi user,

This email is a reminder about {event}.

You have {event} on the date {dateFormatted}
"""
    
    with smtplib.SMTP(HOST, PORT) as server: #opening smtp and closing as soon as done
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(FROM_EMAIL, PASSWORD)
        server.sendmail(FROM_EMAIL, TO_EMAIL, MESSAGE)

    return "Email reminder successfully turned on and sent."

#Welcome message:
bar = f"{'':-<60}"
welcomeScreen = [
    [bar],
    ['|', f"{'':<9}", '          __      _             __      ', f"{'':<9}", '|'],
    ['|', f"{'':<9}", ' \  /\  / |_  |  /  /\  /\  /\  |_      ', f"{'':<9}", '|'],
    ['|', f"{'':<9}", '  \/  \/  |_  |_ \_ \/ /  \/  \ |_      ', f"{'':<9}", '|'],
    ['|', f"{'':<9}", '              ___  /\                   ', f"{'':<9}", '|'],
    ['|', f"{'':<9}", '               |  |  |                  ', f"{'':<9}", '|'],
    ['|', f"{'':<9}", '               |   \/   _          __   ', f"{'':<9}", '|'],
    ['|', f"{'':<9}", ' _   /\   |   __ |\  | | \    /\   | \ |', f"{'':<9}", '|'],
    ['|', f"{'':<9}", '/   /__\  |   |_ | \ | |  |  /__\  |_/ |', f"{'':<9}", '|'],
    ['|', f"{'':<9}", '\_ /    \ |__ |_ |  \| |_/  /    \ | \ .', f"{'':<9}", '|'],
    ['|', f"{'':<58}", '|'],
    ['|', f"{'':<7}", ' __  __  __  /\  /\ ', f"{'':<5}",  ' __      ___        ', f"{'':<6}", '|'],
    ['|', f"{'':<7}", ' |_\ |_\ |_  \   \ ', f"{'':<5}", '  |_ |\ |  |         ', f"{'':<6}", '|'],
    ['|', f"{'':<7}", ' |   | \ |_ \/  \/ ', f"{'':<5}", '  |_ | \|  | . . .   ', f"{'':<6}", '|'],
    [bar],
]

for i in range(len(welcomeScreen)):
    print(''.join(welcomeScreen[i]))

#Arbitrary variable to create a pause buffer between screens/inputs
buffer = input()
print('\n'*3)

#Option Screen:
prompt = "Please enter a command (1-6):"

#Options 1-5
optionsScreen = {
    '1': 'Mark Date',
    '2': 'Delete Date',
    '3': 'check Date',
    '4': 'Reschedule Event',
    '5': 'Reminder On/Off',
    '6': 'Quit Calendar'
}

errorMes = "Wrong input, please try again!"

while True:

    print(prompt, '\n'*2)
    print(bar)
    for command, action in optionsScreen.items():
        print(f"| ( {command} {')':<3}-  {action}")

    #Prompt user for command
    print(bar, '\n'*2)
    comm = input("INPUT = ")

    #Check for validity of command (if in Dict.keys():)
    if comm in optionsScreen.keys():
        if comm == '1':

            #collecting input for marking
            eventName = input("Event name: ")

            #keep validating until correct
            oneChecked = False
            while not oneChecked:

                date = input("Date (dd-mm-yyyy format): ")
                #try validating until no errors are raised
                try:
                    validDate = datetime.strptime(date, '%d-%m-%Y').date()
                    oneChecked = True
                except ValueError:
                    print("Invalid Format. Try dd-mm-yyyy, e.g. 17-08-2012")

            print(mark_date(eventName, validDate))

        elif comm == '2':

            #collecting input for deletion
            eventToDelete = input("Enter event name to delete: ")

            print(f"Deleting event {eventToDelete}...")
            print(delete_date(eventToDelete))

        elif comm == '3':

            #output all marked dates, add a buffer to give user time to read
            print(check_dates())
            buffer = input("Press ENT to continue...")

        elif comm == '4':

            #collecting input for rescheduling
            eventName = input("Event name: ")

            #keep validating until correct
            fourChecked = False
            while not fourChecked:

                date = input("Date (dd-mm-yyyy format): ")
                #try validating until no errors are raised
                try:
                    validDate = datetime.strptime(date, '%d-%m-%Y').date()
                    fourChecked = True
                except ValueError:
                    print("Invalid Format. Try dd-mm-yyyy, e.g. 17-08-2012")

            print(reschedule_event(eventName, validDate))

        elif comm == '5':

            #collecting input for reminder
            event = input("Enter event to remind: ")

            #call function
            if event in calendar.keys():
                print(reminder_on_or_off(event))
            else:
                print("Event not found")

        elif comm == '6':

            #quit loop and end all processes
            break

    else:
        print(bar, '\n', errorMes, '\n', bar, sep='')

#goodbye message
print("Thank you for using the calendar, goodbye!")