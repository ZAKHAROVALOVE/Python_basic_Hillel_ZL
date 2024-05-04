import string
def find_letters_between(dash_letters):
    start_index = min(string.ascii_letters.index(dash_letters[0]), string.ascii_letters.index(dash_letters[-1]))
    end_index = max(string.ascii_letters.index(dash_letters[0]), string.ascii_letters.index(dash_letters[-1]))
    return string.ascii_letters[start_index:end_index + 1]
dash_letters = input("Введіть дві літери через дефіс: ")
print(find_letters_between(dash_letters))