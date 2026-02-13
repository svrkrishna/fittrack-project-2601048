# Theatre Seat Booking
Capacity = 350
Min_Age = 12
Min_Tickets = 1
Max_Tickets = 15
seats_left = Capacity
Total_bookings = 0
Tickets_sold = 0
Rejected_Bookings = 0
while seats_left > 0:
    Tickets = int(input("Enter Number of Tickets(0 to exit): "))
    if Tickets == 0:
        break
    if Tickets < Min_Tickets or Tickets > Max_Tickets:
        print("BOOKING REJECTED - Can book 1 to 15 tickets only")
        Rejected_Bookings += 1
        continue
    if Tickets > seats_left:
        print(f"BOOKING REJECTED - Only {seats_left} seats remaining")
        Rejected_Bookings += 1
        continue
    Age_Restricted = False
    for person in range(1, Tickets + 1):
        Age = int(input(f"Enter the Age of the person{person}: "))
        if Age < Min_Age:
            Age_Restricted = True
            break
    if Age_Restricted:
        remaining = Tickets - person
    if Age_Restricted:
        remaining = Tickets - person
        for _ in range(remaining):
            _ = int(input("Enter age of next person: "))

        print("BOOKING REJECTED - Age restriction")
        Rejected_Bookings += 1
        continue

    # Confirm booking
    Total_bookings += 1
    Tickets_sold += Tickets
    seats_left -= Tickets

    print(f"BOOKING CONFIRMED - {Tickets} tickets")

    if seats_left == 0:
        break

print("\nFINAL REPORT")
print(f"Total Bookings: {Total_bookings}")
print(f"Total Tickets Sold: {Tickets_sold}")
print(f"Rejected Bookings: {Rejected_Bookings}")
print(f"Remaining Seats: {seats_left}")
