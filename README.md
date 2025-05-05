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

# Authentication System Code Explanation

Let's break down the code block by block to understand how this authentication system works:

## 1. `display_menu()` Function

```python
def display_menu():
    """Display the main menu options"""
    print("\nMenu:")
    print("1. Signup")
    print("2. Sign-in")
    print("3. Exit")
```

**Explanation:**
- This is a simple function that displays the menu options to the user.
- It shows three options: Signup, Sign-in, and Exit.
- The `\n` creates a new line before "Menu:" for better readability.
- The function doesn't take any parameters or return any values - it just prints text to the console.

## 2. `validate_email()` Function

```python
def validate_email(email):
    """
    Basic email validation - checks for @ symbol
    """
    return "@" in email
```

**Explanation:**
- This function performs a very basic email validation.
- It takes an email string as input and checks if the "@" symbol is present.
- It returns `True` if the "@" symbol is found, otherwise `False`.
- This is a minimal validation that ensures the email has at least the basic structure of an email address.
- In a production environment, you would want more comprehensive validation using regex patterns.

## 3. `signup()` Function

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

**Explanation:**
- This function handles the entire signup process.
- It takes `user_data` (a dictionary) as a parameter to store and check against existing users.
- Email validation:
  - It uses a while loop to keep asking for an email until a valid one is provided.
  - It first checks if the email is in valid format using the `validate_email()` function.
  - Then it checks if the email already exists in the system to prevent duplicate registrations.
- Password collection:
  - It simply asks for a password without any validation (in a real system, you'd want to enforce password complexity and confirmation).
- User details collection:
  - Collects first name and last name without validation.
- Age validation:
  - Uses another while loop to ensure the age input is a valid positive integer.
  - Uses a try-except block to catch any non-integer inputs.
  - Checks if the age is positive (greater than 0).
- Data storage:
  - Creates a new entry in the `user_data` dictionary with the email as the key.
  - Stores all user details (password, first name, last name, age) as a nested dictionary.
- Finally, it confirms successful registration with a message.

## 4. `signin()` Function

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
        print(f"Welcome, {user_data[email]['first_name']} {user_data[email]['last_name']}!")
        return True
    else:
        print("Invalid email ID or password.")
        return False
```

**Explanation:**
- This function handles the sign-in process.
- It takes `user_data` as a parameter to validate against stored credentials.
- It prompts the user for their email and password.
- Authentication logic:
  - Checks if the email exists in the `user_data` dictionary.
  - If it exists, checks if the password matches the stored password.
  - Both conditions must be true for successful authentication.
- Success handling:
  - On successful authentication, it displays a personalized welcome message.
  - Returns `True` to indicate successful login.
- Failure handling:
  - If either the email doesn't exist or the password doesn't match, it shows an error message.
  - Returns `False` to indicate failed login.
- Note that for security, it doesn't specify whether the email or password was incorrect.

## 5. `main()` Function

```python
def main():
    """
    Main function to run the authentication system
    """
    # Pre-populated user data as provided in the sample dictionary
    user_data = {
        "john.doe@example.com": {"password": "john123", "first_name": "John", "last_name": "Doe", "age": 28},
        "jane.smith@example.com": {"password": "jane456", "first_name": "Jane", "last_name": "Smith", "age": 25},
        # ... more pre-populated users ...
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
```

**Explanation:**
- This is the main driver function of the program.
- It initializes `user_data` with pre-populated users for demonstration purposes.
- The dictionary has:
  - Keys: email addresses
  - Values: nested dictionaries containing password, first name, last name, and age
- It uses an infinite loop (`while True`):
  - Displays the menu using the `display_menu()` function.
  - Prompts the user to choose an option.
  - Uses a try-except block to catch non-integer inputs.
- Option handling:
  - Option 1: Calls the `signup()` function passing the `user_data` dictionary.
  - Option 2: Calls the `signin()` function passing the `user_data` dictionary.
  - Option 3: Displays a goodbye message and breaks the loop, terminating the program.
  - Any other input: Displays an error message.
- The function doesn't return anything as it's the main controller of the program.

## 6. Entry Point

```python
if __name__ == "__main__":
    main()
```

**Explanation:**
- This is a Python idiom that checks if the script is being run directly (not imported).
- If the script is run directly, it calls the `main()` function to start the program.
- This allows the script to be imported elsewhere without automatically running the main functionality.

## Data Structure

The core data structure used is a dictionary (`user_data`) with the following structure:

```python
user_data = {
    "email1@example.com": {
        "password": "password1",
        "first_name": "FirstName1",
        "last_name": "LastName1",
        "age": 25
    },
    "email2@example.com": {
        # user data
    },
    # more users...
}
```

This structure allows for:
- Fast lookup by email (O(1) time complexity)
- Logical grouping of user information
- Easy addition of new users
- Simple authentication by comparing stored passwords

However, in a real-world application, passwords should be hashed and not stored in plain text.


## How to Run

1. Save the script in a file named, for example, `auth_system.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory containing the file.
4. Run the script using the following command:

   ```bash
   python auth_system.py
   
Usage Instructions
Upon running the script, the user will be presented with a main menu:

Menu:
1. Signup
2. Sign-in
3. Exit
Option 1: Signup
Prompts the user to enter a valid email address.

Checks if the email already exists in the system.

If valid, collects password, first name, last name, and age.

Stores the information in an in-memory dictionary.

Option 2: Sign-in
Prompts the user for their email and password.

Validates credentials against the stored data.

Displays a welcome message if the login is successful.

Displays an error message if the credentials are incorrect.

Option 3: Exit
Terminates the program.

Sample Users
The application includes preloaded user data for demonstration and testing purposes. Example:

makefile
Copy
Edit
Email: john.doe@example.com
Password: john123
Code Structure
display_menu() - Displays the main menu options.

validate_email(email) - Performs basic validation by checking the presence of the "@" symbol.

signup(user_data) - Handles new user registration with input validations.

signin(user_data) - Authenticates existing users based on stored credentials.

main() - Controls program flow and user interactions.

## Verified Snapshots

# Sign up process tested

![image](https://github.com/user-attachments/assets/6da9d95e-74ad-4ce9-a98f-b69e78bf7891)

# Sign in process tested

![image](https://github.com/user-attachments/assets/03e92fc6-f201-46ae-b4d4-b887b114385d)

# Exiting process tested

![image](https://github.com/user-attachments/assets/040cd776-ebec-49d9-82ea-a46ab2bb7e33)

# Invalid Sign-in process tested

![image](https://github.com/user-attachments/assets/17993a84-9794-4da0-9f50-7b917f71ee0b)



## Author

Nagashree
