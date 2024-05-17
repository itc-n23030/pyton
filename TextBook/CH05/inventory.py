def d_i(inv):
    print('持ち物リスト')
    item_total = 0 
    for k,v in inv.items():
        item_total += v
        print(v, k)
    print(f'アイテム総数: {str(item_total)}')
stuff = {'rope': 1, 'taimatu': 6, 'gold': 42, 'syuriken': 1, 'ya': 12 }
d_i(stuff)