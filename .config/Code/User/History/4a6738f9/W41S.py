"""
Integrar en lo posible la solucion entre ambos ejercicios anteriores.
"""


def calculate_mount():
    """
    Calculates the final price based on the payment method selected.
    """
    try:
        amount_user = float(input("Enter the total purchase amount: "))

        print("Select the payment method:")
        print("1 - Debit (10% discount)")
        print("2 - Cash (13% discount)")
        print("3 - Credit Card (1 payment, 4% surcharge)")

        pay_form = input("Enter option (1, 2, or 3): ")

        if pay_form == "1":
            total_amount = amount_user * 0.90
            print("Action: 10% discount applied.")
        elif pay_form == "2":
            total_amount = amount_user * 0.87
            print("Action: 13% discount applied.")
        elif pay_form == "3":
            cards = {
                "1": ("Visa", 1.05),
                "2": ("Mastercard", 1.07),
                "3": ("American Express", 1.09)
            }
            print("\nSelect the card: ")

            for key, (name, _) in cards.items():
                print(f"{key} - {name}")

            card_choise = input("Enter option")
            if card == "1":
                total_amount = amount_user * 1.05
            elif card == "2":
                total_amount = amount_user * 1.07
            elif card == "3":
                total_amount = amount_user * 1.09
            else:
                print("Invalid option.")
                total_amount = amount_user

        else:
            print("Invalid payment method. No changes applied.")
            total_amount = amount_user

        print(f"\nThe total amount to pay is: ${total_amount:.2f}")

    except ValueError:
        print("Error: Please enter a valid numerical value for the amount.")


calculate_mount()
