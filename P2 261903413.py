# Initialize variables for storing flight data.
flight_data = {}

while True:
    print("Airplane Management System")
    name = input("Enter Username:")
    password = input("Enter password:")

    if name.lower() == "user" and password.lower() == "user123":
        print("Welcome User:\n1. Book a ticket\n2. Cancel a booking\n3. Show flights")
        user_selection = int(input("Enter a number:"))

        if user_selection == 1:
            print("Available Flights:\n1. Flight company A\n2. Flight company B")
            flight_choice = int(input("Enter flight number: "))

            if 1 <= flight_choice <= 2:
                flight_name = ["Flight company A", "Flight company B"][flight_choice - 1]
                print(f"Booking a ticket for {flight_name}:")

                # Here, you can implement the code to book a ticket, such as selecting a row and seat.
                # You can use 2D arrays or dictionaries to manage seat availability.

                row = int(input("Enter row number: "))
                seat = input("Enter seat letter (A, B, C, D, E.): ").upper()

                # Add your booking logic here
                if row <= 0 or row > 10 or ord(seat) < ord('A') or ord(seat) > ord('E'):
                    print("Invalid row or seat selection.")
                else:
                    # Check if the seat is already booked or not and book if available
                    if flight_data.get(flight_name) is None:
                        flight_data[flight_name] = [['.' for _ in range(5)] for _ in range(10)]
                    if flight_data[flight_name][row - 1][ord(seat) - ord('A')] == '.':
                        flight_data[flight_name][row - 1][ord(seat) - ord('A')] = 'x'
                        print("Ticket booked successfully!")
                    else:
                        print("Error! This seat is already booked.")

            else:
                print("Invalid flight selection")

        elif user_selection == 2:
            print("Cancel a booking")
            # Implement code to cancel a booking here
            flight_name = input("Enter flight name: ")
            if flight_name in flight_data:
                row = int(input("Enter row number: "))
                seat = input("Enter seat letter (A, B, C, D, E.): ").upper()
                
                # Check if the seat is booked and cancel it
                if (
                    1 <= row <= 10 and
                    ord(seat) >= ord('A') and ord(seat) <= ord('E') and
                    flight_data[flight_name][row - 1][ord(seat) - ord('A')] == 'x'
                ):
                    flight_data[flight_name][row - 1][ord(seat) - ord('A')] = '.'
                    print("Booking canceled successfully!")
                else:
                    print("Error! This seat is not booked or invalid input.")
            else:
                print("Flight not found.")

        elif user_selection == 3:
            print("Show available flights and seats")
            # Implement code to show available flights and seats here
            for flight_name, seat_layout in flight_data.items():
                print(f"Flight: {flight_name}")
                for row, seat_row in enumerate(seat_layout, start=1):
                    seat_row_display = " ".join(seat_row)
                    print(f"Row {row}: {seat_row_display}")

        else:
            print("Invalid user selection")

    elif name.lower() == "admin" and password.lower() == "admin123":
        print("Welcome Admin:\n1. Add a flight\n2. Modify a flight\n3. Remove a flight")
        admin_selection = int(input("Enter a corresponding number: "))

        if admin_selection == 1:
            print("Add a flight")
            # Implement code to add a flight here
            flight_name = input("Enter flight company name: ")
            if flight_name not in flight_data:
                flight_data[flight_name] = [['.' for _ in range(5)] for _ in range(10)]
                print(f"Flight {flight_name} added successfully.")
            else:
                print(f"Flight {flight_name} already exists.")

        elif admin_selection == 2:
            print("Modify a flight")
            flight_name = input("Enter flight company name to modify: ")
            if flight_name in flight_data:
                # Display the current seat layout   
                print(f"Current {flight_name} – Seat Layout:")
                seat_layout = flight_data[flight_name]
                for row, seats in enumerate(seat_layout, start=1):
                    row_display = " ".join(seats)
                    print(f"Row {row}: {row_display}")
                # Input the new seat layout
                print(f"Enter the new seat layout for {flight_name}:")
                new_seat_layout = []
                for _ in range(10):
                    row_input = input(f"Enter seats for Row {_ + 1} (e.g., 'x . x . x . . . x .'): ")
                    row_seats = row_input.split()
                    if len(row_seats) != 5:
                        print("Invalid input. Please provide 5 seats for each row.")
                        break
                    new_seat_layout.append(row_seats)
                    
                if len(new_seat_layout) == 10:
                    flight_data[flight_name] = new_seat_layout
                    print(f"{flight_name} seat layout modified successfully.")
                else:
                    print("Flight not found.")
    
        elif admin_selection == 3:
            print("Remove a flight")
            # Implement code to remove a flight here
            flight_name = input("Enter flight company name to remove: ")
            if flight_name in flight_data:
                del flight_data[flight_name]
                print(f"Flight {flight_name} removed successfully.")
            else:
                print("Flight not found.")
        else:
            print("Invalid admin selection")
    else:
        print("Error! Wrong username or password. Try Again")

