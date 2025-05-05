# Code guide and usage guidelines

# Semester2_Python
MODULE 6 project 

# Music Management Application - User Authentication System

## Project Overview

This repository contains the User Authentication System module for a Music Management Application (similar to Spotify). The system handles user registration and login processes, ensuring secure access to music and playlists.

## Features

- **User Registration**: Collect and store user information including email, password, name, and age
- **User Authentication**: Validate user credentials for secure login
- **Data Validation**: Verify email format and user input
- **Pre-populated Users**: Test the sign-in functionality with existing user accounts
- **Simple Menu Interface**: Easy-to-use command-line interface

## Code Explanation

### Main Components

The code is organized into four main functions:

1. `display_menu()`: Shows the application menu options
2. `validate_email()`: Checks if an email has a valid format
3. `signup()`: Handles the user registration process
4. `signin()`: Authenticates user credentials
5. `main()`: Drives the application flow

### Code Breakdown

#### 1. Menu Display Function

```python
def display_menu():
    """Display the main menu options"""
    print("\nMenu:")
    print("1. Signup")
    print("2. Sign-in")
    print("3. Exit")
```
This function simply prints the menu options for the user interface.

#### 2. Email Validation

```python
def validate_email(email):
    """
    Basic email validation - checks for @ symbol and proper domain format
    """
    return "@" in email and "." in email.split("@")[1]
```
This function performs basic validation to ensure the email contains an '@' symbol and a domain with at least one '.' character.

#### 3. Signup Process

```python
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
```

The signup function:
- Collects and validates user email (checks format and uniqueness)
- Gathers password and user details
- Ensures age is a valid positive integer
- Stores the new user in the user_data dictionary
- Provides success feedback

#### 4. Sign-in Process

```python
def signin(user_data):
    """
    Handle the sign-in process, validating user credentials
    """
    print("\nSign-in Process")
    
    email = input("Enter your email ID: ")
    password = input("Enter your password: ")
    
    # Check if email exists and password matches
    if email in user_data and user_data[email]["password"] == password:
        print(f"Welcome back, {user_data[email]['first_name']}!")
        return True
    else:
        print("Invalid email ID or password.")
        return False
```

The signin function:
- Collects user email and password
- Checks if the email exists in the database
- Verifies the password matches the stored value
- Returns True for successful authentication, False otherwise
- Displays appropriate feedback messages

#### 5. Main Function

```python
def main():
    """
    Main function to run the authentication system
    """
    # Pre-populated user data as provided in the sample dictionary
    user_data = {
        "john.doe@example.com": {"password": "john123", "first_name": "John", "last_name": "Doe", "age": 28},
        # More pre-populated users...
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
```

The main function:
- Initializes the user_data dictionary with pre-populated users
- Creates a continuous loop to display the menu and handle user choices
- Calls the appropriate function based on user selection
- Includes error handling for invalid inputs
- Terminates the program when the user selects the exit option

## Data Structure

The user data is stored in a dictionary with the following structure:

```python
user_data = {
    "email@example.com": {
        "password": "user_password",
        "first_name": "First",
        "last_name": "Last",
        "age": 25
    },
    # More user entries...
}
```

This structure allows for:
- Fast lookup by email (used as the key)
- Organized storage of user attributes
- Easy addition of new users

## How to Run the Program

1. Ensure you have Python installed on your system
2. Clone this repository or download the Python file
3. Open a terminal or command prompt
4. Navigate to the directory containing the file
5. Run the command: `python music_auth_system.py`
6. Follow the on-screen prompts to interact with the system

## Sample Usage

### Sign-in with Pre-populated User

```
Menu:
1. Signup
2. Sign-in
3. Exit

Choose an option (1, 2, or 3): 2

Sign-in Process
Enter your email ID: john.doe@example.com
Enter your password: john123
Welcome back, John!
```

### New User Registration

```
Menu:
1. Signup
2. Sign-in
3. Exit

Choose an option (1, 2, or 3): 1

Sign-up Process
Enter your email ID: new.user@example.com
Enter your password: password123
Enter your first name: New
Enter your last name: User
Enter your age: 30
Registration successful!
```

## Verified Snapshots

# Sign up process tested

![image](https://github.com/user-attachments/assets/6da9d95e-74ad-4ce9-a98f-b69e78bf7891)

# Sign in process tested

![image](https://github.com/user-attachments/assets/03e92fc6-f201-46ae-b4d4-b887b114385d)

# Exiting process tested

![image](https://github.com/user-attachments/assets/040cd776-ebec-49d9-82ea-a46ab2bb7e33)



## Author

Nagashree
