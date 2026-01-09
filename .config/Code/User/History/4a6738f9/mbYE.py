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
            print("3 - Credit Card (Installments)")
            pay_form = input("Enter option (1, 2, or 3): ")
            if pay_form in ["1", "2", "3"]:
                break
            print("Invalid option.")

        if pay_form == "1":
            total_amount = amount_user * 0.90
            print("Action: 10% discount applied.")
        elif pay_form == "2":
            total_amount = amount_user * 0.87
            print("Action: 13% discount applied.")
        else:
            while True:
                print("\nSelect the card:")
                for key, (name, _) in card_data.items():
                    print(f"{key} - {name}")
                card_choice = input("Enter option: ")
                if card_choice in card_data:
                    break
                print("Invalid card selection.")

            card_name, installment_options = card_data[card_choice]

            while True:
                print(f"\nInstallment options for {card_name}:")
                for months, rate in installment_options.items():
                    print(f"{months} payments - {rate}% monthly interest")

                    try:
                        chosen_months = int(
                            input("Enter number of payments (3, 6 or 12): "))
                        if chosen_months in installment_options:
                            break
                    except ValueError:
                        pass
                    print("Invalid installment option.")

            monthly_rate = installment_options[chosen_months]
            annual_rate = monthly_rate * 12

            interest_factor = (monthly_rate / 100) * chosen_months
            total_amount = amount_user * (1 + interest_factor)

            print("\n" + "="*35)
            print(f"FINANCIAL REPORT ({card_name})")
            print(f"Monthly interest rate: {monthly_rate}%")
            print(f"Annual interest rate (TNA): {annual_rate}%")
            print(f"Total with interest: ${total_amount:.2f}")
            print(
                f"Each installment ({chosen_months}x): ${total_amount / chosen_months:.2f}")
            print("="*35)
            return

        print(f"\nThe total amount to pay is: ${total_amount:.2f}")
    except ValueError:
        print("Error: Please enter a valid numerical value.")


calculate_mount()
