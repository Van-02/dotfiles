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
            total_mount = amount_user * 0.90
            print("Action: 10% discount applied.")
        elif pay_form == "2":
            total_mount = amount_user * 0.87
            print("Action: 13% discount applied.")
        elif pay_form == "3":
            total_mount = amount_user * 1.04
            print("Action: 4% surcharge applied.")
        else:
            print("Invalid payment method. No changes applied.")
            total_mount = amount_user

        print("The total mount to pay is $", total_mount)


calculate_mount()
