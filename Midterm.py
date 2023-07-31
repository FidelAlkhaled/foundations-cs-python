from datetime import date

def main():

  #https://www.pythontutorial.net/python-basics/python-read-text-file/
  #for reading from a text file
  tickets={}
  global ticket_id
  global highest_event_id
  global username
  ticket_id=0
  highest_event_id=0

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
      print(f"{attempts} remaining attempts ")
    if username=="admin" and password=="admin123123":
      user="admin"
    else:
      exit()
  displayMenu(user,tickets)
  
############################
#this function will recieve the user type and based on it, it will print the menu
def displayMenu(user_type,tickets):
  print("\nChoose an option:")
  print("###################")

  if user_type=="admin":
    option=int(input("1. Display Statistics\n2. Book a Ticket\n3. Display all Tickets\n4. Change Ticket’s Priority\n5. Disable Ticket\n6. Run Events\n7. Exit\n"))
    if option==1:
      displayStatistics(tickets)
      displayMenu(user_type,tickets)
    elif option==2:
      bookTicket(tickets,user_type)
      displayMenu(user_type,tickets)
    elif option==3:
      showTickets(tickets)
      displayMenu(username,tickets) 
    elif option==4:
      changePriority(tickets)
      displayMenu(username,tickets) 
    elif option==5:
      id=input("Enter the id of the ticket you want to remove in this format ex:(tick101) : ")
      removeTicket(tickets,id)
      displayMenu(username,tickets) 
    elif option==6:
      todayEvents(tickets)
      displayMenu(username,tickets) 
    elif option==7:
      save(tickets)
      exit()
  else:
    option=int(input("1. Book a ticket\n2. Exit\n"))
    if option==1:
      bookTicket(tickets,user_type)
      displayMenu(user_type,tickets)
    elif option==2:
      save(tickets)
      exit() 
    
    
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
def bookTicket(tickets,user):
  global ticket_id
  global highest_event_id
  a=[]
  
  
  if user=="admin":
    new_ticket=input("please add by using this same format: username, event id, date(YYYYMMDD), priority: ")
    event=new_ticket.split(',')[1].strip()
    user=new_ticket.split(',')[0].strip()
    priority=new_ticket.split(',')[3].strip()
    datee=new_ticket.split(',')[2].strip()
    a=[f"tick{ticket_id+1}",f" {event}",f" {user}",f" {datee}",f" {priority}"]
  else:
    new_ticket=input("please add by using this same format: event id, date(YYYYMMDD): ")
    event=new_ticket.split(',')[0].strip()
    user=username
    priority=0
    datee=new_ticket.split(',')[1].strip()
    a=[f"tick{ticket_id+1}",f" {event}",f" {user}",f" {datee}",f" {priority}"]
    
    
  #cheking if the event already exist in the dictionary else we will add a new event 
  print(a)
  if event in tickets:
    tickets[event].append(a)
  else:
    tickets[event]=[a]
    
    
  #if the event number entered is higher than the highest_event_id it's value will be changed to event 
  if highest_event_id<int(event.strip()[2:]):
    highest_event_id=int(event.strip()[2:])
    
    
  #automatically incrementing ticket_id after adding one
  ticket_id+=1
  return True
 
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
  id=input("please enter the ticket id ex: tick102 : ")
  new_priority=input("Enter the new priority: ")
  found=False
  for key,value in tickets.items():
    for i in range(len(value)):
      if value[i][0]==id:
       value[i][4]=new_priority
       found=True
       print(value[i])
       break
  if not found:
    print("Ticket is not available!")
  else:
    print("Done!")   
  

###################################
def removeTicket(tickets,id):
  
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
        break
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
      break
  for i in l:
    print(i)
  #using the removeTicket function to delete today's tickets after showing them
  if len(l)>0:
    for i in l:
      removeTicket(tickets,i[0])
  else :
    print("no tickets for today")
  
####################################
def save(tickets):
  s=""
  for key,value in tickets.items():
    for i in value:
      #https://www.geeksforgeeks.org/python-program-to-convert-a-list-to-string/
      s+= ','.join([str(elem) for elem in i])
      s+='\n'
  #https://www.pythontutorial.net/python-basics/python-write-text-file/
  with open('tickets.txt', 'w') as f:
      f.write(s)
  
  
main()