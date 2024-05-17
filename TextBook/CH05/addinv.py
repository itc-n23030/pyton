def add_to_inventory(inv, added_items):
    for i in added_items:
        if i in inv:
            inv[i] += 1 
        else:
            inv[i] = 1
    print('持ち物リスト:')
    total = 0
    for k, v in inv.items():
        total += v
        print(v, k)
    print(f'アイテムの総数:{total}')

inv = {'gold': 42, 'rope': 1}
dragon_loot = ['gold', 'syuriken', 'gold', 'gold', 'ruby']
add_to_inventory(inv, dragon_loot)