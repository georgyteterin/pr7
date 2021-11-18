def max_in(spisok):
    if spisok[0] == max(spisok):
        return 1
    else:
        return (1 + max_in(spisok[1:]))  

print(max_in([1, 13, 14, 2]))

