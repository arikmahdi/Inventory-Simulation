
import numpy as np
import matplotlib.pyplot as plt 


m = int(input("Enter maximum capacity: "))  #maximum capacity
n = int(input("Enter review period: "))  #review period

begining_inventory= 3
demand= 0
ending_inventory= 0
shortage_quantity= 0
order_quantity= 8  
days_of_shortage=0
days_until_order_arrives= 2
ending_inventory_list=[]
days=[]


for cycle in range(1,11):

  print("⚫Cycle no:- ",cycle)

  for day in range (1,n+1):
    print("________________________________________")
    print("Day no: ", day)
    days_until_order_arrives=days_until_order_arrives-1

    ##order arrives code: begining_inventory= begining_inventory+ order_quantity    
    if days_until_order_arrives==-1:
      begining_inventory=ending_inventory+order_quantity

    daily_demand= np.random.choice(a=[0,1,2,3,4],p=[0.10,0.25,0.35,0.21,0.09])
    total_demand = daily_demand + shortage_quantity
    if total_demand> begining_inventory:
      shortage_quantity= total_demand-begining_inventory
      ending_inventory=0
      if shortage_quantity>0:
        days_of_shortage=days_of_shortage+1;
    else:
      ending_inventory= begining_inventory-total_demand
      shortage_quantity=0
    ending_inventory_list.append(ending_inventory) 
    
    print("Begining Inventory: ",begining_inventory)
    print("Daily Demand: ",daily_demand)
    print("Ending Inventory: ",ending_inventory)
    print("Shortage Quantity: ",shortage_quantity)

    begining_inventory=ending_inventory

    ##Review code (Task-1)
    #when day==n: , then you have to place an order. order_quantity; days_until_order_arrives (randomly)
    if day==n:
      #order place, lead time
      days_until_order_arrives= np.random.choice(a=[1,2,3],p=[0.6,0.3,0.1]) #lead time
      order_quantity=m-ending_inventory
      print("Order: ",order_quantity)
     
    if days_until_order_arrives>=0:
      print("Days until order arrives: ",days_until_order_arrives)
    else:
      print("Days until order arrives:---")     

#average_ending_inventory
total=0
total=sum(ending_inventory_list)
length=0
length=len(ending_inventory_list)
average_ending_inventory=total/length
#number of days shortage occurs

print("Days Shortage occurs ", days_of_shortage)


#ending inventory vs days graph:
for i in range(1,length+1):  #days appending [ending inventory occurs every days]
  days.append(i)

# Draw inventory_level vs day graph .
# X -axis : day number
# Y- axis : Ending_inventory of each day

plt.xlabel("Day Number")
plt.ylabel("Ending_inventory of each day")

plt.plot(days,ending_inventory_list) #x,y ploting
print(ending_inventory_list)