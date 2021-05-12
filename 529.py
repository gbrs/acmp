with open('INPUT.TXT', encoding='utf-8') as f:
    x1, y1, x2, y2 = map(int, f.read().strip().split())
with open('OUTPUT.TXT', 'w', encoding='utf-8') as f:
    a = round(((x1 - x2)**2 + (y1 - y2)**2)**0.5, 5)
    f.write(str(a))
