from forex_python.converter import CurrencyRates, RatesNotAvailableError
import pickle

# Initialize CurrencyRates object
cr = CurrencyRates()

# Create an empty history list
history = []

while True:
    # Get user input
    amount = float(input("Please enter the amount: "))
    from_currency = input("Please enter the original currency code: ")
    to_currency = input("Please enter the target currency code: ")

    try:
        # Perform currency conversion
        result = cr.convert(from_currency, to_currency, amount)

        # Add conversion result to history
        history.append((from_currency, to_currency, amount, result))

        # Display conversion result
        print(f"{amount} {from_currency} = {result} {to_currency}")

    except RatesNotAvailableError:
        print("Unable to perform currency conversion. Please check your currency code.")

    # Ask the user if they want to view the history
    view_history = input("Do you want to view the history? (y/n): ")
    if view_history.lower() == 'y':
        for record in history:
            print(f"{record[2]} {record[0]} = {record[3]} {record[1]}")

    # Ask the user if they want to save the history
    save_history = input("Do you want to save the history? (y/n): ")
    if save_history.lower() == 'y':
        with open('history.pkl', 'wb') as f:
            pickle.dump(history, f)

    # Ask the user if they want to continue
    cont = input("Do you want to continue? (y/n): ")
    if cont.lower() != 'y':
        break

