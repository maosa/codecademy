"""

In this project, we’ll build a basic calendar that the user will be able to interact with from the command line. The user should be able to choose to:

1) View the calendar
2) Add an event to the calendar
3) Update an existing event
4) Delete an existing event

"""

from time import sleep, strftime

user = "Andreas"

calendar = {}

def welcome():
  print("\nWelcome " + user)
  print("\nPyCal is now active!\n")
  sleep(1)
  print("Today's date: " + strftime("%A, %d %B %Y"))
  print("Current time: " + strftime("%H:%M:%S"))
  sleep(1)
  print("What would you like to do?")

def start_calendar():
    welcome()
    start = True
    while start == True:
        user_choice = input("Enter A to Add, U to Update, V to View, D to Delete, X to Exit: ")
        user_choice = user_choice.upper()
        if user_choice == "V":
            if len(calendar.keys()) == 0:
                print("\nCalendar is empty. No event found...\n")
            else:
                print(calendar)
        elif user_choice == "U":
            date = input("What date (MM/DD/YYYY)? ")
            update = input("Enter the update: ")
            calendar[date] = update
            print("\nUpdate successful!\n")
            print(calendar)
        elif user_choice == "A":
            event = input("Enter event: ")
            date = input("Enter date (MM/DD/YYYY): ")
            # Check: A date in the format MM/DD/YYYY contains 10 characters if you include the forward slashes
            if len(date) > 10 or int(date[6:]) < int(strftime("%Y")):
                print("\nInvalid date format of year was entered\n")
                try_again = input("Try Again? Y for Yes, N for No: ")
                try_again = try_again.upper()
                if try_again == "Y":
                    continue
                    # The 'continue' keyword will start the loop from the beginning
                else:
                    print("\nThank you for using PyCal. See you later!\n")
                    start = False
                    # This will exit the loop and quit the program
            else:
                calendar[date] = event
                print("\nEvent successfully added!\n")
                print(calendar)
        elif user_choice == "D":
            if len(calendar.keys()) == 0:
                print("\nCalendar is empty. There are no events to delete...\n")
            else:
                event = input("What event? ")
                for date in calendar.keys():
                    if event == calendar[date]:
                        del calendar[date]
                        print("\nEvent successfully deleted!\n")
                        print(calendar)
                    else:
                        print("\nInvalid event specified. Event " + event + " not found.\n")
        elif user_choice == "X":
            print("\nThank you for using PyCal. See you later!\n")
            start = False
        else:
            start = False

start_calendar()
