'''
Ириска весит X грамм, мандарин – Y грамм, пряник – Z грамм.
Требуется написать программу, которая определит,
сколько различных вариантов подарков весом ровно W грамм может сделать Дед Мороз.
'''


def add_weight(weight, space, *makeweights):
    # print(weight, makeweights)
    for i, makeweight in enumerate(makeweights):
        space += 8
        # print(' ' * space, f'+{makeweight}')
        # if weight + makeweight > w:
            # print(' ' * space, weight + makeweight)
            # print(' ' * space, 'xxx')
        if weight + makeweight == w:
            global cnt
            cnt += 1
            # print(' ' * space, cnt, '!!!!!')
            continue
        if weight + makeweight < w:
            # print(' ' * space, end=' ')
            add_weight(weight + makeweight, space, *makeweights[i:])


with open('INPUT.TXT', encoding='utf-8') as f:
    x, y, z, w = map(int, f.read().strip().split())

cnt = space = 0
add_weight(0, space, x, y, z)
# print(cnt)

with open('OUTPUT.TXT', 'w', encoding='utf-8') as f:
    f.write(str(cnt))
