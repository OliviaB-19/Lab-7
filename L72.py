#the authors are Olivia Beck and Elizabeth Wyatt

def counter(y):
    total=0
    for x in y:
        if x=="o":
            total=total+1
    return total
print(counter("bonobos"))
