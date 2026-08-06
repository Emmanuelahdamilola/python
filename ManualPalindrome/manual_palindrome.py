def manual_palindrome(text):
    cleaned = text.replace(" ", "").lower()
    
    reversed_text = ""
    for char in cleaned:
        reversed_text = char + reversed_text
    
    if reversed_text == cleaned:
        return True
    else:
        return False