A_ASCII_VALUE = 97
ALPHABET_AMOUNT = 26


def lasso_letter(letter, shift_amount):
    ascii_value = ord(letter.lower())
    decoded_letter_code = A_ASCII_VALUE + (
        ((ascii_value - A_ASCII_VALUE) + shift_amount) % ALPHABET_AMOUNT
    )
    decoded_letter_code = chr(decoded_letter_code)
    return decoded_letter_code


def lasso_word(word, shift_amount):
    decoded_word = ""
    for letter in word:
        decoded_word += lasso_letter(letter=letter, shift_amount=shift_amount)
    return decoded_word

if __name__ == "__main__":
    print(lasso_letter("p", -2))
