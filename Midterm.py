from datetime import date

def main():

  #https://www.pythontutorial.net/python-basics/python-read-text-file/
  #for reading from a text file
  tickets={}
  global ticket_id
  global highest_event_id
  ticket_id=0
  highest_event_id=0
  # with open("tickets.txt") as t:
  #   for line in t:
  #     l=line.split(',')[1].strip()
  #     tickets[l]=[]
  #     if int(line.split(',')[0][4:])>ticket_id:
  #       ticket_id=int(line.split(',')[0][4:])
  #     if int(line.split(',')[1].strip()[2:])>highest_event_id:
  #       highest_event_id=int(line.split(',')[1].strip()[2:])
  # with open("tickets.txt") as t:
  #   for line in t:
  #     l=line.split(',')[1].strip()
  #     tickets[l].append(line.strip())
  l=list()
  with open("tickets.txt") as t:
     for line in t:
       l.append(line.strip().split(','))
  for i in l:
    tickets[i[1].strip()]=[]
    if int(i[0].strip()[4:])>ticket_id:
      ticket_id=int(i[0].strip()[4:])   
    if int(i[1].strip()[2:])>highest_event_id:
        highest_event_id=int(i[1].strip()[2:])
  for i in l:
    tickets[i[1].strip()].append(i)
  # print(tickets)
  
  
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
  # displayMenu(user)
  # displayStatistics(tickets)
  # bookTicket(tickets)
  # print(tickets)
  # print(ticket_id)
  
  #showTickets(tickets)
  # changePriority(tickets)
  #remember to increment the ticket_id
  # removeTicket(tickets)
  # print(tickets)
  todayEvents(tickets)
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
  
  new_ticket=input("please add: username, event id, date(YYYYMMDD), priority: ")
  
  event=new_ticket.split(',')[1].strip()
  username=new_ticket.split(',')[0].strip()
  priority=new_ticket.split(',')[3].strip()
  # datee="20"+date.today().strftime("%y%m%d")
  datee=new_ticket.split(',')[2].strip()
  #cheking if the event already exist in the dictionary else we will add a new event 
 
  a=[f"tick{ticket_id+1}",event,username,datee,priority]
  if event in tickets:
    tickets[event].append(a)
  else:
    tickets[event]=[a]
 
 
 #############################
 
def showTickets(tickets):
  datee=int("20"+date.today().strftime("%y%m%d"))
  present_tickets=[]
  #in this for loop i check the date if its not in the past it will be added to the present_tickets list
  for key,value in tickets.items():
      for i in value:
        value_date=int(i[3].strip())
        if value_date>=datee:
          present_tickets.append(i)
          
          
  sorted_tickets=[]
  ev=0
  #in this loop the tickets will be sorted by event, tickets with same event number will be added to a list then added to event_sorted_list
  for i in range(highest_event_id+1):
    list=[]
    
    for j in present_tickets:
      if int(j[1].strip()[2:])==ev:
        list.append(j)
    if list:
      sorted_tickets.append(list)
    ev+=1
 
 #used bubblesort to sort the list by the date
  for i in sorted_tickets:
   
    for x in range(len(i)):
      check_swap = False
      for y in range(len(i) - x - 1):
        a=int(i[y][3].strip())
        b=int(i[y + 1][3].strip())
        if a > b:
          check_swap = True
          temp =i[y]
          i[y] = i[y + 1]
          i[y + 1] = temp
      if not check_swap:  
        break
        
  for i in sorted_tickets:
    for j in range(len(i)):
      print(i[j])   
   
        
###################################
def changePriority(tickets):
  id=input("please enter the ticket id: ")
  new_priority=input("Enter the new priority: ")
  found=False
  for key,value in tickets.items():
    for i in range(len(value)):
      if value[i][0]==id:
       value[i][4]=new_priority
       found=True
       break
  if not found:
    print("Ticket is not available!")
  else:
    print("Done!")   


###################################
def removeTicket(tickets):
  id=input("Enter the id of the ticket you want to remove: ")
  l=[]
  k=""
  found=False
  #looping in the dict to look for the ticket id , if its available, the list that this ticket belongs to will be cleared,after that another loop will remove the [] from the dict by adding lists that are not empty
  for key,value in tickets.items():
    for i in range(len(value)):
      if value[i][0]==id:
        value[i].clear()
        k=key
        found=True
  if found:
    for i in tickets[k]:
      if len(i)!=0:   
        l.append(i)
    tickets[k]=l
    print("Done!") 
  else:
    print("Ticket is not available!")
    
##############################
  
def todayEvents(tickets):
  l=[]
  datee=int("20"+date.today().strftime("%y%m%d"))
  #added all values with today's date to a list
  for key,value in tickets.items():
    for i in value:
      if int(i[3])==datee:
        l.append(i)
  print(l)
  
  #bubble sort the list by the date
  for x in range(len(l)):
    check_swap = False
    for y in range(len(l) - x - 1):
      
      if l[y][4] > l[y + 1][4]:
        check_swap = True
        temp = l[y]
        l[y] = l[y + 1]
        l[y + 1] = temp
        
    if not check_swap:  
      return l
  print(l)
  
  
main()