"""
Calendar.py allows you to view the calendar, add an event to the calendar, update an existing event, and delete an existing event
"""
from time import sleep, strftime
name = "WILLIAM_WALLACE"
calendar = {}

def welcome():
  print "Welcome %s" % name 
  print "...Calendar is opening..."
  sleep(1)
  print strftime("%A, %d %B %Y")
  print strftime("%H:%M:%S")
  sleep(1)
  print "What would you like do to?"
  
def start_calendar():
  welcome()
  start = True
  while start == True:
    user_choice = raw_input("Enter A to add, U to Update, V to View, D to Delete, X to Exit: ")
    user_choice = user_choice.upper()
    if user_choice == "V":
      if len(calendar.keys()) < 1:
        print "Calendar is empty"
      else:
        print calendar
    elif user_choice == "U":
      date = raw_input("What date? ")
      update = raw_input("Enter the update: ")
      calendar[date] = update
      print "Update successful."
      print calendar
    elif user_choice == "A":
      event = raw_input("Enter event: ")
      date = raw_input("Enter date (DD/MM/YYYY): ")
      if len(date) > 10 or int(date[6:]) < int(strftime("%Y")):
        print "That date was invalid"
        try_again = raw_input("Try Again? Y for Yes, N for No: ")
        try_again = try_again.upper()
        if try_again == "Y":
          continue
        else:
          start = False
      else: 
        calendar[date] = event
        print "Event was successfuly added to the calendar."
        print calendar
    elif user_choice == "D":
      if len(calendar.keys()) < 1:
        print "Cannot delete events in an empty calendar."
      else: 
        event = raw_input("What event? ")
        for date in calendar.keys():
          if event == calendar[date]:
            del calendar[date]
            print("Event successfully deleted.")
            print calendar
          else:
            print "Event not found in calendar."
    elif user_choice == "X":
      start = False
    else:
      print "Invalid command entered."
      start = False

start_calendar()





