# дан готовый текст
text = (
    "Etiam tincidunt neque erat, quis molestie enim imperdiet vel. "
    "Integer urna nisl, facilisis vitae semper at, dignissim vitae libero"
)

# разбиваем текст
words = text.split()

new_words = []

for word in words:
    if word.endswith(',') or word.endswith('.'):

        punctuation = word[-1]
        clean_word = word[:-1]
        new_words.append(clean_word + 'ing' + punctuation)
    else:
        new_words.append(word + 'ing')

result_text = " ".join(new_words)

print(result_text)
