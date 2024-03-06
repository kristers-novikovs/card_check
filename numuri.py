"""NORĒĶINU KARTES"""

# Code: 
    # Inputs a card number;
    # Checks the length, initial digits, checksum with the Luhn algorithm;
    # If the card is valid, returns TYPE, otherwise INVALID.

# Luhn's algorithm:
    # Katru otro ciparu sākot no iepriekšpēdējā (virzienā pa kreisi) sareizina ar 2, reizinājumus saskaita
    # Saskaita visus pārējos ciparus, kas netika saskaitīti 1. solī
    # Sasummē rezultātus kopā
    # Ja gala summa beidzas ar 0, kartes numurs ir derīgs

# returns True if checksum is valid, otherwise returns False
def Luhn_checks_my_card(card_number):
    digits = list(map(int, str(card_number)[::-1]))
    for i in range(0, len(digits), 2):
        digits[i] = digits[i] * 2
    total = sum(digits)
    if total[-1] == 0:
        return True
    else:
        return False


# Card types:
    # 15 digits. 34 or 37 - AMEX. 
    # 16 digits. 51, 52, 53, 54, 55 - MasterCard
    # 13, 16 digits. 4 - Visa

# returns name of card if digits are valid, otherwise returns "INVALID"
def check_card_type(card_number):
    n = str(card_number)
    if len(n) == 15:
        if n[0] == '3' and n[1] in ['4', '7']:
            return "AMEX"
    elif len(n) == 13:
        if n[0] == '4':
            return "VISA"
    elif len(n) == 16:
        if n[0] == '5' and n[1] in ['1', '2', '3', '4', '5']:
            return "MasterCard"
        elif n[0] == '4':
            return "VISA"
    else:
        return "INVALID"


# main logic
def main():
    card_number = input("Card number: ")
    if Luhn_checks_my_card(card_number):
        print(check_card_type(card_number))
    else:
        print("INVALID")

if __name__ == "__main__":
    main()
