def caesar_cipher(text, shift):
    
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char
    return result

def all_caesar_shifts(text):
    for shift in range(0,26):
        encrypted_text = caesar_cipher(text, shift)
        print(f"Shift {shift}: {encrypted_text}")

all_caesar_shifts("zain")
