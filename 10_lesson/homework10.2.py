def first_word(text: str) -> str:
    """
    Пошук першого слова у переданому рядку.

    Input parameters:
    text: Рядок, у якому потрібно знайти перше слово.

    Output parameters:
    String: Перше слово з переданого тексту.
    """
    text = text.strip("., ")

    word = []
    for char in text:
        if char.isalnum() or char == "'":
            word.append(char)
        else:
            break
    return ''.join(word)


if __name__ == "__main__":
    assert first_word("Hello world") == "Hello", 'Test1'
    assert first_word("greetings, friends") == "greetings", 'Test2'
    assert first_word("don't touch it") == "don't", 'Test3'
    assert first_word(".., and so on ...") == "and", 'Test4'
    assert first_word("hi") == "hi", 'Test5'
    assert first_word("Hello.World") == "Hello", 'Test6'
    print('OK')
