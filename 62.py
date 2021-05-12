with open('INPUT.TXT', encoding='utf-8') as f:
    column, row = list(f.read().strip())
with open('OUTPUT.TXT', 'w', encoding='utf-8') as f:
    if ((column in 'BDFH') * 1 + int(row) % 2) % 2:
        a = 'BLACK'
    else:
        a = 'WHITE'
    f.write(str(a))
