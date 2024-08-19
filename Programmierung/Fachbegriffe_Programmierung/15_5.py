c = 3
d = 2

while d < c:
    d = d + c
    c = c + 1 

else:
    c = c + 1
    if not c < d:
        print(c + d)
