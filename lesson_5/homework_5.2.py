import string

text = input("Введи щось, що буде 'хештегом', але не більше 140 символів: \n ")
title_text = text.title()
#text_exclusion = title_text
for char in string.punctuation + string.whitespace:
    text_exclusion = title_text.replace(char, '')
print(text_exclusion.count(''))
result = text_exclusion[:139]


print("Оригінальний текст:", text)
print("Текст з належними великими літерами:", title_text)
print("Текст без пунктуації:", text_exclusion)
print(result)
print(result.count(''))


