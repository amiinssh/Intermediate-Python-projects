Table of Contents

    Introduction
    Features
    Installation
    Usage Guide
        Main Menu
        User Registration (Sign In)
        User Login
        Banking Operations
            Deposit
            Withdraw
            Transfer
            Check Balance
            Interest Rates
            Compound Interest Calculator
        Forgot PIN
        Exiting the Application
    Technical Details
    Error Handling and Input Validation
    Known Issues
    License

Introduction

This is a Python-based online banking application that allows users to manage their bank accounts. It features typical banking operations like deposits, withdrawals, transfers, balance checks, interest rate information, and compound interest calculations.

The application also supports user registration and login with a unique username and 6-digit PIN. If a user forgets their PIN, there is an option to reset it. All operations are handled via command-line interaction.
Features

    User Registration: Users can create an account with a unique username and a 6-digit PIN.
    User Login: Secure login using the registered username and PIN.
    Deposit: Users can deposit funds into their account.
    Withdraw: Allows users to withdraw money while checking available balances.
    Transfer: Users can transfer money to another account by providing an 8-digit destination account number.
    Check Balance: The current balance can be checked at any time.
    Interest Rates: The app provides deposit interest rates based on the current balance.
    Compound Interest Calculator: Users can calculate compound interest for different time periods based on their deposit amounts.
    Forgot PIN: If a user forgets their PIN, they can reset it securely.
    Exit Option: Users can safely exit or continue to interact with the app.

Installation
Prerequisites

    Python 3.7+ installed on your machine.

Steps to Install

    Clone the repository:

    bash

git clone https://github.com/yourusername/online-banking-app.git

Navigate to the project directory:

bash

cd online-banking-app

Run the application:

bash

    python online_banking_app.py

Usage Guide

Once the program is started, the application will prompt users to choose between signing in (creating an account) or logging in (if they already have an account).
Main Menu

Upon running the application, the main menu will present the following options:

    1 - Sign In: Create a new account.
    2 - Log In: Log in to an existing account.

User Registration (Sign In)

To sign in, users are prompted to create:

    A unique username.
    A 6-digit PIN for authentication.

If the PIN is not 6 digits, the user will be prompted to re-enter it until it meets the requirement.
User Login

Users need to input:

    Their username.
    The previously created 6-digit PIN.

If the username or PIN is incorrect, the user will be asked if they wish to:

    Try logging in again.
    Reset their PIN via the Forgot PIN option.

Banking Operations

After successfully logging in, the user will be presented with a menu of banking operations:

    Deposit:
    The user can deposit a specific amount, which will be added to their current balance.

    Withdraw:
    The user can withdraw money. If the requested withdrawal exceeds the available balance, the transaction will be denied.

    Transfer:
    The user can transfer funds to another account by providing an 8-digit destination account number. The transfer will be processed only if the user's balance is sufficient.

    Check Balance:
    The user can check the current balance in their account.

    Interest Rates:
    The application will provide the deposit interest rate based on the user's current balance:
        3% if the balance is over 50,000.
        2% if the balance is over 30,000.
        1.5% for all other amounts.

    Compound Interest Calculator:
    The user has two options for calculating compound interest:
        Option 1: Based on the current balance and the desired investment period in years.
        Option 2: Based on a user-specified deposit amount and investment period.

Forgot PIN

If a user forgets their PIN, they can reset it by selecting the Forgot PIN option. The user will be prompted to create a new 6-digit PIN.
Exiting the Application

After completing operations, users can either:

    Exit the application, or
    Continue to use the application.

When exiting, the user is prompted with:

plaintext

Do you still want to conduct transactions? Yes/No:

Technical Details
Deposit Interest Calculation

The formula for calculating compound interest is:

plaintext

A = P * e^(r * t)

Where:

    P: The initial principal balance (deposit).
    r: The annual interest rate (in decimal form).
    t: The time in years.
    e: The Euler's number (approximately 2.71828).

Global Variables

    name: Stores the user's name.
    pin: Stores the user's 6-digit PIN.
    currentBalance: Tracks the current balance of the user's account.

Functions

    signIn(): Handles user registration and ensures that the user creates a valid 6-digit PIN.
    forgetPIN(): Allows users to reset their PIN if forgotten.
    depositInterests(p, r, t): Calculates compound interest using the principal amount p, the rate r, and the time t.
    logIn(): Handles user login and provides access to banking operations.
    app_exit(): Handles the exit functionality, prompting the user whether they want to continue or stop using the app.
    mainMenu(): The entry point for the application, displaying the main menu for sign-in or login.

Error Handling and Input Validation

    PIN Validation: The PIN must be exactly 6 digits. If the user provides an invalid PIN during registration or reset, the system will prompt the user to re-enter a valid PIN.

    Transfer Validation: The transfer destination account number must be exactly 8 digits. If the number is invalid, the transfer is rejected.

    Balance Check: The system checks if the user has sufficient funds before processing withdrawals or transfers. If the balance is insufficient, the transaction is denied.

    Numerical Input: For deposit, withdrawal, and transfer amounts, the system expects numeric values. Invalid inputs may crash the application (known issue).

Known Issues

    Input Validation: The application assumes that numeric inputs for deposits, withdrawals, and transfers are valid. If a user inputs non-numeric characters, the application may crash.
        Fix: Additional input validation can be implemented to ensure that the inputs are valid numbers.

    Recursive Login: The current login mechanism uses recursive calls, which could lead to a stack overflow in extreme cases.
        Fix: Replace recursion with a loop to handle repeated login attempts.

License

This project is licensed under the MIT License.