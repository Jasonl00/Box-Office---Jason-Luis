# A movie theater keeps a percentage of the revenue earned from ticket sales. The remainder goes to the distributor. Write a program that calculates a theater's gross and net box office profit for the night. The program should ask for the name of the movie, and how many adult and child tickets were sold. (The price of an adut ticket is $6.00 and a childs is $3.00.)
# Jason Luis
# Professor Ghaforyfard
# February 14, 2024

#Variables

adult_tickets = 0

child_tickets = 0

# Movie input and output
movie_name = input("Movie name: ") 

print('\n"',movie_name,'"') 

#input of the movie tickets 

adult_tickets = int(input("\nAdult Tickets Sold: ")) 

child_tickets = int(input("\nChild Tickets Sold: "))


#calculating the tickets

child_tickets_total = float(child_tickets * 3.00) 

adult_tickets_total = float(adult_tickets * 6.00) 

box_office_net = float(child_tickets_total + adult_tickets_total)

print("\nGross Box Office Profit is: $",box_office_net) 

# Distributor Profit and Net Amount
net_box_office_profit = float(box_office_net * 0.20) 

distributor_amount  = float(box_office_net - net_box_office_profit) 


# outputs 

print("\nAmount paid to Distributor: - $",distributor_amount ) 

print("\nNet Box Office Profit: $", net_box_office_profit,"\n")