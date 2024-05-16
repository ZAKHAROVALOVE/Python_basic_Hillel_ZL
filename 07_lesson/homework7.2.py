def correct_sentence(text: str) -> str:
    """
    Corrects the text by capitalizing the first letter of the sentence and adding a period at the end if it's missing.

    :param text: The input text to be corrected.
    :type text: str
    :return: The corrected text.
    :rtype: str
    """

    corrected_text = text[0].upper() + text[1:]
    if not text.endswith('.'):
        corrected_text += '.'
    return corrected_text


if __name__ == "__main__":
    assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
    assert correct_sentence("hello") == "Hello.", 'Test2'
    assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
    assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
    assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'
    print('OK')
