#                    1         2
#          012345678901234567890123456
letters = "abcdefghijklmnopqrstuvwxyz"

#to spell words using the indexing feature.

print('The word "Penelope" would be spelt as: {5}{1}{2}{1}{3}{4}{0}{1}'
.format(letters[15],letters[4],letters[13],letters[11],letters[14],letters[15].upper()))

print('The word "Christmas" would be spelt as: {0}{1}{2}{3}{4}{5}{6}{7}{4}'
.format(letters[2].upper(),letters[7],letters[17],letters[8],letters[18],letters[19],letters[12],letters[0]))

#auto-search for letters in variable letters?
word_to_find = "Cahristmas"

letters_found = ""
for i in word_to_find:
    for j in letters:
        if i.casefold() is not j:
            continue
        else:
            letters_found+=i
