# task 1: Валидатор почтового адреса
email = "aaa@bbb.ccc"  # True   aaa@bbb.ccc
if email.count("@") == 1 and email.count(".") == 1:
    at_index = email.index("@")
    dot_index = email.index(".")
    if at_index < dot_index and email[0] != "@" and email[-1] != ".":
        print(True)
    else:
        print(False)
else:
    print(False)
"""
abc@ccc. - False
aabbcc.ccc - False
@abc.ccc - False
aaabbb.c@cc - False
aaa@b@bb.ccc - False
"""


# task 2: Поиск слов по условию
s = "aab qq c badcc a qqqqqaqqqqaa tpara"
words = s.split()
result = []
for word in words:
    count_a = word.count('a')
    if count_a == 2:
        result.append(word)
print(' '.join(result).title())


# task 3: Количество слов в предложении
multi_string = "Hello all. Here's pretty cold and hot. Choose yourself."
sentences = multi_string.split('. ')
words_number = []
for sentence in sentences:
    sentence = sentence.strip()
    words = sentence.split(' ')
    words = [word for word in words if word]
    words_number.append(len(words))
print(words_number)


# task 4: Палиндром
# str1 = input().strip().lower()  # 1st input - "    aBC cba " , 2nd input - "a BCQcb a    " , 3rd input - " ab bca"
# str1_reversed = str1[::-1]
# print(str1 == str1_reversed)

