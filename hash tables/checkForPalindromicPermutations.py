import collections

checkString = "foobafraboo"

def checkForPalindromicPermutation(s):
    oddCount = collections.Counter(s)
    oddCount = {k: v for k, v in oddCount.items() if v % 2 != 0}
    print(len(list(oddCount.keys())))
    # return oddCount<2

checkForPalindromicPermutation(checkString)