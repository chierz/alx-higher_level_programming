#!/usr/bin/python3
j = 97
while j <= 122:
    if chr(j) == "e" or chr(j) == "q":
        j+=1
        continue
    print(f"{chr(j)}", end = "")
    j+=1
