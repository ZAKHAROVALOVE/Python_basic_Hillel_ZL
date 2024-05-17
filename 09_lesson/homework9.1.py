def popular_words(text: str, words: list) -> dict:
    """
    Підраховує повторність кожного слова зі списку слів у заданому тексті.

    :param text: текст для пошуку.
    :param words: список слів, популярність яких потрібно визначити.
    :return: словник, де ключі – це слова зі списку, а значення – це кількість входжень кожного слова в тексті.
    """
    word_list = text.lower().split()
    word_count = {word: 0 for word in words}

    for word in word_list:
        if word in word_count:
            word_count[word] += 1

    return word_count


if __name__ == "__main__":
    assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''',
                         ['i', 'was', 'three', 'near']) == {'i': 4, 'was': 3, 'three': 0, 'near': 0}
    print('OK')


