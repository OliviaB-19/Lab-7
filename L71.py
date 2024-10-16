# the authors are Olivia Beck and Elizabeth Wyatt

def too_long():
    if len(x)>=140:
        print("Text is too long.")
    else:
        print("Send")
x="ljnirgeeeeeeeeeeeee ggggggggggggggggggggggggggggggggggggggg"
too_long()

print("Snakes!🐍🐍🐍")

import unicodedata
print(unicodedata.lookup("snake"))
print(unicodedata.lookup("cat"))

print(unicodedata.lookup("dog"))
print(unicodedata.lookup("cat"))
print(unicodedata.lookup("rose"))

import unicodedata
print(unicodedata.name("&"))
print(unicodedata.name("["))
print(unicodedata.name("/"))

x=print(unicodedata.lookup("sun"))
y="What a pretty dog!"

def five_sent(x):
    if x=="sun":
        print("Wow the sun is so bright"+unicodedata.lookup("sun"))
    elif x=="cat":
        print("I love cats!"+unicodedata.lookup("cat"))
    elif x=="two hearts":
        print("Badum!"+unicodedata.lookup("two hearts"))
    elif x=="dog":
        print("What a cute dog!"+unicodedata.lookup("dog"))
    elif x=="rose":
        print("I love the smell of roses!"+unicodedata.lookup("rose"))
five_sent("rose")

