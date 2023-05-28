# palindrom

word = input('введите слово: ')
print(len(word) // 2)

def pol(word, i, flag):
    if i < 0:
        return flag
    else:
        print(i, word[i], word[-i - 1])
        if word[i] != word[-i - 1]:
            flag = False
        return pol(word, i - 1, flag)
    
if pol(word, len(word) // 2 - 1, True):
    print('Это палиндром')
else:
    print('Это не палиндром')