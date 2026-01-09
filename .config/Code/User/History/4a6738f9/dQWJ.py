"""
Integrar en lo posible la solucion entre ambos ejercicios anteriores.
"""


def calculate_mount():
    """
    Calculates final price, monthly rate, and annual rate using a unified data structure.
    """
    card_data = {
        "1": ("Visa", {3: 4.0, 6: 4.0, 12: 5.0}),
        "2": ("Mastercard", {3: 3.0, 6: 4.0, 12: 5.0}),
        "3": ("American Express", {3: 3.8, 6: 5.0, 12: 5.3})
    }

    try:
        amount_user = float(input("Enter the total purchase amount: "))

        while True:
            print("Select the payment method:")
            print("1 - Debit (10% discount)")
            print("2 - Cash (13% discount)")
            print("3 - Credit Card (1 payment, 4% surcharge)")

            pay_form = input("Enter option (1, 2, or 3): ")

            if pay_form in ["1", "2", "3"]:
                break
            print("Invalid option. Please try again.")

        if pay_form == "1":
            total_amount = amount_user * 0.90
            print("Action: 10% discount applied.")
        elif pay_form == "2":
            total_amount = amount_user * 0.87
            print("Action: 13% discount applied.")
        elif pay_form == "3":
            while True:
                cards = {
                    "1": ("Visa", 1.05),
                    "2": ("Mastercard", 1.07),
                    "3": ("American Express", 1.09)
                }
                print("\nSelect the card: ")

                for key, (name, _) in cards.items():
                    print(f"{key} - {name}")

                card_choice = input("Enter option: ")
                if card_choice in ["1", "2", "3"]:
                    break
                print("Invalid option. Please try again.")

            if card_choice == "1":
                while True:
                    payments = {
                        "3": 4.0,
                        "6": 4.0,
                        "12": 5.0
                    }
                    print("Payments form: ")
                    for key, name in payments.items():
                        print(f"{key} - {name}")

                    payment_choise = input("Enter option: ")

                    if payment_choise in ["3", "6", "12"]:
                        break
                    print("Invalid option. Please try again.")

                if payment_choise in payments:
                    payment_name, rate = payments[payment_choise]
                    total_amount = amount_user * rate
                    print(f"Applied: {payment_name} payment surcharge")

            elif card_choice == "2":
                while True:
                    payments = {
                        "3": 3.0,
                        "6": 4.0,
                        "12": 5.0
                    }
                    print("Payments form: ")
                    for key, name in payments.items():
                        print(f"{key} - {name}")

                    payment_choise = input("Enter option: ")

                    if payment_choise in ["3", "6", "12"]:
                        break
                    print("Invalid option. Please try again.")

                if payment_choise in payments:
                    payment_name, rate = payments[payment_choise]
                    total_amount = amount_user * rate
                    print(f"Applied: {payment_name} payment surcharge")

            elif card_choice == "3":
                while True:
                    payments = {
                        "3": 3.8,
                        "6": 5.0,
                        "12": 5.3
                    }
                    print("Payments form: ")
                    for key, name in payments.items():
                        print(f"{key} - {name}")

                    payment_choise = input("Enter option: ")

                    if payment_choise in ["3", "6", "12"]:
                        break
                    print("Invalid option. Please try again.")

                if payment_choise in payments:
                    payment_name, rate = payments[payment_choise]
                    total_amount = amount_user * rate
                    print(f"Applied: {payment_name} payment surcharge")

            print(f"\nThe total amount to pay is: ${total_amount:.2f}")

        else:
            print("Invalid payment method. No changes applied.")
            total_amount = amount_user

        print(f"\nThe total amount to pay is: ${total_amount:.2f}")

    except ValueError:
        print("Error: Please enter a valid numerical value for the amount.")


calculate_mount()
