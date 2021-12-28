from collections import Counter

# letter = "dsfhb fdfdf dfd hfd dufdb ffbd fd fdbbf dfdb df dfh"
# magazine = "df d fdfhi wuweq90j nre78cbjdfjbd 87edhf df"

letter = "abcdff"
magazine = "dcbasdfdsf"

lCounter = Counter(letter)
mCounter = Counter(magazine)

difCounter1 =  mCounter - lCounter
difCounter2 =  lCounter - mCounter

print(difCounter1)
print(difCounter2)

difCounter1Len = len(list(difCounter1.keys()))
difCounter2Len = len(list(difCounter2.keys()))


if(difCounter1Len == 0 and difCounter2Len == 0):
    print("Yes 1")
elif(difCounter2Len> 0):
    print("No 2")
else:
    print("Yes 3")
