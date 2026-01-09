"""
Integrar en lo posible la solucion entre ambos ejercicios anteriores.
"""


def calculate_mount():
    mount_user = float(input("Enter a total mount of buy: "))

    print("Select the form pay:\n")
    print("1 - Debito (10% offer)")
    print("2 - Contado-Efectivo (13%)")
    print("3 - Tarjeta (1 solo pago, 4% recargo)")
    pay_form = input("Enter a pay form: ")

    if pay_form == "1":
        total_mount = mount_user * 0.90
    elif pay_form == "2":
        total_mount = mount_user * 0.87
    elif pay_form == "3":
        total_mount = mount_user * 1.04
    else:
        print("Pay form not avaible.")
        total_mount = mount_user

    print("The total mount to pay is $", total_mount)


calculate_mount()
