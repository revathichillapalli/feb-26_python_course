class MovieTicketBooking:
    def __init__(self):
        self.movies = {
            'Avengers: Endgame': 300,
            'Avatar 2': 250,
            'Jumanji: The Next Level': 180,
            'The Lion King': 220,
            'Spiderman: No Way Home': 350,
            'Doctor Strange 2': 280,
            'Black Panther': 300,
            'Frozen 2': 230
        }
        self.gst_rate = 18  # GST rate is 18%
        self.booking_details = {}

    def show_movies(self):
        print("\nAvailable Movies:")
        for idx, movie in enumerate(self.movies.keys(), start=1):
            print(f"{idx}. {movie} - Price: ₹{self.movies[movie]}")

    def select_movie(self):
        self.show_movies()
        choice = int(input("\nEnter the number corresponding to your movie selection: "))
        if choice < 1 or choice > len(self.movies):
            print("Invalid choice, please try again.")
            return self.select_movie()
        else:
            movie = list(self.movies.keys())[choice - 1]
            return movie

    def enter_ticket_quantity(self):
        try:
            quantity = int(input("\nEnter number of tickets: "))
            if quantity <= 0:
                print("Please enter a valid quantity (greater than 0).")
                return self.enter_ticket_quantity()
            return quantity
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            return self.enter_ticket_quantity()

    def calculate_total(self, movie, quantity):
        base_price = self.movies[movie]
        total_price = base_price * quantity
        gst_amount = total_price * (self.gst_rate / 100)
        total_amount = total_price + gst_amount
        return total_price, gst_amount, total_amount

    def display_booking_summary(self, movie, quantity, total_price, gst_amount, total_amount):
        print("\nBooking Summary:")
        print(f"Movie: {movie}")
        print(f"Number of tickets: {quantity}")
        print(f"Base price: ₹{total_price}")
        print(f"GST (18%): ₹{gst_amount}")
        print(f"Total amount to be paid: ₹{total_amount}")
        self.booking_details = {
            'movie': movie,
            'quantity': quantity,
            'total_price': total_price,
            'gst_amount': gst_amount,
            'total_amount': total_amount
        }

    def payment(self):
        print("\nProceeding to payment...")
        try:
            payment_amount = float(input(f"\nEnter payment amount (₹{self.booking_details['total_amount']}): ₹"))
            if payment_amount < self.booking_details['total_amount']:
                print("Insufficient amount. Please try again.")
                return self.payment()
            else:
                print(f"Payment successful! Change to be returned: ₹{payment_amount - self.booking_details['total_amount']}")
        except ValueError:
            print("Invalid input. Please enter a valid payment amount.")
            return self.payment()

    def confirm_booking(self):
        print("\nBooking confirmed!")
        print("Thank you for booking with us!")
        print("Enjoy your movie!")

    def cancel_booking(self):
        print("\nBooking cancelled.")
        print("No worries, we hope to see you again!")

    def modify_booking(self):
        print("\nModifying your booking...")
        movie = self.select_movie()
        quantity = self.enter_ticket_quantity()
        total_price, gst_amount, total_amount = self.calculate_total(movie, quantity)
        self.display_booking_summary(movie, quantity, total_price, gst_amount, total_amount)

    def view_booking_details(self):
        if not self.booking_details:
            print("\nNo booking found. Please make a booking first.")
        else:
            print("\nBooking Details:")
            for key, value in self.booking_details.items():
                print(f"{key.capitalize()}: {value}")

    def main_menu(self):
        print("\n===== Movie Ticket Booking System =====")
        print("1. Book Tickets")
        print("2. View Booking Details")
        print("3. Modify Booking")
        print("4. Cancel Booking")
        print("5. Exit")
        choice = input("Please select an option (1-5): ")

        if choice == '1':
            self.run_booking_process()
        elif choice == '2':
            self.view_booking_details()
            self.main_menu()
        elif choice == '3':
            self.modify_booking()
            self.main_menu()
        elif choice == '4':
            self.cancel_booking()
            self.main_menu()
        elif choice == '5':
            print("\nExiting the system. Have a great day!")
        else:
            print("\nInvalid choice, please try again.")
            self.main_menu()

    def run_booking_process(self):
        print("\nWelcome to the Movie Ticket Booking System!")
        movie = self.select_movie()
        quantity = self.enter_ticket_quantity()
        total_price, gst_amount, total_amount = self.calculate_total(movie, quantity)
        self.display_booking_summary(movie, quantity, total_price, gst_amount, total_amount)
        self.payment()
        self.confirm_booking()
        self.main_menu()

if __name__ == "__main__":
    booking_system = MovieTicketBooking()
    booking_system.main_menu()
