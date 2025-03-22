def caesar_cipher(text, shift, mode):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    result = ""

    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            new_index = (alphabet.index(char) + (shift if mode == "encode" else -shift)) % 26
            new_char = alphabet[new_index]
            result += new_char.upper() if is_upper else new_char
        else:
            result += char  # Keep spaces, punctuation, and numbers unchanged

    return result


# 🚀 User Interaction Loop
while True:
    mode = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").strip().lower()
    
    if mode not in ["encode", "decode"]:
        print("❌ Invalid input! Please enter 'encode' or 'decode'.")
        continue

    text = input("Type your message:\n").strip()
    
    try:
        shift = int(input("Type the shift number:\n").strip()) % 26  # Ensure shift stays within 26 letters
    except ValueError:
        print("❌ Invalid shift number! Please enter a valid integer.")
        continue

    print(f"Here is the {mode}d result: {caesar_cipher(text, shift, mode)}")

    response = input("Go again? Type 'yes' to continue or 'no' to exit:\n").strip().lower()
    if response == "no":
        print("✅ Have a nice day!")
        break
    elif response == "yes":
        continue
    else:
        print("Invalid input..")
        continue