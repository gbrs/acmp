with open('INPUT.TXT', encoding='utf-8') as f:
    a = int(f.read().strip())
    r = a // 10
    a = 100 * r * (r + 1) + 25
with open('OUTPUT.TXT', 'w', encoding='utf-8') as f:
    f.write(str(a))
