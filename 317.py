'''
Ириска весит X грамм, мандарин – Y грамм, пряник – Z грамм.
Требуется написать программу, которая определит,
сколько различных вариантов подарков весом ровно W грамм может сделать Дед Мороз.
'''


def add_weight(weight, *makeweights):
    # print(weight)
    for makeweight in makeweights:
        if weight + makeweight > w:
            pass
        if weight + makeweight == w:
            global cnt
            cnt += 1
        if weight + makeweight < w:
            add_weight(weight + makeweight, *makeweights)
            add_weight(weight + makeweight, *makeweights[1:])


with open('INPUT.TXT', encoding='utf-8') as f:
    x, y, z, w = map(int, f.read().strip().split())

cnt = 0
add_weight(0, x, y, z)
print(cnt)

with open('OUTPUT.TXT', 'w', encoding='utf-8') as f:
    f.write(str(cnt))