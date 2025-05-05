# MODULE 6_ FINAL PROJECT_MUSIC AUTHORIZATION MANAGEMENT SYSTEM

def display_menu():
    """Display the main menu options"""
    print("\nMenu:")
    print("1. Signup")
    print("2. Sign-in")
    print("3. Exit")

def validate_email(email):
    """
    Basic email validation - checks for @ symbol
    """
    return "@" in email

def signup(user_data):
    """
    Handle the signup process, collecting user information
    """
    print("\nSign-up Process")
    
    # Get email with validation
    while True:
        email = input("Enter your email ID: ")
        if not validate_email(email):
            print("Invalid email format. Please try again.")
            continue
        
        # Check if email already exists
        if email in user_data:
            print("Email ID already exists. Please use a different one.")
            return
        break
    
    # Get password
    password = input("Enter your password: ")
    
    # Get user details
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    
    # Get and validate age
    while True:
        try:
            age = int(input("Enter your age: "))
            if age <= 0:
                print("Age must be a positive number.")
                continue
            break
        except ValueError:
            print("Please enter a valid integer for age.")
    
    # Store user data
    user_data[email] = {
        "password": password,
        "first_name": first_name,
        "last_name": last_name,
        "age": age
    }
    
    print("Registration successful!")

def signin(user_data):
    """
    Handle the sign-in process, validating user credentials
    """
    print("\nSign-in Process")
    
    email = input("Enter your email ID: ")
    password = input("Enter your password: ")
    
    # Check if email exists and password matches
    if email in user_data and user_data[email]["password"] == password:
        print(f"Welcome, {user_data[email]['first_name']} {user_data[email]['last_name']}!")
        return True
    else:
        print("Invalid email ID or password.")
        return False

def main():
    """
    Main function to run the authentication system
    """
    # Pre-populated user data as provided in the sample dictionary
    user_data = {
        "john.doe@example.com": {"password": "john123", "first_name": "John", "last_name": "Doe", "age": 28},
        "jane.smith@example.com": {"password": "jane456", "first_name": "Jane", "last_name": "Smith", "age": 25},
        "alice.jones@example.com": {"password": "alice789", "first_name": "Alice", "last_name": "Jones", "age": 24},
        "bob.brown@example.com": {"password": "bob012", "first_name": "Bob", "last_name": "Brown", "age": 30},
        "charlie.white@example.com": {"password": "charlie345", "first_name": "Charlie", "last_name": "White", "age": 35},
        "diana.green@example.com": {"password": "diana678", "first_name": "Diana", "last_name": "Green", "age": 27},
        "evan.black@example.com": {"password": "evan901", "first_name": "Evan", "last_name": "Black", "age": 29},
        "fiona.red@example.com": {"password": "fiona234", "first_name": "Fiona", "last_name": "Red", "age": 32},
        "george.blue@example.com": {"password": "george567", "first_name": "George", "last_name": "Blue", "age": 26},
        "hannah.yellow@example.com": {"password": "hannah890", "first_name": "Hannah", "last_name": "Yellow", "age": 31}
    }
    
    while True:
        display_menu()
        
        try:
            choice = int(input("\nChoose an option (1, 2, or 3): "))
            
            if choice == 1:
                signup(user_data)
            elif choice == 2:
                signin(user_data)
            elif choice == 3:
                print("Exiting the application. Goodbye!")
                break
            else:
                print("Invalid option. Please select 1, 2, or 3.")
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()
