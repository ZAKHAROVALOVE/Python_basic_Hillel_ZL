def is_palindrome(text: str) -> bool:
    """
    Check if a string is a palindrome.

    Args:
        text (str): The string to check.

    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """

    cleaned_text = ''.join(char.lower() for char in text if char.isalnum())
    reversed_text = cleaned_text[::-1]
    return cleaned_text == reversed_text


if __name__ == "__main__":
    assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
    assert is_palindrome('0P') == False, 'Test2'
    assert is_palindrome('a.') == True, 'Test3'
    assert is_palindrome('aurora') == False, 'Test4'
    print("ОК")