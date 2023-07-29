from datetime import date

def main():

  #https://www.pythontutorial.net/python-basics/python-read-text-file/
  #for reading from a text file
  tickets={}
  global ticket_id
  ticket_id=0
  with open("tickets.txt") as t:
    for line in t:
      l=line.split(',')[1]
      tickets[l]=[]
      if int(line.split(',')[0][4:])>ticket_id:
        ticket_id=int(line.split(',')[0][4:])
  with open("tickets.txt") as t:
    for line in t:
      l=line.split(',')[1]
      tickets[l].append(line.strip())

  

  username=input("Enter your Username: ")
  password=input("Enter your Password: ")

  #login
  user=""
  if len(password)==0:
    user="normal"
  else:
    attempts=5
    while (password!="admin123123" or username!="admin") and attempts>0:
      
      print("Incorrect Username and/or Password")
      username=input("Enter your Username: ")
      password=input("Enter your Password: ")
      attempts-=1
    if username=="admin" and password=="admin123123":
      user="admin"
    else:
      exit()
  displayMenu(user)
  displayStatistics(tickets)
  bookTicket(tickets)
  print(tickets)
  print(ticket_id)
  #remember to increment the ticket_id


############################
#this function will recieve the user type and based on it, it will print the menu
def displayMenu(user_type):
  print("\nChoose an option:")
  print("###################")

  if user_type=="admin":
    print("1. Display Statistics\n2. Book a Ticket\n3. Display all Tickets\n4. Change Ticket’s Priority\n5. Disable Ticket\n6. Run Events\n7. Exit")
  else:
    print("1. Book a ticket\n2. Exit")
##############################   
def displayStatistics(tickets):
#this function loops in the dictionary which contains all the tickets and has the key as the ticket event id , and by comparing the len of the values we get the event id with the highest number of tickets
  k=0
  l=0
  for key, value in tickets.items():
    if len(value)>l:
      l=len(value)
      k=key
  print(f"event {k} has the highest number of tickets which is {l}")

###############################
def bookTicket(tickets):
  #!!!!use .strip() for better comparison
  new_ticket=input("please add: username, event id, priority: ")
  
  event=new_ticket.split(',')[1]
  username=new_ticket.split(',')[0]
  priority=new_ticket.split(',')[2]
  datee="20"+date.today().strftime("%y%m%d")

  #cheking if the event already exist in the dictionary else we will add a new event 
  if event in tickets:
    tickets[event].append([f"tick{ticket_id+1}",event,username,datee,priority])
  else:
    tickets[event]=[f"tick{ticket_id+1}",event,username,datee,priority]
 
  
main()