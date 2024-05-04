def generate_hashtag(s):
    hashtag = '#' + ''.join(word.capitalize() for word in s.split() if word)
    hashtag = ''.join(filter(str.isalnum, hashtag))[:140]
    return hashtag
print(generate_hashtag(input("Введіть рядок: ")))