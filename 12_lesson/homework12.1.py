import codecs
import re


def delete_html_tags(html_file: str, result_file: str = 'cleaned.txt') -> None:
    """
    Читання файлу HTML, видалення тегів HTML, запис чистого тексту у вказаний файл.
    """
    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.read()

    clean_text = re.sub(r'<.*?>', '', html)

    with open(result_file, 'w', encoding='utf-8') as file:
        file.write(clean_text)


if __name__ == "__main__":
    delete_html_tags('draft.html', 'cleaned.txt')