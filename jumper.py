def sc(f): 
    if f<2:return''
    return '💩 '*(f-1)+'🤕'*(f<7) +'☠️'*(f>6)

floor = input('Enter the floor you want to jump from ')
floor = int(floor)
scream = sc(floor)
print(scream)
