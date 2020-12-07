W = int(input())
words = input().split()
# code below
# words[-1] = words[-1].replace(".", "")
print(words)
sumLen = 0
count = 0
blankAll = len(words) - 1
A = []


def numOfWords(words, num):
    i = num
    wordCount, sumLen = 0, 0

    while True:
        if sumLen + len(words[i]) >= W:
            if sumLen + len(words[i]) == W and i == 0:
                wordCount += 1
                break
            break
        sumLen += len(words[i]) + 1
        wordCount += 1
        print("sumLen:", sumLen, "worCount:", wordCount)
        if i == 0:
            break
        i -= 1

    return wordCount


i = len(words)
while(i != 0):

    wordCount = numOfWords(words, i-1)
    print("i:", i, "wordCount:", wordCount)

    if wordCount == 1:
        A.append((W - len(words[i-1]))**3)
        i -= 1

    elif i - wordCount + 1 == len(words):
        wordLen, wordLen1, blank = 0, 0, 0
        for k in range(wordCount):
            wordLen += len(words[k])
        blank = wordCount-1
        A.append((W - wordLen - blank)**3)
        i -= wordCount

    else:
        wordLen1, blank, check = 0, -1, 0

        for k in range(wordCount-1):
            idx = i-k-1
            blank += 1
            # if idx == len(words) - 1:
            #     blank -= 1
            print("idx:", idx)
            wordLen1 += len(words[idx])
            print("wordLen1:", wordLen1)
        print("before:", words[idx], blank)
        penalty1 = (W - wordLen1 - blank)**3
        print(W, wordLen1, blank)

        wordLen2 = wordLen1 + len(words[idx-1])
        blank += 1

        print("next:", words[idx-1], blank)
        penalty2 = (W - wordLen2 - blank)**3

        if penalty1 > penalty2:
            A.append(penalty2)
            i -= wordCount
        else:
            A.append(penalty1)
            i -= (wordCount-1)

        print(penalty1, penalty2)


print(A)
